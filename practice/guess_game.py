import random
secret_number = random.randint(1,20)
print("I guessed a number now you have to guess that number\n")
attempt = 0
print("\t\t\tYou have 5 attempt to guess the number\n\t\t\tAnd the number is between 1 to 20")
while attempt<5:
    guess = 0
    while True:
        try:
            guess = int(input("Enter your guess : "))
            break
        except:
            print("This is not an integer\nType again\n")
    if(guess > secret_number):
        print("Your guess is greater than me\n")
    elif(guess < secret_number):
        print("Your guess is less than me\n")
    elif(guess == None):
        print("Please enter a valid guess")
    else:
        break
    attempt+=1
if(attempt <5):
    print("You caught me in ",attempt," attempt\nGood job")
else:
    print("Hu hu You failed to caught me\nI win You loose\n")
    
