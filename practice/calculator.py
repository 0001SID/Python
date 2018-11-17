#making an infinite loop calculator
while True:
    operator = str(input('What you want to do?''\n'))
    if operator == 'sum':
        fst1 = (input('Enter the first number  '))
        snd1 = (input('Enter the second number  '))
        try:
            int(fst1)
            float(snd1)
            float(fst1)
            float(snd1)
            fst = float(fst1)
            snd = float(snd1)
            result = fst + snd
            print ('The summesion of the two number  is ',result)
        except:
            print('This is not a number')
    elif operator == 'div':
        fst1 = (input('Enter the first number '))
        snd1 = (input('Enter the second number '))
        try:
            int(fst1)
            float(snd1)
            float(fst1)
            float(snd1)
            fst = float(fst1)
            snd = float(snd1)
            result = fst/snd
            print ('The division of the two number is ', result)
        except:
            print('This is not a number')
    elif operator == 'mult':
        fst1 = (input('Enter the first number '))
        snd1 = (input('Enter the second number '))
        try:
            int(fst1)
            float(snd1)
            float(fst1)
            float(snd1)
            fst = float(fst1)
            snd = float(snd1)
            result = fst *snd
            print ('The multiplication of the two number  is ' , result)
        except:
            print('This is not a number')
    elif operator == 'sub':
        fst1 = (input('Enter the first number '))
        snd1 = (input('Enter the second number '))
        try:
            int(fst1)
            float(snd1)
            float(fst1)
            float(snd1)
            fst = float(fst1)
            snd = float(snd1)
            result = fst - snd
            print ( 'The subtraction of the two number is ',result)
        except:
            print('This is not a number')
    elif operator == 'exit':
        break
    else:
        print('You have entered a wrong keyword''\n''Please enter the right keyeord''\n'
            'The supported keyword is sum,mult,div,sub')
    continue