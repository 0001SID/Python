from sys import argv
script , filename = argv
def print_all(f):
    print(f.read())
def rewind(f):
    f.seek(0)
def print_line(line,f):
    print(line,f.readline())
open_file = open(filename)
print('At first we are going to print the whole file')
print_all(open_file)
print('Then we are going to read the file from start')
rewind(open_file)
print('Now we are going to print the line of the file one by one')
line = 1
print_line(line,open_file)
line+=1
print_line(line,open_file)
line+= 1
print_line(line,open_file)
open_file.close()