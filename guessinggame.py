import random
def guessinggame():
    print("Welcome to the Guessing game")
    name=input("What is your name?")
    wanna_play=input('Do you want to play now ?(yes/no)')
    if wanna_play=="no":
       print("Maybe next time")
      
    secret_num=random.randint(1,10)
    attempts=0
    max_attempts=3
    print("You have only 3 attempts to guess the number.")

    while attempts<max_attempts:
        guess=int(input("Enter your guess:"))
        attempts=attempts+1

        if guess==secret_num:
            print("Well done, you guesses it right")
            break
        elif guess<secret_num:
            print("Try a bigger number!")
        else:
            print("Try a smaller number")
        
        print("Attempts left:",max_attempts-attempts)
    else:
        print("You lost.The correct number is",secret_num)
    print("Thank you for playing.")
guessinggame()


