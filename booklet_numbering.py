#!/usr/bin/env python3
"""
Prints the numbering required for printing a booklet
"""
from __future__ import print_function, division
import sys
import argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('N', type=int, help='Number of pages, must be a multiple of 4')
args = parser.parse_args()

if args.N <= 0:
    print('N must be strictly positive')
    sys.exit(0)
if 4*(args.N//4) != args.N:
    print('N must be a multiple of 4')
    sys.exit(0)

for j in range(args.N//4):
    i = 2*j
    print(args.N-i, i+1, i+2, args.N-(i+1), sep=' ', end=' ')

print('')
