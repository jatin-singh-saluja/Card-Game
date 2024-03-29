# main.py
from player import Player
from game import Game

if __name__ == "__main__":
    player1 = Player(name="Player 1")
    player2 = Player(name="Player 2")
    game = Game(players=[player1, player2])

    # Shuffle the deck
    game.deck.shuffle()

    # Distribute cards to players
    for player in game.players:
        player.draw_pile.extend(game.distribute_cards(20))

    # Play the game
    game.play_game()
