"""
CP1401 2021-1 Assignment 2
Market Garden Simulator
Student Name: Rajkumar Senthilraj Ragulraj
Date started: 07/09/2021

Pseudocode:
menu items = (Wait, display, Add new plants, Quit) -
plants = (parsley, sage, rosmary, Thyme)
Ask for food generated
Ask for number of days

Display starter message
Ask user for his/her choice
if user choice = Q, then quit program and display exit message
if user choice = W, use random.randint to generate rain. If rainfall < min rain, remove plant
if user choice = A, prompt use to ad plant
"""

import random

menu_items = ["(W)ait", "(D)isplay plants", "(A)dd new plant", "(Q)uit"]
plants = ["Parsley", "Sage", "Rosemary", "Thyme"]
food_generated = []
num_days = []


def main():
    starter_message()
    choice = ' '
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
    This part gets the choice of the user. The choices are given above
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
    This part displays the exit message when the user chooses the option to quit
    '''
    print("\n")
    display_stats()
    print("Thank you for simulating. Now go and enjoy a real garden.")


def display_stats():
    '''
    This part displays the number of days passed, number of plants and the amount of food avaliable.
    '''
    total_food = get_total_food()
    print(f"After {len(num_days)} days, you have {len(plants)} plants and your total food is {total_food}.")


def wait():
    '''
    This part simulates rain and produces food for the plant according to the rain simulated
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
    This part removes plants if the rain is lower than expected
    '''
    delete_plant = random.randint(0, len(plants) - 1)
    print(f"Sadly your {plants[delete_plant]} has died.")
    plants.pop(delete_plant)


def add_new_plant():
    '''
    This part allows the user to add plants
    '''
    new_plant = input("Enter plant name: ")
    total_food = get_total_food()
    if len(new_plant) > total_food:
        print(f"{new_plant} would cost {len(new_plant)} food. With only {total_food}, you cannot afford it")
    elif new_plant in plants:
        print(f"You a  lready have a {new_plant}.")
    else:
        plants.append(new_plant)
        food_generated.append(0 - len(new_plant))


def get_total_food():
    '''
   This part collects the total food available.
    '''
    total_food = 0
    for i in range(len(food_generated)):
        total_food += (food_generated[i])
    return total_food


main()





