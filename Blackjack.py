import random

def assign_cards():
    card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(card_deck)
    return card


def calculate(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return '21'

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, comp_score):
    if user_score > 21 and comp_score > 21:
        return "You went over 21! You Lose."

    if user_score == comp_score:
        return "Draw"
    elif comp_score == 21:
        return "Computer has a blackjack! You Lose."
    elif user_score == 21:
        return "Woh! You have a blackjack. You won."
    elif comp_score > 21:
        return "Computer went over. You won"
    elif user_score > 21:
        return "You went over. You Lose."
    elif user_score > comp_score:
        return "You won."
    else:
        return "You Lose"

def play_game():
        user_cards = []
        comp_cards = []
        for i in range(2):
            user_cards.append(assign_cards())
            comp_cards.append(assign_cards())    
            
        user_score = calculate(user_cards)
        print(f"Your first two cards: {user_cards}. Your current score: {user_score}")
        comp_score = calculate(comp_cards)
        print(f"Computer's first card: {comp_cards[0]}")

        game_over = False
        while not game_over:
            if user_score == 21 or comp_score == 21 or int(user_score) > 21:
                game_over = True
            else:
                want_card = input("Type 'y' to get another card, or type 'n' to pass.")
                if want_card == 'y':
                    user_cards.append(assign_cards())
                    print(f"Your cards: {user_cards}")
                    user_score = calculate(user_cards)
                    print(f"Score : {user_score}")
                else:
                    game_over = True
                    
        while comp_score!= 0 and int(comp_score) < 17:
            comp_cards.append(assign_cards())
            comp_score = calculate(comp_cards)

        print(f"   Your final hand: {user_cards}, final score: {user_score}")
        print(f"   Computer's final hand: {comp_cards}, final score: {comp_score}")
        print(compare(user_score, comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  import blackjack_art
  print(blackjack_art.logo)
  play_game()





    




