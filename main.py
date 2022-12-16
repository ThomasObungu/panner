from socket import *
import time
import timeit
from os import system, name

# Define a function to clear the console screen
def clear():
       if name == 'nt':
        _= system('cls')

open_ports = []

if __name__ == "__main__":
    # Define a function to get the target IP address from the user
    def getarget():
        # Prompt the user to enter a host for scanning
        global target
        target=input("Enter host for scanning (Type 127.0.0.1 for localhost): ")
        # Try to convert the hostname to an IP address
        try:
            target_IP = gethostbyname(target)
        # If an error occurs, print an error message and prompt the user to try again
        except gaierror:
            print(f"Invalid host IP address: {target}\nPlease try again.")
            time.sleep(2)
            clear()
            getarget()
    # Call the getarget() function to get the target IP address from the user
    getarget()

    # Convert the hostname to an IP address and handle any errors that may occur
    try:
        target_IP = gethostbyname(target)
    except gaierror:
        print(f"Error: Invalid host IP address: {target}\nPlease try again.")
        time.sleep(2)
        clear()
        getarget()
        
    # Prompt the user to enter a range of ports to scan
    port_range = input("Enter the range of ports to scan (e.g 0-1024) or a single port (e.g 445): ")

    # If the port range contains a dash, split it into start_port and end_port
    if "-" in port_range:
        start_port, end_port = map(int, port_range.split("-"))
    # Otherwise, treat the entire input as the value for start_port
    else:
        start_port = int(port_range)    
        # If a single port is provided, end_port will be the same as start_port
        end_port = start_port

    # Print the target IP address and port range being scanned
    print(f"\nScanning port(s) {port_range} on host : {target_IP}\n")

    # Record the start time of the scan
    start_time = timeit.default_timer() 

    # Scan each port in the specified range
    for port in range(start_port, end_port + 1):
        # Create a new socket
        sock = socket(AF_INET, SOCK_STREAM)
        # Set a timeout of 0.0001 seconds for the socket
        sock.settimeout(1e-04)
        # Try to connect to the port
        connection = sock.connect_ex((target_IP, port))
        # If the connection is successful, print the port number and add it to the list of open ports
        if connection == 0:
            print(f"Port {port}: OPEN")
            open_ports.append(port)
        # Close the socket
        sock.close()

    # If a single port or the ports scanned are closed, print a message indicating that they are closed
    if start_port==end_port and connection==1 or open_ports==[]:
        print(f'Port(s) {port_range}: CLOSED')

    # If the list of open ports is empty, set it to None
    if open_ports==[]:
        open_ports=[None]

    # Print the list of open ports
    print(f"\nOpen port(s) : {open_ports}")

    # Record the end time of the scan
    end_time = timeit.default_timer()
    
    # Print the time taken to complete the scan
    print(f"\nScan complete. Time taken: {end_time-start_time:.2f} seconds")

    # Wait for the user to press ENTER before closing the program
    input('\nPress ENTER to exit...')
