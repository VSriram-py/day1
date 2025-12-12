import random

uppercase_letters = [chr(i) for i in range(65, 91)]      # A–Z
lowercase_letters = [chr(i) for i in range(97, 123)]     # a–z
numbers = [str(i) for i in range(10)]
symbols = list("!@#$%^&*()-_=+[]{};:,.<>?/\\|`~")

# print("Uppercase:", uppercase_letters)
# print("Lowercase:", lowercase_letters)
# print("Numbers:", numbers)
# print("Symbols:", symbols)

print("Welcome to Password generator.\n")
while True:
    try:
        length = int(input("Enter the password length (8–16): "))
    except ValueError:
        print("Enter an integer")
        continue

    if length < 8 or length > 16:
        print("Enter a value between 8 and 16")
        continue
    break

while True:
    try:
        ul  = int(input("Enter number of UPPERCASE letters: "))
        ll  = int(input("Enter number of LOWERCASE letters: "))
        num = int(input("Enter number of NUMBERS: "))
        sy  = int(input("Enter number of SYMBOLS: "))
    except ValueError:
        print("Enter only integer values for character counts.")
        continue
    total = ul + ll + num + sy
    if total < length:
        print("The total count of all characters must be **less than or equal** to the password length.")
        print(f"You entered total: {total}, but length is {length}. Try again.\n")
        continue
    elif total > length:
        print("The total count of all characters must not be **greater than or equal** to the password length.")
        print(f"You entered total: {total}, but length is {length}. Try again.\n")
        continue
    else:
        break
password = []
ps = ""
password += random.sample(uppercase_letters, ul)
password += random.sample(lowercase_letters, ll)
password += random.sample(numbers, num)
password += random.sample(symbols, sy)
random.shuffle(password)
for i in password:
    ps += i
print(f"your random password is {ps}")


