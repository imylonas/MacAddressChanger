#!/usr/bin/env python
"""
One simple Mac Address Changer in order to
upgrade my Python programming skills!
"""

# Subprocess module allows us to use system commands
import subprocess

subprocess.call("ifconfig", shell=True)
subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:12:23:34:45:56", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
subprocess.call("ifconfig", shell=True)
