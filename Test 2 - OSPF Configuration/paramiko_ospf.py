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

#Connection Loop Starts
for router in three_routers:

    #Connect to the router
    client.connect(router['host'], username=router['username'], password=router['password'])

    #Create SSH shell
    connected = client.invoke_shell()

    #Send the necessary command
    connected.send("show ip route connected\n")

    output = ""
    time.sleep(1)

    #Get the connected networks
    while not connected.recv_ready():
        continue

    while connected.recv_ready():
        output = output + connected.recv(65535).decode('utf-8')

    #Find the networks from the response using regular expression
    networks = re.findall(r"\d+\.\d+\.\d+\.\d+/\d\d", output)

    #Go to correct router configuration level
    connected.send("configure terminal\n")

    #Start OSPF configuration
    connected.send("router ospf 1\n")

    #loop through the networks
    for network in networks:

        #Seperate the network address from the subnet mask
        net_ip = network.split("/")[0]

        slash_mask = int(network.split("/")[1])

        #Convert Slash notation subnet mask to binary
        bin_mask = ("0" * slash_mask) + ("1" * (32 - slash_mask))

        #Convert Binary in to IP format Subnet mask
        new_mask = [int(bin_mask[:8], 2), int(bin_mask[8:16], 2), int(bin_mask[16:24], 2), int(bin_mask[24:], 2)]

        new_mask = list(map(str, new_mask))

        #Send the network command to the router
        connected.send("network " + net_ip + " " + ".".join(new_mask) + " area 0\n")
    
    #Wait to make sure command has sent before disconnecting
    time.sleep(1)

    #Disconnect from the router
    connected.close()

#Close Paramiko SSH connection client
client.close()

#Print finished time to the screen
print('{:.3f}'.format(time.time() - start))