#! /usr/bin/env python3

import os
import requests
from dotenv import load_dotenv

dayN = 6
################ GRAB INPUT ################
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file_path = f"{dir_path}/input/day{dayN}.txt"
url = f"https://adventofcode.com/2020/day/{dayN}/input"

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

################ COMPUTE - DAY 6.1 ################

# split into groups
arr = input.strip().split("\n\n")

# make a list of characters in each group, then uniquify by making it a set
yess = [ set(list(s.replace("\n", ""))) for s in arr ]
yess = [ len(x) for x in yess ]
print(sum(yess))


################ COMPUTE - DAY 6.2 ################

allyess = [ s.split("\n") for s in arr ]

# return the intersection of str1 and str2
def strIntersect(str1, str2):
    print(f"comparing: {str1}, {str2}")
    ans = ""
    for c in str1:
        if c in str2:
            ans += c
    return ''.join(set(list(ans)))

# Tests
# print(strIntersect("aaa", "aaa"))
# print(strIntersect("abc", "def"))
# print(strIntersect("pie", "pop"))
# print(strIntersect("oop", "pot"))
# print(strIntersect("oof", "mango"))
# print(strIntersect("mango", "oof"))
# print(strIntersect("toffeess", "coffee"))

# count the number of common characters
# this is more work than necessary. can just use a map :D
def countStrIntersect(strArr):
    if len(strArr) > 1:
        acc = strIntersect(strArr[0], strArr[1])

        for s in strArr[2:]:
            strIntersect(s, acc)

        print(acc)
        return len(acc)
    else:
        return len(strArr[0])

# Tests
# print(countStrIntersect(['abc']))
# print(countStrIntersect(['a', 'b', 'c']))
# print(countStrIntersect(['ab', 'ac']))
# print(countStrIntersect(['a', 'a', 'a']))
# print(countStrIntersect(['ab', 'abc', 'abcd', 'a', 'a'])) #! acc contains chars that are lost
# print(countStrIntersect(['a', 'a', 'c']))
# print(countStrIntersect(['c']))

# ATTEMPTS
# 3185 - too high

def countStrIntersect2(strArr):
    charMap = dict()
    count = 0

    for s in strArr:
        # make sure strings don't have duplicate chars
        setStr = ''.join(set(list(s)))
        for c in setStr:
            if c in charMap:
                charMap[c] += 1
            else:
                charMap[c] = 1

    # count the letters that appear for all group members
    for key, val in charMap.items():
        if val == len(strArr):
            count += 1

    return count

# Test
print(countStrIntersect2(['a', 'a', 'c']))
print(countStrIntersect2(['ab', 'abc', 'abcd', 'a', 'a']))

allyess = [ countStrIntersect2(group) for group in allyess ]
print(sum(allyess))
