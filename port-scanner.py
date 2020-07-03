#!/bin/python

import sys
import socket
from datetime import datetime

# Define our target

if len(sys.argv) == 2:
    # dns resolves or translates the hostname into the IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print('Invalid amount of arguments supplied ')
    print('SYNTAX: python3 filename.py <ip>')

# Adding the loading banner

print('\n' + "-" * 50)
print("Scanning started for target - " + target)
print("Scanning started at " + str(datetime.now()))
print('-' * 50 + '\n')


try:
    # Scanning in the short port range for faster scanning
    for port in range(1, 65535):

        # First argument is IPV4 address, and second one is the port number.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Attempt to connect the port, if it is connectable, it is going to wait 1 second, else move on.
        socket.setdefaulttimeout(1)

        # Using connect_ex so that it returns the error indicator.
        # If port is open, it is going to trigger 0, else if port is closed it is going to trigger 0.
        result = s.connect_ex((target, port))

        if(result == 0):
            print("Port {} is open".format(port))

        s.close()

except KeyboardInterrupt:
    print('\nExiting program...')
    sys.exit()

except socket.gaierror:
    print('\nHostname couldn\'t be resolved')
    sys.exit()

except socket.error:
    print('Couldn\'t connect to the server ')
