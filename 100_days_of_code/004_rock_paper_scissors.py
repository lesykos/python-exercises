import random
import ASCII_Art as ascii

items = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}

print(f"0 - {items[0]}, 1 - {items[1]}, 2 - {items[2]}")
user_option = input("Your option: ")
pc_option = random.randint(0,2)
test_user_options = map(str, items.keys())

if user_option.isnumeric() and user_option in test_user_options:
    user_option = int(user_option)
else:
    print("Invalid option")
    exit()

def print_item_ascii(item):
    match item:
        case "Rock":    print(ascii.rock())
        case "Paper":   print(ascii.paper())
        case "Scissors":    print(ascii.scissors())
        case _:         print("Invalid option")

print_item_ascii(items[user_option])

print(f"PC choose {items[pc_option]}")

print_item_ascii(items[pc_option])

match (items[user_option], items[pc_option]):
    case ("Rock", "Rock"):
        print("Draw :)")
    case ("Rock", "Paper"):
        print("You lose...")
    case ("Rock", "Scissors"):
        print("You WIN!")
    case ("Paper", "Rock"):
        print("You WIN!")
    case ("Paper", "Paper"):
        print("Draw :)")
    case ("Paper", "Scissors"):
        print("You lose...")
    case ("Scissors", "Rock"):
        print("You lose...")
    case ("Scissors", "Paper"):
        print("You WIN!")
    case ("Scissors", "Scissors"):
        print("Draw :)")
    case _:
        print("Hmm..")
