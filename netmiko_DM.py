import netmiko, time, re

start = time.time()

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

for router in three_routers:

    connected = netmiko.ConnectHandler(**router)

    print("Router: " + connected.find_prompt())

    #show file systems
    fs_info = re.findall(r"\d+\s+\d+\s+\w+", connected.send_command("show file systems"))[0].split()
    fs_perc = '{:.2f}'.format((int(fs_info[1]) / int(fs_info[0])) * 100)
    print("File System Usage:\nType: " + fs_info[2], "Size(b): " + fs_info[0], "Free: " + fs_info[1],
          "Percent Used: " + str(fs_perc) + "%\n")

    #show memory
    mem_use = re.search(r"\d{9}\s+\d+\s+\d+", connected.send_command("show memory statistics")).group().split()
    mem_perc = '{:.2f}'.format((int(mem_use[1]) / int(mem_use[0])) * 100)
    print("Memory Usage:\nTotal Memory(b): " + mem_use[0], "Free Memory(b): " + mem_use[2],
          "Percent Used: " + mem_perc + "%\n")

    #show ip protocols
    protocol = re.search(r"\"\w+", connected.send_command("show ip protocols")).group()
    print("Routing Protocol Information:\n", "Protocol: " + protocol[1:])

    #show ip ospf neighbors
    neighbours = re.findall(r"\d\.\d\.\d\.\d", connected.send_command("show ip ospf neighbor"))
    print("Neighbour Routers:", ", ".join(neighbours) + "\n")

    #backup running config
    netmiko.file_transfer(connected, source_file="startup-config", dest_file = "/root/" + connected.find_prompt() 
                          + "config.txt", file_system = "nvram:", direction="get")
    print("Configuration Backed up\n")

    connected.disconnect()

print('{:.3f}'.format(time.time() - start))