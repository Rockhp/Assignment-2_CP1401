"""
CP1401 2021-1 Assignment 2
Market Garden Simulator
Student Name: Rajkumar Senthilraj Ragulraj
Date started: 06/09/2021

Pseudocode:
"""
import random

menu_items = ["(W)ait", "(D)isplay plants", "(A)dd new plant", "(Q)uit"]
plants = ["Parsley", "Sage", "Rosemary", "Thyme"]
food_generated = []
num_days = []


def main():
    starter_message()
    choice = ''
    while choice != "q":
        menu()
        choice = input("Choose: ").lower()
        get_choice(choice)
    quit_program()


def starter_message():
    print("Welcome to the Market Garden Simulator \n"
          "Plants cost and generate food according to their name length (e.g., Sage plants cost 4). \n"
          "You can buy new plants with the food your garden generates. \n"
          "You get up to 100 mm of rain per day. Not all plants can survive with less than 30. \n"
          "Let's hope it rains... a lot! \n"
          "You start with these plants:")
    display_plants()


def display_plants():
    for i in plants:
        print(i, end=", ")


def menu():
    print("\n")
    display_stats()
    for option in menu_items:
        print(option)


def get_choice(choice):
    '''
    gets user choice and calls the corresponding function
    '''
    if choice == 'w':
        wait()
    elif choice == 'd':
        display_plants()
    elif choice == 'a':
        add_new_plant()
    elif choice == 'q':
        print("You finished with these plants:")
        display_plants()
    else:
        print("Invalid choice")


def quit_program():
    '''
    displays the exit message
    '''
    print("\n")
    display_stats()
    print("Thank you for simulating. Now go and enjoy a real garden.")


def display_stats():
    '''
    displays the number of days passed, number of plants and food available
    '''
    total_food = get_total_food()
    print(f"After {len(num_days)} days, you have {len(plants)} plants and your total food is {total_food}.")


def wait():
    '''
    simulates rainfall and generates food according to the simulated rainfall
    '''
    rainfall = random.randint(0, 100)
    print(f"Rainfall: {rainfall}mm")
    MIN_RAIN = 30
    food_generated_temp = []
    if rainfall < MIN_RAIN:
        remove_plant()
    for i in range(len(plants)):
        multiplier = random.randint(int(rainfall / 2), int(rainfall))
        final_multiplier = multiplier / 100
        gen_food = int(final_multiplier * len(plants[i]))
        food_generated.append(gen_food)
        food_generated_temp.append(gen_food)
    for i in range(len(plants)):
        print(f"{plants[i]} produced {food_generated_temp[i]}", end=", ")
    num_days.append(1)


def remove_plant():
    '''
    removes a plant in case of low rainfall
    '''
    delete_plant = random.randint(0, len(plants) - 1)
    print(f"Sadly your {plants[delete_plant]} has died.")
    plants.pop(delete_plant)


def add_new_plant():
    '''
    allows the user to add a new plant
    '''
    new_plant = input("Enter plant name: ")
    total_food = get_total_food()
    if len(new_plant) > total_food:
        print(f"{new_plant} would cost {len(new_plant)} food. With only {total_food}, you cannot afford it")
    elif new_plant in plants:
        print(f"You already have a {new_plant}.")
    else:
        plants.append(new_plant)
        food_generated.append(0 - len(new_plant))


def get_total_food():
    '''
    calculates the total food available
    '''
    total_food = 0
    for i in range(len(food_generated)):
        total_food += (food_generated[i])
    return total_food


main()
