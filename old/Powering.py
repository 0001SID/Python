# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:11:57 2018

@author: SID
"""

print ("\n\n                         POWERING")
print ('  ')
print ( " ")
x =int( input ('Enter your number \n'))
y =int( input ( 'Enter the power \n'))
power = x
interval = y
while (interval != 2):
    power = power*x
    interval -=1
ans = 0
while (power != 0):
    ans += x
    power -= 1
print ('\n' + 'Your answer is ' + str(ans))