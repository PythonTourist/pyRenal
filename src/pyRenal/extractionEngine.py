#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       extractionEngine.py
#       
#       Copyright 2011 A144220 <A144220@A144220W>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#       

import random
import sys
import getopt


class extractionEngine():
	sack_size = None
	number_extracted = None
	sack = []
	serie = []
	
	def __init__(self, s = 90, n = 6):
		self.sack_size = s
		self.number_extracted = n
		self.sack = []
		self.serie = []

	def calculate(self):
		# self.sack = []
		# self.serie = []
# This will simulate a sack with the sack_size numbers in. This is not necessary for random number extraction,
# is just a mode to intend it.
		for i in range(1,self.sack_size+1):
			self.sack.append(i)
# The sack is shuffled        
		random.shuffle(self.sack)
		i = 0
		while i < self.number_extracted:
# The number is randomly extracted from the sack
			indice = random.randint(0,self.sack_size-1)
# Check if the position is already extracted
			if self.sack[indice] <> '':
# Add the number extracted at the dated position in the serie
				self.serie.append(self.sack[indice])
# Delete the number at the position
				self.sack[indice] = ''
# The sack is shuffled again at every extraction                
				random.shuffle(self.sack)
				i = i+1
# Sort the serie       
		self.serie.sort()
		return self.serie

# BEST_OF_N: Take the most extracted numbers in N extraction		
	def bestofn(self):
		stats = {}
		j = 0
# Initialize the stats matrix		
		for i in range(1,self.sack_size+1):
			stats[i] = 0

		while j < 500000:
			indice = random.randint(1,self.sack_size)
			stats[indice] = stats[indice] + 1
			j = j + 1
		items = stats.items()
		backitems=[ [v[1],v[0]] for v in items]
		backitems.sort(reverse=True)
		sortedlist=[ backitems[i][1] for i in range(0,len(backitems))]
		for i in range(0,self.number_extracted):
			self.serie.append(sortedlist[i])
		self.serie.sort()
		return self.serie
	
if __name__ == '__main__':
	opts, args = getopt.getopt(sys.argv[1:], "h1:2:")
	result = []
	c = extractionEngine()
	for opt, arg in opts:                
		if opt in ("-h", "--help"):     
			print("Accepted parameteres:")
			print("-1 SuperEnalotto")
			print("-2 Win4Life")
			print("-b Best of N")
			# usage()                     
			sys.exit()                  
		elif opt in ("-1"):
			s = 90
			n = 6
			c = extractionEngine(s, n)
		elif opt in ("-2"):
			s = 20
			n = 10
			c = extractionEngine(s, n)
		if arg in ("standard"):
			result = c.calculate()
			print (str(result))
		elif arg in ("bestofn"):
			result = c.bestofn()
			print (str(result))	
			
	
