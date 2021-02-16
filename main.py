############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.

def main():
  from replit import clear
  from art import logo
  print(logo)
  print("******Welcome to the BLACKJACK!!!****")
  print("\n Let's deal the cards: \n")
  import random
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  def deal_card(cards):
    card=random.choice(cards)
    return card

  user_cards = []
  computer_cards = []
  for i in range(2):
    user_cards.append(deal_card(cards))
    computer_cards.append(deal_card(cards))

  print(f"You got: {user_cards}")
  print(f"Dealer got: {computer_cards}")
  def calculate_score(hand):
    score=0
    for i in range(0,len(hand)):
      if hand[i]==11:
        score=score + hand[i]
        if score>21:
          score=score-10;
          hand.remove(11)
          hand.append(1)
      else:
        score+=hand[i]
    if score==21:
      score=0  #blackjack
    return score

   

  user=calculate_score(user_cards)
  comp=calculate_score(computer_cards)

  if user==0:
    decide="n"
    print("You have a blackjack! Let's see what the dealer will get...")
  else:
    decide=input("Would you like to draw next card? y or n?").lower()
  if decide=="y":
    while decide=="y":
      user_cards.append(deal_card(cards))
      user=calculate_score(user_cards)
      print(f"You have: {user_cards} and a score of {user}")
      if user==0:
        print("You have a blackjack! Let's see what the dealer will get...\n")
        decide="n"
      elif user>21:
        print("You have more than 21.")
        decide="n"
        comp=1
      else:
        decide=input("Would you like to draw next card? y or n?").lower()
  else:
    if comp==1:
      print(f"Dealer got {comp}. You lose.")
    else:
      while comp<=17 and comp<user:
        computer_cards.append(deal_card(cards))
        comp=calculate_score(computer_cards)
      print(computer_cards)
    
  print(user_cards)
  print(computer_cards)



  def compare(user, comp):
    if user==comp:
      print(f"It's a draw! You both have {user}")
    elif user==0:
      print("User wins with blackjack.")
    elif comp==0:
      print("Dealer wins with blackjack.")
    elif user>21:
      print("Dealer wins")
    elif comp>21: 
      print("User wins")
    else:
      if user>comp:
        print("User wins")
      else:
        print("Dealer wins")
    
  compare(user,comp)

  # Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

  start_over=input("Do you want to go again? Type y or n.").lower()
  if start_over=="y":
    clear()
    main()
  else:
    exit()

main()