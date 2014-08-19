#!/usr/bin/env python

"""
Minecraft connector library for python3
Copyright (c) 2014, Tyler Philbrick
See COPYING for license information
"""

import socket
import sys
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
		self.read_lines()

	def _assemble_packet(self, *data):
		raw = b''.join((bytes(i) for i in data))
		plen = varInt(len(raw))
		send = bytes(plen) + raw
		return send

	def _handshake(self, state):
		"""
		"""
		pID = varInt(0)
		version = varInt(self.protocol_version)
		address = self.server_info[0]
		addrlen = varInt(len(address))
		port = self.server_info[1]
		portS = port.to_bytes(2, byteorder="big")
		state = varInt(state)

		data = [pID, version, addrlen, address, portS, state]
		self.sock.send(self._assemble_packet(*data))

	def status(self):
		self._handshake(1)
		data = [varInt(0)] #Request
		self.sock.send(self._assemble_packet(*data))
		data = [varInt(1), b"\xaa\xff\xaa\xff\xaa\xff\xaa\xff"] #Ping
		self.sock.send(self._assemble_packet(*data))

	def login(self, name):
		self._handshake(2)
		data = [varInt(0), varInt(len(name)), name] #Login Start
		self.sock.send(self._assemble_packet(*data))

	def _pong(self):
		pass

	def read_lines(self):
		"""TODO: have this track packet lengths so it can respond to pings/etc
		TODO: encryption
		"""
		buffer = bytearray()
		packet_len = 0
		packet_stt = 0
		while True:
			inp = self.sock.recv(1024)
			if not inp: break
			buffer += inp
			plen = varInt.first(buffer)
			packet_len = int(plen)
			packet_stt = len(bytes(plen))
			if len(buffer) > packet_len:
				yield bytes(buffer[packet_stt:packet_len + packet_stt])
				del buffer[:packet_len + packet_stt]

