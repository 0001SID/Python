'''from sys import argv
from os.path import exists
script, from_file, to_file = argv
print('Now here we are going to copy one file into another file')
print(f'from {from_file} to {to_file} the file will copied')
text = open(from_file)
indata = text.read()
print(f'The file size is {len(indata)} bytes')
print(f'Is the destination file exists? {exists(to_file)}')
print('If you want to copy then press enter')
input()
text1 = open(to_file,'w')
text1.write(indata)
text1 = open(to_file,'r')
print('Do you want to view the copied file?, then press enter')
input()
print(text1.read())
text.close()
text1.close()'''
#Short form of the above code
from sys import argv
script, from_file , to_file = argv
open(to_file,'w').write(open(from_file).read())

