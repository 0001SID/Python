# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:37:09 2018

@author: SID
"""
s = 'good'
count =0
for char in s:
    if (char == 'a' or char == 'e' or char =='i' or char == 'o' or char == 'u'):
        count += 1
print ('Number of vowels: ' + str(count))
