import os
import sys
import typing
from typing import List
import argparse
from abc import ABC

def two_sum(arr: List[int], num):
    records = {}
    for index, i in enumerate(arr):
        print(num-i,records.get(num-i))
        print(records)
        if records.get(num-i) is not None:
            print("inside")
        return records.get(num-i), index
    records[i]=index



def test_function():
    print("this is a test function")


def test_function2():
    pass


class DataWrangler(ABC):
    def __init__(self, sum: int):
        self.sum = sum
    def compute_two_sum(self, arr: list) -> List[int]:
        return two_sum(arr, self.sum)


class BinarySearcher:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
        return -1
            

if __name__ == "__main__":
    # this is for running two_sum and dataWrangler
    # print("start")
    # p = argparse.ArgumentParser()
    # p.add_argument('arr', nargs="+", type=int)
    # p.add_argument('--num', type=int)
    # print(sys.argv)
    # parser = p.parse_args()
    # print(parser)
    # print(parser.arr)
    # print(two_sum(parser.arr, parser.num))
    # data = DataWrangler(parser.num)
    # results = data.compute_two_sum(parser.arr)
    # print(results)

     print(BinarySearcher().search([1,3,4,6,7], 6))
