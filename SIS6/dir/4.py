import os

path = r'/Users/abylay/PP2_ab.abilay/SIS6/dir/text.txt'

with open(path, 'r') as f:
	lines = len(f.readlines())
	print(lines)