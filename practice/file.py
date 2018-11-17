from sys import argv
script , filename = argv
txt = open(filename)
print('This is youur file name ',filename)
print(txt.read())
filename1 = input('Write down the file name again')
text1 = open(filename1)
print(text1.read())