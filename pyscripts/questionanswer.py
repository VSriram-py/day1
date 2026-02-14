import random

data = [
    {"q": "The capital of India is Bombay", "a": "False"},
    {"q": "The Earth revolves around the Sun", "a": "True"},
    {"q": "Water boils at 100 degrees Celsius at sea level", "a": "True"},
    {"q": "The Great Wall of China is visible from space with the naked eye", "a": "False"},
    {"q": "Humans have walked on the Moon", "a": "True"},
    {"q": "Lightning never strikes the same place twice", "a": "False"},
    {"q": "Mount Everest is the tallest mountain above sea level", "a": "True"},
    {"q": "Birds are mammals", "a": "False"},
    {"q": "Sharks are fish", "a": "True"},
    {"q": "Venus is the closest planet to the Sun", "a": "False"},
    {"q": "The human body has 206 bones", "a": "True"},
    {"q": "The Pacific Ocean is the largest ocean on Earth", "a": "True"},
    {"q": "Bats are blind", "a": "False"},
    {"q": "Gold is heavier than silver", "a": "True"},
    {"q": "Spiders are insects", "a": "False"},
    {"q": "The Nile is the longest river in the world", "a": "True"},
    {"q": "Sound travels faster than light", "a": "False"},
    {"q": "The Eiffel Tower is in London", "a": "False"},
    {"q": "Humans and dinosaurs lived at the same time", "a": "False"},
    {"q": "The Moon has gravity", "a": "True"},
    {"q": "Plants produce oxygen through photosynthesis", "a": "True"},
    {"q": "Antarctica is the largest desert in the world", "a": "True"},
    {"q": "A leap year has 366 days", "a": "True"},
    {"q": "Humans have five senses", "a": "True"},
    {"q": "The chemical symbol for gold is Au", "a": "True"},
    {"q": "An octopus has three hearts", "a": "True"},
    {"q": "Mercury is the hottest planet in the solar system", "a": "False"},
    {"q": "The Amazon rainforest is the largest rainforest on Earth", "a": "True"},
    {"q": "A triangle has four sides", "a": "False"},
    {"q": "Ostriches can fly", "a": "False"},
    {"q": "Your fingernails and hair continue to grow after death", "a": "False"},
    {"q": "Dolphins are mammals", "a": "True"},
    {"q": "The speed of light is faster than the speed of sound", "a": "True"},
    {"q": "The Statue of Liberty was a gift from France to the United States", "a": "True"},
    {"q": "Polar bears live in Antarctica", "a": "False"},
    {"q": "Bananas grow on trees", "a": "False"},
    {"q": "The human heart has four chambers", "a": "True"},
    {"q": "The Sahara is the coldest desert in the world", "a": "False"},
    {"q": "Humans share about 50% of their DNA with bananas", "a": "True"},
    {"q": "A group of lions is called a pride", "a": "True"},
    {"q": "The Sun is a star", "a": "True"},
    {"q": "The capital of Australia is Sydney", "a": "False"},
    {"q": "There are seven continents on Earth", "a": "True"},
    {"q": "Ice sinks in water", "a": "False"},
    {"q": "An eagle is a reptile", "a": "False"},
    {"q": "Honey never spoils", "a": "True"},
    {"q": "Humans need oxygen to survive", "a": "True"},
    {"q": "Whales are fish", "a": "False"},
    {"q": "There are 24 hours in a day", "a": "True"},
    {"q": "The brain is part of the circulatory system", "a": "False"}
]

def normalize_answer(user_input):
    user_input = user_input.strip().lower()
    if user_input in {"q", "quit"}:
        return "quit"
    truthy = {"t", "true", "y", "yes"}
    falsy = {"f", "false", "n", "no"}
    if user_input in truthy:
        return "true"
    if user_input in falsy:
        return "false"
    return None

class Question:
    def __init__(self, q, a):
        self.q = q
        self.a = a

class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list
        self.score = 0
    def next_question(self):
        current_q = self.q_list[self.q_num]
        self.q_num += 1
        while True:
            raw = input(f"Q.{self.q_num}: {current_q.q} (True/False or q to quit): ")
            user_a = normalize_answer(raw)
            if user_a == "quit":
                print("\nExiting quiz...")
                print(f"Final Score: {self.score}/{self.q_num - 1}")
                exit()
            if user_a is None:
                print("Invalid input. Enter t/f, true/false, y/n, or q to quit.")
            else:
                break
        self.check_a(user_a, current_q.a)

    def check_a(self, user_a, correct_a):
        if user_a == correct_a.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Wrong!")
        print(f"The correct answer is: {correct_a}.")
        print(f"Score: {self.score}/{self.q_num}\n")

    def still_has_q(self):
        return self.q_num < len(self.q_list)

q_bank = [Question(q["q"], q["a"]) for q in data]
random.shuffle(q_bank)
quiz = QuizBrain(q_bank)
while quiz.still_has_q():
    quiz.next_question()
print(f"Quiz complete! Final score: {quiz.score}/{len(q_bank)}")












# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# print(table)



# #import turtle
# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
