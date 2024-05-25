import pygame
from sys import exit
pygame.init()

class Aereo:
    def __init__(self, vel_x, vel_y, pos_x, pos_y,):
        self.image = pygame.image.load('immagini/aeroplano.png')
        self.image = pygame.transform.scale(self.image, (100,50))
        self.rect = self.image.get_rect()      
        self.rect.topleft = (pos_x, pos_y)
        self.vel_x = 4
        self.vel_y = 2
    
    def cordinate(self):
        return self.rect.topleft
    
    def muoviti (self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def stampa (self, screen):
        screen.blit(self.image, self.rect.topleft)
    
aereo = Aereo (4,2,200,200)

screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Atomic bomb')
clock = pygame.time.Clock()

sfondox = pygame.image.load('immagini/sfondo2.png').convert()
sfondo = pygame.transform.scale(sfondox, (1200, 750))

prova2 = pygame.image.load('immagini/aeroplano.png')
prova = pygame.transform.scale(prova2, (100, 50))
prova1 = prova.get_rect()

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           exit()
       elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_LEFT:
               
    aereo.muoviti() 
    screen.blit(sfondo, (0,0))
    aereo.stampa(screen)



    pygame.display.update()
    clock.tick(60)