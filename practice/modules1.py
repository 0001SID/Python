from sys import argv
script,user_name = argv
print(f'Hi {user_name} nice to meet you')
print(f'I am your script name {script}')
print(f'Now I want to know something about you')
age = int(input('what is your age\n'))
height = int(input('what is your height\n'))
live = str(input('Where you live\n'))
print(f'''ok your age is {age}
your height is {height}
and you live in {live}
nice to meet you mr. {user_name}''')