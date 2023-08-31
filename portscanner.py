from socket import *
from os import system, name
import threading, time, timeit

class PortScan:
    def __init__(self, target, start_port, end_port):
        self.target, self.start_port, self.end_port, self.open_ports = target, start_port, end_port, []
       
    def clear_screen(self):
        if name == 'nt':
            _ = system('cls')

    def get_target(self):
        try:
            self.target_IP = gethostbyname(self.target)
        except gaierror:
            print(f"Invalid host IP address: {self.target}\nPlease try again.")
            time.sleep(2)
            self.clear_screen()
            self.get_target()


    def scan_port(self, port):
            sock = socket(AF_INET, SOCK_STREAM)
            sock.settimeout(1e-04)
            self.connection = sock.connect_ex((self.target, port))
            if self.connection == 0:
                print(f"Port {port}: OPEN")
                self.open_ports.append(port)
            sock.close()
   
    def scan_ports(self):
        print(f"\nScanning port(s) {self.start_port}-{self.end_port} on host : {self.target}\n")
        start_time = timeit.default_timer() 

        threads = [] 
        
        for port in range(self.start_port, self.end_port + 1):
            thread = threading.Thread(target=self.scan_port, args=(port,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
        
        if self.start_port == self.end_port and self.connection == 1 or self.open_ports == []:
            print(f'Port(s) {self.start_port}-{self.end_port}: CLOSED')
        if self.open_ports == []:
            self.open_ports = [None]

        print(f"\nOpen port(s) : {self.open_ports}")

        end_time = timeit.default_timer()
        print(f"\nScan complete. Time taken: {end_time - start_time:.2f} seconds")
        input('\nPress ENTER to exit...')
