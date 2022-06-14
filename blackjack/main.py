from art import logo
import random


def draw_two(player, computer, deck):
    """draw two cards each for the player and dealer. show all player's cards, and only one dealer card
    """
    def deal_card(deck):
        return random.choice(list(deck))

    for _ in range(2):
        player.append(deal_card(deck))
        computer.append(deal_card(deck))


def draw_one_more(deck):
    return random.choice(list(deck))


def calculate_score(player, dealer, deck):
    player_score = sum([deck.get(i) for i in player])
    dealer_score = sum([deck.get(i) for i in dealer])

    return player_score, dealer_score


def main():

    print(logo)

    play_on = True
    while play_on:

        card_dict = {'A': 11, '1': 1, '2': 2, '3': 3, '4': 4,
                     '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                     '10': 10, 'J': 10, 'Q': 10, 'K': 10}

        player_cards = list()
        dealer_cards = list()

        response = input("Welcome to Blackjack. Play? (y/n): ").lower()

        if response.startswith('n'):
            print("Well, piss off then...")
            break
        else:
            draw_two(player_cards, dealer_cards, deck=card_dict)

            print("Your cards: ", player_cards)
            print("Computer's first card: ", [dealer_cards[0]])

            player_score, dealer_score = calculate_score(
                player_cards, dealer_cards, deck=card_dict)

            if player_score == 21 and dealer_score != 21:
                print("You win")
                continue

            if player_score == dealer_score:
                print("It's a tie. That means you lose")
                continue

            if 'A' in player_cards and '10' in player_cards:
                print("Blackjack. You win:", player_cards)
                continue
            elif 'A' in dealer_cards and '10' in dealer_cards:
                print(f"Computer has Blackjack: {dealer_cards}. You lose.")
                continue

            if player_score < 21:
                one_more = input(
                    "Do you want to draw one more card? (y/n): ").lower()

                if one_more.startswith('y'):
                    additional_card = draw_one_more(deck=card_dict)
                    player_cards.append(additional_card)

            if dealer_score < 17:
                dealer_draws = draw_one_more(deck=card_dict)
                dealer_cards.append(dealer_draws)

            player_score, dealer_score = calculate_score(
                player_cards, dealer_cards, deck=card_dict)

            print("Player Cards", player_cards)
            print("Dealer Cards", dealer_cards)

            print("Player Score", player_score)
            print("Dealer Score", dealer_score)

            if player_score < 21 and dealer_score > 21:
                print("You win")
            elif player_score < 21 and (player_score > dealer_score):
                print("You win")
            else:
                print("You lose")


if __name__ == "__main__":
    main()
