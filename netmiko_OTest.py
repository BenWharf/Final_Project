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

def connection_test (neighbour_id, neighbour_ip):

    ping_result = re.search(r"\d+\s\bpercent", connected.send_command("ping " + neighbour_ip)).group()
    print("Connection to Neighbour Router", neighbour_id, "is:", ping_result, "successful")

for router in three_routers:

    connected = netmiko.ConnectHandler(**router)

    router_id = re.search(r"\d+.\d+.\d+.\d+", connected.send_command("show ip ospf")).group()

    print("The current Router is:", router_id)

    ospf_neighbour = re.findall(r"\d+.\d+.\d+.\d+", connected.send_command("show ip ospf neighbor"))

    if(len(ospf_neighbour) == 2):
        connection_test(ospf_neighbour[0], ospf_neighbour[1])

    elif (len(ospf_neighbour) > 2 and len(ospf_neighbour) % 2 == 0):

        ospf_neighbour = iter(ospf_neighbour)

        for x in ospf_neighbour:
            connection_test(x, next(ospf_neighbour))
    
    connected.disconnect()
    print(" ")

print('{:.3f}'.format(time.time() - start))