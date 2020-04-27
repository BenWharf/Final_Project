import netmiko, time, re

#Start in-code timer
start = time.time()

#Router connection details
three_routers = [{
    "host":"192.168.0.1",
    "username":"admin",
    "password":"admin",
    "device_type":"cisco_ios"
    }, {
    "host":"192.168.0.2",
    "username":"admin",
    "password":"admin",
    "device_type":"cisco_ios"
    }, {
    "host":"192.168.0.3",
    "username":"admin",
    "password":"admin",
    "device_type":"cisco_ios"
    }]

#Connection Loop Starts
for router in three_routers:

    #Connect to the router
    connected = netmiko.ConnectHandler(**router)

    #Get the current routers hostname
    print("Router: " + connected.find_prompt())

    #Get the information about the file systems
    fs_info = re.findall(r"\d+\s+\d+\s+\w+", connected.send_command("show file systems"))[0].split()
    fs_perc = '{:.2f}'.format(100 - (int(fs_info[1]) / int(fs_info[0])) * 100)
    print("File System Usage:\nType: " + fs_info[2], "Size(b): " + fs_info[0], "Free: " + fs_info[1],
          "Percent Used: " + str(fs_perc) + "%\n")

    #Get the information about the memory use
    mem_use = re.search(r"\d{9}\s+\d+\s+\d+", connected.send_command("show memory statistics")).group().split()
    mem_perc = '{:.2f}'.format((int(mem_use[1]) / int(mem_use[0])) * 100)
    print("Memory Usage:\nTotal Memory(b): " + mem_use[0], "Free Memory(b): " + mem_use[2],
          "Percent Used: " + mem_perc + "%\n")

    #Show the current dynamic routing system
    protocol = re.search(r"\"\w+", connected.send_command("show ip protocols")).group()
    print("Routing Protocol Information:\n" + "Protocol: " + protocol[1:])

    #Show the current dynamic routing protocols neigbours
    neighbours = re.findall(r"\d\.\d\.\d\.\d", connected.send_command("show ip ospf neighbor"))
    print("Neighbour Routers:", ", ".join(neighbours) + "\n")

    #Back up the start-up configuration file using SCP
    netmiko.file_transfer(connected, source_file="startup-config", dest_file = "/root/" + connected.find_prompt() 
                          + "config.txt", file_system = "nvram:", direction="get")
    print("Configuration Backed up\n")

    #Disconnect from the router
    connected.disconnect()

print('{:.3f}'.format(time.time() - start))