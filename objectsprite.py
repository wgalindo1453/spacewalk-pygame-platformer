import pygame

import spritesheet

BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class ObjectSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, NAME):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((100, 50))
        # change color of the surface
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = NAME
        self.direction = 1
        self.levitating_bottom_limit = 800
        self.levitating_top_limit = 300
        self.moving_bottom_limit = 800
        self.moving_top_limit = 300
        self.spike_sprite_sheet = spritesheet.SpriteSheet('pictures/spike.png')
        self.spike = self.spike_sprite_sheet.image_at((194, 10, 46, 138))
        self.ladder_img = pygame.image.load('pictures/ladder.png')

    def update(self):
        # if self.name == "platform":
        # if the platform is a levatating platform change the color to blue and make it move up and down slowly
        if self.name == "levitating platform":
            if not hasattr(self, 'direction'):
                self.direction = 1  # start moving down
            self.rect.y += self.direction
            if self.rect.y > self.levitating_bottom_limit:  # if platform reaches 800 pixels from the top of the screen, start moving up
                self.direction = -1  # start moving up
            elif self.rect.y < self.levitating_top_limit:  # if platform reaches 300 pixels from the top of the screen, start moving down
                self.direction = 1  # start moving down
        if self.name == "moving platform":
            self.rect.x += self.direction
            if self.rect.x > 800:
                self.direction = -1
            elif self.rect.x < 300:
                self.direction = 1
        if self.name == "door":
            self.image.fill(BROWN) # change the color of the door to brown
            #create a black circle middle right of the door to make it look like a handle
            pygame.draw.circle(self.image, BLACK, (90, 65), 10)

            # make door shape a rectangle instead of a square
            self.rect = pygame.Rect(self.rect.x, self.rect.y, 100, 130)
            self.image = pygame.transform.scale(self.image, (100, 130))
            # change the color of the door to yellow
            if self.name == "key":
                self.image.fill((255, 255, 255))

        if self.name == "spike":
            self.image = self.spike
            self.image.set_colorkey((0, 0, 0))

        if self.name == "ladder":
            self.image.fill((255, 255, 255))
            self.image.set_colorkey((0, 0, 0))
            # change the color of the ladder to white
            #change the shape of the ladder to a rectangle
            self.rect = pygame.Rect(self.rect.x, self.rect.y, 80, 130)
            self.image = pygame.transform.scale(self.image, (80, 130))
            #set the image of the ladder to the ladder image
            self.image = self.ladder_img
            #scale the image of the ladder to the size of the rectangle
            self.image = pygame.transform.scale(self.image, (80, 130))





                # change the color of the key to white
