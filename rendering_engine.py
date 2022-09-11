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

    def draw_game(self, number_of_cards_left, is_players_turn):
        # Draw the game
        # So draw a card in the middle of the screen
        self.window.fill((0, 0, 0))
        pygame.draw.rect(self.window, (255, 255, 255), (self.WINDOW_WIDTH / 2 - 100, self.WINDOW_HEIGHT / 2 - 200, 200, 200), 5)
        # Then draw the number of cards in the middle on the middle card
        font = pygame.font.SysFont("Arial", 35)
        text = font.render(str(number_of_cards_left) + "              Cards Remaining", True, (255, 255, 255)) # <--- This is a hack to make the text centered
        self.window.blit(text, (self.WINDOW_WIDTH / 2 - 10, self.WINDOW_HEIGHT / 2 - text.get_height() / 2 - 100))
        # Now draw three cards on the bottom of the screen
        # It should look like this:
        # 
        #           __
        #          |21| 
        #           --
        #
        #      __   __   __
        #     | 1| | 2| | 3|
        #      --   --   --
        # Display 1 in the first card to the left
        pygame.draw.rect(self.window, (255, 255, 255), (self.WINDOW_WIDTH / 2 - 300, self.WINDOW_HEIGHT / 2 + 50, 200, 200), 5)
        text = font.render("1", True, (255, 255, 255))
        self.window.blit(text, (self.WINDOW_WIDTH / 2 - 300 + 100 - text.get_width() / 2, self.WINDOW_HEIGHT / 2 + 50 + 100 - text.get_height() / 2))
        # Display 2 in the second card
        pygame.draw.rect(self.window, (255, 255, 255), (self.WINDOW_WIDTH / 2 - 100, self.WINDOW_HEIGHT / 2 + 50, 200, 200), 5)
        text = font.render("2", True, (255, 255, 255))
        self.window.blit(text, (self.WINDOW_WIDTH / 2 - 100 + 100 - text.get_width() / 2, self.WINDOW_HEIGHT / 2 + 50 + 100 - text.get_height() / 2))
        # Display 3 in the third card
        pygame.draw.rect(self.window, (255, 255, 255), (self.WINDOW_WIDTH / 2 + 100, self.WINDOW_HEIGHT / 2 + 50, 200, 200), 5)
        text = font.render("3", True, (255, 255, 255))
        self.window.blit(text, (self.WINDOW_WIDTH / 2 + 100 + 100 - text.get_width() / 2, self.WINDOW_HEIGHT / 2 + 50 + 100 - text.get_height() / 2))
        # Now display the text "Your Turn" or "Computer's Turn"
        # depending on who's turn it is
        if is_players_turn:
            text = font.render("Your Turn", True, (255, 255, 255))
        else:
            text = font.render("Computer's Turn", True, (255, 255, 255))
        # Display the text at the top of the screen
        self.window.blit(text, (self.WINDOW_WIDTH / 2 - text.get_width() / 2, 0))
        # Draw text on the right hand side saying "Be the last to take a card!"
        text = font.render("Be the last to take a card!", True, (255, 255, 255))
        self.window.blit(text, (self.WINDOW_WIDTH - text.get_width(), self.WINDOW_HEIGHT - text.get_height()))
        pygame.display.update()
    
    def listen_for_events(self):
        # Listen for events
        # If the user clicks the X in the top right corner
        # then close the window
        while True:
            for input in pygame.event.get():
                if input.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif input.type == pygame.MOUSEBUTTONDOWN:
                    # Check where the user clicked
                    # If they clicked on the first card
                    if input.pos[0] > self.WINDOW_WIDTH / 2 - 300 and input.pos[0] < self.WINDOW_WIDTH / 2 - 100 and input.pos[1] > self.WINDOW_HEIGHT / 2 + 50 and input.pos[1] < self.WINDOW_HEIGHT / 2 + 250:
                        return 1
                    # If they clicked on the second card
                    elif input.pos[0] > self.WINDOW_WIDTH / 2 - 100 and input.pos[0] < self.WINDOW_WIDTH / 2 + 100 and input.pos[1] > self.WINDOW_HEIGHT / 2 + 50 and input.pos[1] < self.WINDOW_HEIGHT / 2 + 250:
                        return 2
                    # If they clicked on the third card
                    elif input.pos[0] > self.WINDOW_WIDTH / 2 + 100 and input.pos[0] < self.WINDOW_WIDTH / 2 + 300 and input.pos[1] > self.WINDOW_HEIGHT / 2 + 50 and input.pos[1] < self.WINDOW_HEIGHT / 2 + 250:
                        return 3

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