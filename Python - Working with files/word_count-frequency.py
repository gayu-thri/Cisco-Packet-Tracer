# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:48:52 2020

@author: egayu
"""
import string
#avoids punctuations also

file = open("story.txt","r")

mydict = dict()

for line in file:
     # Remove the leading spaces and newline character 
    line = line.strip() 
    
    line = line.lower() #to avoid mismatch
    
    line = line.translate(line.maketrans("", "", string.punctuation))
    
    words = line.split(" ")
    
    for word in words:
        if word in mydict:
            mydict[word] += 1
        else:
            mydict[word] = 1

for key in list(mydict.keys()):
    print(key,":", mydict[key])    
    
file.close()

'''
    Syntax : maketrans(str1, str2, str3)

Parameters :
str1 : Specifies the list of characters that need to be replaced.
str2 : Specifies the list of characters with which the characters need to be replaced.
str3 : Specifies the list of characters that needs to be deleted.

    
    Syntax : translate(table, delstr)

Parameters :
table : Translate mapping specified to perform translations.
delstr : The delete string can be specified as optional argument is not mentioned in table.

Returns : Returns the argument string after performing the translations using the translation table.
'''