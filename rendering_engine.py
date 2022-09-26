from time import sleep
try:
    import pygame
except ImportError:
    print("Pygame is not installed. Please install it and try again. You can install it with pip using the command:\npip install pygame")
    exit()

class RenderingEngine:
    def __init__(self):
        self.set_constants()
        # Open the window
        self.start_window()

    def choose_first_or_second(self):
        # Cut the window in half and draw a line down the middle
        # To represent which goes first
        # the left side will be the first and shown with the text "First"
        # the right side will be the second and shown with the text "Second"
        # The user will click on the side they want to go first
        # The function will return True if the user wants to go first
        self.window.fill((0, 0, 0))
        pygame.draw.line(self.window, (255, 255, 255), (self.WINDOW_WIDTH / 2, 0), (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT), 5)
        pygame.draw.rect(self.window, (255, 255, 255), (0, 0, self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT), 5)
        pygame.draw.rect(self.window, (255, 255, 255), (self.WINDOW_WIDTH / 2, 0, self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT), 5)
        font = pygame.font.SysFont("Arial", 50)
        first_text = font.render("First", True, (255, 255, 255))
        second_text = font.render("Second", True, (255, 255, 255))
        self.window.blit(first_text, (self.WINDOW_WIDTH / 4 - first_text.get_width() / 2, self.WINDOW_HEIGHT / 2 - first_text.get_height() / 2))
        self.window.blit(second_text, (self.WINDOW_WIDTH / 4 * 3 - second_text.get_width() / 2, self.WINDOW_HEIGHT / 2 - second_text.get_height() / 2))
        pygame.display.update()
        while True:
            for input in pygame.event.get():
                if input.type == pygame.MOUSEBUTTONDOWN:
                    if input.pos[0] < self.WINDOW_WIDTH / 2:
                        return True
                    else:
                        return False

    def set_constants(self):
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.WINDOW_TITLE = "Nim"

    def start_window(self):
        # Initialize pygame
        pygame.init()
        # Set the window size
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        # Set the window title
        pygame.display.set_caption(self.WINDOW_TITLE)

    def draw_game(self, row, is_players_turn):
        # We will render some dots on the screen. Row could be multiple and is structured in a 2D list.
        # Each row will be rendered on a separate line
        # Each dot will be rendered as a circle
        

    def draw_final_screen(self, player_won):
        # Clear the screen
        self.window.fill((0, 0, 0))
        if player_won:
            text = "You Won!"
        else:
            text = "You Lost!"
        font = pygame.font.SysFont("Arial", 50)
        text = font.render(text, True, (255, 255, 255))
        self.window.blit(text, (self.WINDOW_WIDTH / 2 - text.get_width() / 2, self.WINDOW_HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
    
    def choose_impossible_mode(self):
        # First clear the screen
        self.window.fill((0, 0, 0))
        # Split the screen in half
        # The left half will be the "Normal mode" button
        # The right half will be the "Impossible mode" button
        # The user can click on either button
        pygame.draw.rect(self.window, (255, 255, 255), (0, 0, self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT), 5)
        pygame.draw.rect(self.window, (255, 255, 255), (self.WINDOW_WIDTH / 2, 0, self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT), 5)
        font = pygame.font.SysFont("Arial", 50)
        text = font.render("Normal Mode", True, (255, 255, 255))
        self.window.blit(text, (self.WINDOW_WIDTH / 4 - text.get_width() / 2, self.WINDOW_HEIGHT / 2 - text.get_height() / 2))
        text = font.render("Impossible Mode", True, (255, 255, 255))
        self.window.blit(text, (self.WINDOW_WIDTH / 4 * 3 - text.get_width() / 2, self.WINDOW_HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
        while True:
            for input in pygame.event.get():
                if input.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif input.type == pygame.MOUSEBUTTONDOWN:
                    if input.pos[0] < self.WINDOW_WIDTH / 2:
                        return False
                    else:
                        return True

    def display_computers_move(self, move):
        # Clear the screen
        self.window.fill((0, 0, 0))
        font = pygame.font.SysFont("Arial", 50)
        text = font.render("Computer chose card " + str(move), True, (255, 255, 255))
        self.window.blit(text, (self.WINDOW_WIDTH / 2 - text.get_width() / 2, self.WINDOW_HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(2000)

    def play_again(self):
        # Clear the screen
        self.window.fill((0, 0, 0))
        font = pygame.font.SysFont("Arial", 50)
        # Create a rectangle on the left hand side of the screen
        pygame.draw.rect(self.window, (255, 255, 255), (0, 0, self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT), 5)
        # Create a rectangle on the right hand side of the screen
        pygame.draw.rect(self.window, (255, 255, 255), (self.WINDOW_WIDTH / 2, 0, self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT), 5)
        # Create text on the left hand side saying "Play Again"
        text = font.render("Play Again", True, (255, 255, 255))
        self.window.blit(text, (self.WINDOW_WIDTH / 4 - text.get_width() / 2, self.WINDOW_HEIGHT / 2 - text.get_height() / 2))
        # Create text on the right hand side saying "Quit"
        text = font.render("Quit", True, (255, 255, 255))
        self.window.blit(text, (self.WINDOW_WIDTH / 4 * 3 - text.get_width() / 2, self.WINDOW_HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
        while True:
            for input in pygame.event.get():
                if input.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif input.type == pygame.MOUSEBUTTONDOWN:
                    if input.pos[0] < self.WINDOW_WIDTH / 2:
                        return True
                    else:
                        return False
    def draw_invalid_move(self):
        # Clear the screen
        self.window.fill((0, 0, 0))
        font = pygame.font.SysFont("Arial", 50)
        text = font.render("Invalid Move", True, (255, 255, 255))
        self.window.blit(text, (self.WINDOW_WIDTH / 2 - text.get_width() / 2, self.WINDOW_HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(2000)