#A looping game
print('This is a game where you will get many room \nand you have to enter each room carefully with a logical decesion')
print('''Now there is three room and each room has diferent things
1. animal
2. material
3. place

and you have to get out from the trap''')
main = True
while main == True:
    print('Now In which room you want to go')
    home = input()
    if home == 'animal':
        ad = True
        while ad ==True:
            print('There is four animal: 1.Dog, 2.Tiger, 3. Wolf, 4. Cow\nIn which room you want to go?')
            animal_choice = input()
            if animal_choice == 'dog':
                print('You are such a week hearted person \nNow there is only one choice and that is\n\'go to drain\'')
                dc1 = input('So do you want to go drain yes/no?\n')
                print('I don\'t care about your wish just go to drain')
                print('Game over')
                ad = False
                main = False
            elif animal_choice == 'tiger':
                print('So you are so brave.\nI want to know your name.\nWhat is your name?')
                username = input()
                print(f'nice to meet you Mr. {username}')
                ad1 = True
                while ad1 == True:
                    print('Here is two type of tiger 1. male and 2. female\nWhere you want to go?')
                    tc1 = input()
                    if tc1 == 'male':
                        print('So you are brave but you have lack of knowledge so you are trapped')
                        print('Game over')
                        main = False
                        ad1 = False
                        ad = False
                    elif tc1 == 'female':
                        ad2 = True
                        while ad2 == True:
                            print('So you are brave and knowladgeble too\nSo now there is only one way and that is the gate\nSo are you want to get out from this trap?')
                            tc2 = input()
                            if tc2 == 'yes':
                                print('Congrasulation')
                                print('You won')
                                main = False
                                ad = False
                                ad1 = False
                                ad2 = False
                            elif tc2 == 'no':
                                print('you are a big full')
                                print('Game over')
                                main = False
                                ad = False
                                ad1 = False
                                ad2 = False
                            else:
                                print('you have entered a wrong keyword please enter the right one')
                                ab2 = True
                    else:
                        print('This is very sad that you have entered a wrong keyword\nPlease enter the right keyword')
                        ab1 = True
                
            elif animal_choice == 'wolf':
                print('So you are so brave.\nI want to know your name.\nWhat is your name?')
                username = input()
                print(f'nice to meet you Mr. {username}')
                af = True
                while af == True:
                    print('Here is two type of tiger 1. male and 2. female\nWhere you want to go?')
                    tw1 = input()
                    if tw1 == 'male':
                        print('So you are brave but you have lack of knowledge so you are trapped')
                        print('Game over')
                        main = False
                        af = False
                        ad = False
                    elif tw1 == 'female':
                        af1 = True
                        while af1 == True:
                            print('So you get the way of out\nDo you want to get out from this trap?')
                            tw = input()
                            if tw == 'yes':
                                print('Congrasulation')
                                print('You won')
                                main = False
                                af = False
                                af1 = False
                                ad = False
                            elif tw == 'no':
                                print('You are such a fool now live here forever')
                                print('You won ')
                                main = False
                                af = False
                                af1 = False
                                ad = False
                            else:
                                print('You have enterd a wron keyword please enterd the right keyword')
                                af1 = True
                    else:
                        print('You have entered a wrong keyword please enter the right keyword')
                        af = True
            elif animal_choice == 'cow':
                print('Yor are such a cow now you are trapped here forever')
                print('Game over')
                ad = False
                main = False
            else:
                print('At first learn how to type then come here to play')
                print('Enter the right keyword')
                ad = True

    elif home == 'material':
        print('So you are interested in material\nThere are two types of material\n1. gold, 2. iron')
        mt = True
        while mt == True:
            mc1 = input('Which one you want to get\n')
            if mc1 == 'gold':
                print('you are so greedy now you are trapped here forever')
                print('Game over')
                main = False
                mt = False
            elif mc1 == 'iron':
                ir = True
                while ir == True:
                    print('So you are a talented one')
                    print('Now there is two room 1. good , 2. bad')
                    mc2 = input('Whre you want to go\n')
                    if mc2 == 'good':
                        print('Here you choose the good choice')
                        print('you are run out')
                        print('You won')
                        main = False
                        mt = False
                        ir = False
                    elif mc2 == 'bad':
                        print('hei what man!')
                        print('You are trapped')
                        print('Game over')
                        main = False
                        mt = False
                        ir = False
                    else:
                        print('you have entered wrong keyword please entered the right keyword')
                        ir = True
            else:
                print('you have entered a wrong keyword please entered the right keyword')
                mt = True
    elif home == 'place':
        pl = True
        while pl == True:
            print('So you are interested in place')
            print('Now there is two place available here\n1. Coochbehar 2. america')
            pc1 = input('So where you want to go?\n')
            if pc1 == 'coochbehar':
                print('So you love your home town very much')
                print('Now there is two place available\n1. home 2. school')
                input('Where you want to go?\n')
                print('Wherever you go you are out from trap')
                print('You won')
                main = False
                pl = False
               
            elif pc1 == 'america':
                print('You don\'t have enough money to go there')
                print('YOu are trapped')
                print('Game over')
                main = False
                pl = False
            else:
                print('You have eneteed a wrong keyword please enter the right keyword')
                main = True
                pl = True
    else:
        print('Hei atleast type the correct room name')
        main = True