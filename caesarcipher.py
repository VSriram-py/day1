#alphabet = "abcdefghijklmnopqrstuvwxyz"
#numbers = "0123456789"
symbol = " ,."
alphabet = [chr(i) for i in range(97, 123)]
#print(alphabet)
numbers = [str(i) for i in range(10)]
#print(numbers)
#symbol = [" ", ".", ","]
i = 0
while True:
    direction = input("Type 'encode' to encode, type 'decode' to decode: ").lower()
    if not (direction == "encode" or direction == "decode"):
        print("invalid input, Try again. ")
        i += 1
        if i >= 3:
            print("Maximum retries exceeded. Exiting program.")
            exit()
        continue
    else:
        break
i = 0
direction = "encode"
while True:
    if i >= 3:
        print("Maximum retries exceeded. Exiting program.")
        exit()
    text = input(f"Type your message to {direction}:\n").lower()
    valid = True
    for c in text:
        #if not (c.isalnum() or c in " ,."):
        if not (c in alphabet or c in numbers or c in symbol):
            print('Unsupported char, only alphabet, numbers, space, "," and "." allowed.')
            valid = False
            i += 1
            break
    if valid:
        break

i = 0
while True:
    if i >= 3:
        print("Maximum retries exceeded. Exiting program.")
        exit()
    try:
        shift = int(input("Type the shift number [1-99]: "))
        if not 1 <= shift <= 99:
            print("The number is out of range.")
            i += 1
            continue
        else:
            break
    except ValueError:
        i += 1
        print("Invalid Number.")


def encrypt(text, shift):
    for c in text:
        if c in symbol:
            print(c,end = "")
        elif c in numbers:
            print((int(c) + shift) % len(numbers),end = "")
        elif c in alphabet:
            print(chr(((ord(c) - 97 + shift) % len(alphabet)) + 97),end = "")
        else:
            print("bug")
            exit()

def dencrypt(text, shift):
    for c in text:
        if c in symbol:
            print(c,end = "")
        elif c in numbers:
            print((int(c) - shift) % len(numbers),end = "")
        elif c in alphabet:
            print(chr(((ord(c) - 97 - shift) % len(alphabet)) + 97),end = "")
        else:
            print("bug")
            exit()

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    dencrypt(text, shift)
else:
    print("invalid input\n")

# def calculate_love_score(name1, name2):
#     totaltrue,totallove = 0,0
#     w1,w2="true","love"
#     for n in w1:
#         i = 0
#         for m in name1:
#             if n == m:
#                 i += 1 
#         print(f"{n.upper()} occurs {i} times")
#         totaltrue += i
#         print(f"Total = {totaltrue}")
#     for n in w2:
#         i = 0
#         for m in name2:
#             if n == m:
#                 i += 1 
#         print(f"{n.upper()} occurs {i} times")     
#         totallove += i
#         print(f"Total = {totallove}")
#     return(totaltrue+totallove)   
    
# n1 = input("enter the first name: ").lower()
# n2 = input("enter the second name: ").lower()
# print(f"Love Score = {calculate_love_score(name1=n1, name2=n2)}")


# def life_in_weeks(age):
#     bal = 90 - int(age)
#     return (bal * 52)

# age = input("Enter you age: ")
# print(f"You have {life_in_weeks(age)} weeks left.")



# def greet(name):
#     print("hello..." + name.capitalize())
#     print("how do you do!")
#     print("Isn't the weather nice?")

# greet("sriram")


# #print("length : " + str(len(" Hello " + "Username :" + input("Whats ur name ?\t:\t") + "!")))
# print("int " + str(type(123)))
# print("Float " + str(type(1.1)))
# print("string " + str(type("sfasdff")))
# print("bool " + str(type(True)))
# print("")