import nmap
import nmap3

nmap3 = nmap3.Nmap()
version_result = nmap3.nmap_version()
print(version_result)
results = nmap3.scan_top_ports("192.168.1.10")
print(results)
results = nmap3.nmap_dns_brute_script("david-Ubuntu.local")
print("\n")
print(results)
results = nmap3.nmap_list_scan("david-Ubuntu")
print("\n")
print(results)
results = nmap3.nmap_os_detection("192.168.1.10")
print("\n")
print(results)
results = nmap3.nmap_subnet_scan("your-host")  # Must be root
print("\n")
print(results)
results = nmap3.nmap_version_detection("your-host")  # Must be root
print("\n")
print(results)
# nmap = nmap3.NmapScanTechniques()
# results = nmap.nmap_fin_scan("192.168.1.10")
# print("\n")
# print(results)
'''
# https://pypi.org/project/python3-nmap/
# https://pypi.org/project/python-nmap/

#mynmap = nmap3.Nmap()
results = nmap.scan_top_ports("192.168.1.10")
print(results)
# And you would get your results in json

#results = mynmap.nmap_list_scan("127.0.0.1")
#print(results)
'''
nm = nmap.PortScanner()
nm.scan('192.168.1.10', '22-443')
nm.scan('192.168.1.10', '9000, 9001, 9004, 9005, 514')
nm.command_line()
'nmap -oX - -p 22-443 -sV 127.0.0.1'
nm.scaninfo()
nm.all_hosts()
nm['192.168.1.10'].hostname()
nm['192.168.1.10'].state()
nm['192.168.1.10'].all_protocols()
nm['192.168.1.10']['tcp'].keys()
nm['192.168.1.10'].has_tcp(22)
#nm['192.168.1.10'].has_tcp(23)
#nm['192.168.1.10']['tcp'][22]
#nm['192.168.1.10'].tcp(22)
#nm['192.168.1.10']['tcp'][22]['state']

for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        lport = nm[host][proto].keys()
        # lport = [9000, 9001, 9004, 9005, 514]
        lport.sort()
        for port in lport:
            print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

nm.scan(hosts='192.168.1.10/24', arguments='-n -sP -PE -PA21,23,80,3389')
# nm.scan(hosts='127.0.0.1', arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
print(hosts_list)
for host, status in hosts_list:
    print('{0}:{1}'.format(host, status))

print(nm.csv())


nma = nmap.PortScannerAsync()


def callback_result(host, scan_result):
    print('------------------')
    print(host, scan_result)


nma.scan(hosts='192.168.1.0/24', arguments='-sP', callback=callback_result)
while nma.still_scanning():
    print("Waiting >>>")
    nma.wait(2)  # you can do whatever you want but I choose to wait after the end of the scan

nm = nmap.PortScannerYield()
for progressive_result in nm.scan('127.0.0.1/24', '22-25'):
    print(progressive_result)

nm = nmap.PortScanner()
nm.scan('127.0.0.1', '22-40043', timeout=10)
