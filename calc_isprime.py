#calc, is prime
def calculate(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid Operation"

num1 = float(input("Enter first number: "))
op = input("Enter operation (+ - * /): ")
num2 = float(input("Enter second number: "))
result = calculate(num1, op, num2)
print("Result:", result)

while True:
    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice != "yes":
        print("Exiting calculator.")
        break
    num1 = result
    print(f"Starting new operation with num1 = {num1}")
    op = input("Enter operation (+ - * /): ")
    num2 = float(input("Enter next number: "))
    result = calculate(num1, op, num2)
    print("Result:", result)

# def is_prime(num):
#     if num <= 1:
#         return False
#     if num == 2:
#         return True
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
# i = 0
# while (input("Do you want find the prime number [y/n]: ").strip().lower() == "y"):
#     i += 1
#     num = int(input(f"Example Input {i}\n"))
#     print(f"Example Output {i}")
#     if is_prime(num):
#         print("True")
#     else:
#         print("False")