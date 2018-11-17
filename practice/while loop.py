i = 0
numbers = []
def while_loop():
    i = 0
    while i<8:
        print('The value of i is{}'.format(i))
        h = numbers.append(i)
        i += 1
    return h,i
h,i = while_loop()
print('At last the value of i is {}'.format(i))
print(f'The list of numbers of i is {numbers}')