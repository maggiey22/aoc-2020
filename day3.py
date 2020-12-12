#! /usr/bin/env python3

import os
import requests
from dotenv import load_dotenv

dayN = 3
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

################ COMPUTE - DAY 3.1 ################

input = input.rstrip()
arr = input.split("\n")
# arr = ['..##..', '..#...', etc.]

def countTrees(arr, dx):
    trees = 0
    for i, l in enumerate(arr):
        if l[(dx*i) % len(l)] == '#':
            trees += 1
    return trees

print(countTrees(arr, 3))

################ COMPUTE - DAY 3.2 ################

# 0. Right 1, down 1.
# 1. Right 3, down 1. (This is the slope you already checked.)
# 2. Right 5, down 1.
# 3. Right 7, down 1.
# 4. Right 1, down 2.

def countTrees2(arr, dx, dy):
    x = 0
    y = 0
    trees = 0

    while y < len(arr):
        if arr[y][x] == '#':
            trees += 1

        x = (x + dx) % len(arr[0])
        y += dy

    return trees
        
print(countTrees(arr, 1) * countTrees(arr, 3) * countTrees(arr, 5) *
      countTrees(arr, 7) * countTrees2(arr, 1, 2))


###################### SCRAPS ######################

test = '''
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
'''

test = test.strip().split('\n')

def updateAns(px, py, i, arr, ans):
    # print(f"x: {px}, y: {py}")
    if py < len(arr):
        if arr[py][px] == '#':
            ans[i] += 1

def followSlope(arr):
    ans = [0, 0, 0, 0, 0]
    it = 0
    posX = 0
    posY = 0
    llen = len(arr[0])
    
    while posY < len(arr):
        if it % 5 == 0:
            posX = (posX + 1) % llen
            posY += 1
            updateAns(posX, posY, 0, arr, ans)
        elif it % 5 == 1:
            posX = (posX + 3) % llen
            posY += 1
            updateAns(posX, posY, 1, arr, ans)
        elif it % 5 == 2:
            posX = (posX + 5) % llen
            posY += 1
            updateAns(posX, posY, 2, arr, ans)
        elif it % 5 == 3:
            posX = (posX + 7) % llen
            posY += 1
            updateAns(posX, posY, 3, arr, ans)
        elif it % 5 == 4:
            posX = (posX + 1) % llen
            posY += 2
            updateAns(posX, posY, 4, arr, ans)
        it += 1

    print(ans[0] * ans[1] * ans[2] * ans[3] * ans[4])

# ATTEMPTS
# 228150 - too low -- I only checked the exact points, gotta check the in between?

# This is unfortunate proof that I need to work on my reading comprehension skills :')
# supposed to use the specified slopes for the entire map each time!
