############### Blackjack Project #####################
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,comp_score):
    if user_score > 21 and comp_score > 21:
        return "You Lose"
    if user_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "you lose"
    elif user_score == 0:
        return "You Win"
    elif user_score > comp_score:
        return "You Win"
    elif comp_score > 21 :
        return "You Win"
    elif user_score > 21 :
        return "You Lose"
    else:
        return "You Lose"
    
def play_game():
    user = []
    comp = []
    is_game_over = False

    for _ in range(2):
        user.append(deal_card())
        comp.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user)
        comp_score = calculate_score(comp)
        print (f"Your cards: {user}, current score : {user_score}")
        print (f"Comp first card: {comp[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Type 'y' to get another card or 'n' to pass : " )
            if user_choice == "y":
                user.append(deal_card())
            else : 
                is_game_over = True
    while comp_score != 0  and comp_score < 17:
        comp.append(deal_card())
        comp_score = calculate_score(comp)

    print(f"Your final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {comp}, final score: {comp_score}")
    print(compare(user_score,comp_score))
while input("Do you want to play a game of Blackjack?? Type 'y' or 'n': ") == "y":
    play_game()
