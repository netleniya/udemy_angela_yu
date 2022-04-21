from art import logo
import random

print(logo)

card_dict = {'A': 11, '1': 1, '2': 2, '3': 3, '4': 4,
             '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             '10': 10, 'J': 10, 'Q': 10, 'K': 10}


player_cards = list()
dealer_cards = list()


def deal_card(population):
    return random.choice(list(population))


for _ in range(2):
    player_cards.append(deal_card(card_dict))
    dealer_cards.append(deal_card(card_dict))

print("player: ", player_cards)
print("dealer: ", dealer_cards)


player_score = sum([card_dict.get(i) for i in player_cards])
dealer_score = sum([card_dict.get(i) for i in dealer_cards])

print("Player Score", player_score)
print("Dealer Score", dealer_score)


def calculate_score(player, dealer):
    player_score = sum([card_dict.get(i) for i in player])
    dealer_score = sum([card_dict.get(i) for i in dealer])


calculate_score(player=player_cards, dealer=dealer_cards)
