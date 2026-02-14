# import random
# from random import choice

# choices = ["Rock", "Paper", "Scissors"]

# while True:
#     user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 For Scissors.\n"))
#     if not isinstance(user, int) or user < 0 or user > 2:
#         print("Enter valid input. Try again\n")
#         continue
#     break

# comp = random.choice([0,1,2])
# #print(user, comp)
# if user == comp:
#     print(f"both selected {choices[user]}, so tie!")
# elif (user == 0 and comp == 2) or (user == 1 and comp == 0) or (user ==2 and comp ==1):
#     print(f"user selected {choices[user]} and comp selected {choices[comp]}, so user wins!")
# else:
#     print(f"user selected {choices[user]} and comp selected {choices[comp]}, so comp wins!")



for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")



# print("\thello" + " " + "Sri\nram")

# print("Notes from Day 1")
# print("The print statement is used to output strings")
# print("Strings are strings of characters")
# print("String Concatenation is done with the + sign")
# print("New lines can be created with a \ and the letter n")
