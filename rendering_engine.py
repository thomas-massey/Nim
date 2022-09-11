import pygame

class RenderingEngine:
    def __init__(self):
        self.set_constants()
        # Open the window
        self.start_window()

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