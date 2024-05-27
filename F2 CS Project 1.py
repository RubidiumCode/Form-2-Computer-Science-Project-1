# Import the system module so we can clear the screen, making the UI cleaner
from os import system

# Basic function to return information about the sack based on its weight and type
# The  function returns if the sack is of an acceptable weight, is not why, and the full name of the type of sack, so the code further on can be neater
def get_sack_info(content, weight):
    # I only referenced the first character of the input as the UI intends for the input to be only one character, so if the user inputs more than that we assume it was a typo or they inputted the full name of the sack they wanted. eg "Concrete" instead of "c"
    
    if content[0] == "c" or content[0] == "C":
        if weight >= 25.1:
            return False, "Sack is too heavy", "Concrete"
        elif weight <= 24.9:
            return False, "Sack is too light", "Concrete"
        else:
            return True, "Concrete"
    elif content[0] == "g" or content[0] == "G":
        if weight >= 50.1:
            return False, "Sack is too heavy", "Gravel"
        elif weight <= 49.9:
            return False, "Sack is too light", "Gravel"
        else:
            return True, "Gravel"
    elif content[0] == "s" or content[0] == "S":
        if weight >= 50.1:
            return False, "Sack is too heavy", "Sand"
        elif weight <= 49.9:
            return False, "Sack is too light", "Sand"
        else:
            return True, "Sand"
    else:
        return False, "Invalid Sack Type", "Unknown"

# Initialising important variables
number_of_sand_sacks = 0
number_of_gravel_sacks = 0
number_of_concrete_sacks = 0

# I keep a running count of the weight, instead of just multiplying the number of sacks by its accepted weight, as it allows a small range of acceptable weights, and this is to keep the total weights more accurate
total_sand_weight = 0
total_gravel_weight = 0
total_concrete_weight = 0

number_of_rejected_sacks = 0

# infinite loop to allow the user to order as much as they want until they are done
while True:

    # Promt for the user to input what sack they want, the letters in brackets imply what letter should be inputted to select that option. eg. [C]oncrete implies for the letter c to be inputted
    print(
        "Input Sack\n",
        "[S]and\n",
        "[G]ravel\n",
        "[C]oncrete\n",
        "[D]one\n"
    )
    sack_input_type = input("> ")

    # Code to escape out of the loop if they say they are done
    if sack_input_type[0] == "d" or sack_input_type[0] == "D":
        break

    # Clear the screen to make the UI neater
    system("cls")

    # Prompt the user to input the intended weight of the sack they want to order
    print(
        "Enter weight of sack(kg):"
    )
    # Casts(converts) the user input to a float(real), as the input would otherwise be considered a string by the program
    sack_input_weight = float(input("> "))

    # Clear the screen to make the UI neater
    system("cls")

    # Returns an array of values for other information about the sack based on its weight and contents demonstrated in the get_sack_info() function above
    sack_info = get_sack_info(sack_input_type, sack_input_weight)

    # Tells the user if their sack got rejected or accepted, and updates the relevant statistics that we want to keep track of
    if sack_info[0]:
        print(f"Accepted {sack_info[1]} sack of weight {sack_input_weight}\n")
        if sack_info[1] == "Sand":
            total_sand_weight += sack_input_weight
            number_of_sand_sacks += 1
        elif sack_info[1] == "Gravel":
            total_gravel_weight += sack_input_weight
            number_of_gravel_sacks += 1
        elif sack_info[1] == "Concrete":
            total_concrete_weight += sack_input_weight
            number_of_concrete_sacks += 1
    else:
        print(f"{sack_info[2]} sack rejected, reason: {sack_info[1]}\n")
        number_of_rejected_sacks += 1

# Clear the screen to make the UI neater
system("cls")

# Tells the user how much they ordered and how many sacks were rejected
print(f"Total order weight: {total_concrete_weight + total_gravel_weight + total_sand_weight}kg")
print(f"Total number of rejected sacks: {number_of_rejected_sacks}")

# Calculates the cost of the customer's order
concrete_cost = number_of_concrete_sacks * 3
sand_cost = number_of_sand_sacks * 2
gravel_cost = number_of_gravel_sacks * 2
total_cost = concrete_cost + gravel_cost + sand_cost

# Calculated how much discount the customer is entitled to
number_of_special_packs = int(min(number_of_concrete_sacks, number_of_sand_sacks * 2, number_of_gravel_sacks * 2)/2)
discount_price = number_of_special_packs * 10

# Prints all the relevant statistics to the user
print(
    f"Concrete cost: ${concrete_cost}",
    f"\nSand cost: ${sand_cost}",
    f"\nGravel cost: ${gravel_cost}",
    f"\nSubtotal: ${total_cost}"
    f"\nNumber of special packs: {number_of_special_packs}",
    f"\n\nAmount saved: ${discount_price}",
    f"\nTotal price: ${total_cost - discount_price}"
)