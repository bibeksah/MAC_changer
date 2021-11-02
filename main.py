#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="interface to be getting new mac address")
parser.add_option("-m", "--mac", dest="New_mac", help="to enter new mac address")

(options, arguments) = parser.parse_args()
interface = options.interface
new_mac = options.new_mac

print("[+] changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
