from typing import List, Tuple, Union
import argparse
from abc import ABC
import sys


def two_sum(arr: List[int], num) -> Union[Tuple[int, int], None]:
    records = {}
    for index, i in enumerate(arr):
        print(num - i, records.get(num - i))
        print(records)
        if records.get(num - i) is not None:
            print("inside")
            return records[num - i], index


def test_function():
    print("this is a test function")


def test_function2():
    pass


class DataWrangler(ABC):
    def __init__(self, sum: int):
        self.sum = sum

    def compute_two_sum(self, arr: list):
        return two_sum(arr, self.sum)


if __name__ == "__main__":
    print("start")
    p = argparse.ArgumentParser()
    p.add_argument("arr", nargs="+", type=int)
    p.add_argument("--num", type=int)
    print(sys.argv)
    parser = p.parse_args()
    print(parser)
    print(parser.arr)
    print(two_sum(parser.arr, parser.num))
    data = DataWrangler(parser.num)
    results = data.compute_two_sum(parser.arr)
    print(results)
