# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:09:20 2018

@author: SID
"""

print ('\n\n                                      MULTIPLYING')
x = int (input('1st number\n'))
y = int (input('2nd number\n'))
ans = 0
while (y != 0):
    ans += x
    y -= 1
print ('\n' + str(ans))