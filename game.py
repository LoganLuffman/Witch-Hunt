import pygame
from menu import *


class Game:

    def __init__(self):
        pygame.init()

        # Window display size
        self.DISPLAY_WIDTH = 1366
        self.DISPLAY_HEIGHT = 768
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

        # Variable used to signify App is running but game hasn't started yet.
        self.running = True

        # Variable used to signify when Start button is selected in menu and game loop is good to execute
        self.playing = False

        # Variables used to signify when keys are pressed
        self.UP_KEY = pygame.K_UP
        self.DOWN_KEY = pygame.K_DOWN
        self.LEFT_KEY = pygame.K_LEFT
        self.RIGHT_KEY = pygame.K_RIGHT
        self.START_KEY = pygame.K_RETURN
        self.BACK_KEY = pygame.K_BACKSPACE
        self.ATTACK_KEY = pygame.K_SPACE
        self.MOUSECLICK_KEY = pygame.MOUSEBUTTONDOWN

        self.UP = False
        self.DOWN = False
        self.LEFT = False
        self.RIGHT = False
        self.START = False
        self.BACK = False
        self.ATTACK = False
        self.MOUSECLICK = False

        # Create surface and window where the player will be able to see the menu / game
        self.display = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.window = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))

        # Specifying text to use. Can be changed by uploading text files to project folder and assigning it.
        self.font_name = pygame.font.get_default_font()

        # Creating menu objects
        self.main_menu = MainMenu(self)
        self.settings = SettingsMenu(self)
        self.volume = VolumeMenu(self)
        self.controls = ControlsMenu(self)

        self.current_menu = self.main_menu

    # Game loop for when the start button on the menu is pressed.
    def game_loop(self):
        while self.playing:
            self.check_events()

            # Used to go back to previous screen. This can be deleted once gameplay is implemented
            if self.BACK:
                self.playing = False

            # Setting the background color and drawing placeholder text on the screen.
            # Can be modified once gameplay is implemented
            self.display.fill(self.BLACK)
            self.draw_text('GAME START', 60, self.DISPLAY_WIDTH / 2, self.DISPLAY_HEIGHT / 2)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()

            self.reset_keys()

    # Function used to check what events the play may be doing
    # May have to be modified when gameplay is introduced
    def check_events(self):
        for event in pygame.event.get():
            # Event to terminate the game
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.current_menu.run_display = False

            # Checks if certain keys are press
            elif event.type == pygame.KEYDOWN:
                if event.key == self.START_KEY:
                    self.START = True
                elif event.key == self.BACK_KEY:
                    self.BACK = True
                if event.key == self.DOWN_KEY:
                    self.DOWN = True
                if event.key == self.UP_KEY:
                    self.UP = True
                if event.key == self.LEFT_KEY:
                    self.LEFT = True
                if event.key == self.RIGHT_KEY:
                    self.RIGHT = True
                if event.key == self.ATTACK_KEY:
                    self.ATTACK = True

            elif event.type == self.MOUSECLICK_KEY:
                self.MOUSECLICK = True
            # TODO: Make window resizable and have text on screen dynamically change with window size
            # elif event.type == pygame.VIDEORESIZE:
            #     self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = event.size
            #     self.display = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
            #     self.window = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT), pygame.RESIZABLE)

    # Function used to reset the keys
    def reset_keys(self):
        self.UP = False
        self.DOWN = False
        self.LEFT = False
        self.RIGHT = False
        self.START = False
        self.BACK = False
        self.ATTACK = False
        self.MOUSECLICK = False

    # Function used to draw text on the screen
    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
