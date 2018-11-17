# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:51:32 2018

@author: SID
"""
print ('\n\n                         Determine the cubic root')
cube = int (input('Enter an integer: '))
guess = 0 
while (guess**3 < abs(cube)):
    guess += 1
if (guess**3 != abs(cube)):
    print ('This is not a perfect cube')
else:
    if cube < 0:
        guess = - guess
    print ('The perfect cube root of your number is ' + str(guess))


"""We can use an another way to take the nearest cubic root of the given number"""

"""cube = float (input('Enter an integer: '))
guess = 0 
while (guess**3 < abs(cube)):
    guess += 1
if (guess**3 != abs(cube)):
    if (cube <0):
        guess =-guess
    print ('This is not a perfect cube but the nearest ans is '+ str(guess))
else:
    if cube < 0:
        guess = -guess
    print ('The perfect cube root of your number is ' + str(guess))"""
    
"""But this does not give the perfect result, I don't know why?"""