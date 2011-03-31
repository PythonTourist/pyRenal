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


class extractionEngine():
	sack_size = None
	number_extracted = None
	
	def __init__(self, s = 90, n = 6):
		self.sack_size = s
		self.number_extracted = n

	def calculate(self):
		sack = []
		serie = []
# This will simulate a sack with the sack_size numbers in. This is not necessary for random number extraction,
# is just a mode to intend it.
		for i in range(1,self.sack_size):
			sack.append(i)
# The sack is shuffled        
		random.shuffle(sack)
		i = 0
		while i < self.number_extracted:
# The number is randomly extracted from the sack
			indice = random.randint(0,self.sack_size-1)
# Check if the position is already extracted
			if sack[indice] <> '':
# Add the number extracted at the dated position in the serie
				serie.append(sack[indice])
# Delete the number at the position
				sack[indice] = ''
# The sack is shuffled again at every extraction                
				random.shuffle(sack)
				i = i+1
# Sort the serie       
		serie.sort()
		return serie

if __name__ == '__main__':
	opts, args = getopt.getopt(argv, "h12:d", ["help", "grammar="])
	for opt, arg in opts:                
		if opt in ("-h", "--help"):      
			usage()                     
			sys.exit()                  
		elif opt == '-1':                
			s = 90
			n = 6               
		elif opt == '-2':
			s = 20
			n = 10   
	c = extractionEngine(s, n)
	s = c.calculate()
	print str(s)

