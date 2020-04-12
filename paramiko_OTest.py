import paramiko, time, re

start = time.time()

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

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def connection_test (neighbour_id, neighbour_ip):

    connected.send("ping " + neighbour_ip + "\n")
    ping_result = ""
    time.sleep(1)
    while not connected.recv_ready():
        continue
    while connected.recv_ready():
        ping_result = ping_result + connected.recv(65535).decode('utf-8')

    ping_result = re.search(r"\d+\s\bpercent", ping_result).group()
    print("Connection to Neighbour Router", neighbour_id, "is:", ping_result, "successful")

for router in three_routers:

    client.connect(router['host'], username=router['username'], password=router['password'])

    connected = client.invoke_shell()
    
    connected.send("show ip ospf\n ")
    router_id = ""
    time.sleep(1)
    while not connected.recv_ready():
        continue
    while connected.recv_ready():
        router_id = router_id + connected.recv(65535).decode('utf-8')
    router_id = re.search(r"\d+.\d+.\d+.\d+", router_id).group()

    print("The current Router is:", router_id)

    connected.send("show ip ospf neighbor\n")
    neighbour_id = ""
    time.sleep(1)
    while not connected.recv_ready():
        continue
    while connected.recv_ready():
        neighbour_ids = neighbour_id + connected.recv(65535).decode('utf-8')

    ospf_neighbour = re.findall(r"\d+.\d+.\d+.\d+", neighbour_ids)

    if(len(ospf_neighbour) == 2):
        connection_test(ospf_neighbour[0], ospf_neighbour[1])

    elif (len(ospf_neighbour) > 2 and len(ospf_neighbour) % 2 == 0):

        ospf_neighbour = iter(ospf_neighbour)

        for x in ospf_neighbour:
            connection_test(x, next(ospf_neighbour))

    connected.close()
    print(" ")

client.close()

print('{:.3f}'.format(time.time() - start))