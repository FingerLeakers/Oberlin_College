# Author: Trevor Martin
# Date of Completion: 21 March 2019
# Language: Makefile
# Class: CSCI 241 | Systems Programming | Oberlin College
# Homework#: 4, Makefile
#===================================================================================================
# DESCRIPTION
#===================================================================================================
# Compiles all of HW4's programs.
#===================================================================================================  

all: freq tooctal todecimal tobinary tohex encode_bits decode_bits

freq: freq.c
	gccx -o freq freq.c

tooctal: tooctal.c
	gccx -o tooctal tooctal.c

todecimal: todecimal.c
	gccx -o todecimal todecimal.c

tobinary: tobinary.c
	gccx -o tobinary tobinary.c

tohex: tohex.c
	gccx -o tohex tohex.c

encode_bits: encode_bits.c
	gccx -o encode_bits encode_bits.c

decode_bits: decode_bits.c
	gccx -o decode_bits decode_bits.c

clean:
	rm -f freq bits encode_bits decode_bits todecimal tobinary tooctal tohex
