from socket import *
from os import system, name
import threading, time, timeit
from portscanner import PortScan

def main():
    target = input("Enter host for scanning (Type 127.0.0.1 for localhost): ")
    
    while True:
        try:
            port_range = input("Enter the range of ports to scan (e.g 0-1024) or a single port (e.g 445): ")
            if "-" in port_range:
                start_port, end_port = map(int, port_range.split("-"))
            else:
                start_port = int(port_range)    
                end_port = start_port
            break
        except ValueError:
            print("Invalid port range. Please try again.\n")
    
    scan = PortScan(target, start_port, end_port)
    scan.get_target()
    scan.scan_ports()

if __name__ == "__main__":
    main()
