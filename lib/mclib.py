#!/usr/bin/env python

"""
Minecraft connector library for python3
Copyright (c) 2014, Tyler Philbrick
See COPYING for license information
"""

import socket
from lib.varInt import varInt


class client(object):
	"""
	"""
	def __init__(self):
		self.sock = socket.socket()
		self.protocol_version = 5

	def _send(self, raw_data):
		self.sock.send(raw_data)

	def connect(self, server_info):
		"""
		"""
		self.server_info = server_info
		self.sock.connect(server_info)
		self._handshake(1)
		self.read_lines()

	def _assemble_packet(self, *data):
		print(data)
		raw = ''.join((str(i) for i in data))
		plen = varInt(len(raw))
		send = str(plen) + raw
		return send

	def _handshake(self, state):
		"""
		"""
		pID = varInt(0)
		version = varInt(self.protocol_version)
		address = self.server_info[0]
		addrlen = varInt(len(address))
		port = self.server_info[1]
		portS = chr(port % 256) + chr((port >> 8) % 256)
		state = varInt(state)

		data = [pID, version, addrlen, address, portS, state]
		self.sock.send(self._assemble_packet(*data))

	def status(self):
		self._handshake(1)
		data = [varInt(0)]
		self.sock.send(self._assemble_packet(*data))

	def _pong(self):
		pass

	def read_lines(self):
		"""TODO: have this track packet lengths so it can respond to pings/etc
		TODO: encryption
		"""
		while True:
			inp = self.sock.recv(1024)
			if not inp: break
			yield inp
