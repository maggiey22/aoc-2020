#! /usr/bin/env python3

import os
import requests
from dotenv import load_dotenv

import re

dayN = 4
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

################ COMPUTE - DAY 4.1 ################
input = input.rstrip()
arr = input.split("\n\n")

arr = [x.replace("\n", " ") for x in arr]

def goodPassport(p):
    return (("byr" in p) and
            ("iyr" in p) and
            ("eyr" in p) and
            ("hgt" in p) and
            ("hcl" in p) and
            ("ecl" in p) and
            ("pid" in p))
           
res = [x for x in arr if goodPassport(x)]
print(len(res))

################ COMPUTE - DAY 4.2 ################

def goodPassport2(p):
    return (re.search("(^|\s)byr:((19[2-9][0-9])|(200[0-2]))($|\s)", p) and                                # 1920-2002
            re.search("(^|\s)iyr:((201[0-9])|(2020))($|\s)", p) and                                        # 2010-2020
            re.search("(^|\s)eyr:((202[0-9])|(2030))($|\s)", p) and                                        # 2020-2030
            re.search("(^|\s)hgt:((((1[5-8][0-9])|(19[0-3]))cm)|(((59)|(6[0-9])|(7[0-6]))in))($|\s)", p) and # 150-193cm || 59-76in
            re.search("(^|\s)hcl:#[0-9|a-f]{6}($|\s)", p) and                                            # ex. #123abc
            re.search("(^|\s)ecl:(amb|blu|brn|gry|grn|hzl|oth)($|\s)", p) and                            # eye colors
            re.search("(^|\s)pid:[0-9]{9}($|\s)", p))                                                    # 9 digit num

badPassports = ["eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
                "iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946",
                "hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
                "hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007"]

goodPassports = ["pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",
                 "eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
                 "hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022",
                 "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"]

bad = [x for x in badPassports if goodPassport2(x)]
print(len(bad)) # should be 0

good = [x for x in goodPassports if goodPassport2(x)]
print(len(good)) # should be 4

res = [x for x in arr if goodPassport2(x)]
print(len(res))

# Wrong guesses
# 177 too high
# 176 too high - regex missed case where hgt:150 was ok (too many parens ><)
# 175 !!! - forgot to check for start and end of lines
