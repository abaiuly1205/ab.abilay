import random

def game():
    x = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20.")
    for tries in range(1, 7):
        a = int(input("Take a guess: "))
        if a < x:
            print("Your guess is too low.")
        elif a > x:
            print("Your guess is too high.")
        else:
            break

    if a == x:
        print("Good job! You guessed my number in " + str(tries) + " guesses.")
    else:
        print("Sorry, the number I was thinking of was " + str(x) + ".")

game()
