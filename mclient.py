#!/usr/bin/env python3

"""
Minecraft client program for python3
Copyright (c) 2014, Tyler Philbrick
See COPYING for license information
"""

import lib.mclib as mclib

import json

x = mclib.client()
a = ("l.vms.pw", 25565)
b = ("mort.openredstone.org", 25569)
c = ("rsw.openredstone.org", 25566)
x.connect(b)
x.status()

for i in x.read_lines():
	print(i)
