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

    ospf_set = ["router ospf 1"]

    output = connected.send_command("show running-config")

    networks = re.findall("\d+\.\d+\.\d+\.\d+\s\d+\.\d+\.\d+\.\d+", output)

    for network in networks:
        print(network)
        netmask = network.split()[1]
        nmconv = netmask.split(".")

        wildcard = []
        for num in nmconv:
            wildcard.append(str(255 - int(num)))
        ospf_set.append("network " + network.replace(netmask, ".".join(wildcard)) + " area 0")
    
    connected.send_config_set(ospf_set)

    connected.disconnect()

print('{:.3f}'.format(time.time() - start))
