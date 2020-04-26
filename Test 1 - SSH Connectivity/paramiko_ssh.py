#****************
#* 1 Router SSH *
#****************
import paramiko, time

#Start in-code timer
start = time.time()

#Create the Paramiko SSH Client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Connect to the router using these details
router = client.connect(
    "192.168.0.1",
    username="admin",
    password="admin"
)

#Send success message to the screen
print("Router Connected")

#Disconnect from router
client.close()

#Print finished time to the screen
print('{:.3f}'.format(time.time() - start))

#****************
#* 2 Router SSH *
#****************
import paramiko, time

#Start in-code timer
start = time.time()

#Create the Paramiko SSH Client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

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
    client.connect(router['host'], username=router['username'], password=router['password'])

    #Send success message to the screen
    print("Router Connected")

    #Disconnect from router
    client.close()

#Print finished time to the screen
print('{:.3f}'.format(time.time() - start))

#****************
#* 3 Router SSH *
#****************
import paramiko, time

#Start in-code timer
start = time.time()

#Create the Paramiko SSH Client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

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
for router in three_routers:

    #Connect to the router in the current loop
    client.connect(router['host'], username=router['username'], password=router['password'])

    #Send success message to the screen
    print("Router Connected")

    #Disconnect from router    
    client.close()

#Print finished time to the screen
print('{:.3f}'.format(time.time() - start))