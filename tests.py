import pytest
from deck import Deck
from player import Player
from card import Card
from game import Game

@pytest.fixture
def deck():
    return Deck()

def test_new_deck_contains_40_cards(deck):
    assert len(deck.cards) == 40, "A new deck should contain 40 cards"

@pytest.fixture
def shuffled_deck(deck):
    original_deck = deck.cards.copy()
    deck.shuffle()
    return deck, original_deck

def test_shuffle_deck(shuffled_deck):
    deck, original_deck = shuffled_deck
    original_cards = [card.number for card in original_deck]
    shuffled_cards = [card.number for card in deck.cards]
    assert original_cards != shuffled_cards, "Shuffle function should shuffle the deck"

@pytest.fixture
def player_with_empty_draw_pile():
    player = Player(name="TestPlayer")
    player.discard_pile = [Card(number=1), Card(number=2), Card(number=3)]
    return player

def test_draw_card_with_empty_draw_pile(player_with_empty_draw_pile):
    player = player_with_empty_draw_pile
    original_discard_pile = player.discard_pile.copy()

    # Attempt to draw a card with an empty draw pile
    drawn_card = player.draw_card()

    assert drawn_card is not None, "Drawn card should not be None"
    assert drawn_card.number in [card.number for card in original_discard_pile], "Drawn card should be from the discard pile"
    assert len(player.draw_pile) == 2, "Discard pile is moved into draw pile"
    assert len(player.discard_pile) == 0, "Discard pile is now empty"
    assert player.discard_pile != original_discard_pile, "Shuffling should change the order of the discard pile"

def test_compare_cards_higher_card_wins():
    card1 = Card(number=5)
    card2 = Card(number=8)

    game = Game(players=[Player(name="Player 1"), Player(name="Player 2")])
    winner_index = game.compare_cards([card1, card2])

    assert winner_index == 1  # Player 2 should win as card2 has a higher value

def test_current_round_winner_wins_4_cards_after_tie():
    player1 = Player(name="Player 1")
    player2 = Player(name="Player 2")
    player1.draw_pile = [Card(number=1)]
    player2.draw_pile = [Card(number=1)] 

    game = Game(players=[player1, player2])
    game.play_turn()

    player1.draw_pile = [Card(number=5)]
    player2.draw_pile = [Card(number=1)]
    game.play_turn()

    assert len(player1.discard_pile) == 4, "Player 1 has 4 cards after the tie"
    