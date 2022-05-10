#!/usr/bin/env python

import sys

"""
sys.argv includes the script name as the first arg
This takes everything from the first arg onwards
"""
args = sys.argv[1:]

if len(args) == 0:
	sys.exit("No arguments given. Exiting.\n")

for arg in args:

	# Split string into an array of letters.
	letters = list(arg)

#TODO
def capitalise():
	return upper()
