'''numbers =[]
for i in range(1,8):
    print('This is the value of i',i)
    numbers.append(i)
print('The last number is ',i)
print(numbers)'''
fst = float(input('Enter the first number'))
snd = float(input('Enter the second number'))
result = 0
for i in range(0,int(snd)):
    result += fst
print(result)
