# create attack sprite class for playersprite to use
import pygame
from pygame.locals import *
import spritesheet
import random


class Attack(pygame.sprite.Sprite):
    # create a constructor for the attack class that takes in the attack x and y position , and name of the attack
    def __init__(self, x, y, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.cat_attack_spritesheet = spritesheet.SpriteSheet('pictures/mortycatattack.png')
        self.cat_attack_img1 = self.cat_attack_spritesheet.image_at((1, 1, 201, 131))
        self.cat_attack_img2 = self.cat_attack_spritesheet.image_at((222, 2, 204, 150))
        self.cat_attack_img3 = self.cat_attack_spritesheet.image_at((445, 2, 175, 127))
        self.cat_attack_img4 = self.cat_attack_spritesheet.image_at((665, 5, 180, 126))
        self.cat_attack_img5 = self.cat_attack_spritesheet.image_at((887, 2, 200, 132))
        self.cat_attack_img6 = self.cat_attack_spritesheet.image_at((2, 157, 208, 143))
        self.cat_attack_img7 = self.cat_attack_spritesheet.image_at((224, 157, 216, 116))
        self.cat_attack_img8 = self.cat_attack_spritesheet.image_at((444, 156, 209, 130))

        #create a list of all the attack images
        self.cat_attack_images = [self.cat_attack_img1, self.cat_attack_img2, self.cat_attack_img3, self.cat_attack_img4, self.cat_attack_img5, self.cat_attack_img6, self.cat_attack_img7, self.cat_attack_img8]
        self.image = self.cat_attack_images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
        self.direction = "right"
        self.image.set_colorkey((0, 0, 0))
        self.attack_list = []
        self.image_index = 0

    def update(self):
        # if self.direction == "right": then iterate through the list of images and set the image to the next image in the list
        if self.direction == "right":
            self.image = self.cat_attack_images[self.image_index]
            self.image_index += 1
            if self.image_index > len(self.cat_attack_images) - 1:
                self.image_index = 0
            self.image = self.cat_attack_images[self.image_index]

    def attack(self, direction):
        self.direction = direction
        if self.direction == "right":
            self.rect.x += self.speed
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.rect.x > 800:
            self.kill()
        if self.rect.x < 0:
            self.kill()
