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

    connected.send("show ip route connected\n")

    output = ""
    time.sleep(1)
    while not connected.recv_ready():
        continue

    while connected.recv_ready():
        output = output + connected.recv(65535).decode('utf-8')

    networks = re.findall(r"\d+\.\d+\.\d+\.\d+/\d\d", output)

    connected.send("configure terminal\n")

    connected.send("router ospf 1\n")

    for network in networks:

        net_ip = network.split("/")[0]

        slash_mask = int(network.split("/")[1])

        bin_mask = ("0" * slash_mask) + ("1" * (32 - slash_mask))

        new_mask = [int(bin_mask[:8], 2), int(bin_mask[8:16], 2), int(bin_mask[16:24], 2), int(bin_mask[24:], 2)]

        new_mask = list(map(str, new_mask))

        connected.send("network " + net_ip + " " + ".".join(new_mask) + " area 0\n")
    time.sleep(1)
    connected.close()

client.close()

print('{:.3f}'.format(time.time() - start))