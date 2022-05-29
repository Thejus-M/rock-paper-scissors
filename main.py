# #* Rock, paper,scissors
#! Remember to create requirements.txt
from tabulate import tabulate
from rich.table import Column, Table
from rich.console import Console
import pyfiglet
import random

i = '''
            ____  _____  ___  _  _    ____   __    ____  ____  ____ 
           (  _ \(  _  )/ __)( )/ )  (  _ \ /__\  (  _ \( ___)(  _ \ 
            )   / )(_)(( (__  )  (    )___//(__)\  )___/ )__)  )   / 
           (_)\_)(_____)\___)(_)\_)  (__) (__)(__)(__)  (____)(_)\_) 
         __    _  _  ____     ___   ___  ____  ___  ___  _____  ____  ___  
        /__\  ( \( )(  _ \   / __) / __)(_  _)/ __)/ __)(  _  )(  _ \/ __)
       /(__)\  )  (  )(_) )  \__ \( (__  _)(_ \__ \\__ \  )(_)(  )   /\__ \ 
      (__)(__)(_)\_)(____/   (___/ \___)(____)(___/(___/(_____)(_)\_)(___/\n

'''
computer_score = 0
user_score = 0
console = Console()
list1 = [1, 2, 3]
choices = ["Error", "Rock", "Paper", "Scissor"]
result = pyfiglet.figlet_format(
    "Rock Paper\n      and\n\t  Scissor", font="digital")

result = i
print("🪨📄✂")


def check_win():
    if (choices[computer_choice] == choices[user_choice]):
        print("Tie")
    elif (computer_choice+1) % 3 == user_choice:
        print("You Won")
    else:
        print("You Lose")


console.print("Welcome to \n",style="bold blue")
console.print(result,style="bold blue")
for _ in range(1, 4):
    print("Enter your choice : ")
    print("\t1.Rock \n\t2.Paper\n\t3.Scissors")
    computer_choice = random.choice(list1)
    user_choice = int(input(">"))
    check_win()
    print("\nComputer choice : ", choices[computer_choice],
        "\nUser choice     : ", choices[user_choice])


