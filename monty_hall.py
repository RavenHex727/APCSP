import random
import copy

# initialize variables
doors = [0, 0, 0]  # 0 represents a goat, 1 represents a car

# randomly assign the car behind one of the doors
car_index = random.randint(0, 2)
doors[car_index] = 1

# the player selects a door
print("Welcome to the Monty Hall Problem! In front of you, you will find three doors!")
print("[DOOR 1] [DOOR 2] [DOOR 3]")
print("Behind one of these doors is a brand! new! car!!!! Behind the other two...a mean, annoying GOAT!")
selected_door = int(input("CHOOSE WISELY! CHOOSE NOW! (1, 2, or 3): "))

def select_reveal_door(doors, selected_door, car_index):
  # FINISH THIS CODE TO CHOOSE A DOOR TO REVEAL
  # THE DOOR SHOULD HAVE A GOAT BEHIND IT BUT SHOULD NOT BE THE DOOR THE PLAYER HAS CHOSEN

    if int(selected_door) - 1 == car_index:
        reveal_door = random.choice([index for index in range(0, 3) if index != car_index]) + 1

    else:
        doors_copy = [n + 1 for n in range(len(copy.deepcopy(doors)))]
        doors_copy.remove(int(selected_door))
        doors_copy.remove(int(car_index + 1))
        reveal_door = doors_copy[0]

    return reveal_door

print("YOU HAVE CHOSEN DOOR ", selected_door)
revealed_door = select_reveal_door(doors, selected_door, car_index)
print("I CAN REVERAL TO YOU THAT ", revealed_door, " IS NOT HIDING A CAR! ")
switch_response = input("Would you like to switch? Y or N? ")

def end_game(doors, selected_door, revealed_door, switch_response):
  # BASED ON THE PLAYERS SWITCH CHOICE, DECIDE IF THE PLAYER HAS WON
    doors_copy = [n + 1 for n in range(len(copy.deepcopy(doors)))]

    for door_num in range(len(doors)):
        if doors[door_num] == 1:
            car_door = door_num + 1

    if switch_response == "N":
        if doors[int(selected_door) - 1] == 1:
            return True

    if switch_response == "Y":
        doors_copy.remove(int(selected_door))
        doors_copy.remove(int(revealed_door))
        remaining_door = doors_copy[0]

        if doors[int(remaining_door) - 1] == 1:
            return True

    return False

# PRINT THE WIN/LOSS SCENARIO
print(end_game(doors, selected_door, revealed_door, switch_response))

## MONTY PYTHON SIMULATIONS
# Define the number of simulations and initialize the counters for wins
num_simulations = int(input("How many simulations would you like to run on the monty hall python problem? "))


def monty_hall_problem(num_simulations):
    switch_wins = 0
    stay_wins = 0

    for n in range(num_simulations):
        doors = [0, 0, 0]  # 0 represents a goat, 1 represents a car
        car_index = random.randint(0, 2)
        doors[car_index] = 1
        selected_door = random.choice(["1", "2", "3"])
        revealed_door = select_reveal_door(doors, selected_door, car_index)

        if end_game(doors, selected_door, revealed_door, "Y") == True:
            switch_wins += 1

        if end_game(doors, selected_door, revealed_door, "N") == True:
            stay_wins += 1

    return f"Num switch wins: {switch_wins} \n Num stay wins: {stay_wins}"
  

# Print the results

print(monty_hall_problem(num_simulations))