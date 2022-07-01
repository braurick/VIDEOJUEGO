import os
import pygame 
from .config import *

class Player(pygame.sprite.Sprite):

    def __init__(self, left, bottom, dir_images):
        pygame.sprite.Sprite.__init__(self)

        self.image = self.image = pygame.image.load( os.path.join(dir_images, "Diapocitiva2.PNG"))

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        self.pos_y = self.rect.bottom
        self.vel_y = 0

        self.can_jump = False

        self.playing = True

    # este elemnto me permite dectectar coliciones
    def collide_with(self, sprites):
        objects = pygame.sprite.spritecollide(self, sprites, False)
        if objects:
            return objects[0]

    def collide_bottom(self, wall):
        return self.rect.colliderect(wall.rect_top)

    def skid(self, wall):
        self.pos_y = wall.rect.top
        self.vel_y = 0
        self.can_jump = True 

    def validate_platform(self , platform):
        result = pygame.sprite.collide_rect(self , platform)
        if result:
            self.vel_y = 0
            self.pos_y = platform.rect.top
            self.can_jump = True

    def jump(self):
        if self.can_jump:
          self.vel_y = -23
          self.can_jump = False


    def update_pos(self):
        self.vel_y += player_grav
        self.pos_y += self.vel_y + 0.2 * player_grav
    
    def update(self):
        if self.playing:

            self.update_pos()

            self.rect.bottom = self.pos_y

    def stop(self):
        self.playing = False 




