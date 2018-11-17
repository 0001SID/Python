#In this process we can make an infinite loop
def print_infinite():
    print ('hello world')
    return print_infinite()
print_infinite()