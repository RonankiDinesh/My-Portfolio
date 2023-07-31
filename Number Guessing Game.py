import random
import math
lower_value = int(input("Enter the lower range :- "))
upper_value = int(input("Enter the upper range :- "))

def main(l,u):
    if l<u :
        print(f"Your Chosen Range is {l} to {u}")
        x= random.randint(l,u)
        guess = round(math.log(u-l+1,2))
        print(f"You can guess it in {guess} guesses")
        rounds = 0
        while rounds<guess :
            rounds += 1
            number = int(input("Guess the number :- "))

            if number==x :
                print(f"Congrats You have guessed in {rounds} chances")
                break
            elif number<x :
                print(f"You have entered {x-number} lesser value")
            elif number>x :
                print(f"You have entered {number-x} bigger value")

            if rounds == guess :
                print("You lost it")
    else :
        print("Your Chosen Range is not valid")
        lower_value = int(input("Enter the lower range :- "))
        upper_value = int(input("Enter the upper range :- "))
        main(lower_value,upper_value)   
main(lower_value,upper_value)