import random
import math
import tkinter as tk 
from tkinter import messagebox,simpledialog

def guess_number():
    try:
        lower_value = simpledialog.askinteger("Input" ,"Enter the lower range :- ")
        upper_value = simpledialog.askinteger("Input" ,"Enter the upper range :- ")
        main(lower_value,upper_value)
    except ValueError :
        messagebox.showerror = ("Invalid Input" , "Please enter an integer")

def main(l,u):
    second_display = tk.Tk()

    if l<u :
        tk.Label(second_display,text=f"Your Chosen Range is {l} to {u}").pack()
        x= random.randint(l,u)
        guess = round(math.log(u-l+1,2))
        tk.Label(second_display,text=f"You can guess it in {guess} guesses").pack()

        rounds = 0
        while rounds<guess :
            rounds += 1
            guess_num = tk.Label(second_display,text="Guess the number").pack()
            value = tk.Entry(second_display)
            value.pack()
            number = int(value.get())

            if number==x :
                tk.Label(second_display,text=f"Congrats You have guessed in {rounds} chances").pack()
                break
            elif number<x :
                tk.Label(second_display,text=f"You have entered {x-number} lesser value").pack()
            elif number>x :
                tk.Label(second_display,text=f"You have entered {number-x} bigger value").pack()

            if rounds == guess :
                tk.Label(second_display,text=f"You lost it").pack()
            else :
                tk.Label(second_display,text=f"Your Chosen Range is not valid").pack()
                lower_value = int(input("Enter the lower range :- "))
                upper_value = int(input("Enter the upper range :- "))
                
                main(lower_value,upper_value)
   
display = tk.Tk()
display.title("Number Guessing Game")

intro = tk.Label(display , text= "Welcome to Number Guessing Game")
intro.pack()

start_button = tk.Button(display, text="Start Guessing" , command=guess_number).pack()

display.mainloop()