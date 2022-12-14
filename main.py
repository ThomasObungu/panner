from socket import *
import time
import re

portRangeFormat = re.compile("([0-9]+)-([0-9]+)")

runTime = time.time()

channel = socket(AF_INET, SOCK_STREAM)

openPorts=[]   

if __name__=="__main__":
    target = input('Enter host for scanning (Type "127.0.0.1" for localhost): ').lower()
    targetIP = gethostbyname(target)
    
    while True:
        portRange = input("Enter the range of ports you want to scan in <int>-<int> format (e.g 20-25) : ")
        
        portRangeValidFormat = portRangeFormat.search(portRange.replace(" ",""))
        
        if portRangeValidFormat:
          minPortRange=int(portRangeValidFormat.group(1))
          maxPortRange=int(portRangeValidFormat.group(2))
          break

    print(f'\nScanning port(s): {portRange} on host: {targetIP}\n')
    
    for i in range(minPortRange, maxPortRange):
        connection = channel.connect_ex((targetIP, i))
        
        print(f'Port {i}: OPEN') if connection==0 else print(f'Port {i}: CLOSED')
        
        if connection==0:
                openPorts.append(i)
    
    channel.close

print(f'\nOpen ports : {openPorts}')
print(f'Time taken: {time.time() - runTime}')
input('\nPress ENTER to exit')
