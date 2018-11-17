#making an infinite loop calculator with password
attemp = 1
while attemp <=6:
    pas = input('Enter password to run the program''\n')
    password = 9091
    if pas == str(password):
        print ('Password matched')
        attemp = 1
        while True:
            def inp(fst,snd):
                fst1 = (input('Enter the first number  '))
                snd1 = (input('Enter the second number  '))
                try:
                    int(fst1)
                    int(snd1)
                    float(fst1)
                    float(snd1)
                    fst = float(fst1)
                    snd = float(snd1)
                    return [fst,snd]
                except ValueError:
                    print('This is not a number')
            operator = str(input('What you want to do?''\n'))
            if operator == 'sum':
                get = inp('fst','snd')
                if get:
                    result = get[0]+get[1]
                    print ('The summesion of the two number  is ',result)
            elif operator == 'div':
                get = inp('fst','snd')
                if get:
                    result = get[0]/get[1]
                    print ('The division of the two number is ', result)
            elif operator == 'mult':
                get = inp('fst','snd')
                if get:
                    result = get[0] * get[1]
                    print ('The multiplication of the two number  is ' , result)
            elif operator == 'sub':
                get = inp('fst','snd')
                if get:
                    result = get[0] - get[1]
                    print ( 'The subtraction of the two number is ',result)
            elif operator == 'exit':
                break
            else:
                print('You have entered a wrong keyword''\n''Please enter the right keyeord''\n'
                    'The supported keyword is sum,mult,div,sub')
            #continue
    elif pas == 'exit':
        break
    else:
        print ('You have entered a wrong password please try again''\n''You have ',int(6-attemp), 'attemp left')
        attemp +=1
    continue