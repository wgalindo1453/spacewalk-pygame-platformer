import math
import random

import pygame
import spritesheet


# create a class for the player
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, screen, image, left_images_list, up_images_list, name):
        pygame.sprite.Sprite.__init__(self)
        self.starting_x = x
        self.move_range = 100
        self.direction = None
        self.image = image
        self.base_image = image
        self.name = name
        self.rect = self.image.get_rect()
        # remove black background
        self.image.set_colorkey((0, 0, 0))
        self.screenwidth = screen.get_width()
        self.screenheight = screen.get_height()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.screen = screen
        self.left_images = left_images_list
        self.up_images = up_images_list
        self.image_index = 0
        self.jump = False  # boolean to check if the player is jumping
        self.jump_level = 10  # how high the player can jump
        # self.bg_music = pygame.mixer.music.load('music/bg_music.mp3')
        self.map_level = 1  # the level of the map the player is on
        self.changing_level = False  # boolean to check if the player is changing levels
        self.player = None



        # pygame.mixer.music.play(-1)

        # create update function that allows the player to move

    # create a function that takes a list of images and flips them
    def flip_images(self, image_list):
        flipped_images = []  # create a list to hold the flipped images
        for image in image_list:  # loop through the list of images
            flipped_image = pygame.transform.flip(image, True, False)
            flipped_images.append(flipped_image)
            self.image.set_colorkey((0, 0, 0))
        return flipped_images

    # create a gravity function

    def gravity(self):
        if self.rect.y < self.screenheight - self.rect.height: # if the player is not on the ground
            self.rect.y += 3  # add 1 to the y position of the player to simulate gravity



    def check_above_platform(self, object_rect):
        if self.rect.bottom > object_rect.top: # if the player is below the platform and the player is above the platform rect.bottom has to be greater than the top of the platform to mean that the player is above the platform
            self.rect.bottom = object_rect.top
            print("object top: " + str(object_rect.top))
            print("object bottom: " + str(object_rect.bottom))
            print("rect.bottom > object_rect.top: " + str(self.rect.bottom > object_rect.top))


    def check_below_platform(self, object_rect):
        if self.rect.top < object_rect.bottom and self.rect.top > object_rect.top and self.rect.right > object_rect.left and self.rect.left < object_rect.right:
            self.rect.top = object_rect.bottom


    def check_left_of_platform(self, object_rect):
        if self.rect.right > object_rect.left and self.rect.right < object_rect.right and self.rect.bottom > object_rect.top and self.rect.top < object_rect.bottom:
            #if the player jumps on the platform from the left side, move player to top left corner of platform
            # if self.rect.bottom < object_rect.top:
            #     self.rect.bottom = object_rect.top
            # else:
            self.rect.right = object_rect.left
            print("object top: " + str(object_rect.top))


    def check_right_of_platform(self, object_rect):
        if self.rect.left < object_rect.right and self.rect.left > object_rect.left and self.rect.bottom > object_rect.top and self.rect.top < object_rect.bottom:
            self.rect.left = object_rect.right


    def collisiondetection(self, object_group):
        for object in object_group:
            if self.rect.colliderect(object.rect):
                if object.name == "platform" or object.name == "levitating platform" or object.name == "moving platform":
                    if self.check_above_platform(object.rect):
                        return
                    elif self.check_below_platform(object.rect):
                        return
                    elif self.check_left_of_platform(object.rect):
                        return
                    elif self.check_right_of_platform(object.rect):
                        return
                elif object.name == "spike":
                    print("Collision detected with spike")
                    #change object shape to triangle


                elif object.name == "coin":
                    print("Collision detected with coin")
                    object_group.remove(object)
                    print("Coin removed")
                elif object.name == "door":
                    print("Collision detected with door")
                    #if player is inside the door, move to next level
                    if self.rect.x > object.rect.x and self.rect.x < object.rect.x + object.rect.width and self.rect.y > object.rect.y and self.rect.y < object.rect.y + object.rect.height:
                        print("Player inside door")
                        self.map_level += 1
                        self.changing_level = True
                        print("map level: " + str(self.map_level))



    # def handle_collision(self, object_group):
    #     """
    #     Handle collisions between the player and objects in the object group.
    #     """
    #     for collision_object in object_group:
    #         if self.rect.colliderect(collision_object.rect):
    #             if collision_object.name == "platform":
    #                 self.resolve_platform_collision(collision_object)

    # def resolve_platform_collision(self, platform):




    def update(self):
        # make enemy move towards player if they are close enough
        player_pos = (self.player.rect.x, self.player.rect.y)
        enemy_pos = (self.rect.x, self.rect.y)
        if abs(player_pos[0] - enemy_pos[0]) < 100 and abs(player_pos[1] - enemy_pos[1]) < 100:
            self.move_towards_player(player_pos, enemy_pos)
        else:
            
            self.image.set_colorkey((0, 0, 0))
            #else move randomly
            self.move_randomly()

        if self.direction == "right":
            self.rect.x += self.speed
            self.image.set_colorkey((0, 0, 0))
            flipped_images = self.flip_images(self.left_images)
            self.image.set_colorkey((0, 0, 0))
            self.image_index = self.image_index + 1
            if self.image_index > 3:
                self.image_index = 0
            self.image = flipped_images[self.image_index]
            self.image.set_colorkey((0, 0, 0))

        # if the left key is pressed move the player left
        if self.direction == "left":


             # print the image index
            self.rect.x -= self.speed  # move the player left
            self.image_index = self.image_index + 1
            if self.image_index > 3:  # if the image is the last image in the list
                self.image_index = 0  # set the image index to 0
                # increment the image index
            self.image = self.left_images[self.image_index]  # set the image to the image at the image index
            self.image.set_colorkey((0, 0, 0))





        # apply gravity
        self.gravity()


        # check if player is changing levels
        if self.changing_level:
            self.rect.x = 100
            self.rect.y = 100
            self.changing_level = False

        #make enemy move towards player if they are close enough

        #if not make enmy move randomly back and forth



        # if player collides with a platform do not let them fall through

        # if the player goes off the screen, move them back on
        if self.rect.right > self.screenwidth:  # if the player goes off the right side of the screen
            self.rect.right = self.screenwidth  # move them back on
            self.direction = "left"
        if self.rect.left < 0:  # if the player goes off the left side of the screen
            self.rect.left = 0  # move them back on
            self.direction = "right"
        if self.rect.top < 0:  # if the player goes off the top of the screen
            self.rect.top = 0  # move them back on
        if self.rect.bottom > self.screenheight:  # if the player goes off the bottom of the screen
            self.rect.bottom = self.screenheight


    def move_towards_player(self, player_pos, enemy_pos):
        if player_pos[0] > enemy_pos[0]:
            self.direction = "right"
            #update starting x
            self.starting_x = self.rect.x
        elif player_pos[0] < enemy_pos[0]:
            self.direction = "left"
            #update starting x
            self.starting_x = self.rect.x

    def move_randomly(self):
        #move the player left and right inside moverange distance
        if self.rect.x > self.starting_x + self.move_range:
            #if enemy hits left side of screen change direction
            if self.rect.x < 0:
                self.direction = "right"
            self.direction = "left"

        elif self.rect.x < self.starting_x - self.move_range:
            #if enemy hits right side of screen change direction
            if self.rect.x > self.screenwidth:
                self.direction = "left"
            self.direction = "right"








