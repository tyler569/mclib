#!/usr/bin/env python

"""
Minecraft client program for python2.7
Copyright (c) 2014, Tyler Philbrick
See COPYING for license information
"""

import lib.MClib


x = MClib.MClib()
x.connect(("rsw.openredstone.org", 25567))
