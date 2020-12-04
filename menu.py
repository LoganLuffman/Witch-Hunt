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
        if self.game.DOWN:
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
        elif self.game.UP:
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

        if self.game.START:
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
        if self.game.BACK:
            self.game.current_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP or self.game.DOWN:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controls_x + self.offset, self.controls_y)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.vol_x + self. offset, self.vol_y)
        elif self.game.START:
            if self.state == 'Volume':
                self.game.current_menu = self.game.volume
                self.run_display = False
            elif self.state == 'Controls':
                self.game.current_menu = self.game.controls
                self.run_display = False


class VolumeMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game)

        self.label_x = self.mid_width / 2
        self.vol_x, self.vol_y = self.label_x, self.mid_height - 200

    def display_menu(self):

        self.run_display = True

        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))

            self.game.draw_text('Main Volume', 60, self.vol_x, self.vol_y)

            self.blit_screen()

    def check_input(self):
        if self.game.BACK:
            self.game.current_menu = self.game.settings
            self.run_display = False


class ControlsMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game)

        # Labels for the controls of the game
        self.label_x = self.mid_width / 2
        self.UP_x, self.UP_y = self.label_x, self.mid_height - 200
        self.DOWN_x, self.DOWN_y = self.label_x, self.mid_height - 100
        self.LEFT_x, self.LEFT_y = self.label_x, self.mid_height
        self.RIGHT_x, self.RIGHT_y = self.label_x, self.mid_height + 100
        self.ATTACK_x, self.ATTACK_y = self.label_x, self.mid_height + 200

        # Button sizes
        self.button_length = 150
        self.button_width = 50

        # Button rect locations to change the default controls
        self.UP_offset_x, self.UP_offset_y = self.UP_x + 600, self.UP_y - 20
        self.DOWN_offset_x, self.DOWN_offset_y = self.DOWN_x + 600, self.DOWN_y - 20
        self.LEFT_offset_x, self.LEFT_offset_y = self.LEFT_x + 600, self.LEFT_y - 20
        self.RIGHT_offset_x, self.RIGHT_offset_y = self.RIGHT_x + 600, self.RIGHT_y - 20
        self.ATTACK_offset_x, self.ATTACK_offset_y = self.ATTACK_x + 600, self.ATTACK_y - 20

    def display_menu(self):

        self.run_display = True

        while self.run_display:
            self.game.display.fill((0, 0, 0))

            self.draw_button('UP', self.UP_x, self.UP_y)
            self.draw_button('DOWN', self.DOWN_x, self.DOWN_y)
            self.draw_button('LEFT', self.LEFT_x, self.LEFT_y)
            self.draw_button('RIGHT', self.RIGHT_x, self.RIGHT_y)
            self.draw_button('ATTACK', self.ATTACK_x, self.ATTACK_y)

            self.game.draw_text('Up', 60, self.UP_x, self.UP_y)
            self.game.draw_text('Down', 60, self.DOWN_x, self.DOWN_y)
            self.game.draw_text('Left', 60, self.LEFT_x, self.LEFT_y)
            self.game.draw_text('Right', 60, self.RIGHT_x, self.RIGHT_y)
            self.game.draw_text('Attack', 60, self.ATTACK_x, self.ATTACK_y)

            self.game.check_events()
            self.check_input()
            self.blit_screen()

    def check_input(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.game.BACK:
            self.game.current_menu = self.game.settings
            self.run_display = False

        # Checking to make sure the the mouse is being clicked within the Button rect
        # Print statements used for testing
        if self.game.MOUSECLICK:
            if (self.UP_offset_x <= mouse_pos[0] <= self.UP_offset_x + self.button_length and
                    self.UP_offset_y <= mouse_pos[1] <= self.UP_offset_y + self.button_width):
                print('UP')
            elif (self.DOWN_offset_x <= mouse_pos[0] <= self.DOWN_offset_x + self.button_length and
                  self.DOWN_offset_y <= mouse_pos[1] <= self.DOWN_offset_y + self.button_width):
                print('DOWN')
            elif (self.LEFT_offset_x <= mouse_pos[0] <= self.LEFT_offset_x + self.button_length and
                  self.LEFT_offset_y <= mouse_pos[1] <= self.LEFT_offset_y + self.button_width):
                print('LEFT')
            elif (self.RIGHT_offset_x <= mouse_pos[0] <= self.RIGHT_offset_x + self.button_length and
                  self.RIGHT_offset_y <= mouse_pos[1] <= self.RIGHT_offset_y + self.button_width):
                print('RIGHT')
            elif (self.ATTACK_offset_x <= mouse_pos[0] <= self.ATTACK_offset_x + self.button_length and
                  self.ATTACK_offset_y <= mouse_pos[1] <= self.ATTACK_offset_y + self.button_width):
                print('ATTACK')

    def draw_button(self, key, x, y):
        color_dark, color_light = (100, 100, 100), (170, 170, 170)
        button_offset_x, button_offset_y = x + 600, y - 20
        text_offset_x, text_offset_y = x + 675, y + 7

        mouse_pos = pygame.mouse.get_pos()

        # Hover effect for if the mouse is over the button rect or not
        if (button_offset_x <= mouse_pos[0] <= button_offset_x + self.button_length and
                button_offset_y <= mouse_pos[1] <= button_offset_y + self.button_width):
            pygame.draw.rect(self.game.display, color_light, [button_offset_x, button_offset_y, self.button_length, self.button_width])
        else:
            pygame.draw.rect(self.game.display, color_dark, [button_offset_x, button_offset_y, self.button_length, self.button_width])

        # Pulls keybindings currently assigned to the controls and displays the text information
        if key == 'UP':
            key_name = pygame.key.name(self.game.UP_KEY)
            self.game.draw_text(key_name.capitalize(), 40, text_offset_x, text_offset_y)
        elif key == 'DOWN':
            key_name = pygame.key.name(self.game.DOWN_KEY)
            self.game.draw_text(key_name.capitalize(), 40, text_offset_x, text_offset_y)
        elif key == 'LEFT':
            key_name = pygame.key.name(self.game.LEFT_KEY)
            self.game.draw_text(key_name.capitalize(), 40, text_offset_x, text_offset_y)
        elif key == 'RIGHT':
            key_name = pygame.key.name(self.game.RIGHT_KEY)
            self.game.draw_text(key_name.capitalize(), 40, text_offset_x, text_offset_y)
        elif key == 'ATTACK':
            key_name = pygame.key.name(self.game.ATTACK_KEY)
            self.game.draw_text(key_name.capitalize(), 40, text_offset_x, text_offset_y)
