import os
import sys
import typing
from typing import List
import argparse


def two_sum(arr: List[int], num):
	records = {}
	for index, i in enumerate(arr):
		print(num-i,records.get(num-i))
		print(records)
		if records.get(num-i) is not None:
			print("inside")
			return records.get(num-i), index
		records[i]=index
	

if __name__ == "__main__":
	print("start")
	p = argparse.ArgumentParser()
	p.add_argument('arr', nargs="+", type=int)
	p.add_argument('--num', type=int)
	print(sys.argv)
	parser = p.parse_args()
	print(parser)
	print(parser.arr)
	print(two_sum(parser.arr, parser.num))
