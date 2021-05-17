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
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random
import art

#Variables

deck_of_cards = []

#functions

#create and return a deck of cards
def populate_deck():
    for i in range(4):
        deck_of_cards.append("A")
        deck_of_cards.append("2")
        deck_of_cards.append("3")
        deck_of_cards.append("4")  
        deck_of_cards.append("5")
        deck_of_cards.append("6")
        deck_of_cards.append("7")
        deck_of_cards.append("8")
        deck_of_cards.append("9")
        deck_of_cards.append("10")
        deck_of_cards.append("J")
        deck_of_cards.append("Q")
        deck_of_cards.append("K")
    return deck_of_cards

#shuffles a deck of cards
def shuffle(deck):
    random.shuffle(deck)

#draws a card from a deck, returns to user
def draw(deck):
    card = deck.pop()
    return card


#play a hand
def play_a_hand(deck):
    user_hand = []
    computer_hand = []

    user_hand.append(draw(deck))
    user_hand.append(draw(deck))
    computer_hand.append(draw(deck))
    computer_hand.append(draw(deck))

    #begin the hitting process
    keep_going = True
    while keep_going == True:
        print(f"Your Cards: {user_hand}. Your current total is {calculate_score(user_hand)}")
        print(f"Computer's first card: {computer_hand[0]}")

        hit_me = input("Would you like another card? Y or N ")
        if hit_me == "N":
            keep_going = False
        elif hit_me == "Y":
            user_hand.append(draw(deck))
    
    #Computer's turn
    while calculate_score(computer_hand) <=16:
        computer_hand.append(draw(deck))

    print("The dealer will now stay")
    
    #compare scores
    compare(user_hand, computer_hand)
    

#return total score of hand
def calculate_score(hand):
    score = 0
    for card in hand:
        if card == "A":
            score += 11
        elif card in ["K","Q","J"]:
            score += 10
        else:
            score += int(card)
    return score

def compare(user_hand, dealer_hand):
    user_score = calculate_score(user_hand)
    dealer_score = calculate_score(dealer_hand)

    print(f"Your hand: {user_hand}. Total is {user_score}")
    print(f"Dealer's hand: {dealer_hand}. Total is {dealer_score}")

    if user_score > 21:
        print("You went over 21. You lose.")
    elif user_score > dealer_score:
        print("You win")
    elif dealer_score > user_score:
        print("The dealer wins")
    elif dealer_score == user_score:
        print("It's a draw")

#game loop

print(art.logo)

print("Welcome to Black Jack. Let's play.")

play = True
while play == True:
    my_deck = populate_deck()
    shuffle(my_deck)
    play_a_hand(my_deck)
    keep_going = input("Would you like to play again? Y or N ")
    if keep_going == "N":
        play = False

