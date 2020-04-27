import paramiko, scp, time, re

#Start in-code timer
start = time.time()

#Router connection details
three_routers = [{
    "host":"192.168.0.1",
    "username":"admin",
    "password":"admin"
    }, {
    "host":"192.168.0.2",
    "username":"admin",
    "password":"admin"
    }, {
    "host":"192.168.0.3",
    "username":"admin",
    "password":"admin"
    }]

#Create Paramiko SSH connection client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Connection Loop Starts
for router in three_routers:

    #Connect to the router
    client.connect(router['host'], username=router['username'], password=router['password'])

    #Create SSH shell
    connected = client.invoke_shell()

    #Get the current routers hostname
    router_id = connected.recv(65535).decode('utf-8').strip("\r\n")
    print("Router: " + router_id)

    #Get the information about the file systems
    connected.send("show file systems\n")
    fs_result = ""
    time.sleep(1)
    while not connected.recv_ready():
        continue
    while connected.recv_ready():
        fs_result = fs_result + connected.recv(65535).decode('utf-8')

    fs_info = re.findall(r"\d+\s+\d+\s+\w+", fs_result)[0].split()
    fs_perc = '{:.2f}'.format(100 - (int(fs_info[1]) / int(fs_info[0])) * 100)
    print("File System Usage:\nType: " + fs_info[2], "Size(b): " + fs_info[0], "Free: " + fs_info[1],
          "Percent Used: " + str(fs_perc) + "%\n")

    #Get the information about the memory use
    connected.send("show memory statistics\n")
    mem_result = ""
    time.sleep(1)
    while not connected.recv_ready():
        continue
    while connected.recv_ready():
        mem_result = mem_result + connected.recv(65535).decode('utf-8')

    mem_use = re.search(r"\d{9}\s+\d+\s+\d+", mem_result).group().split()
    mem_perc = '{:.2f}'.format((int(mem_use[1]) / int(mem_use[0])) * 100)
    print("Memory Usage:\nTotal Memory(b): " + mem_use[0], "Free Memory(b): " + mem_use[2],
          "Percent Used: " + mem_perc + "%\n")


    #Show the current dynamic routing system
    connected.send("show ip protocols\n")
    protocol_result = ""
    time.sleep(1)
    while not connected.recv_ready():
        continue
    while connected.recv_ready():
        protocol_result = protocol_result + connected.recv(65535).decode('utf-8')

    protocol = re.search(r"\"\w+", protocol_result).group()
    print("Routing Protocol Information:\n" + "Protocol: " + protocol[1:])

    #Show the current dynamic routing protocols neigbours
    connected.send("show ip ospf neighbor\n")
    neighbours_result = ""
    time.sleep(1)
    while not connected.recv_ready():
        continue
    while connected.recv_ready():
        neighbours_result = neighbours_result + connected.recv(65535).decode('utf-8')

    neighbours = re.findall(r"\d\.\d\.\d\.\d", neighbours_result)
    print("Neighbour Routers:", ", ".join(neighbours) + "\n")
    connected.close()

    #Back up the start-up configuration file using SCP
    client.connect(router['host'], username=router['username'], password=router['password'])
    scp_connection = scp.SCPClient(client.get_transport())
    scp_connection.get("nvram:startup-config", "/root/" + router_id + "config.txt")
    scp_connection.close()
    print("Configuration Backed up\n")

#Close Paramiko SSH connection client
client.close()

print('{:.3f}'.format(time.time() - start))