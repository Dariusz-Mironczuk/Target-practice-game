#Importing libraries
import pygame
import random

#Making a target class
class Target(pygame.sprite.Sprite):
    #Defaut constructor
    def __init__(self):

        #Inhariting from the Sprite class
        super().__init__()

        #Class fields
        self.image = pygame.image.load('assets/target.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [random.randint(self.image.get_width(), 580), random.randint(60, 420)]

        