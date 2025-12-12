def fibonacci_gen(n, m=10):
    if not isinstance(n, int) or n <= 0:
        print("Invalid value. Enter a +ve integer.")
        return
    if n > m:
        print(f"Enter an integer less than {m}. Try again.")
        return
    a, b = 0, 1
    for _ in range(n):
        yield a  #generator
        a, b = b, a + b

n = int(input("Enter the value of n: "))
print(list(fibonacci_gen(n)))



# def fibonacci(n, m=10):
#     if n <= 0:
#         print("invalid value")
#         return[]
#     elif n == 1:
#         return[0]
#     elif n == 2:
#         return[0,1]
#     elif n > m:
#         print(f"enter a interger less than {m}, try again")
#     else:
#         fs = [0,1]
#         for _ in range (2,n):
#             next_number = fs[-1] + fs[-2]
#             fs.append(next_number)
#         return fs
# print(fibonacci(int(input("Enter the value of n: "))))


# def fibonacci(n):
#     fib_series = []
#     a, b = 0, 1
#     for _ in range(n):
#         fib_series.append(a)
#         a, b = b, a+b
#     return fib_series
# n_terms = 10
# print(f"First {n_terms} Fibonacci numbers: {fibonacci(n_terms)}")


# number_to_check = int(input("whats the number you want to check?: "))
# if (number_to_check % 2) == 0:
#     print("even")
# else:
#     print("odd")


# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)
# if bmi < 18.5:
#     print("Under Weight")
# elif(bmi >= 18.5 and bmi <=24.9):
#     print("Normal")
# elif(bmi >= 25 and bmi <= 29.9):
#     print("over weight")
# else:
#     print("unkown")

