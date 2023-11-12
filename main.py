import pygame
from pygame import time

import spritesheet
import playersprite as ps
import objectsprite as os
import enemysprite as es

# screen size
SCREEN_WIDTH = 1000  # 500
SCREEN_HEIGHT = 900  # 450

# loading images into pygame
# bg_img = pygame.image.load('pictures/bg.jpg')
# resize the image to fit the screen
# bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))


# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
SALMON = (250, 128, 114)
GREY = (128, 128, 128)


# create a class for the player


# game class
class Game:
    i = 0

    def __init__(self):
        self.font_name = pygame.font.match_font('arial')
        pygame.init()  # initialize pygame
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # create screen
        self.clock = pygame.time.Clock()  # create clock
        self.running = True  # game loop
        self.font = pygame.font.SysFont('comic sans', 16)  # create font
        self.i = 0
        self.bg_img = pygame.image.load('pictures/bg.jpg')
        self.bg_img = pygame.transform.scale(self.bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bg_music = pygame.mixer.music.load('music/bg_musicWelcome.mp3')
        pygame.mixer.music.play(-1)
        player_spritesheet = spritesheet.SpriteSheet('pictures/Morty.png')
        ghost_spritesheet = spritesheet.SpriteSheet('pictures/ghostmorty.png')
        girl_ghost_spritesheet = spritesheet.SpriteSheet('pictures/enemy/ghostgirl.png')
        # morty
        self.player_base_image = player_spritesheet.image_at((27, 703, 79, 113))  # dont forget to remove negative sign
        self.player_base_image.convert_alpha()
        # ghost morty
        self.ghost_base_image = ghost_spritesheet.image_at((27, 703, 79, 113))  # dont forget to remove negative sign
        self.ghost_base_image.convert_alpha()

        # spikes
        self.bigMorty = pygame.image.load('pictures/morty2.jpg')
        # remove black background
        self.player_base_image.set_colorkey((0, 0, 0))
        self.left_images = []  # list of images for left and right movement
        self.player_left_image1 = player_spritesheet.image_at((9, 877, 93, 108))
        self.player_left_image2 = player_spritesheet.image_at((138, 876, 92, 108))
        self.player_left_image3 = player_spritesheet.image_at((267, 877, 93, 108))
        self.player_left_image4 = player_spritesheet.image_at((395, 876, 95, 109))
        self.left_images = [self.player_left_image1, self.player_left_image2,
                            self.player_left_image3, self.player_left_image4]
        # MORTY UP IMAGES
        self.up_images = []
        self.player_right_image1 = player_spritesheet.image_at((28, 1042, 78, 109))
        self.player_right_image2 = player_spritesheet.image_at((157, 1042, 78, 108))
        self.player_right_image3 = player_spritesheet.image_at((286, 1042, 78, 109))
        self.player_right_image4 = player_spritesheet.image_at((415, 1042, 78, 109))
        self.up_images = [self.player_right_image1, self.player_right_image2,
                          self.player_right_image3, self.player_right_image4]

        self.ghost_base_image.set_colorkey((0, 0, 0))
        # MORTY GHOST LEFT IMAGES
        self.ghost_left_images = []  # list of images for left and right movement
        self.ghost_left_image1 = ghost_spritesheet.image_at((9, 877, 93, 108))
        self.ghost_left_image2 = ghost_spritesheet.image_at((138, 876, 92, 108))
        self.ghost_left_image3 = ghost_spritesheet.image_at((267, 877, 93, 108))
        self.ghost_left_image4 = ghost_spritesheet.image_at((395, 876, 95, 109))
        self.ghost_left_images = [self.ghost_left_image1, self.ghost_left_image2,
                                  self.ghost_left_image3, self.ghost_left_image4]

        # MORTY GHOST UP IMAGES
        self.ghost_images = []
        self.ghost_right_image1 = ghost_spritesheet.image_at((28, 1042, 78, 109))
        self.ghost_right_image2 = ghost_spritesheet.image_at((157, 1042, 78, 108))
        self.ghost_right_image3 = ghost_spritesheet.image_at((286, 1042, 78, 109))
        self.ghost_right_image4 = ghost_spritesheet.image_at((415, 1042, 78, 109))
        self.ghost_up_images = [self.ghost_right_image1, self.ghost_right_image2,
                                self.ghost_right_image3, self.ghost_right_image4]


        # Ghost Girl Images
        self.ghostgirl_base_image = girl_ghost_spritesheet.image_at((20, 721, 95, 124))
        self.ghost_facing_screen = girl_ghost_spritesheet.image_at((20, 721, 95, 124))
        self.ghostgirl_left_image1 = girl_ghost_spritesheet.image_at((27, 896, 82, 116))
        self.ghostgirl_left_image2 = girl_ghost_spritesheet.image_at((154, 896, 82, 118))
        self.ghostgirl_left_image3 = girl_ghost_spritesheet.image_at((1281, 896, 82, 116))
        self.ghostgirl_left_image4 = girl_ghost_spritesheet.image_at((407, 896, 83, 117))
        self.ghostgirl_left_images = [self.ghostgirl_left_image1, self.ghostgirl_left_image2, self.ghostgirl_left_image3, self.ghostgirl_left_image4]

        # Ghost girl up images
        self.ghostgirl_up_images = []
        self.ghostgirl_up_image1 = girl_ghost_spritesheet.image_at((21, 1052, 94, 125))
        self.ghostgirl_up_image2 = girl_ghost_spritesheet.image_at((150, 1050, 94, 130))
        self.ghostgirl_up_image3 = girl_ghost_spritesheet.image_at((275, 1052, 94, 125))
        self.ghostgirl_up_image4 = girl_ghost_spritesheet.image_at((400, 1050, 94, 127))
        self.ghostgirl_up_images = [self.ghostgirl_up_image1, self.ghostgirl_up_image2, self.ghostgirl_up_image3, self.ghostgirl_up_image4]



        # create player
        self.player_group = pygame.sprite.Group()
        # TODO: change the player's x and y position to bottom left corner starting position
        self.player = ps.Player(0, SCREEN_HEIGHT, 79, 113, self.screen, self.player_base_image,
                                self.left_images, self.up_images, "player")
        # create a group for the objects
        self.object_group = pygame.sprite.Group()
        # create a ladder object for the player to climb
        self.platform = os.ObjectSprite(self.player_base_image, 200, SCREEN_HEIGHT - 20, "platform")
        # change platform color to brown with a black border
        self.platform.image.fill((139, 69, 19))

        # create more platforms so player can climb to the top keep in mind the player's height is 113 and keep platforms close to each other
        self.platform2 = os.ObjectSprite(self.player_base_image, 300, SCREEN_HEIGHT - 40, "platform")
        # change platform color to brown with a black border
        self.platform2.image.fill((139, 69, 19))
        # create a black border around the platform
        pygame.draw.rect(self.platform2.image, BLACK, self.platform2.rect, 1)
        self.platform3 = os.ObjectSprite(self.player_base_image, 400, SCREEN_HEIGHT - 60, "platform")
        # change platform color to brown with a black border
        self.platform3.image.fill((139, 69, 19))

        self.platform4 = os.ObjectSprite(self.player_base_image, 500, SCREEN_HEIGHT - 80, "platform")
        # change platform color to brown with a black border
        self.platform4.image.fill((139, 69, 19))

        self.platform5 = os.ObjectSprite(self.player_base_image, 600, SCREEN_HEIGHT - 100, "platform")
        # change platform color to brown with a black border
        self.platform5.image.fill((139, 69, 19))

        self.platform6 = os.ObjectSprite(self.player_base_image, 700, SCREEN_HEIGHT - 120, "platform")
        # change platform color to brown with a black border
        self.platform6.image.fill((139, 69, 19))
        # create a ladder to the right of platform 6
        self.ladder = os.ObjectSprite(self.player_base_image, 770, SCREEN_HEIGHT - 100, "ladder")
        # create a levatatingplatform
        self.platform7 = os.ObjectSprite(self.player_base_image, 800, SCREEN_HEIGHT - 140, "levitating platform")
        # change platform color to brown with a black border
        self.platform7.image.fill((139, 69, 19))

        # create a platform at height 300 so play can jump to it
        self.platform8 = os.ObjectSprite(self.player_base_image, 700, SCREEN_HEIGHT - 600, "platform")
        # change platform color to brown with a black border
        self.platform8.image.fill((139, 69, 19))
        # create another platfrom to left of platform 8 so player can jump to it
        self.platform9 = os.ObjectSprite(self.player_base_image, 600, SCREEN_HEIGHT - 600, "platform")
        # change platform color to brown with a black border
        self.platform9.image.fill((139, 69, 19))
        # create another platform to left of platform 9 so player can jump to it
        self.platform10 = os.ObjectSprite(self.player_base_image, 500, SCREEN_HEIGHT - 600, "platform")
        # change platform color to brown with a black border
        self.platform10.image.fill((139, 69, 19))
        # create another platform to left of platform 10 so player can jump to it
        self.platform11 = os.ObjectSprite(self.player_base_image, 400, SCREEN_HEIGHT - 600, "platform")
        # change platform color to brown with a black border
        self.platform11.image.fill((139, 69, 19))

        # create another platform to left of platform 11 so player can jump to it
        self.platform12 = os.ObjectSprite(self.player_base_image, 300, SCREEN_HEIGHT - 600, "platform")
        # change platform color to brown with a black border
        self.platform12.image.fill((139, 69, 19))

        # create another platform to left of platform 12 so player can jump to it
        self.platform13 = os.ObjectSprite(self.player_base_image, 200, SCREEN_HEIGHT - 600, "platform")
        # change platform color to brown with a black border
        self.platform13.image.fill((139, 69, 19))
        # create another platform to left of platform 13 so player can jump to it
        self.platform14 = os.ObjectSprite(self.player_base_image, 100, SCREEN_HEIGHT - 600, "platform")
        # change platform color to brown with a black border
        self.platform14.image.fill((139, 69, 19))
        # create another platform to left of platform 14 so player can jump to it
        self.platform15 = os.ObjectSprite(self.player_base_image, 0, SCREEN_HEIGHT - 600, "platform")
        # change platform color to brown with a black border
        self.platform15.image.fill((139, 69, 19))
        # create another platform to left of platform 15 so player can jump to it
        self.platform16 = os.ObjectSprite(self.player_base_image, -100, SCREEN_HEIGHT - 600, "platform")
        # change platform color to brown with a black border
        self.platform16.image.fill((139, 69, 19))
        pygame.draw.rect(self.platform16.image, BLACK, [0, 0, 200, 20], 2)

        # create a door to the right of the screen
        self.door1 = os.ObjectSprite(self.player_base_image, 0, SCREEN_HEIGHT - 730, "door")
        # change door color to brown with a black border
        self.door1.image.fill((139, 69, 19))
        # create a black border around the door
        pygame.draw.rect(self.door1.image, (0, 0, 0), (0, 0, 79, 113), 5)

        # create a group for the enemies
        self.enemy_group = pygame.sprite.Group()
        # create a ghost enemy
        self.ghost = es.Enemy(500, SCREEN_HEIGHT, 79, 113, self.screen, self.ghost_base_image,
                              self.ghost_left_images, self.ghost_up_images, "ghost")
        self.ghost.player = self.player

        #create a ghostgirl enemy
        self.ghostgirl = es.Enemy(500, SCREEN_HEIGHT, 79, 113, self.screen, self.ghostgirl_base_image, self.ghostgirl_left_images, self.ghostgirl_up_images, "ghostgirl")
        self.ghostgirl.player = self.player



        # add the player to the player group
        self.enemy_group.add(self.ghost)

        self.platforms = [self.platform, self.platform2, self.platform3, self.platform4, self.platform5, self.platform6,
                          self.platform7, self.platform8, self.platform9, self.platform10, self.platform11,
                          self.platform12,
                          self.platform13, self.platform14, self.platform15, self.platform16]

        self.player_group.add(self.player)
        self.object_group.add(self.platform)
        self.object_group.add(self.platform2)
        self.object_group.add(self.platform3)
        self.object_group.add(self.platform4)
        self.object_group.add(self.platform5)
        self.object_group.add(self.platform6)
        self.object_group.add(self.ladder)
        self.object_group.add(self.platform7)
        self.object_group.add(self.platform8)
        self.object_group.add(self.platform9)
        self.object_group.add(self.platform10)
        self.object_group.add(self.platform11)
        self.object_group.add(self.platform12)
        self.object_group.add(self.platform13)
        self.object_group.add(self.platform14)
        self.object_group.add(self.platform15)
        self.object_group.add(self.platform16)

        self.object_group.add(self.door1)

    # create a platform update method to update the platforms to the correct position and color
    def platform_update(self, platform, new_x, new_y, color, levitating_top, levitating_bottom):
        platform.rect.x = new_x  # set the platform's x position
        platform.rect.y = new_y  # set the platform's y position
        platform.image.fill(color)  # change the platform's color
        pygame.draw.rect(platform.image, BLACK, [0, 0, 200, 20], 2) # create a black border around the platform
        if platform.name == "levitating platform":
            platform.levitating_top = levitating_top # set the platform's levitating top position
            platform.levitating_bottom = levitating_bottom # set the platform's levitating bottom position

    # create healthbar method to display the player's health top middle of the screen
    def health_bar(self):
        # Define colors
        HEALTH_COLOR = (255, 0, 0)
        BAR_COLOR = (0, 255, 0)
        TEXT_COLOR = (255, 255, 255)

        # Calculate bar width based on player health
        bar_width = int((self.player.health / self.player.max_health) * 200)

        # Draw the health bar background
        pygame.draw.rect(self.screen, HEALTH_COLOR, [20, 20, 200, 20])

        # Draw the health bar
        pygame.draw.rect(self.screen, BAR_COLOR, [20, 20, bar_width, 20])

        # Add text displaying player health
        health_text = f"{self.player.health}/{self.player.max_health}"
        # font = pygame.font.Font(None, 20)
        # text = font.render(health_text, True, TEXT_COLOR)
        # self.screen.blit(text, (20, 45))

    # create levelplatformchange method to rearrange the platforms for each level based off of the player's map_level
    def level_platform_change(self):
        if self.player.map_level == 2:
            # call the platform update method to update the platforms to the correct position and color
            # self.platform2.image.fill(RED)
            # pygame.draw.rect(self.platform2.image, BLACK, [0, 0, 200, 20], 2)
            #
            # self.platform2.name = "moving platform"
            # call the platform update method to update the platforms to the correct position and color
            self.platform2.name = "moving platform"
            self.platform_update(self.platform2, 0, SCREEN_HEIGHT - 300, BROWN, 0, 0)

            self.platform_update(self.platform3, 600, SCREEN_HEIGHT - 300, BROWN, 0, 0)

            # create a ladder object to left of platform 3
            self.ladder2 = os.ObjectSprite(self.player_base_image, 540, SCREEN_HEIGHT - 300, "ladder")
            self.object_group.add(self.ladder2)
            self.ladder3 = os.ObjectSprite(self.player_base_image, 540, SCREEN_HEIGHT - 200, "ladder")
            self.object_group.add(self.ladder3)
            # create another platform to right of platform 3 so player can jump to it
            # self.platform4.rect.x = 800
            # self.platform4.rect.y = SCREEN_HEIGHT - 300
            # # change color of platform
            # self.platform4.image.fill(BROWN)
            # pygame.draw.rect(self.platform4.image, BLACK, [0, 0, 200, 20], 2)


            # create a platform to the right of platform 3
            self.platform55 = os.ObjectSprite(self.player_base_image, 690, SCREEN_HEIGHT - 300, "platform")
            self.platform55.image.fill(BROWN)
            pygame.draw.rect(self.platform55.image, BLACK, [0, 0, 200, 20], 2)

            # add platform to object group
            self.object_group.add(self.platform55)

            # create a livtating platform to the right of platform 4
            self.platform5.rect.x = 900
            self.platform5.rect.y = SCREEN_HEIGHT - 300
            # change color of platform
            self.platform5.image.fill(BROWN)
            pygame.draw.rect(self.platform5.image, BLACK, [0, 0, 200, 20], 2)
            self.platform5.name = "levitating platform"
            self.platform5.levitating_top_limit = 400
            self.platform5.levitating_bottom_limit = 700

            # create another platform to left of platform 5 so player can jump to it
            self.platform6.rect.x = 700
            self.platform6.rect.y = SCREEN_HEIGHT - 500
            # change color of platform
            self.platform6.image.fill(BROWN)
            pygame.draw.rect(self.platform6.image, BLACK, [0, 0, 200, 20], 2)

            # create another platform to left of platform 6 so player can jump to it
            self.platform7.rect.x = 600
            self.platform7.rect.y = SCREEN_HEIGHT - 500
            self.platform7.name = "platform"
            # change color of platform
            self.platform7.image.fill(BROWN)
            pygame.draw.rect(self.platform7.image, BLACK, [0, 0, 200, 20], 2)

            # create another platform to left of platform 7 so player can jump to it
            self.platform8.rect.x = 500
            self.platform8.rect.y = SCREEN_HEIGHT - 500
            # change color of platform
            self.platform8.image.fill(BROWN)
            pygame.draw.rect(self.platform8.image, BLACK, [0, 0, 200, 20], 2)

            # create another platform to left of platform 8 so player can jump to it
            self.platform9.rect.x = 400
            self.platform9.rect.y = SCREEN_HEIGHT - 500
            # change color of platform
            self.platform9.image.fill(BROWN)
            pygame.draw.rect(self.platform9.image, BLACK, [0, 0, 200, 20], 2)

            # create another platform to left of platform 9 so player can jump to it
            self.platform10.rect.x = 300
            self.platform10.rect.y = SCREEN_HEIGHT - 500
            # change color of platform
            self.platform10.image.fill(BROWN)
            pygame.draw.rect(self.platform10.image, BLACK, [0, 0, 200, 20], 2)

            # create another platform to left of platform 10 so player can jump to it
            self.platform11.rect.x = 200
            self.platform11.rect.y = SCREEN_HEIGHT - 500
            # change color of platform
            self.platform11.image.fill(BROWN)
            pygame.draw.rect(self.platform11.image, BLACK, [0, 0, 200, 20], 2)

            # move ladder to the right of platform 11
            self.ladder.rect.x = 800
            self.ladder.rect.y = SCREEN_HEIGHT - 500

            # create another platform to left of platform 11 so player can jump to it
            self.platform12.rect.x = 100
            self.platform12.rect.y = SCREEN_HEIGHT - 500
            # change color of platform
            self.platform12.image.fill(BROWN)
            pygame.draw.rect(self.platform12.image, BLACK, [0, 0, 200, 20], 2)

            # create another levitating platform to the left of platform 12 so player can jump to it that bottom limit is at platform 12 and goes up 200 pixels
            self.platform13.rect.x = 0
            self.platform13.rect.y = SCREEN_HEIGHT - 500
            # change color of platform
            self.platform13.image.fill(BROWN)
            pygame.draw.rect(self.platform13.image, BLACK, [0, 0, 200, 20], 2)
            self.platform13.name = "levitating platform"
            self.platform13.levitating_top_limit = 200
            self.platform13.levitating_bottom_limit = 500

            # create another platform to the right of platform 13s top limit so player can jump to it
            self.platform14.rect.x = 100
            self.platform14.rect.y = SCREEN_HEIGHT - 700
            # change color of platform
            self.platform14.image.fill(BROWN)
            pygame.draw.rect(self.platform14.image, BLACK, [0, 0, 200, 20], 2)

            # create another platform to the right of platform 14 so player can jump to it
            self.platform15.rect.x = 200
            self.platform15.rect.y = SCREEN_HEIGHT - 700
            # change color of platform
            self.platform15.image.fill(BROWN)
            pygame.draw.rect(self.platform15.image, BLACK, [0, 0, 200, 20], 2)

            # create another platform to the right of platform 15 so player can jump to it
            self.platform16.rect.x = 300
            self.platform16.rect.y = SCREEN_HEIGHT - 700
            # change color of platform
            self.platform16.image.fill(BROWN)
            pygame.draw.rect(self.platform16.image, BLACK, [0, 0, 200, 20], 2)

            # create a door ontop of platform 16
            self.door1.rect.x = 300
            self.door1.rect.y = SCREEN_HEIGHT - 830
            # change color of door
            self.door1.image.fill(BLUE)
            pygame.draw.rect(self.door1.image, BLACK, [0, 0, 200, 20], 2)
            self.door1.name = "door"

        if self.player.map_level == 3:
            # create spikes on the ground
            # create a spike object and add it to the list of objects

            self.spike1 = os.ObjectSprite(self.player_base_image, 100, SCREEN_HEIGHT - 100, "spike")

            # create a platform
            self.platform.rect.x = 0
            self.platform.rect.y = SCREEN_HEIGHT - 50
            # change color of platform
            self.platform.image.fill(BLUE)
            pygame.draw.rect(self.platform.image, BLACK, [0, 0, 200, 20], 2)

            # create another platform to the right of platform 1 so player can jump to it
            self.platform2.rect.x = 100
            self.platform2.rect.y = SCREEN_HEIGHT - 50
            # change color of platform
            self.platform2.image.fill(BLUE)
            pygame.draw.rect(self.platform2.image, BLACK, [0, 0, 200, 20], 2)

            # create another platform to the right of platform 2 so player can jump to it
            self.platform3.rect.x = 200
            self.platform3.rect.y = SCREEN_HEIGHT - 50
            # change color of platform
            self.platform3.image.fill(BLUE)
            pygame.draw.rect(self.platform3.image, BLACK, [0, 0, 200, 20], 2)

            # create another platform to the right of platform 3 so player can jump to it
            self.platform4.rect.x = 300
            self.platform4.rect.y = SCREEN_HEIGHT - 50
            # change color of platform
            self.platform4.image.fill(BLUE)
            pygame.draw.rect(self.platform4.image, BLACK, [0, 0, 200, 20], 2)

            # create another platform to the right of platform 4 so player can jump to it
            self.platform5.rect.x = 400
            self.platform5.rect.y = SCREEN_HEIGHT - 50
            # change color of platform
            self.platform5.image.fill(BLUE)
            pygame.draw.rect(self.platform5.image, BLACK, [0, 0, 200, 20], 2)

            # create another platform to the right of platform 5 so player can jump to it
            self.platform6.rect.x = 500
            self.platform6.rect.y = SCREEN_HEIGHT - 50
            # change color of platform
            self.platform6.image.fill(BLUE)
            pygame.draw.rect(self.platform6.image, BLACK, [0, 0, 200, 20], 2)

            # change color of platform7
            self.platform7.image.fill(BLUE)
            pygame.draw.rect(self.platform7.image, BLACK, [0, 0, 200, 20], 2)

            # change color of platform8
            self.platform8.image.fill(BLUE)
            pygame.draw.rect(self.platform8.image, BLACK, [0, 0, 200, 20], 2)

            # change color of platform9
            self.platform9.image.fill(BLUE)
            pygame.draw.rect(self.platform9.image, BLACK, [0, 0, 200, 20], 2)

            # change color of platform10
            self.platform10.image.fill(BLUE)
            pygame.draw.rect(self.platform10.image, BLACK, [0, 0, 200, 20], 2)

            # change color of platform11
            self.platform11.image.fill(BLUE)
            pygame.draw.rect(self.platform11.image, BLACK, [0, 0, 200, 20], 2)

            # change color of platform12
            self.platform12.image.fill(BLUE)
            pygame.draw.rect(self.platform12.image, BLACK, [0, 0, 200, 20], 2)

            # change color of platform13
            self.platform13.image.fill(BLUE)
            pygame.draw.rect(self.platform13.image, BLACK, [0, 0, 200, 20], 2)

            # change color of platform14
            self.platform14.image.fill(BLUE)
            pygame.draw.rect(self.platform14.image, BLACK, [0, 0, 200, 20], 2)

            # change color of platform15
            self.platform15.image.fill(BLUE)
            pygame.draw.rect(self.platform15.image, BLACK, [0, 0, 200, 20], 2)

            # change color of platform16
            self.platform16.image.fill(BLUE)
            pygame.draw.rect(self.platform16.image, BLACK, [0, 0, 200, 20], 2)
        if self.player.map_level == 4:
            #temporarily remove all platforms
            self.platform.kill()
            self.platform2.kill()
            self.platform3.kill()
            self.platform4.kill()
            self.platform5.kill()
            self.platform6.kill()
            self.platform7.kill()
            self.platform8.kill()
            self.platform9.kill()
            self.platform10.kill()
            self.platform11.kill()
            self.platform12.kill()
            self.platform13.kill()
            self.platform14.kill()
            self.platform15.kill()
            self.platform16.kill()

            #create a levitating platform on the bottom right of the screen
            self.platform.rect.x = 500
            self.platform.rect.y = SCREEN_HEIGHT - 50
            # change color of platform
            self.platform.image.fill(GREY)

            #move the door on top of the levitating platform
            self.door1.rect.x = 500
            self.door1.rect.y = SCREEN_HEIGHT - 100
            #change color of door
            self.door1.image.fill(RED)
            #outline door
            pygame.draw.rect(self.door1.image, BLACK, [0, 0, 200, 20], 2)



            #kill all enemies
            self.ghost.kill()
            #create new enemy boss and add to sprite list
            self.enemy_group.add(self.ghostgirl)




    def change_level(self):
        # change all the platforms to level 1
        if self.player.map_level == 1:
            print("changing level")
            self.bg_music = pygame.mixer.music.load("music/bg_musiclvl1.mp3")
            pygame.mixer.music.play(-1)
        # change all the platforms to level 2
        if self.player.map_level == 2:
            self.next_level_screen()
            self.next_level_screen()
            self.player.map_level = 2
            self.player.rect.x = 0
            self.player.rect.y = SCREEN_HEIGHT
            self.level_platform_change()
            self.bg_img = pygame.image.load("pictures/desertbg.jpg").convert()
            self.bg_img = pygame.transform.scale(self.bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.bg_music = pygame.mixer.music.load("music/bg_musiclvl2.mp3")
            pygame.mixer.music.play(-1)
            self.player.changing_level = False
        elif self.player.map_level == 3:
            self.next_level_screen()
            self.player.map_level = 3
            self.player.rect.x = 0
            self.player.rect.y = SCREEN_HEIGHT
            self.level_platform_change()
            self.bg_img = pygame.image.load("pictures/snowbg.jpg").convert()
            self.bg_img = pygame.transform.scale(self.bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.bg_music = pygame.mixer.music.load("music/bg_musiclvl3.mp3")
            pygame.mixer.music.play(-1)
            self.player.changing_level = False
        elif self.player.map_level == 4:
            self.next_level_screen()
            self.player.map_level = 4
            self.player.rect.x = 0
            self.player.rect.y = SCREEN_HEIGHT
            self.level_platform_change()
            self.bg_img = pygame.image.load("pictures/bosslvlbg.jpg").convert()
            self.bg_img = pygame.transform.scale(self.bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.bg_music = pygame.mixer.music.load("music/bg_musiclvl4.mp3")
            pygame.mixer.music.play(-1)
            self.player.changing_level = False

    # create game over screen function
    def game_over_screen(self):
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER", 48, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text("Press a key to play again", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        pygame.display.flip()
        self.wait_for_key()

    # create a welcome screen function
    def welcome_screen(self):
        self.screen.fill(BLUE)
        self.draw_text("Welcome to the game", 48, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text("Press a key to play", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        # display bigMorty
        self.screen.blit(self.bigMorty, (SCREEN_WIDTH - 300, SCREEN_HEIGHT / 2 - 200))
        # remove background
        self.screen.set_colorkey(BLUE)
        pygame.display.flip()
        self.wait_for_key()

    # create next level screen function
    def next_level_screen(self):
        self.screen.fill(BLACK)
        self.draw_text("Next Level", 48, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text("changing levels...", 22, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        pygame.display.flip()
        # wait for 4 seconds
        pygame.time.wait(4000)

    def run(self):

        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    # Handles events in the game such as key presses and mouse clicks
    def events(self):
        for event in pygame.event.get():  # event loop
            if event.type == pygame.QUIT:  # if user clicks X button
                self.running = False

    # Updates the game state such as player position and enemy position
    # This is where the game logic goes
    def update(self):
        self.player_group.update()
        self.object_group.update()
        self.enemy_group.update()
        self.player.gravity()
        self.player.collisiondetection(self.object_group)
        self.player.collisiondetection(self.enemy_group)

        if self.player.changing_level:
            self.change_level()

        if self.player.health <= 0:
            self.running = False
            self.game_over_screen()

        # self.player.handle_collision(self.object_group)

    def draw(self):
        # set background to background image and draw it
        self.screen.blit(self.bg_img, (0, 0))
        self.player_group.draw(self.screen)  # draw player
        self.object_group.draw(self.screen)  # draw object
        self.enemy_group.draw(self.screen)  # draw enemy
        # display health bar
        self.health_bar()
        pygame.display.flip()  # update a portion of the screen

    # create a function to handle

    def quit(self):
        pygame.quit()

    def draw_text(self, param, param1, WHITE, param2, param3):
        # create a font
        font = pygame.font.Font(self.font_name, param1)
        text_surface = font.render(param, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (param2, param3)
        self.screen.blit(text_surface, text_rect)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False
                    # reset game

                    self.player.map_level = 1
                    self.__init__()
                    self.change_level()


# main

if __name__ == '__main__':
    game = Game()
    game.welcome_screen()
    game.run()
    game.quit()
