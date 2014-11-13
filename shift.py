#!/usr/bin/python
#Evan Widloski
#simulates an arbitrary number of n length shift registers where the output of the first and last flipflop
#of one shift register are connected to the clock and serial pins of the next shift register
#Example: http://imgur.com/weGoXfm

shift_registers=3
bits=4
reg_array=[]
for register in range(0,shift_registers):
	buff=[]
	buff+=[1]
	buff+=[0]*(bits-1)
	reg_array.append(buff)

print reg_array

def shift(bit,register):
	#shift all elements of 'register', then shift in 'bit'
	for index,_ in reversed(list(enumerate(reg_array[register][:-1]))):
		reg_array[register][index + 1]=reg_array[register][index]
	reg_array[register][0]=bit


	#if clock rising edge (first two) and serial
	if not reg_array[register][1] and reg_array[register][0] and reg_array[register][-1]:
		#are we already at the last shift register?
		#if not, shift output to next register
		if register + 1 < shift_registers:
			shift(1,register + 1)
		#otherwise, print the output
		else:
			print 'one'

	if not reg_array[register][1] and reg_array[register][0] and not reg_array[register][-1]:
		if register + 1 < shift_registers:
			shift(0,register + 1)
		else:
			print 'zero'
	
	print reg_array
	
	
while 1:
	#shift numbers forward by 1 element for register 0
	shift(int(raw_input()),0)


