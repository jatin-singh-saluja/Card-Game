# deck.py
from typing import List
from dataclasses import dataclass, field
from card import Card
import random

@dataclass
class Deck:
    cards: List[Card] = field(default_factory=lambda: [Card(i) for i in range(1, 11)] * 4)

    def shuffle(self):
        deck_size = len(self.cards)
        for current_index in range(deck_size - 1, 0, -1):
            random_index = random.randint(0, current_index)
            self.cards[current_index], self.cards[random_index] = self.cards[random_index], self.cards[current_index]
