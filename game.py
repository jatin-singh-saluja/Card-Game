# game.py
from typing import List, Optional
from dataclasses import dataclass, field
from card import Card
from deck import Deck
from player import Player

@dataclass
class Game:
    players: List[Player]
    deck: Deck = field(default_factory=Deck)
    drawn_tied_cards: List[Card] = field(default_factory=list)  # to store tied cards
    is_last_round_tied: bool = False

    def distribute_cards(self, num_cards: int):
        return [self.deck.cards.pop() for _ in range(num_cards)]

    def play_turn(self):
        drawn_cards = [player.draw_card() for player in self.players]

        for i, player in enumerate(self.players):
            if drawn_cards[i] is not None:
                print(f"{player.name} ({len(player.draw_pile) + len(player.discard_pile) +1} cards): {drawn_cards[i].number}")

        winner_index = self.compare_cards(drawn_cards)

        if winner_index is not None:
            if self.is_last_round_tied:
                print(f"{self.players[winner_index].name} wins this round!\n")
                self.players[winner_index].discard_cards(drawn_cards + self.drawn_tied_cards)
                self.drawn_tied_cards = []  # Reset the drawn tied cards
            else:
                print(f"{self.players[winner_index].name} wins this round!\n")
                self.players[winner_index].discard_cards(drawn_cards)

        # Update is_last_round_tied based on the current round
        self.is_last_round_tied = bool(self.drawn_tied_cards)

    def compare_cards(self, drawn_cards: List[Card]) -> Optional[int]:
        max_card_value = max(card.number for card in drawn_cards if card is not None)
        winners = [i for i, card in enumerate(drawn_cards) if card is not None and card.number == max_card_value]

        if len(winners) == 1:
            return winners[0]
        elif len(winners) > 1:
            print("No winner in this round.\n")
            self.drawn_tied_cards.extend(drawn_cards)  # Accumulate tied cards
            return None
        else:
            return None

    def play_game(self):
        print("Starting the game!\n")

        while all(player.draw_pile or player.discard_pile for player in self.players):
            self.play_turn()

        winner = max(self.players, key=lambda player: len(player.discard_pile))
        print(f"\n{winner.name} wins the game!")

if __name__ == "__main__":
    player1 = Player(name="Player 1")
    player2 = Player(name="Player 2")
    game = Game(players=[player1, player2])

    game.deck.shuffle()

    for player in game.players:
        player.draw_pile.extend(game.distribute_cards(20))

    while all(player.draw_pile or player.discard_pile for player in game.players):
        game.play_turn()
