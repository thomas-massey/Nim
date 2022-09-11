from time import sleep
import pygame

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
        self.move_not_detected = True
        while self.move_not_detected:
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

    def draw_game(self, number_of_cards_left):
        # Draw the game
        # So draw a card in the middle of the screen
        self.window.fill((0, 0, 0))
        pygame.draw.rect(self.window, (255, 255, 255), (self.WINDOW_WIDTH / 2 - 100, self.WINDOW_HEIGHT / 2 - 200, 200, 200), 5)
        # Then draw the number of cards in the middle on the middle card
        font = pygame.font.SysFont("Arial", 50)
        text = font.render(str(number_of_cards_left), True, (255, 255, 255))
        self.window.blit(text, (self.WINDOW_WIDTH / 2 - text.get_width() / 2, self.WINDOW_HEIGHT / 2 - text.get_height() / 2 - 100))
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
        pygame.display.update()
        sleep(5)