#1 Router SSH
import paramiko, time

start = time.time()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router = client.connect(
    "192.168.0.1",
    username="admin",
    password="admin"
)

print("Router Connected")

client.close()

print('{:.3f}'.format(time.time() - start))

#2 Router SSH
import paramiko, time

start = time.time()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

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

    client.connect(router['host'], username=router['username'], password=router['password'])

    print("Router Connected")

    client.close()

print('{:.3f}'.format(time.time() - start))

#3 Router SSH
import paramiko, time

start = time.time()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

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

    client.connect(router['host'], username=router['username'], password=router['password'])

    print("Router Connected")

    client.close()

print('{:.3f}'.format(time.time() - start))