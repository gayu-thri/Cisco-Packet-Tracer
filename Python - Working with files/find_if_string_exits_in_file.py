# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:29:05 2020

@author: egayu
"""

# PRINTS FIRST OCCURENCE (LIKE str.find())
import string

s = input("Enter the word to search in file > ")

file = open("story.txt","rt")
flag = line_number = 0

for line in file:
    line = line.lower()
    line = line.strip()
    line = line.translate(line.maketrans("", "", string.punctuation))
    #line = line.strip().split('\n')
    line_number += 1
    #print(line)
    if s in line:
        flag = 1
        break

if flag == 0:
    print(f"Sorry couldn't find {s}")
else:
    print(f"Found {s} in line {line_number}")
        

file.close()