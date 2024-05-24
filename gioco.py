import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Atomic bomb')
clock = pygame.time.Clock()





while True:
    for event in pygame.event:
       if event.type == pygame.QUIT:
           pygame.quit()
           exit()




    pygame.display.update()
    clock.tick(60)