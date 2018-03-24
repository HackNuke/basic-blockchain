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

import sys
from japronto import Application
from bbchain.net.network import Server

class HttpServerMiner(Server):
	def __init__(self, host, port, bc):
		super().__init__(host, port, bc)
		
	def start_miner(self):
		app = Application()
		app.router.add_route('/add_data', self.add_data)
		app.router.add_route('/', self.help_miner)
		app.run(debug=True, host=self.host, port=self.port)
	
	def help_miner(self, request):
		return request.Response(json={
			"help": []	
		})
		
	def add_data(self, request):
		return request.Response(json={"Status": "OK"})
			
	
class HttpServerMaster(Server):
	def __init__(self, host, port, bc):
		super().__init__(host, port, bc)
		
	def start_master(self):
		app = Application()
		app.router.add_route('/get_blocks', self.get_blocks)
		app.router.add_route('/', self.help_master)
		app.run(debug=True, host=self.host, port=self.port)

	def help_master(self, request):
		return request.Response(json={
			"help": [
				"get_blocks",
			]
		})
			
	def get_blocks(self, request):
		count = int(request.query['count']) if 'count' in request.query else 10
		pointer = request.query['from_hash'] if 'from_hash' in request.query else self.bchain.last_hash
		
		chain = []
		
		while pointer and count > 0:
			block = self.bchain.db.get_block(pointer)
			chain.append(block.to_dict())
			pointer = block.prev_block_hash
			count -= 1

		return request.Response(json={ 'chain': chain})	
		
