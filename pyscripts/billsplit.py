import re
MAX_RETRIES = 3
def secure_input(prompt, pattern=None, cast_fn=None, min_value=None, max_value=None):
    for attempt in range(MAX_RETRIES):
        user_input = input(prompt).strip()
        if len(user_input) > 50:
            print("Input too long. Please enter a reasonable value.")
            continue
        if pattern and not re.fullmatch(pattern, user_input):
            print("Input contains invalid characters. Try again.")
            continue
        try:
            value = cast_fn(user_input)
        except ValueError:
            print("Invalid number format. Please try again.")
            continue
        if min_value is not None and value < min_value:
            print(f"Value must be at least {min_value}. Try again.")
            continue
        if max_value is not None and value > max_value:
            print(f"Value must be at most {max_value}. Try again.")
            continue
        return value
    raise ValueError("Maximum retries exceeded. Program terminated.")


print("Welcome to the NIST-validated Tip Calculator!\n")

bill = secure_input(
    prompt="Total bill amount: ",
    pattern=r"[0-9]+(\.[0-9]{1,2})?",
    cast_fn=float,
    min_value=0.50,
    max_value=10000
)

tip = secure_input(
    prompt="Tip % (e.g., 10, 12, 15): ",
    pattern=r"[0-9]{1,2}(\.[0-9]{1,2})?",
    cast_fn=float,
    min_value=0,
    max_value=30
)

share = secure_input(
    prompt="Number of people splitting the bill: ",
    pattern=r"[0-9]{1,3}",
    cast_fn=int,
    min_value=1,
    max_value=100
)

each = round(bill * (1 + tip / 100) / share, 2)

print(f"\nEach person pays: ${each:.2f}")
print(f"Bill: ${bill}, Tip: {tip}%, People: {share}")





# def get_int(prompt):
#     while True:
#         try:
#             value = int(input(prompt))
#             if value <= 0:
#                 print("Value must be greater  than 0, Try again.")
#                 continue
#             return value
#         except ValueError:
#             print("Invalid integer. Please Try again.")

# def get_float(prompt):
#     while True:
#         try:
#             value = float(input(prompt))
#             if value <= 0:
#                 print("value must be greater than 0, Try again.")
#                 continue
#             return value
#         except ValueError:
#             print("Invalid integer, Please Try again.")

# print("Welcome to the tip Calculator.\n")
# bill = get_float("What was the total Bill?: $")
# tip = get_float("What % of Tip whould you like to give (e.g., 10, 20, 30)?: ")
# share = get_int("how many people to split the bill ?: ")

# each = round(bill * (1 + tip / 100) / share, 2)

# print(f"\nEach persons pays: ${each:.2f}")
# print(f"Bill: ${bill:.2f}, Tip: {tip:.2f}%, People: {share}")
