import secrets
import string

WORDS_WITH_HINTS = {
    "camel": "A desert animal with a hump.",
    "forest": "A large area filled with trees.",
    "python": "A popular programming language.",
    "ocean": "A vast body of salt water.",
    "keyboard": "You type on this device.",
    "mountain": "A very tall natural elevation.",
    "island": "Land surrounded by water.",
    "tiger": "A striped wild cat.",
    "planet": "Earth is one of these.",
    "guitar": "A string musical instrument.",
    "desert": "A dry, sandy region.",
    "river": "A flowing body of fresh water.",
    "castle": "A large old fortification.",
    "robot": "A machine capable of performing tasks.",
    "bridge": "Structure built to cross obstacles.",
    "jungle": "A dense tropical forest.",
    "rocket": "Used for space travel.",
    "shield": "Used for protection in combat.",
    "lantern": "A portable light source.",
    "helmet": "Protective headgear."
}

def get_secure_random_word():
    word = secrets.choice(list(WORDS_WITH_HINTS.keys()))
    return word.lower(), WORDS_WITH_HINTS[word]

def play_game():
    word, hint = get_secure_random_word()
    guessed = set()
    attempts = 0
    max_attempts = len(word)

    print(f"\nWord length: {len(word)}")
    print(f"Hint: {hint}\n")

    while True:
        #if attempts > max_attempts:
        if attempts > 7:
            print(f"\nNo attempts left! The word was: {word}\n")
            break
        user_char = input("Enter a letter: ").strip().lower()
        if len(user_char) != 1 or user_char not in string.ascii_lowercase:
            print("Invalid input. Enter a single alphabetic letter.\n")
            continue
        if user_char in guessed:
            print("You already guessed this letter.\n")
            continue
        guessed.add(user_char)
        display = ""
        for ch in word:
            if ch in guessed:
                display += ch 
            else:
                 display += "_"

        if not user_char in word:
            attempts += 1

        print(display + "\n")
        if "_" not in display:
            print("You won!")
            break

def main():
    print("Welcome to the Secure Word Guess Game!")

    while True:
        play_game()
        choice = input("Do you want to play again? (y/n): ").strip().lower()
        if choice in ("n", "no"):
            print("\nThanks for playing! Goodbye.\n")
            break
        elif choice in ("y", "yes"):
            continue
        else:
            print("Invalid choice. Exiting for safety.\n")
            break

if __name__ == "__main__":
    main()





# import random
# import secrets

# word = secrets.choice(ENGLISH_WORDS)

# #word = "camel"
# wl = len(word)
# print(wl)
# #user_char = input("Enter the Char :")
# i = 0
# user_input = []
# #output_char = ""
# while True:
#     output_char = ""
#     i += 1
#     if i > wl:
#         print(f"\ndead! the world is {word}\n")
#         break
#     user_char = input("\nEnter the Char :")

#     for char in word:
#         if user_char == char:
#             user_input.append(user_char)
#             output_char += char
#         elif char in user_input:
#             output_char += char
#         else:
#             output_char += "_"
                    
#     print(output_char + "\n")
#     if "_" not in output_char:
#         print("You won!!!")
#         break














# #input("Whats ur name ?\t:\t")
# print(" Hello " + input("Whats ur name ?\t:\t") + "!")

# print("brand name gen")
# name = input("Whats ur name ?\t:\n")
# print(f"username : {name}\n")
# name2 = input("Whats ur name ?\t:\n")
# print(f"username : {name2}\n")
# mystery = 734_529.678
# print(mystery)

# street_name = "Abbey Road"
# print(street_name[4] + street_name[7])