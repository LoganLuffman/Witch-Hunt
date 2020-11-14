import pygame


# Parent class that all other menu will inherit from.
class Menu:

    # Initializing base variables that other classes may use
    def __init__(self, game):
        self.game = game
        self.mid_width = self.game.DISPLAY_WIDTH / 2
        self.mid_height = self.game.DISPLAY_HEIGHT / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -125

    # Creating cursor to signify where player's selector is at
    def draw_cursor(self):
        self.game.draw_text('-->', 25, self.cursor_rect.x, self.cursor_rect.y)

    # Used to update the menu screen when it is changed
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


# Main menu class that first appears to the player
class MainMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game)
        # Variable used to signify which option for the cursor to point to
        self.state = 'Start'

        # Positional variables
        self.start_x, self.start_y = self.mid_width, self.mid_height + 100
        self.scores_x, self.scores_y = self.mid_width, self.mid_height + 150
        self.settings_x, self.settings_y = self.mid_width, self.mid_height + 200
        self.exit_x, self.exit_y = self.mid_width, self.mid_height + 250
        self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)

    def display_menu(self):

        # Signifies that a display menu is running
        # Set to false during gameplay
        self.run_display = True

        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)

            # Text that will be displayed in the Main Menu
            self.game.draw_text('Witch Hunt', 72, self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2 - 100)
            self.game.draw_text('Start Game', 40, self.start_x, self.start_y)
            self.game.draw_text('High Scores', 40, self.scores_x, self.scores_y)
            self.game.draw_text('Settings', 40, self.settings_x, self.settings_y)
            self.game.draw_text('Exit', 40, self.exit_x, self.exit_y)

            # Putting the cursor on the screen and displaying the text on the Main Menu
            self.draw_cursor()
            self.blit_screen()

    # Logic to move cursor when an arrow key is pressed
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.scores_x + self.offset, self.scores_y)
                self.state = 'Scores'
            elif self.state == 'Scores':
                self.cursor_rect.midtop = (self.settings_x + self.offset, self.settings_y)
                self.state = 'Settings'
            elif self.state == 'Settings':
                self.cursor_rect.midtop = (self.exit_x + self.offset, self.exit_y)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exit_x + self.offset, self.exit_y)
                self.state = 'Exit'
            elif self.state == 'Scores':
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = 'Start'
            elif self.state == 'Settings':
                self.cursor_rect.midtop = (self.scores_x + self.offset, self.scores_y)
                self.state = 'Scores'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.settings_x + self.offset, self.settings_y)
                self.state = 'Settings'

    # Logic to see if a menu is item is selected and
    # what to do what an option is selected
    def check_input(self):
        self.move_cursor()

        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Scores':
                pass
            elif self.state == 'Settings':
                self.game.current_menu = self.game.settings
            elif self.state == 'Exit':
                quit()

            self.run_display = False


# Settings menu class for when the Settings option is selected by the player
class SettingsMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game)

        # State variable to signify what option is selected
        self.state = 'Volume'

        # Positional variables
        self.vol_x, self.vol_y = self.mid_width, self.mid_height + 50
        self.controls_x, self.controls_y = self.mid_width, self.mid_height + 100
        self.cursor_rect.midtop = (self.vol_x + self.offset, self.vol_y)

    def display_menu(self):

        # Signifies that a display menu is running
        # Set to false during gameplay
        self.run_display = True

        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))

            # Text that will be displayed
            self.game.draw_text('Settings', 72, self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2 - 100)
            self.game.draw_text('Volume', 40, self.vol_x, self.vol_y)
            self.game.draw_text('Controls', 40, self.controls_x, self.controls_y)

            # Putting the cursor on the screen and displaying the text on the Main Menu
            self.draw_cursor()
            self.blit_screen()

    # Logic to see if a menu is item is selected and
    # what to do what an option is selected
    def check_input(self):
        if self.game.BACK_KEY:
            self.game.current_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controls_x + self.offset, self.controls_y)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.vol_x + self. offset, self.vol_y)
        elif self.game.START_KEY:
            # TODO: Create a Volume Menu and a Controls Menu
            pass
