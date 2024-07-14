#Importing libraries
import pygame

#Making a crosshair class
class Crosshair(pygame.sprite.Sprite):
    def __init__(self, width, height,color):

        #Initializing the object inherated
        super().__init__()

        #Class fields
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound('assets/AWP Shooting - CS GO - QuickSounds.com.mp3')

    def Shoot(self, target_group,):
        self.gunshot.play()
        collided_targets = pygame.sprite.spritecollide(self, target_group, True)
        

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        