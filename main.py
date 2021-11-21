#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest=" interface", help="interface to be getting new mac address")
    parser.add_option("-m", "--mac", dest=" New_mac", help="to enter new mac address")
    return parser.parse_args()

def change_mac(interface, new_mac):
    print("[+] changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.serach(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-]  Could not read MAC address. ")

(options,arguments) = get_arguments()
c_mac = current_mac(options.interface)
print("current MAC = ", str(c_mac))
change_mac(options.interface, options.new_mac)
