#****************
#* 1 Router SSH *
#****************
import netmiko, time

#Start in-code timer
start = time.time()

#Connect to the router using these details
router = netmiko.ConnectHandler(
    "192.168.0.1",
    username="admin",
    password="admin",
    device_type="cisco_ios",
)

#Send success message to the screen
print("Router Connected")

#Disconnect from the router
router.disconnect()

#Print finished time to the screen
print('{:.3f}'.format(time.time() - start))

#****************
#* 2 Router SSH *
#****************
import netmiko, time

#Start in-code timer
start = time.time()

#Put the router information in Dictionaries
#that are placed into a Python list
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

#Run through the python list in a loop
for router in two_routers:

    #Connect to the router in the current loop
    connected = netmiko.ConnectHandler(**router)

    #Send success message to the screen
    print("Router Connected")

    #Disconnect from router
    connected.disconnect()

#Print finished time to the screen
print('{:.3f}'.format(time.time() - start))

#****************
#* 3 Router SSH *
#****************
import netmiko, time

start = time.time()

#Put the router information in Dictionaries
#that are placed into a Python list
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

#Run through the python list in a loop
for router in two_routers:

    #Connect to the router in the current loop
    connected = netmiko.ConnectHandler(**router)

    #Send success message to the screen
    print("Router Connected")

    #Disconnect from router
    connected.disconnect()

#Print finished time to the screen
print('{:.3f}'.format(time.time() - start))