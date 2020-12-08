#! /usr/bin/env python3

import os
import requests
from dotenv import load_dotenv

################ GRAB INPUT ################
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file_path = f"{dir_path}/input/day1.txt"
url = "https://adventofcode.com/2020/day/1/input"

load_dotenv(verbose=True, dotenv_path=f"{dir_path}/.env")

if os.path.exists(input_file_path):
    print("Input file exists!")
else:
    print("Grabbing input file!")
    secret = dict(session=os.getenv("AOC_SESSION"))
    
    r = requests.get(url, allow_redirects=False, cookies=secret)
    open(input_file_path, 'wb').write(r.content)

with open(input_file_path, 'r') as file:
    input = file.read()

nums = [int(x) for x in input.split()]

################ COMPUTE - DAY 1.1 ################
def _twoSum(arr, tgt):
    theMap = {}
    theAns = []

    for n in arr:
        if n in theMap.keys():
            print(f"Product of 2sum with {n} and {theMap[n]}: {n * theMap[n]}")
        else:
            theMap[tgt - n] = n

def twoSum(arr, tgt, retMap=False, retFound=False):
    theMap = {}
    theAns = []

    for n in arr:
        if n in theMap.keys():
            print(f"Product of 2sum with {n} and {theMap[n]}: {n * theMap[n]}")
            if retFound:
                return n * theMap[n]
        else:
            theMap[tgt - n] = n

    if retMap:
        return theMap

map1 = twoSum(nums, 2020, True)

################ COMPUTE - DAY 1.2 ################
i = 0
for key, value in map1.items():
    newArr = nums[i:]
    ans = twoSum(newArr, key, retFound=True)
    if ans:
        print(f"Third value: {value}")
        print(f"Product of 3sum: {value * ans}")
        break
    i += 1

# trying the 2 'ptr' method
def twoSum2Ptr(arr, tgt):
    arr.sort()

    # i = index, n = value
    for i, n in enumerate(arr):
        ptr1 = i + 1
        ptr2 = len(arr) - 1
        tgtSum = tgt - n
        while ptr1 < ptr2:
            num1 = arr[ptr1]
            num2 = arr[ptr2]
            if num1 + num2 == tgtSum:
                print(f"{num1} {num2} {n}")
                return num1, num2, n
            elif num1 + num2 > tgtSum:
                ptr2 -= 1
            elif num1 + num2 < tgtSum:
                ptr1 += 1

twoSum2Ptr(nums, 2020)
