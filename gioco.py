import pygame
from sys import exit
pygame.init()

class Aereo:
    def __init__(self, vel_x, vel_y, pos_x, pos_y,):
        self.image = pygame.image.load('immagini/aeroplano.png')
        self.image = pygame.transform.scale(self.image, (100,50))
        self.rect = self.image.get_rect()      
        self.rect.topleft = (pos_x, pos_y)
        # self.vel_x = 4
        # self.vel_y = 2
    
    def cordinate(self):
        return self.rect.topleft
    
    def muoviti (self, vel_x, vel_y):
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def stampa (self, screen):
        screen.blit(self.image, self.rect.topleft)
    
    def controllox (self):
        if self.rect.x > 1200:
            self.rect.x = -50
        
        if self.rect.x < -50:
            self.rect.x = 1200
            
    def controlloy (self, vel_y):
        if self.rect.y < -20:
            return (-vel_y)
        else:
            return (vel_y)
            

aereo = Aereo (4,2,200,200)

screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Atomic bomb')
clock = pygame.time.Clock()

sfondox = pygame.image.load('immagini/sfondo2.png').convert()
sfondo = pygame.transform.scale(sfondox, (1200, 750))

prova2 = pygame.image.load('immagini/aeroplano.png')
prova = pygame.transform.scale(prova2, (100, 50))
prova1 = prova.get_rect()

vel_x = 4
vel_y = 0

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           exit()
       
       elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               vel_x = -4
            elif event.key == pygame.K_RIGHT:
               vel_x = 4  
            elif event.key == pygame.K_DOWN:
               vel_y = 2 
            elif event.key == pygame.K_UP:
               vel_y = -2

    
    aereo.controllox()
    vel_y = aereo.controlloy(vel_y)
    aereo.muoviti(vel_x, vel_y) 
    screen.blit(sfondo, (0,0))
    aereo.stampa(screen)
    


    pygame.display.update()
    clock.tick(60)