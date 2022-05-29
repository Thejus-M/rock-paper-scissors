# #* Rock, paper,scissors
#! Remember to create requirements.txt
from rich.markdown import Markdown
from tabulate import tabulate
from rich.table import Column, Table
from rich.console import Console
import pyfiglet
import random
import emoji


console = Console()
list1 = [1, 2, 3]
choices = ["Error", "Rock", "Paper", "Scissor"]
my_data = []

won = ["You won this round"]
loss = ["You loss this round"]
tie = ["This round was a tie"]


main_table = Table(show_header=True, header_style="bold magenta")
main_table.add_column("Attempt No.", justify="center", width=7)
main_table.add_column("Bot choice", width=14)
main_table.add_column("User choice", justify="right", width=14)
main_table.add_column("Score", justify="center")





def check_win():
    global computer_score, user_score
    if (choices[computer_choice] == choices[user_choice]):
        display_win(0)
    elif (computer_choice+1) % 3 == user_choice:
        user_score = 1+user_score
        display_win(1)
    else:
        computer_score = 1+computer_score
        display_win(2)


def display_win(p):
    global main_table
    if p == 0:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Attempt No.", justify="center", width=7)
        table.add_column("Bot choice", width=14)
        table.add_column("User choice", justify="right", width=14)
        table.add_column("Score", justify="center")
        table.add_row(f"[bold yellow]{attempt}[/bold yellow]",
                      f"[bold yellow]{choices[computer_choice]}[/bold yellow]",
                      f"[bold yellow]{choices[user_choice]}[/bold yellow]",
                      f"[bold yellow]{str(computer_score)}-{str(user_score)}[/bold yellow]")
        console.print(table)
        console.print(tabulate(my_data, headers=tie,
                               tablefmt="grid"), style="bold yellow")
        main_table.add_row(f"[bold yellow]{attempt}[/bold yellow]",
                           f"[bold yellow]{choices[computer_choice]}[/bold yellow]",
                           f"[bold yellow]{choices[user_choice]}[/bold yellow]",
                           f"[bold yellow]{str(computer_score)}-{str(user_score)}[/bold yellow]")
    elif p == 1:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Attempt No.", justify="center", width=7)
        table.add_column("Bot choice", width=14)
        table.add_column("User choice", justify="right", width=14)
        table.add_column("Score", justify="center")
        table.add_row(f"[bold green]{attempt}[/bold green]",
                      f"[bold green]{choices[computer_choice]}[/bold green]",
                      f"[bold green]{choices[user_choice]}[/bold green]",
                      f"[bold green]{str(computer_score)}-{str(user_score)}[/bold green]")
        console.print(table)
        console.print(tabulate(my_data, headers=won,
                               tablefmt="grid"), style="bold green")
        main_table.add_row(f"[bold green]{attempt}[/bold green]",
                           f"[bold green]{choices[computer_choice]}[/bold green]",
                           f"[bold green]{choices[user_choice]}[/bold green]",
                           f"[bold green]{str(computer_score)}-{str(user_score)}[/bold green]")
    elif p == 2:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Attempt No.", justify="center", width=7)
        table.add_column("Bot choice", width=14)
        table.add_column("User choice", justify="right", width=14)
        table.add_column("Score", justify="center")
        table.add_row(f"[bold red]{attempt}[/bold red]",
                      f"[bold red]{choices[computer_choice]}[/bold red]",
                      f"[bold red]{choices[user_choice]}[/bold red]",
                      f"[bold red]{str(computer_score)}-{str(user_score)}[/bold red]")
        console.print(table)
        console.print(tabulate(my_data, headers=loss,
                               tablefmt="grid"), style="bold red")
        main_table.add_row(f"[bold red]{attempt}[/bold red]",
                           f"[bold red]{choices[computer_choice]}[/bold red]",
                           f"[bold red]{choices[user_choice]}[/bold red]",
                           f"[bold red]{str(computer_score)}-{str(user_score)}[/bold red]")
    else:
        print("ERROR!")
    if attempt==3:
        main_table.add_row()
    print("\n\n")


# * main code block
console.print("Welcome to \n", style="bold blue")
with open("intro.txt") as file1:
    console.print(file1.read(), style="bold blue")
main_choice = 0
while main_choice != 3:
    computer_score = 0
    user_score = 0
    attempt = 1
    print("What do you want to do :")
    print("\t1.New Game.\n\t2.Rules\n\t3.Exit")
    main_choice = int(input("→ "))
    if main_choice == 1:
        while attempt <= 3:
            with open("comic_top.txt") as file1:
                console.print(file1.read())
            print(" | Enter your choice :   |")
            print(" |\t1.Rock           |\n |\t2.Paper          |\n |\t3.Scissors       |")
            computer_choice = random.choice(list1)
            with open("comic_bottom.txt") as file1:
                console.print(file1.read())
            user_choice = int(input("→ "))
            print("\n\n")
            check_win()
            attempt += 1
            print("========================================================")
        console.print(main_table)
        console.print("")
        if computer_score < user_score:
            console.print(tabulate(my_data, headers=["Congrats, you won!!"],
                                tablefmt="grid"), style="bold green")
            with open("prize1.txt") as file1:
                console.print(file1.read(), style="bold yellow")
            print("Beginners luck,I guess!", style="bold magenta")
        elif computer_score > user_score:
            console.print(tabulate(my_data, headers=["You loss better luck next time!"],
                                tablefmt="grid"), style="bold yellow")
            with open("prize3.txt") as file1:
                console.print(file1.read(), style="bold green")
            console.print("", style="bold magenta")
        elif computer_score == user_score:
            console.print(tabulate(my_data, headers=["The match was a tie"],
                                tablefmt="grid"), style="bold blue")
            with open("prize2.txt") as file1:
                console.print(file1.read(), style="bold yellow")
            console.print("Want to try your luck again!!", style="bold magenta")
    elif main_choice == 2:
        with open("Rules.md") as readme:
            markdown = Markdown(readme.read())
        console.print(markdown)
        gb=0
        while gb!=1 or gb!=2:
            print("\n\n\t1.Go back\n\t2.Exit")
            gb = int(input("→ "))
            if gb == 1:
                break
            elif gb == 2:
                exit()



