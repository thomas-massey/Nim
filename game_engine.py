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
        # Let the user chose wether to play first or second
        self.go_first = self.render_engine.choose_first_or_second()
        # Start the game
        self.render_engine.start_game(self.go_first)
        self.game_active = True
        # Start the game loop
        while self.game_active:
            # Update the display
            self.render_engine.update_display()
            # Check for events
            self.move = self.render_engine.listen_for_events()
            # Check if the move is valid
