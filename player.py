# player.py
from typing import List, Optional
from dataclasses import dataclass, field
from card import Card
import random

@dataclass
class Player:
    name: str
    draw_pile: List[Card] = field(default_factory=list)
    discard_pile: List[Card] = field(default_factory=list)

    def draw_card(self) -> Optional[Card]:
        if not self.draw_pile:
            if not self.discard_pile:
                return None
            # Shuffle discard pile and use it as the new draw pile
            random.shuffle(self.discard_pile)
            self.draw_pile, self.discard_pile = self.discard_pile, []
        return self.draw_pile.pop()

    def discard_cards(self, cards: List[Card]):
        self.discard_pile.extend(cards)
