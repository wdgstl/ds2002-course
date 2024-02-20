#!/usr/bin/python3

import os 

COLOR = input("What is your favorite color? ")

HOBBY = input("What is your favorite hobby? ")

SPORT = input("What is your favorite sport? ")

os.environ["COLOR"] = COLOR

os.environ["HOBBY"] = HOBBY

os.environ["SPORT"] = SPORT

print(f'Color env-var: {os.getenv("COLOR")}')

print(f'Hobby env-var: {os.getenv("HOBBY")}')

print(f'Sport env-var: {os.getenv("SPORT")}')

