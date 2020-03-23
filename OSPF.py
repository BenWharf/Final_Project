import re

output = '''
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            209.165.200.233 YES NVRAM  up                    up
FastEthernet0/1            unassigned      YES NVRAM  administratively down down
Serial1/0                  172.16.1.2      YES NVRAM  up                    down
Serial1/1                  172.16.2.2      YES NVRAM  up                    down
Serial1/2                  unassigned      YES NVRAM  administratively down down
Serial1/3                  unassigned      YES NVRAM  administratively down down
Serial2/0                  unassigned      YES NVRAM  administratively down down
Serial2/1                  unassigned      YES NVRAM  administratively down down
Serial2/2                  unassigned      YES NVRAM  administratively down down
Serial2/3                  unassigned      YES NVRAM  administratively down down
'''

ospf_set = ["router ospf 1"]

ips = re.findall("\d+\.\d+\.\d+\.\d+", output)
passive = re.findall("\d+\.\d+\.\d+\.\d+", output)

for ip in ips:
    ospf_set.append("network " + ip)

print(ospf_set)
