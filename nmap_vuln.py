from nmap_inter import NmapInterface
import nmap
import socket

class NmapVuln(NmapInterface):

    def __init__(self):
        self.scanner = nmap.PortScanner()
        self.ip_address = '127.0.0.1'

    def get_open_services(self):
        # Arguments : --privilliged  in order to gain sudo privileges
        # -v stand for Verbose , it asks for more detailed info in the scan
        # -sV stand for service version , you get the version of all services
        self.scanner.scan(self.ip_address, self.TOP_PORTS_1000, ' --privileged -v -sV -sS')
        scan_res = "Opened Ports : " + str(self.scanner[self.ip_address]['tcp'].keys())
        ports = self.scanner._scan_result['scan'][self.ip_address]['tcp']
        # get info on every port scanned
        for port in ports:
            product = ports[port]['product']
            if product != '':
                scan_res += "\n" + "Port " + str(port) + " Service: " + product + ports[port]['version']
            else:
                name = ports[port]['name']
                scan_res += "\n" + "Port "+str(port)+" Service: "+name
        return scan_res

    def get_operating_system(self):
        machine = self.scanner.scan(self.ip_address, self.TOP_PORTS_1000, '--privileged -O')['scan'][self.ip_address]
        machine = machine['osmatch'][0]['name']
        return "Operating System is : "+machine + "\n Please mind the script doesn't gurentee it's the right " \
                                                  "OS, it's a wild guess based on the behaviour of the machine "

    def get_vulnerabilities(self):
        # -sV stand for service version , you get the version of all services
        # nmap-vulners script from NSE is being used
        try:
            self.scanner.scan(self.ip_address, self.TOP_PORTS_1000, arguments='--script /home/niv/nmap-vulners/ -sV')
            ports = self.scanner._scan_result['scan'][self.ip_address]['tcp']
            vulner = ''
            keys_list = list(ports.keys())
            for key in keys_list:
                try:
                    vulner += "Port : " + str(key) + ports[key]['script']['vulners']
                    vulner += "\n"
                except KeyError:
                    pass

            return vulner
        except KeyError as e:
            return "couldn't finish the scan for some reason "

    def set_ip_address(self, ip_address):

        host_name = str(ip_address).strip()
        self.ip_address = socket.gethostbyname(host_name)
        print("set the ip to : ", self.ip_address)
