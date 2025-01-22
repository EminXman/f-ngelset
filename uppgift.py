# Import the random module for potential future use
import random

# Function to sort students into houses
def sort_student():
    # Ask the student for their name
    name = input("Welcome to the Sorting Ceremony! What is your name? ")

    # Questions about the student's traits and convert the answers to integers
    courage = int(input("How courageous are you on a scale of 1-10? "))
    intelligence = int(input("How intelligent are you on a scale of 1-10? "))
    loyalty = int(input("How loyal are you on a scale of 1-10? "))
    ambition = int(input("How ambitious are you on a scale of 1-10? "))

    # Compare the student's answers and sort them into the right house
    if courage >= intelligence and courage >= loyalty and courage >= ambition:
        house = "Gryffindor"
    elif intelligence >= courage and intelligence >= loyalty and intelligence >= ambition:
        house = "Ravenclaw"
    elif loyalty >= courage and loyalty >= intelligence and loyalty >= ambition:
        house = "Hufflepuff"
    else:
        house = "Slytherin"

    # Print the result with formatted output
    print(f"{name}, you have been sorted into {house}!\n")

# Main program that asks if the student wants to be sorted again
def main_program():
    while True:
        sort_student()
        wants_to_sort_again = input("Do you want to be sorted again? (yes/no): ")
        if wants_to_sort_again.lower() != "yes":
            print("Thank you for participating in the Sorting Ceremony!")
            break

# Start the program
main_program()
