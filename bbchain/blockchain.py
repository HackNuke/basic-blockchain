# -*- coding: utf-8 -*-
# bbchain - Basic cryptocurrency, based on blockchain, implemented in Python
#
# Copyright (C) 2017-present Jeremies Pérez Morata
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import shelve
from bbchain.block import Block	

class BlockChain(object):
	def __init__(self):
		self.blocks = []
		self.blocks.append(self.create_genesis_block())
		
	def add_block(self, data):
		prev_block = self.blocks[len(self.blocks)-2]
		new_block = Block(data, prev_block.hash)
		self.blocks.append(new_block)
		
	def create_genesis_block(self):
		return Block("Genesis Block", b'')