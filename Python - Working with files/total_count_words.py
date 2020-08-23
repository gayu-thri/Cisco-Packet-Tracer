# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:40:44 2020

@author: egayu
"""

'''
ALGORITHM

1. Open a file ( read mode) using a file pointer.
2. Read a line from the file.
3. Split the line into words and store in an array.
4. Iterate through the array, increment count by 1 for each word.
5. Repeat 2-4 until all the lines from the file has been read
'''

count = 0

#open file in r mode
file = open("story.txt", "rt")

#data = file.read()
#words = data.split()
#print(len(words))


for line in file:
    words = list()
    words = line.split(" ")
    count = count + len(words)

print('Number of words in the file: ',count)

file.close()
