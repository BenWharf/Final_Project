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

def connection_test (neighbour_id, neighbour_ip):
    #Function to test connectivity

    #Send ping command and find success rate in the returned result
    ping_result = re.search(r"\d+\s\bpercent", connected.send_command("ping " + neighbour_ip)).group()

    #Print ping result to the screen
    print("Connection to Neighbour Router", neighbour_id, "is:", ping_result, "successful")

#Connection Loop Starts
for router in three_routers:

    #Connect to the router
    connected = netmiko.ConnectHandler(**router)

    #Get the router ID
    router_id = re.search(r"\d+.\d+.\d+.\d+", connected.send_command("show ip ospf")).group()

    #Print the current ID to the screen
    print("The current Router is:", router_id)

    #Find the neighbours and there IP addresses
    ospf_neighbour = re.findall(r"\d+.\d+.\d+.\d+", connected.send_command("show ip ospf neighbor"))

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
    connected.disconnect()
    print(" ")

#Print finished time to the screen
print('{:.3f}'.format(time.time() - start))