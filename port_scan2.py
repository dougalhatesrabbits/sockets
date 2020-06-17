import nmap
import nmap3

mynmap = nmap3.Nmap()
results = mynmap.scan_top_ports("127.0.0.1")
print(results)
# And you would get your results in json


results = mynmap.nmap_list_scan("127.0.0.1")
print(results)


nm = nmap.PortScanner()
#nm.scan('127.0.0.1', '22-443')
nm.scan('127.0.0.1', '9000, 9001, 9004, 9005, 514')
nm.command_line()


for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        lport = nm[host][proto].keys()
        #lport = [9000, 9001, 9004, 9005, 514]
        #lport.sort()
        for port in lport:
            print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

nm.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
#nm.scan(hosts='127.0.0.1', arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
print(hosts_list)
for host, status in hosts_list:
   print('{0}:{1}'.format(host,status))



