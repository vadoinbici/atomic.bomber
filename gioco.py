import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Atomic bomb')
clock = pygame.time.Clock()

sfondo = pygame.image.load('immagini/sfondo.png')



while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           exit()
               
    screen.blit(sfondo, (0,0))



    pygame.display.update()
    clock.tick(60)