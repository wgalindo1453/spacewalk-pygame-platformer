import pygame
import spritesheet


# create a class for the player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, screen, image, left_images_list, up_images_list, type):
        pygame.sprite.Sprite.__init__(self)
        self.max_health = 100
        self.health = 100
        self.image = image
        self.base_image = image
        self.type = type
        self.rect = self.image.get_rect()
        # remove black background
        self.image.set_colorkey((0, 0, 0))
        self.screenwidth = screen.get_width()
        self.screenheight = screen.get_height()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.screen = screen
        self.left_images = left_images_list
        self.up_images = up_images_list
        self.image_index = 0
        self.jump = False  # boolean to check if the player is jumping
        self.jump_level = 10  # how high the player can jump
        # self.bg_music = pygame.mixer.music.load('music/bg_music.mp3')
        self.map_level = 1  # the level of the map the player is on
        self.changing_level = False  # boolean to check if the player is changing levels

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
        if self.rect.y < self.screenheight - self.rect.height:  # if the player is not on the ground
            self.rect.y += 3  # add 1 to the y position of the player to simulate gravity

    def check_above_platform(self, object_rect):
        if self.rect.bottom > object_rect.top:
            # check to make sure player is not comming from bottom
            if self.rect.bottom < object_rect.bottom:
                self.rect.bottom = object_rect.top
                print("object top: " + str(object_rect.top))
                print("object bottom: " + str(object_rect.bottom))
                print("player bottom:" + str(self.rect.bottom))

    def check_below_platform(self, object_rect):
        if object_rect.bottom > self.rect.top > object_rect.top and self.rect.right > object_rect.left and self.rect.left < object_rect.right:
            self.rect.top = object_rect.bottom

    def check_left_of_platform(self, object_rect):
        if self.rect.right > object_rect.left and self.rect.right < object_rect.right and self.rect.bottom > object_rect.top and self.rect.top < object_rect.bottom:
            # if the player jumps on the platform from the left side, move player to top left corner of platform
            # if self.rect.bottom < object_rect.top:
            #     self.rect.bottom = object_rect.top
            # else:
            self.rect.right = object_rect.left
            print("object top left: " + str(object_rect.top))

    def check_right_of_platform(self, object_rect):
        if self.rect.left < object_rect.right and self.rect.left > object_rect.left and self.rect.bottom > object_rect.top and self.rect.top < object_rect.bottom:
            self.rect.left = object_rect.right

    def collisiondetection(self, object_group):
        keys = pygame.key.get_pressed()
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
                    # change object shape to triangle


                elif object.name == "coin":
                    print("Collision detected with coin")
                    object_group.remove(object)
                    print("Coin removed")
                elif object.name == "door":
                    print("Collision detected with door")
                    # if player is inside the door, move to next level
                    if self.rect.x > object.rect.x and self.rect.x < object.rect.x + object.rect.width and self.rect.y > object.rect.y and self.rect.y < object.rect.y + object.rect.height:
                        print("Player inside door")
                        self.map_level += 1
                        self.changing_level = True
                        print("map level: " + str(self.map_level))
                elif object.name == "ghost":
                    self.health -= 0.1
                    # make player move back a few pixels
                    self.rect.x -= 10
                    if self.check_above_platform(object.rect):
                        return
                    elif self.check_below_platform(object.rect):
                        return
                    elif self.check_left_of_platform(object.rect):
                        return
                    elif self.check_right_of_platform(object.rect):
                        return
                elif object.name == "ghostgirl":
                    self.health -= 1.0
                    #make the screen flash red
                    self.screen.fill((255, 0, 0))
                    pygame.display.flip()
                    pygame.time.wait(100)
                    self.screen.fill((0, 0, 0))
                    pygame.display.flip()
                    # make the player jump up and back a few pixels
                    self.rect.y -= 10
                    self.rect.x -= 10
                    if self.check_above_platform(object.rect):
                        return
                    elif self.check_below_platform(object.rect):
                        return
                    elif self.check_left_of_platform(object.rect):
                        return
                    elif self.check_right_of_platform(object.rect):
                        return


            # if object is a ladder allow player to climb up and down
                elif object.name == "ladder":
                # check if player presses up arrow key
                    if keys[pygame.K_UP]:
                        self.rect.y -= 5
                    if keys[pygame.K_DOWN]:
                        self.rect.y += 5

            # make player move back a few pixels

            # make player lose health

    # def handle_collision(self, object_group):
    #     """
    #     Handle collisions between the player and objects in the object group.
    #     """
    #     for collision_object in object_group:
    #         if self.rect.colliderect(collision_object.rect):
    #             if collision_object.name == "platform":
    #                 self.resolve_platform_collision(collision_object)

    # def resolve_platform_collision(self, platform):

    # create a health bar for the player that decreases when the player collides with a spike

    def update(self):

        self.image.set_colorkey((0, 0, 0))
        # get the keys pressed
        keys = pygame.key.get_pressed()
        # if the right key is pressed move the player right
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.image.set_colorkey((0, 0, 0))
            flipped_images = self.flip_images(self.left_images)
            self.image.set_colorkey((0, 0, 0))
            self.image_index = self.image_index + 1
            if self.image_index > 3:
                self.image_index = 0
            self.image = flipped_images[self.image_index]

        # if the left key is pressed move the player left
        if keys[pygame.K_LEFT]:

            # print the image index
            self.rect.x -= self.speed  # move the player left
            self.image_index = self.image_index + 1
            if self.image_index > 3:  # if the image is the last image in the list
                self.image_index = 0  # set the image index to 0
                # increment the image index
            self.image = self.left_images[self.image_index]  # set the image to the image at the image index

        # if the up key is pressed move the player up

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.image = self.up_images[0]
        # if the down key is pressed move the player down
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.image = self.base_image

        if self.jump == False:  # if the player is not jumping
            if keys[pygame.K_SPACE]:  # if the space bar is pressed
                self.jump = True  # set the jump boolean to true
        else:  # if the player is jumping
            if self.jump_level >= -10:  # if the jump level is greater than or equal to -10
                self.rect.y -= (self.jump_level * abs(self.jump_level)) * 0.5  # move the player up or down
                self.jump_level -= 2  # decrement the jump level


            else:
                self.jump = False  # set the jump boolean to false
                self.jump_level = 10  # set the jump level to 10

        # if player collides with a platform do not let them fall through

        # if the player goes off the screen, move them back on
        if self.rect.right > self.screenwidth:  # if the player goes off the right side of the screen
            self.rect.right = self.screenwidth  # move them back on
        if self.rect.left < 0:  # if the player goes off the left side of the screen
            self.rect.left = 0  # move them back on
        if self.rect.top < 0:  # if the player goes off the top of the screen
            self.rect.top = 0  # move them back on
        if self.rect.bottom > self.screenheight:  # if the player goes off the bottom of the screen
            self.rect.bottom = self.screenheight
