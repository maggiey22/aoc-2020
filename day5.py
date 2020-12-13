#! /usr/bin/env python3

import os
import requests
from dotenv import load_dotenv

dayN = 5
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

################ COMPUTE - DAY 5.1 ################

tix = input.strip().split()
# ex ticket: FBFBBFFRLR
# first 7 chars -> row (front / back)
# last  3 chars -> col (left / right)

#            t    'F'/'L'   'B'/'R'  128/8   0/8     8/10
def getPos(ticket, lilChar, bigChar, size, strStart, strEnd):
    w = size
    lo = 0
    hi = size - 1

    for c in range(strStart, strEnd):
        w //= 2      # floor division
        if ticket[c] == lilChar:
            hi -= w
        elif ticket[c] == bigChar:
            lo += w

    return lo

def getRow(t):
    return getPos(t, 'F', 'B', 128, 0, 7)

def getCol(t):
    return getPos(t, 'L', 'R', 8, 7, 10)

# Tests
# print(getRow("FBFBBFFRLR")) # row 44
# print(getRow("BFFFBBFRRR")) # row 70
# print(getRow("FFFBBBFRRR")) # row 14
# print(getRow("BBFFBBFRLL")) # row 102

# print(getCol("FBFBBFFRLR")) # col 5
# print(getCol("BFFFBBFRRR")) # col 7
# print(getCol("FFFBBBFRRR")) # col 7
# print(getCol("BBFFBBFRLL")) # col 4

ids = [getRow(t) * 8 + getCol(t) for t in tix]
max = max(ids)
print(max)

################ COMPUTE - DAY 5.2 ################

ids.sort()
middle = ids[1:len(ids)-1]

# look for the gap
for i, id in enumerate(middle):
    if i != 0 and (id != middle[i-1] + 1): # negative indices wrap around (?)
        print(id - 1)
