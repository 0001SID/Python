def print_two(*args):
    arg1,arg2 = args
    print(f'arg1:{arg1}\narg2:{arg2}')
def print_two_again(arg1,arg2):
    print(f'arg1:{arg1}\narg2:{arg2}')
def print_one(arg):
    print(f'arg:{arg}')
def print_none():
    print('I have no argument')
def inp(fst,snd):
    fst = int(input())
    snd = int(input())
    print(fst + snd)
print_two('fst','snd')
print_two_again('fst again','snd again')
print_one('one')
print_none()
inp('fst','snd')