from multiprocessing import cpu_count
import random
from this import d
print("Welcoming you to Rock-Paper-Scissors game\n Here You'are going to play against the CPU machine\n The rules of the game are: ")
print(" Paper beats Rock\nScissors \n Rock beats Scissors\n beats Paper")
print("There are 3 options, to pick one for every move\n which are: 'R' for 'Rock', 'P' for 'Paper' and 'S' for 'Scissors'")


list_of_choices = ["R", "P", "S"]
user_count = 0
CPU_counter = 0
while True:
    user = input("pick your move, either R or P or S:\n").upper()
    while user not in list_of_choices:          
        user = input("Error! picked a invalid option, try again\nplease pick either R or P or S:\n").upper()
    CPU = random.choice(list_of_choices)
    if user == CPU:
        print("its a tie, repeat")
        continue
    elif user == 'R' and CPU == 'S':
        print("user (Rock) : CPU (Scissors)")
        user_count += 1
        print("wins %d:%d" % (user_count, CPU_counter))
    elif user == 'R' and CPU == 'P':
        print("user (Rock) : CPU (Paper)")
        CPU_counter += 1
        print("wins %d:%d" % (user_count, CPU_counter))
    elif user == 'P' and CPU == 'R':
        print("user (Paper) : CPU (Rock)")
        user_count += 1
        print("wins %d:%d" % (user_count, CPU_counter))
    elif user == 'P' and CPU == 'S':
        print("user (Paper) : CPU (Scissors)")
        CPU_counter += 1
        print("wins %d:%d" % (user_count, CPU_counter))
    elif user == 'S' and CPU == 'R':
        print("user (Scissors) : CPU (Rock)")
        CPU_counter += 1
        print("wins %d:%d" % (user_count, CPU_counter))
    else:
        print("user (Scissors) : CPU (Paper)")
        user_count += 1
        print("wins %d:%d" % (user_count, CPU_counter))
    winner = False
    if user_count != CPU_counter and (user_count == 3 or CPU_counter == 3):
        if user_count > CPU_counter and user_count == 3:
            print("The user is the winner\nThank you for playing this game")
            break
        else:
            print("The CPU is the winner\nThank you for playing this game")
            break