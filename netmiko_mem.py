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

    mem_use = re.search("\d{8}\s+\d+", connected.send_command("show memory statistics")).group()

    max_mem = mem_use.split()[0]

    bef_mem_used = mem_use.split()[1]

    bef_mem_per = '{:.2f}'.format(int(bef_mem_used) / int(max_mem) *100)

    ospf_set = ["router ospf 1"]

    output = connected.send_command("show ip route connected")

    networks = re.findall("\d+\.\d+\.\d+\.\d+/\d\d", output)

    for network in networks:

        net_ip = network.split("/")[0]

        slash_mask = int(network.split("/")[1])

        bin_mask = ("0" * slash_mask) + ("1" * (32 - slash_mask))

        new_mask = [int(bin_mask[:8], 2), int(bin_mask[8:16], 2), int(bin_mask[16:24], 2), int(bin_mask[24:], 2)]

        new_mask = list(map(str, new_mask))

        ospf_set.append("network " + net_ip + " " + ".".join(new_mask) + " area 0\n")

        ospf_set.append("passive-interface fa 0/0")
    
    connected.send_config_set(ospf_set)

    mem_use = re.search("\d{8}\s+\d+", connected.send_command("show memory statistics")).group()


    aft_mem_used = mem_use.split()[1]

    aft_mem_per = '{:.2f}'.format(int(aft_mem_used) / int(max_mem) *100)

    connected.disconnect()

    print("Memory Usage Before OSPF:" + str(bef_mem_per) + "%")
    print("Memory Usage After OSPF:" + str(aft_mem_per) + "%\n")

print('{:.3f}'.format(time.time() - start))