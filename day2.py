#! /usr/bin/env python3

import os
import requests
from dotenv import load_dotenv

################ GRAB INPUT ################
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file_path = f"{dir_path}/input/day2.txt"
url = "https://adventofcode.com/2020/day/2/input"

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

################ COMPUTE - DAY 2.1 ################
lines = input.strip().split("\n")

def parseLine(line):
    return line.replace(":", "").replace("-", " ")

lines = [parseLine(l).split(" ") for l in lines]
# lines = list(map(lambda x: x.split(" "), lines))

# lines = [['1', '3', 'a', 'abcde'], ['1', '3', 'b', 'cdefg'], ['2', '9', 'c', 'ccccccccc']]

def goodPwd(x):
    pwd = x[3]
    char = x[2]
    minOcc = int(x[0])
    maxOcc = int(x[1])
    return pwd.count(char) >= minOcc and pwd.count(char) <= maxOcc

res = [b for b in lines if goodPwd(b)]
# had a lot of trouble because of a newline at the end that i forgot to trim :(

print(len(res))

################ COMPUTE - DAY 2.2 ################

def goodPwd2(x):
    pwd = x[3]
    char = x[2]
    posA = int(x[0]) - 1 # 1-based indexing
    posB = int(x[1]) - 1
    return (pwd[posA] == char and pwd[posB] != char) or (pwd[posA] != char and pwd[posB] == char)

res = [b for b in lines if goodPwd2(b)]
print(len(res))
