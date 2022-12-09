import pygame
import sys
from pygame.locals import *
import time
import sound_effects as se

# Help from Matthew McClelland on creating the game objects and bouncing the ball off the block
# Help from Hava Szarafinski on creating buttons and placing them on the screen
# Help from Peter Lee on creating messages
# Help form Juan Ortiz Perez on the logistics of the game and loss conditions


class Brickbreaker:

    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.font.get_fonts()
        # Screen and Screen settings
        self.screen_dimensions = (0, 0)
        self.screen_color = (75, 30, 215)
        self.screen = pygame.display.set_mode(self.screen_dimensions, pygame.FULLSCREEN)
        pygame.display.set_caption('Nicks Bricks')
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.screen_original_height = 0
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height),
                                              HWSURFACE | DOUBLEBUF | RESIZABLE)
        pic = pygame.image.load("images/space.png")
        self.screen.blit(pygame.transform.scale(pic, (self.screen_width, self.screen_height)), (0, 0))
        pygame.display.flip()

        # Paddle Settings
        self.movingblock_color = (215, 30, 75)
        self.movingblock_width = 300
        self.movingblock_height = 20
        self.movingblock_speed = 2.5

        # Create Paddle
        self.movingblock = pygame.Rect(255, 255, self.movingblock_width, self.movingblock_height)
        self.screen.blit(self.screen, self.movingblock)

        # Ball settings
        self.ball_color = (150, 150, 150)
        self.ball_radius = 15
        self.ball_width = 15
        self.ball_speed_x = 1
        self.ball_speed_y = 1
        self.original_ball_speed_x = 1
        self.original_ball_speed_y = 1

        # Ball Position
        self.ball_y = self.screen_height/2
        self.ball_x = self.screen_width/2
        self.ball_pos = (self.ball_x, self.ball_y)

        # Background Brick settings
        self.aliens = pygame.sprite.Group()

        # moving block position
        self.movingblock.x = self.screen_width/2 - self.movingblock_width/2
        self.movingblock.y = 0

        # brick settings
        self.brick_width = 300
        self.brick_height = 20
        self.brick_color = (0, 155, 0)
        self.brick_size = self.brick_width, self.brick_height
        self.bricks = pygame.sprite.Group()

        # Start game screen
        self.start_screen = pygame.display.set_mode(self.screen_dimensions, pygame.FULLSCREEN)
        self.start_screen_color = (100, 100, 100)
        self.start_screen_rect = self.start_screen.get_rect()

        # creating the button to start the game
        self.play_button_width = 300
        self.play_button_height = 100
        self.play_button_text_color = (255, 255, 255)
        self.play_button_color = (0, 0, 0)
        self.font = pygame.font.SysFont("arial", 36)
        self.play_button_rect = pygame.Rect(0, 0, self.play_button_width, self.play_button_height)
        self.play_button_rect.center = (self.screen_width/2, self.screen_height/1.33)
        self.play_button_text = "Play"
        self.play_button_message = self.font.render(self.play_button_text, True, self.play_button_text_color,
                                                    self.play_button_color)
        self.play_button_message_rect = self.play_button_message.get_rect()
        self.play_button_message_rect.center = self.play_button_rect.center

        # Creating the quit button
        self.quit_button_width = 100
        self.quit_button_height = 50
        self.quit_button_text_color = (255, 255, 255)
        self.quit_button_color = (0, 0, 0)
        self.font_2 = pygame.font.SysFont("tahoma", 28)
        self.quit_button_rect = pygame.Rect(0, 0, self.quit_button_width, self.quit_button_height)
        self.quit_button_rect.center = (self.screen_width / 2, self.screen_height - (1.5 * self.quit_button_height))
        self.quit_button_text = "Quit"
        self.quit_button_message = self.font_2.render(self.quit_button_text, True, self.quit_button_text_color,
                                                    self.quit_button_color)
        self.quit_button_message_rect = self.quit_button_message.get_rect()
        self.quit_button_message_rect.center = self.quit_button_rect.center

        # Restart message
        # Help from Hava on how to create buttons and place them on the screen
        self.message_button_color = (0, 0, 0)
        self.message_button_text_color = (255, 255, 255)
        self.message_button_width = 700
        self.message_button_height = 150
        self.message_button_rect = pygame.Rect(self.screen_width/2 - (1/2) * self.message_button_width,
                                               self.screen_height/2 - self.message_button_height,
                                               self.message_button_width, self.message_button_height)
        self.message_button_rect_center = (self.screen_width / 2, self.screen_height / 2)
        self.message_button_text_1 = "Game will restart in 3 seconds"
        self.message_button_text_2 = "Game will restart in 2 seconds"
        self.message_button_text_3 = "Game will restart in 1 second"
        self.loss_button_text = "You Lose, Good Try!"
        # Message button 1
        self.message_button_message_1 = self.font.render(self.message_button_text_1, True,
                                                         self.message_button_text_color,
                                                       self.message_button_color)
        self.message_button_message_1_rect = self.message_button_message_1.get_rect()
        self.message_button_message_1_rect.center = self.message_button_rect.center

        # Message button 2
        self.message_button_message_2 = self.font.render(self.message_button_text_2, True,
                                                         self.message_button_text_color,
                                                       self.message_button_color)
        self.message_button_message_2_rect = self.message_button_message_2.get_rect()
        self.message_button_message_2_rect.center = self.message_button_rect.center

        # Message button 3
        self.message_button_message_3 = self.font.render(self.message_button_text_3, True,
                                                         self.message_button_text_color,
                                                       self.message_button_color)
        self.message_button_message_3_rect = self.message_button_message_3.get_rect()
        self.message_button_message_3_rect.center = self.message_button_rect.center

        # You Lose text box
        self.loss_button_rect = pygame.Rect(self.screen_width/2 - (1/2) * self.message_button_width,
                                               self.screen_height/2 - self.message_button_height,
                                               self.message_button_width, self.message_button_height)
        self.loss_button_rect_center = (self.screen_width / 2, self.screen_height / 2)
        self.loss_button_message = self.font.render(self.loss_button_text, True,
                                                         self.message_button_text_color,
                                                         self.message_button_color)
        self.loss_button_message_rect = self.loss_button_message.get_rect()
        self.loss_button_message_rect.center = self.loss_button_rect.center

        # Instructions box
        self.Instruction_button_color = (100, 100, 100)
        self.Instruction_button_text_color = (0, 0, 0)
        self.Instruction_button_width = 700
        self.Instruction_button_height = 300
        self.Instruction_button_rect = pygame.Rect(self.screen_width / 2 - (1 / 2) * self.message_button_width,
                                               self.screen_height / 4,
                                               self.Instruction_button_width, self.Instruction_button_height)
        self.Instruction_button_rect_center = (self.screen_width / 2, self.screen_height / 2.5)
        self.Instruction_button_text = "Use the Left and Right arrow keys to move. " \
                                       "Don't let the ball touch the bottom. Press esc to quit!"
        self.Instruction_button_message = self.font.render(self.Instruction_button_text, True,
                                                         self.Instruction_button_text_color,
                                                         self.Instruction_button_color)
        self.Instruction_button_message_rect = self.Instruction_button_message.get_rect()
        self.Instruction_button_message_rect.center = self.Instruction_button_rect.center

        # Determine if the paddle is moving
        self.movingblock_right = False
        self.movingblock_left = False

        # Determine if the paddle is at the edge of the screen
        self.movingblock_edge = False

        # Determine if the paddle has been hit
        self.movingblock_hit = False

        # Determine if the paddle is at the edge of the screen
        self.movingblock_boundary = False

        # Determine if the background bricks have been hit
        self.brick_hit = False

        # Determines if the player loses
        self.movingblock_loss = False

        # Determines if the play buttons have been clicked
        self.play_button_clicked = False
        self.quit_button_clicked = False

        # puts the start screen up to start the game and Determines if the game is running
        self.start_screen_type = True

        # self.restart_screen_type = False
        self.game_start = False

        # timer runs to start the game a few seconds after you press play
        self.timer_count = True

        # Plays background Music
        se.background_sound.play()

        # Setting to help increase the difficulty after the paddle has been hit a certain amount of times
        self.number_times_hit = 0

    def run_game(self):

        while True:
            # if you are on the start screen, display buttons, message, and check events
            if not self.game_start and self.start_screen_type == True:
                self.display_start_screen()
                self._check_events()
                pygame.display.flip()

            # runs the game and reset conditions
            if self.game_start:
                self._check_events()
                self.draw_blocks()
                self.move_paddle()
                self.move_ball()
                self.check_boundaries()
                self.check_ball_edge()
                self.bounce_ball_off_bricks()
                self.check_brick_collision()
                self.how_to_lose_game()
                self.initialize_variables()
                pygame.mouse.set_visible(False)
                self.timer()

    def _check_events(self):
        # Checks events that happen like mouse click or key pushes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button_clicked(mouse_pos)
                self.check_quit_button_clicked(mouse_pos)

    def _check_keydown_events(self, event):
        # responds to keypresses
        if event.key == pygame.K_RIGHT:
            self.movingblock_right = True
        if event.key == pygame.K_LEFT:
            self.movingblock_left = True
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        # Responds to key releases
        if event.key == pygame.K_RIGHT:
            self.movingblock_right = False
        if event.key == pygame.K_LEFT:
            self.movingblock_left = False

    def timer(self):
        # Creates a timer before the game starts
        if self.timer_count:
            time.sleep(2)
            self.timer_count = False

    def draw_blocks(self):
        # Creates the game objects
        self.screen.fill(self.screen_color)
        self.move_ball()
        pygame.draw.rect(self.screen, self.movingblock_color, self.movingblock)
        pygame.draw.circle(self.screen, self.ball_color, self.ball_pos, self.ball_radius, self.ball_width)
        pygame.display.flip()

    def move_paddle(self):
        # Moves the paddle that the human controls
        if self.movingblock_right:
            self.movingblock.x += 3 * self.movingblock_speed
        if self.movingblock_left:
            self.movingblock.x += -3 * self.movingblock_speed
        self.draw_blocks()

    def move_ball(self):
        # moves the ball at a set speed
        self.ball_x = self.ball_x + self.ball_speed_x
        self.ball_y = self.ball_y + self.ball_speed_y
        self.ball_pos = [self.ball_x, self.ball_y]

    def check_boundaries(self):
        # If the paddle is at the edge of the screen, it wont go any further
        if self.movingblock.x >= self.screen_width - self.movingblock_width:
            self.movingblock_boundary = True
            self.movingblock.x = self.screen_width - self.movingblock_width
        if self.movingblock.x <= -1:
            self.movingblock_boundary = True
            self.movingblock.x = 0

    # Help from Matt on how to bounce the ball off of certain object including the walls and the paddle
    def check_ball_edge(self):
        # If the ball hits the edge of the screen, it bounces off
        if self.ball_x >= self.screen_width:
            self.ball_speed_x = self.ball_speed_x * -1
        if self.ball_x <= 0:
            self.ball_speed_x = self.ball_speed_x * -1
        if self.ball_y <= self.screen_original_height:
            self.ball_speed_y = self.ball_speed_y * -1
        if self.ball_y <= self.screen_height:
            self.ball_speed_y = self.ball_speed_y * -1

    def check_brick_collision(self):
        # If the ball hits the paddle, it bounces off depending on where the paddle and ball are.
        if self.ball_x >= self.movingblock.x and self.ball_x <= self.movingblock.x + self.movingblock_width:
            if self.ball_y == self.movingblock.y + self.movingblock_height:
                self.movingblock_hit = True
            if self.movingblock_hit:
                se.ball_sound.play()
                self.number_times_hit += 1
                self.increase_difficulty()
                self.bounce_ball_off_bricks()

    def bounce_ball_off_bricks(self):
        # Continuation of bouncing the ball off the paddle
        self.ball_speed_y = self.ball_speed_y * -1
        self.movingblock_hit = False

    def how_to_lose_game(self):
        # Creates a losing condition if the ball hits the bottom of the screen,
        # displays a loss message, and resets game objects to a starting position
        if self.ball_y > self.screen_height:
            self.movingblock_loss = True
            self.display_loss_button()
            time.sleep(3)
            self.display_message_button_1()
            time.sleep(1)
            self.display_message_button_2()
            time.sleep(1)
            self.display_message_button_3()
            time.sleep(1)
            self.reset_ball()
            self.reset_movingblock()
            self.number_times_hit = 0
            self.game_start = True

    def initialize_variables(self):
        # Set the paddle to its starting y position and once the play button is clicked, take away the main menu screen
        self.movingblock.y = self.screen_height - 80
        self.start_screen_type = False

    def display_message_button_1(self):
        # displays the first message
        self.screen.fill(self.message_button_color, self.message_button_rect)
        self.screen.blit(self.message_button_message_1, self.message_button_message_1_rect)
        pygame.display.flip()

    def display_message_button_2(self):
        # displays the second message
        self.screen.fill(self.message_button_color, self.message_button_rect)
        self.screen.blit(self.message_button_message_2, self.message_button_message_2_rect)
        pygame.display.flip()

    def display_message_button_3(self):
        # displays the third message
        self.screen.fill(self.message_button_color, self.message_button_rect)
        self.screen.blit(self.message_button_message_3, self.message_button_message_3_rect)
        pygame.display.flip()

    def display_loss_button(self):
        # displays the 'you lose' button for a few seconds before restarting the game
        self.screen.fill(self.message_button_color, self.message_button_rect)
        self.screen.blit(self.loss_button_message, self.loss_button_message_rect)
        pygame.display.flip()

    def display_quit_button(self):
        # displays a constant quit button in case someone wants to exit the system
        self.screen.fill(self.quit_button_color, self.quit_button_rect)
        self.screen.blit(self.quit_button_message, self.quit_button_message_rect)
        # pygame.display.flip()

    def display_instructions(self):
        # displays the instructions on the main menu
        self.screen.fill(self.Instruction_button_color, self.Instruction_button_rect)
        self.screen.blit(self.Instruction_button_message, self.Instruction_button_message_rect)
        # pygame.display.flip()

    def display_start_screen(self):
        # displays the start screen, play button, and instructions
        self.start_screen.fill(self.start_screen_color)
        self.display_play_button()
        self.display_instructions()
        self.display_quit_button()
        # pygame.display.flip()

    def display_play_button(self):
        # Creates the play button
        self.start_screen.fill(self.play_button_color, self.play_button_rect)
        self.start_screen.blit(self.play_button_message, self.play_button_message_rect)

    def check_play_button_clicked(self, mouse_pos):
        # if the play button is clicked, run through the events and start the game
        self.play_button_clicked = self.play_button_rect.collidepoint(mouse_pos)
        if self.play_button_clicked and self.game_start == False and self.start_screen_type == True:
            self.initialize_variables()
            self.play_button_clicked = True
            self.game_start = True

    def check_quit_button_clicked(self, mouse_pos):
        # if the quit button is clicked, exit the system
        self.quit_button_clicked = self.quit_button_rect.collidepoint(mouse_pos)
        if self.quit_button_clicked:
            sys.exit()

    def reset_ball(self):
        # resets the ball to its starting position
        self.ball_y = self.screen_height / 2
        self.ball_x = self.screen_width / 2
        self.ball_pos = (self.ball_x, self.ball_y)

    def reset_movingblock(self):
        # resets the paddle to its starting position
        self.movingblock.x = self.screen_width / 2 - self.movingblock_width / 2
        self.movingblock.y = self.screen_height - 80

    def increase_difficulty(self):
        # increases the difficulty of the game by increasing the speed after the paddle is hit a certain number of times
        if self.number_times_hit >= 3:
            self.ball_speed_x = self.original_ball_speed_x * 1.5
            self.ball_speed_y = self.original_ball_speed_y * 1.5
        if self.number_times_hit >= 6:
            self.ball_speed_x = self.original_ball_speed_x * 2
            self.ball_speed_y = self.original_ball_speed_y * 2
        if self.number_times_hit >= 10:
            self.ball_speed_x = self.original_ball_speed_x * 2.5
            self.ball_speed_y = self.original_ball_speed_y * 2.5
        if self.number_times_hit >= 15:
            self.ball_speed_x = self.original_ball_speed_x * 3
            self.ball_speed_y = self.original_ball_speed_y * 3


# Creates an instance of the game and runs it
game = Brickbreaker()
game.run_game()
