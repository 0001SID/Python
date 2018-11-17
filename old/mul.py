# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 12:22:46 2018

@author: SID
"""

x = float (input('Enter the first number: '))
y = float (input ('Enter the second number: '))
ans = 0
while (y != 0):
    ans += x
    y -= 1
print('Your ans is: ' + str(ans))