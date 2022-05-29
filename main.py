# #* Rock, paper,scissors
#! Remember to create requirements.txt
from tabulate import tabulate
from rich.table import Column, Table
from rich.console import Console
import pyfiglet
import random
import emoji

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
prize_1='''
................................................................................
................................................................................
....................................:::::.......................................
........................:***!:!!**%%%***%*!:::!**:!**:..........................
.......................:%!::*@$!*%$$%***%%*!::*$@%*!!**.........................
.......................!*...!$$!*%$$%***%%*!::*$$%...:*:........................
.......................:%:..::%**%$$%*%%%%*!::%@%::..!*.........................
........................!*:...!%!%$@$%%%%%*!:!$&!...!*:.........................
.........................:*!:.:$!%%%%%****!::%@@:.:**:..........................
...........................!*!.*!!****!!!!!:!$&!:!*:............................
............................:!!!*::!!!!!!!::!$%!!:..............................
...............................:*%!:!!!!!!:!$$!:................................
.................................!%*!%&@@!*%%:..................................
................................::!::*&@%*!:!::.................................
................................::...:*%!:..::..................................
.....................................:%%*.......................................
.....................................:%%*:......................................
......................................%**.......................................
.....................................:%**:......................................
...................................::%@$%%!::...................................
................................!&$@&&&&&@@&&%..................................
................................$S@$$$%%%%%$&&:.................................
................................$S$*!!!:::::&&:.................................
.............................::.$S$%%%******&&:::::.............................
....................::::::!!!!!%S*SSSSSSSSSSS*@!!!:::::::::.....................
.................:::::::::!!!!!$&@@&&&&&&&&&@@@*!!!:::::::......................
...............................................:................................
................................................................................
................................................................................
'''
prize_2 = '''
.............:....................................................:.............
............$S&%!..............................................:%@#$............
...........@*****&$:........................................:%@#SSSS$:..........
..........@*********........................................!#SSSSSSS@:.........
.........@*******S*.............:!!*%%$$$@@@@@@$$%*!::.....:.!#SSSSSSS@:........
.......:@*******S*:&@*::......:$##SSSSSSSSSSSSSSSSSS##&@@@@&&:!#SSSSSSS@:.......
......:&*******S!:#***SS#&@*.!&SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS&!!#SSSSSSS@:......
.....:&*******S!:#********@:%#SSSSSSS###SSSSSSSSSSSSSSSSSSSSSS#!:&SSSSSSS@:.....
....:&*******S!:#*******S*:@SSSSSS&%*!!!*$&#SSSSSSSSSSSSSSSSSSS#!:&SSSSSSS&:....
...:&*******S!!S*******S!:&SSSSSS$:*&#SS@%!!%@#SSSSSSSSSSSSSSSSS#!:&SSSSSSS&:...
..:&*******S!!S********!:#SSSS#@!:@********#$!!*@#SSSSSSSSSSSSSSS#!:&SSSSSSS&:..
.:#*******#:!S********S.*#&&$*!!$S************#$*!*@#SSSSSSSSSSSSS#!:&SSSSSSS&:.
!#*******#:!S**********@*!**%$#******************#$!!%&SSSSSSSSSSSS#!:&SSSSSSS&!
&*******#:!S****************************************#%!!$#SSSSSSSSSS#*:&SSSSSSS&
:!$#***#:*********************************************S@*:*&SSSSSSSSS#!:@SSS&$!:
...:!@&:.!&**********************************************#%!!$#SSSSS&*:.:$$!:...
...........%S&%*%@S***#&&#*********************#$#*********S@!:%##@*............
............::$@$*:@#*:**!!@*******************#%!!$#*********&*::..............
............!#SSSS%.:*#SS#%.@********************S&%!!$#********#:..............
...........:#SSSS#*:$SSSSS&.*#S**********************&%!!$#*******..............
...........:$#SS&!!&SSSSS@::*!!%#***********%!$#********&%!!$&#&%...............
.............!*!:*#SSSSS$:%#SS&!:S**********S&%!!$#********@....................
................!SSSSS#*:@SSSSS$.$#S***********S&%!!%&S****%....................
................:@SSS@:!&SSSSS$:!*!!%S**S&S********#$!!%%%!.....................
..................!**.!SSSSS#%.%#SS&:!S*#*!!%&S********.........................
......................!#SSS&!:@SSSSS%.#***S&$*!*$#SS#$:.........................
.......................:%$%::#SSSSS$:%********S&!.::............................
............................:@SSS#*..*%@&#SSSS&%:...............................
.............................:*$%!........::::..................................
'''
prize_3 = '''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
'''

attempt = 1
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

computer_score = 0
user_score = 0



def check_win():
    global computer_score,user_score
    if (choices[computer_choice] == choices[user_choice]):
        display_win(0)
    elif (computer_choice+1) % 3 == user_choice:
        user_score=1+user_score
        display_win(1)
    else:
        computer_score=1+computer_score
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
    print("\n\n")

choice1 = '''
 |-----------------------|  '''
choice2 = ''' |                       |
 |-----------------------|
        \ (•◡•) /
         \     /
''' 


# * main code block
console.print("Welcome to \n", style="bold blue")
console.print(i, style="bold blue")
while attempt <= 3:
    print(choice1)
    print(" | Enter your choice :   |")
    print(" |\t1.Rock           |\n |\t2.Paper          |\n |\t3.Scissors       |")
    computer_choice = random.choice(list1)
    print(choice2)
    user_choice = int(input("→ "))
    print("\n\n")
    check_win()
    attempt += 1
console.print(main_table)
console.print("")
if computer_score < user_score:
    console.print(tabulate(my_data, headers=["Congrats, you won!!"],
                    tablefmt="grid"), style="bold green")
    console.print(prize_1,style="bold yellow")
elif computer_score > user_score:
    console.print(tabulate(my_data, headers=["You loss better luck next time!"],
                    tablefmt="grid"), style="bold yellow")
    console.print(prize_3,style="bold green")
elif computer_score == user_score:
    console.print(tabulate(my_data, headers=["The match was a tie"],
                    tablefmt="grid"), style="bold blue")
    console.print(prize_2,style="bold white")
