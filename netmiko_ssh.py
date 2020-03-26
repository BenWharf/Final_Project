#1 Router SSH
import netmiko, time

start = time.time()

router = netmiko.ConnectHandler(
    "192.168.0.1",
    username="admin",
    password="admin",
    device_type="cisco_ios",
)

print("Router Connected")

router.disconnect()

print('{:.3f}'.format(time.time() - start))

#2 routers SSH
import netmiko, time

start = time.time()

two_routers = [{
    "host":"192.168.0.1",
    "username":"admin",
    "password":"admin",
    "device_type":"cisco_ios"
    }, {
    "host":"192.168.0.2",
    "username":"admin",
    "password":"admin",
    "device_type":"cisco_ios"
    }]

for router in two_routers:

    connected = netmiko.ConnectHandler(**router)

    print("Router Connected")

    connected.disconnect()

print('{:.3f}'.format(time.time() - start))

#3 Router SSH
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

    print("Router Connected")
    
    connected.disconnect()

print('{:.3f}'.format(time.time() - start))