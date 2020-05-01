# How to Recreate the Topology

#### Topology Diagram
<img src="https://github.com/BenWharf/1716043_Final_Project/blob/master/topology.png" alt="Your image title" width="400"/>

#### Steps to recreate the topology

1. The simulated network devices are put in the configuration shown in the figure below, in this dissertation the router c3725, an unmanaged switch and a simulated Ubuntu Linux PC was used. 

2. Connect the devices in the configuration shown in the figure above. In the case of this topology, the routers were connected using Serial links. The other connections, Router to Switch and PC to Switch used FastEthernet cabling, this may change depending on the device. The exact interfaces used in the experiment are shown below in Table 1.

##### Table 1: Interface Usage Table
Device | Interface to R1 | Interface to R2 | Interface to R3 | Interface to Switch
-------|-----------------|-----------------|-----------------|--------------------
R1 | N/A | Serial | S0/1 |	N/A |	Fast Ethernet 0/0
R2 |	Serial 0/1 |	N/A |	Serial 1/1 |	Fast Ethernet 0/0
R3 |	N/A |	Serial 1/1 |	N/A |	Fast Ethernet 0/0


3. Basic configuration was implemented on each router, shown in Table 2 on the next page. This allowed the routers and PC to connect, over the Secure Shell Protocol version 2.

4. The PC was configured to install the necessary resources needed to complete all the tests. This included installing the latest version of Python, which is Python 3.8 and installing the necessary Python libraries used in the test. These being Paramiko, Netmiko and SCP libraries.

5. Once all the prior steps have been completed the test can be conducted, any additional configuration on the routers was added per test. The in-depth router configurations and the individual commands used to configure the Ubuntu PC can be found in the  	 [Ubuntu PC Setup](https://github.com/BenWharf/1716043_Final_Project/blob/master/Ubuntu%20PC%20Setup.txt) file

##### Table 2: Interface Usage Table
<table>
  <thead>
    <th>Hostname</th>
    <th>R1</th>
    <th>R2</th>
    <th>R3</th>
  </thead>
  <tbody>
    <tr>
      <td>Interfaces/IP Addresses</td>
      <td>Serial Port 0/1:<br> 
          IP: 192.168.12.1<br> 
          Mask: 255.255.255.252<br><br> 
          Fast Ethernet 0/0:<br> 
          IP: 192.168.0.1<br> 
          Mask: 255.255.255.0<br>
      </td>
      <td>Serial Port 0/1:<br> 
          IP: 192.168.12.2<br>
          Mask: 255.255.255.252<br><br>
          Serial Port 1/1:<br>
          IP: 192.168.23.1<br>
          Mask: 255.255.255.252<br><br>
          Fast Ethernet 0/0:<br>
          IP: 192.168.0.2<br>
          Mask: 255.255.255.0
      </td>
      <td>Serial Port 0/1:<br>
          IP: 192.168.12.1<br>
          Mask: 255.255.255.252 <br><br>
          Fast Ethernet 0/0:<br>
          IP: 192.168.0.1<br>
        Mask: 255.255.255.0
      </td>
    </tr>
    <tr>
      <td>SSH Version</td>
      <td colspan=3>Version 2</td>
    </tr>
      <td>SSH Domain Name</td>
      <td>R1.com</td>
      <td>R2.com</td>
      <td>R3.com</td>
    <tr>
      <td>RSA Key Modulus</td>
      <td colspan=3>1024</td>
    </tr>
    <tr>
      <td>Login Username/Password</td>
      <td colspan=3>Username: admin <br> Password: admin</td>
    </tr>
    <tr>
      <td>Virtual Terminals Configured</td>
      <td colspan=3>0 to 4</td>
    </tr>
    <tr>
      <td>Virtual Terminal Login Type</td>
      <td colspan=3>Login Local</td>
    </tr>
    <tr>
      <td>Transport Input</td>
      <td colspan=3>SSH</d>
    </tr>
    <tr>
    </tr>
  </tbody>
</table>
