import netmiko, time

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

    netmiko.file_transfer(connected, source_file="startup-config", dest_file = "/root/" + router["host"] + "config.txt", 
                          file_system = "nvram:", direction="get")

    print(router["host"], "Config Backed Up")
    
    connected.disconnect()

print('{:.3f}'.format(time.time() - start))