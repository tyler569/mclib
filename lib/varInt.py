

"""
VarInt class for python3
Copyright (c) 2014, Tyler Philbrick
See COPYING for license information
"""

class varInt(object):
	def __init__(self, num, byteorder="big"):
		"""
		"""
		self.byteorder = byteorder
		if isinstance(num, int):
			self.int = num
			self.bytes = self.iToV(num)
		elif isinstance(num, bytes):
			self.bytes = num
			self.int = self.vToI(num)
		elif isinstance(num, varInt):
			self = num
		else:
			raise TypeError("Value must be int, varInt, or bytes object representing a varInt")

	def vToI(self, v):
		"""
		"""
		if type(v) is not bytes:
			raise TypeError()
		i = 0
		arr = [char & 0x7f for char in v]
		if self.byteorder == "little":
			arr = reversed(arr)
		for p, num in enumerate(arr):
			i += num << (p*7)
		return i

	def iToV(self, i):
		"""
		"""
		if (type(i) is not int) or (i < 0):
			raise TypeError()
		if i == 0:
			return b"\x00"
		arr = bytearray()
		while i > 0:
			arr.append(i % 0x80)
			i >>= 7
		arr_out = []
		for p, c in enumerate(arr):
			if p != len(arr) - 1:
				arr_out.append(c + 0x80)
			else:
				arr_out.append(c)
		if self.byteorder == "little":
			arr_out = reversed(arr_out)
		return bytes(arr_out)

	def __int__(self):
		return self.int

	def __bytes__(self):
		return self.bytes

