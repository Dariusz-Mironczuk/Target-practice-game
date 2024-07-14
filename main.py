#Importing libraries
import pygame
import sys
from settings import *
from crosshair import *
from target import *


#Making the game it's own class
class Game():

    #The defaut constructor for the game class
    def __init__(self):

        #Initializing pygame
        pygame.init()


        #GAME WINDOW
        self.DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_icon(ICON)
        pygame.display.set_caption(NAME)
        self.clock = pygame.time.Clock()

        #Making a crosshair instance
        pygame.mouse.set_visible(False)
        self.crosshair = Crosshair(6, 6,(0,255,0))
        self.crosshair_group = pygame.sprite.Group()
        self.crosshair_group.add(self.crosshair)

        #Making a target instance
        self.target_group = pygame.sprite.Group()
        for target in range(20):
            new_target = Target()
            self.target_group.add(new_target)

        



    #Making a run method to activate the game
    def run(self):
        while True:
            #Filling the display
            self.DISPLAY.fill((0,0,0))
            #Adding a background
            self.DISPLAY.blit(background, (0,0))
            

            #EVENT HANDLER
            for event in pygame.event.get():

                #Closing the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.crosshair.Shoot(self.target_group)
            
            #Drawing the targets
            self.target_group.draw(self.DISPLAY)
            #Drawign the crosshair to the display
            self.crosshair_group.draw(self.DISPLAY)
            self.crosshair.update()
            #UPDATING THE DISPLAY
            pygame.display.update()
            #Setting the game FPS
            self.clock.tick(FPS)




if __name__ == '__main__':
    game = Game()
    game.run()
