"""
network_scanner.py: Handles scanning of given target addresses returning that status of the ports and optionally their
service type.

Add desired hosts to scan to hosts.txt before running the script. Each host should be in a new line.
"""

__author__ = "Elmoatazbellah Mohamed"
__version__ = "0.1.0"

import nmap

def scan(targets, with_services=False):
    """
    Main function to start the attack simulation on given url. Vulnerabilities of the site are tested and reported.
    :param targets: The target addresses to scan.
    :param with_services: Optional flag to scan with services.
    """
    try:
        scanner = nmap.PortScanner()
    except nmap.PortScannerError:
        print("Port Scanner Error. Please make sure your system has nmap installed.")
        return

    # Nmap options set to scan with TCP SyYN stealth scan through ports 1 to 1000. Optionally can scan services.
    if with_services:
        options = "-sS -sV -p 1-1000"
        print("Scan will start with services for ports 1 to 1000")
    else:
        options = "-sS -p 1-1000"
        print("Scan will start with ports 1 to 1000")

    # Run the Nmap scan with the specified options
    try:
        # Loop through target addresses
        for target in targets:
            print("Scanning: ", target)
            scanner.scan(target, arguments=options)

            # Show report of the scan results
            for host in scanner.all_hosts():
                print("Host: ", host)
                print("State: ", scanner[host].state())
                for proto in scanner[host].all_protocols():
                    print("Protocol: ", proto)
                    ports = scanner[host][proto].keys()
                    for port in ports:
                        print("Port: ", port, "State: ", scanner[host][proto][port]['state'])
                        # Only print services if option is picked and port is open
                        if with_services and scanner[host][proto][port]['state'] == 'open':
                            print("Service: ", scanner[host][proto][port]['name'])

    except nmap.PortScannerError:
        print("Port Scanner Error")
        return

if __name__ == "__main__":
    hosts = []
    # Get hosts from file
    try:
        hosts_lines = open("hosts.txt", "r").readlines()
    except:
        print("Could not read or find file hosts.txt. Exiting...")
        exit()

    # Ask user whether to scan with services
    user_choice = input("Do you wish to scan with services of open ports? y/n: ")
    if user_choice.lower() == "y":
        scan_with_services = True
    else:
        scan_with_services = False

    # Loop through all lines in hosts.txt and extract hosts into a list
    for line in hosts_lines:
        line = line.strip()
        hosts.append(line)

    # Start scanning hosts
    scan(hosts, scan_with_services)