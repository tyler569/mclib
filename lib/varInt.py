

"""
VarInt class for python3
Copyright (c) 2014, Tyler Philbrick
See COPYING for license information
"""

class varInt(object):
	def __init__(self, num, byteorder="big"):
		self.byteorder = byteorder
		if isinstance(num, int):
			self.val = num
			self.str = self.iToV(num)
		elif isinstance(num, str):
			self.str = num
			self.val = self.vToI(num)
		elif isinstance(num, varInt):
			self = num
		else:
			raise TypeError("Value must be int or varInt")

	def __int__(self):
		return self.val

	def __str__(self):
		return self.str

	
	def vToI(self, v):
		if type(v) is not str:
			raise TypeError()
		arr = []
		for char in v:
			arr.append(ord(char) & 0x7f)
		i = 0
		for p, num in enumerate(arr):
			i += num << (p*7)
		return i
	
	def iToV(self, i):
		if (type(i) is not int) or (i < 0):
			raise TypeError()
		arr = []
		if i == 0:
			return "\x00"
		while i > 0:
			arr.append(i % 0x80)
			i >>= 7
		arro = []
		for p, c in enumerate(arr):
			if p != len(arr) - 1:
				arro.append(c + 0x80)
			else:
				arro.append(c)
		v = ""
		if self.byteorder == "big":
			arro = reversed(arro)
		for char in arro:
			v += chr(char)
		return v
