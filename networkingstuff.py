#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n****** details of interface - ' + i + ' ******')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message


print("\n\n    ****    New Stuff    ****    \n")

def print_ip(ifname):
    print(ifname)
    ifname_ip = (netifaces.ifaddresses(ifname)[netifaces.AF_INET])[0]['addr']
    print(ifname_ip)  # Prints the IP address
    return ifname_ip


def print_mac(ifname):
    print(ifname)
    ifname_mac = (netifaces.ifaddresses(ifname)[netifaces.AF_LINK])[0]['addr']
    print(ifname_mac)
    return ifname_mac


ip = print_ip('{D849206B-00B1-4E73-BC8B-4535BDC37B36}')
mac = print_mac('{D849206B-00B1-4E73-BC8B-4535BDC37B36}')

print(ip, mac)
