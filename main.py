import random
from replit import clear
from art import logo

def get_a_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    generated_card = random.choice(cards)
    return generated_card

def sum_of_cards(cards_list):
    if sum(cards_list) == 21 and len(cards_list) == 2:
        result = 0
        return result
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)
        return sum(cards_list)
    else:
        return sum(cards_list)
    
def check_who_win(human_score, pc_score, human_cards, pc_cards):
    if human_score == 0 and len(human_cards) == 2:
        print("Win with a Blackjack 😎")
    elif pc_score == 0 and len(pc_cards) == 2:
        print("Lose, opponent has Blackjack!")
    else:
        if human_score > 21 and pc_score <= 21:
            print("You went over. You lose 😭")
        elif pc_score > 21 and human_score <= 21:
            print("You opponent went over. You Win 😃")
        elif pc_score > 21 and human_score > 21:
            print("You both went over. Nobody wins 😃")
        elif pc_score == human_score:
            print("Draw!")
        elif human_score > pc_score:
            print("You win 😃")
        elif human_score < pc_score:
            print("You lose 😭")

def print_current_score(human_cards, human_score, pc_cards):
    print(f"\tYour cards: {human_cards}, current score: {human_score}")
    print(f"\tComputer's first card: {pc_cards[0]}")

def play_blackjack():
  play_game = True 
  while play_game:
      want_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
      if want_play == 'y':
          clear()
          print(logo)
          human_cards, pc_cards = [], []
          
          for i in range(2):
              human_cards.append(get_a_card())
              pc_cards.append(get_a_card())
          
          human_score = sum_of_cards(human_cards)
          pc_score = sum_of_cards(pc_cards)
          print_current_score(human_cards, human_score, pc_cards)

          if not human_score == 0 and not pc_score == 0: 
              draw_a_card = True
              while draw_a_card:
                  human_choice = input("Type 'y' to get another card, type 'n' to pass: ")
                  if sum_of_cards(pc_cards) < 17:  
                          pc_cards.append(get_a_card())
                  if human_choice == 'y':
                      human_cards.append(get_a_card())
                      print_current_score(human_cards, sum_of_cards(human_cards), pc_cards)
                      if sum_of_cards(human_cards) > 21:
                          break
                  else:
                      break

          # final check()
          pc_score = sum_of_cards(pc_cards)
          print(f"\tYour final hand: {human_cards}, final_score: {sum_of_cards(human_cards)}")
          print(f"\tComputer's final hand: {pc_cards}, final_score: {sum_of_cards(pc_cards)}")
          check_who_win(sum_of_cards(human_cards), sum_of_cards(pc_cards), human_cards, pc_cards)
      else:
          play_game = False

play_blackjack()