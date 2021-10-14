s = "snake"
w = "water"
g = "gun"

list = ["s", "w", "g"]
import random
item = random.choice(list)

total_chance = 5
chance = 0
human_point = 0
computer_point = 0
print("\t\t\t\t\t\t\t__SNAKE WATER GUN GAME__")
while chance < total_chance :
    int = input("Enter : s for snake, w for water, g for gun\n")
    rand = random.choice(list)

    if int == rand :
        print("This is a tie.\n 0 point each")

    # if user gives input s
    
    elif int == "s" and rand == "w" :
        human_point = human_point + 1
        print(f"You choose {int} and computers choice is {rand}\n")
        print("Congo!\nYou Won.")
        print(f"Human point is {human_point} and computer point is {computer_point}\n")
    elif int == "s" and rand == "g" :
        computer_point = computer_point + 1
        print(f"You choose {int} and computers choice is {rand}")
        print("Sorry!\nYou Lost.")
        print(f"Human point is {human_point} and computer point is {computer_point}")

    # if user gives input w
    
    elif int == "w" and rand == "g" :
        human_point = human_point + 1
        print(f"You choose {int} and computers choice is {rand}")
        print("Congo!\nYou Won.")
        print(f"Human point is {human_point} and computer point is {computer_point}")
    elif int == "w" and rand == "s" :
        computer_point = computer_point + 1
        print(f"You choose {int} and computers choice is {rand}")
        print("Sorry!\nYou Lost.")
        print(f"Human point is {human_point} and computer point is {computer_point}")
    
    # if user gives input g
    
    elif int == "g" and rand == "s" :
        human_point = human_point + 1
        print(f"You choose {int} and computers choice is {rand}")
        print("Congo!\nYou Won.")
        print(f"Human point is {human_point} and computer point is {computer_point}")
    elif int == "g" and rand == "w" :
        computer_point = computer_point + 1
        print(f"You choose {int} and computers choice is {rand}")
        print("Sorry!\nYou Lost.")
        print(f"Human point is {human_point} and computer point is {computer_point}")

    else :
        print("Invalid input.")

    chance = chance + 1
    print(f"{chance} chances used out of {total_chance}")

print("Game over")
print(f"\nYour point is {human_point} and computer point is {computer_point}")

if computer_point < human_point :
    print("Congrats!You won.")
else :
    print("Better luck next time.")    
     