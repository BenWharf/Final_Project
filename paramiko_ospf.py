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

for router in three_routers:

    client.connect(router['host'], username=router['username'], password=router['password'])

    connected = client.invoke_shell()

    connected.send("show running-config\n      ")

    output = ""
    time.sleep(1)
    while not connected.recv_ready():
        continue

    while connected.recv_ready():
        output = output + connected.recv(65535).decode('utf-8')

    networks = re.findall("\d+\.\d+\.\d+\.\d+\s\d+\.\d+\.\d+\.\d+", output)

    connected.send("configure terminal")

    connected.send("router ospf 1")
    for network in networks:
        netmask = network.split()[1]
        nmconv = netmask.split(".")

        wildcard = []
        for num in nmconv:
            wildcard.append(str(255 - int(num)))
        print("network " + network.replace(netmask, ".".join(wildcard)) + " area 0")
        
client.close()

print('{:.3f}'.format(time.time() - start))