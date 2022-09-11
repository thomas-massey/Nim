import random
from re import T
from time import sleep
import rendering_engine

class GameEngine:
    def __init__(self):
        # State the render engine
        self.render_engine = rendering_engine.RenderingEngine()
        # Initialize the game
        self.start_game()

    def start_game(self):
        # Start the window
        self.render_engine.start_window()
        self.restart_game_loop = True
        while self.restart_game_loop:
            number_of_cards_left = 21
            # Let the user chose wether to play first or second
            self.go_first = self.render_engine.choose_first_or_second()
            if self.go_first:
                self.is_players_turn = True
            else:
                self.is_players_turn = False
            # Ask if they want impossible mode
            self.impossible_mode = self.render_engine.choose_impossible_mode()
            # Start the game
            self.game_active = True
            self.restart_game_loop = False
            # Start the game loop
            while self.game_active:
                # Draw the game
                # So draw a card in the middle of the screen
                self.render_engine.draw_game(number_of_cards_left, self.is_players_turn)
                if self.is_players_turn:
                    # Check for events
                    self.move_not_valid = True
                    while self.move_not_valid:
                        self.move = self.render_engine.listen_for_events()
                        if self.move > number_of_cards_left:
                            # Invalid move
                            self.render_engine.draw_invalid_move()
                            sleep(1)
                            self.render_engine.draw_game(number_of_cards_left, self.is_players_turn)
                            self.move = self.render_engine.listen_for_events()
                        else:
                            self.move_not_valid = False
                    number_of_cards_left -= self.move
                    self.render_engine.draw_game(number_of_cards_left, self.is_players_turn)
                    sleep(1)
                    self.is_players_turn = False
                else:
                    if self.impossible_mode:
                        if number_of_cards_left % 4 == 0:
                            # Try to make the number of cards left a multiple of 4
                            self.move = random.randint(1, 3)
                        else:
                            # If the number of cards left is not a multiple of 4, then make it one
                            self.move = number_of_cards_left % 4
                        self.render_engine.draw_game(number_of_cards_left, self.is_players_turn)
                        sleep(1)
                        self.is_players_turn = True
                    else:
                        # Pick a random number of cards to take that is possible with the number of cards left
                        if number_of_cards_left > 3:
                            self.move = random.randint(1, 3)
                        else:
                            self.move = random.randint(1, number_of_cards_left)
                    self.render_engine.display_computers_move(self.move)
                    self.is_players_turn = True
                    number_of_cards_left -= self.move
                # Check if the game is over
                if number_of_cards_left <= 0:
                    if self.is_players_turn:
                        self.player_won = False
                    else:
                        self.player_won = True
                    self.game_active = False
                    self.render_engine.draw_final_screen(self.player_won)
                    sleep(2)
                    # Maybe add play again option?
                    if self.render_engine.play_again():
                        self.restart_game_loop = True