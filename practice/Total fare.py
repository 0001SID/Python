#Finding the total fare amount for a given distance
A = float(input('First checking distance in k.m?''\n'))
M = float(input('fare''\n'))
N = float(input('subsequent distance fare''\n'))
D = float(input('How long you want to go?''\n'))
fpay = (A* M)+(N*(D-A))
print('your total payment is '+ str(fpay))