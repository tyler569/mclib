#!/usr/bin/env python

"""
Minecraft connector library for python2.7
Copyright (c) 2014, Tyler Philbrick
See COPYING for license information
"""

import socket
from varInt import varInt


class MClib(object):
	"""
	"""
	def __init__(self):
		self.sock = socket.socket()
		self.version = 4

	def connect(self, server_info):
		"""
		"""
		self.server_info = server_info
		self.sock.connect(server_info)
		self._handshake(1)
		# self.read_lines()

	def _handshake(self, state):
		"""
		"""
		pID = varInt(0)
		version = varInt(self.version)
		address = self.server_info[0]
		addrlen = varInt(len(address))
		port = self.server_info[1]
		portS = chr(port % 256) + chr((port >> 8) % 256)
		state = varInt(state)

		sendi = pID.str
		print(sendi)
		sendi += version.str
		print(sendi)
		sendi += addrlen.str
		print(sendi)
		sendi += address
		print(sendi)
		sendi += portS
		print(sendi)
		sendi += state.str
		print(sendi)
		plen = varInt(len(sendi))
		send = str(plen) + sendi

		print(send)
		# self.sock.send(send)

	def read_lines(self):
		"""
		"""
		while True:
			inp = self.sock.recv(1024)
			if not inp: break
			print(inp)
