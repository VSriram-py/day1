import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
def cal_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw!"
    elif comp_score == 0:
        return "Lose, opponent has Backjack!!!"
    elif user_score == 0:
        return "Win with Balckjack "
    elif user_score > 21:
        return "You went over,  You lose!!!"
    elif comp_score > 21:
        return "Opponent went over, You Win"
    elif user_score > comp_score:
        return "You Win"
    else:
        return "You Lose"
def play_game():
    user_cards = []
    comp_cards = []
    user_score = -1
    comp_score = -1
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not game_over:
        user_score = cal_score(user_cards)
        comp_score = cal_score(comp_cards)
        print(f"Your card: {user_cards}, current score: {user_score}")
        print(f"Computers First card: {comp_cards[0]}")


        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = cal_score(comp_cards)

    print(f"Your Final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower() == "y":
    print("\n" * 20)
    play_game()


# bidder = {}
# def askbid():
#     name = input("what is your name?: ")
#     val = int(input("what is your bid?: $"))
#     bidder[name] = val

# def highestbid(bidder):
#     hbidder = {}
#     hbidder = dict(sorted(bidder.items(), key=lambda x: x[1], reverse=True))
#     for key in hbidder:
#         print(f"{key}: {hbidder[key]}")
#     return hbidder

# while True:
#     #print("\n" * 30)
#     askbid()
#     cont = input("Do you want to continue with another user who want to bid?[Yes/no]: ").strip().lower()
#     if cont in ("yes", "y"):
#         print("\n" * 10)
#         continue
#     elif cont in ("no","n"):
#         print("\n" * 10)
#         print(f"Higher Bidder is")
#         highestbid(bidder)
#         break
#     else:
#         print("invalid input!, default Yes")
#         continue



# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}
# for key in student_scores:
#     if 91 <= student_scores[key] <= 100:
#         student_grades[key] = "Outstanding"
#     elif 81 <= student_scores[key] <= 90:
#         student_grades[key] = "Exceeds Expectations"
#     elif 71 <= student_scores[key] <= 80:
#         student_grades[key] = "Acceptable"
#     elif 0 <= student_scores[key] <= 70:
#         student_grades[key] = "Fail"
#     else:
#         print(f"Something Wrong!!! {key} not found in dictionary.")
        
# for key in student_grades:
#     print(f"{key}: {student_grades[key]}")