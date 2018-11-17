secret = 98
guess = 0
tries = 0
print ("this is a game where u have to type a number")
print ("now let's start guessing")


while guess != secret and tries < 6:
    guess = int(input("what is ur guess?"))
    if guess < secret:
        print ("you are a dog")
    if guess > secret:
        print ("you are a cow")
    if guess == secret:
        print ("you are rock")
    tries = tries + 1
else:
    print ("no more guess")
