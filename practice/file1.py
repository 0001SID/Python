from sys import argv
script, filename = argv
print(f'We are going to erase your file {filename}')
print ('If you want to erase press enter')
print ('IF You want to cancel then press CTRL+C')
input()
print ('At first we are showig you the file content')
text = open(filename,)
print (text.read())
print('Now do you still want to erase this file?')
input()
text = open(filename,'w')
text.truncate
print('Now we are going to write something in this empty file')
line1 = input('Write the first line\n')
n1 = '\n'
line2 = input('Write the second line\n')
n2= '\n'
line3= input('Write the third line\n')
text.write(line1)
text.write(n1)
text.write(line2)
text.write(n2)
text.write(line3)
print('Now if you want to open the new file then press enter')
input()
text = open(filename,'r')
print(text.read())
text.close()