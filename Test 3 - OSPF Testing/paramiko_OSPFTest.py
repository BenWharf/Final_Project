import paramiko, time, re

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

def connection_test (neighbour_id, neighbour_ip):
    #Function to test connectivity

    #Send ping command
    connected.send("ping " + neighbour_ip + "\n")
    
    #Get the returned result
    ping_result = ""
    time.sleep(1)
    while not connected.recv_ready():
        continue
    while connected.recv_ready():
        ping_result = ping_result + connected.recv(65535).decode('utf-8')

    #Find the success rate
    ping_result = re.search(r"\d+\s\bpercent", ping_result).group()

    #Print success rate to the screen
    print("Connection to Neighbour Router", neighbour_id, "is:", ping_result, "successful")

#Connection to the router
for router in three_routers:

    #Connect to the router
    client.connect(router['host'], username=router['username'], password=router['password'])

    #Connect to the router
    connected = client.invoke_shell()
    
    #Send the command to get the current router ID
    connected.send("show ip ospf\n ")

    #Get the response
    router_id = ""
    time.sleep(1)
    while not connected.recv_ready():
        continue
    while connected.recv_ready():
        router_id = router_id + connected.recv(65535).decode('utf-8')

    #Find the router ID    
    router_id = re.search(r"\d+.\d+.\d+.\d+", router_id).group()

    #Print the current ID to the screen
    print("The current Router is:", router_id)

    #Send the command to get the neighbours
    connected.send("show ip ospf neighbor\n")

    #Get the response from the router
    neighbour_id = ""
    time.sleep(1)
    while not connected.recv_ready():
        continue
    while connected.recv_ready():
        neighbour_ids = neighbour_id + connected.recv(65535).decode('utf-8')

    #Find the neighbours and IP Addresses
    ospf_neighbour = re.findall(r"\d+.\d+.\d+.\d+", neighbour_ids)
    
    #If statement to check how many neighbours there are
    if(len(ospf_neighbour) == 2):
        #Send the neigbour information to the connection test function
        connection_test(ospf_neighbour[0], ospf_neighbour[1])

    elif (len(ospf_neighbour) > 2 and len(ospf_neighbour) % 2 == 0):
    #Else if statement if the list is bigger than 2 and a even number
        ospf_neighbour = iter(ospf_neighbour)

        #Loop through the neigbour list
        for x in ospf_neighbour:
            #Send the neigbour information to the connection test function
            connection_test(x, next(ospf_neighbour))

    #Disconnect from the router
    connected.close()
    print(" ")

#Close Paramiko SSH connection client
client.close()

#Print finished time to the screen
print('{:.3f}'.format(time.time() - start))