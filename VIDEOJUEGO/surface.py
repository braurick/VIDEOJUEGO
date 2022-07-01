import sys 
import pygame

pygame.init()

width = 0
height = 0

surface = pygame.display.set_mode( (width , height) )
pygame.display.set_caption("QUITSIS")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()

            
