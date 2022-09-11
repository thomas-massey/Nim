import random
from time import sleep
import rendering_engine

class GameEngine:
    def __init__(self):
        # State the render engine
        self.render_engine = rendering_engine.RenderingEngine()
        # Initialize the game
        self.start_game()

    def start_game(self):
        number_of_cards_left = 21
        # Start the window
        self.render_engine.start_window()
        # Let the user chose wether to play first or second
        self.go_first = self.render_engine.choose_first_or_second()
        if self.go_first:
            self.is_players_turn = True
        else:
            self.is_players_turn = False
        # Start the game
        self.game_active = True
        # Start the game loop
        while self.game_active:
            # Draw the game
            # So draw a card in the middle of the screen
            self.render_engine.draw_game(number_of_cards_left, self.is_players_turn)
            if self.is_players_turn:
                # Check for events
                self.move = self.render_engine.listen_for_events()
                self.is_players_turn = False
            else:
                if self.impossible_mode:
                    pass
                    self.is_players_turn = True
                else:
                    # Pick a random number of cards to take that is possible with the number of cards left
                    if number_of_cards_left > 3:
                        self.move = random.randint(1, 3)
                    else:
                        self.move = random.randint(1, number_of_cards_left)
                    self.is_players_turn = True
            # Check if the game is over
            number_of_cards_left -= self.move
            if number_of_cards_left <= 0:
                if self.is_players_turn:
                    self.player_won = False
                else:
                    self.player_won = True
                self.game_active = False
                self.render_engine.draw_final_screen(self.player_won)