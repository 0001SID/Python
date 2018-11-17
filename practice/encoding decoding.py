#Here we are going to encode and decode some strings
from sys import argv
script, input_encoding , error = argv
filename = input('Enter the file name')
def print_line(filename,encodings,errors):
    line = indata.readline()
    if line:
        next_lan = line.strip()
        raw_file = next_lan.encode(encodings,errors = errors)
        string = raw_file.decode(encodings,errors = errors)
        print(f'{raw_file}<------>{string}')
        return print_line(filename,encodings,errors)
indata = open(filename)
print_line(filename,input_encoding,error)