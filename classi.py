import pygame
from random import randint
from sys import exit
import time
pygame.init()

class Aereo:
    def __init__(self, vel_x, vel_y, pos_x, pos_y,):
        self.image = pygame.image.load('immagini/aeroplano.png')
        self.image = pygame.transform.scale(self.image, (100,50))
        self.image1 = self.image
        self.rect = self.image.get_rect()      
        self.rect.topleft = (pos_x, pos_y)
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.flipped = False
    
    # def cordinate(self):
    #     return self.rect.topleft
    
    def muoviti (self, vel_x, vel_y):
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def velx (self, vel_x, acc_x):
        if vel_x >= 3:
            if acc_x < 0:
                vel_x += acc_x
                vel_x = round(vel_x, 1)
                return (vel_x)
        elif vel_x <= -3:
            if acc_x > 0:
                vel_x += acc_x
                vel_x = round(vel_x, 1)
                return (vel_x)
        else:
            vel_x += acc_x
            return (vel_x)
        return (vel_x)

    def vely (self, vel_y, acc_y):

        if vel_y >= 2:
            if acc_y < 0:
                vel_y += acc_y
                # print (acc_y)
                return (vel_y)
        elif vel_y <= -2:
            if acc_y > 0:
                vel_y += acc_y
                vel_y = round(vel_y, 1)
                # print (acc_y)
                return (vel_y)
        else:
            vel_y += acc_y
            vel_y = round(vel_y, 1)
            # print (acc_y)
            return (vel_y)
        vel_y = round(vel_y, 1)
        # print (acc_y)
        return (vel_y)
    
    def accy (self, vel_y, acc_y):
        if vel_y == 0:
            acc_y = 0
            return (acc_y)
        return (acc_y)
    
    def ruota (self, acc_y, vel_x):
        if vel_x > 0:
            if acc_y == 0.2:
                self.image1 = pygame.transform.rotate(self.image, -20)
            elif acc_y == -0.2:
                self.image1 = pygame.transform.rotate(self.image, 20)
            else:
                self.image1 = self.image
        else:
            if acc_y == 0:
                self.flipped = pygame.transform.flip(self.image, True, False)
                self.image1 = self.flipped
            else:
                self.flipped = pygame.transform.flip(self.image, True, False)

                if acc_y == 0.2:
                    self.image1 = pygame.transform.rotate(self.flipped, 20)
                elif acc_y == -0.2:
                    self.image1 = pygame.transform.rotate(self.flipped, -20)
                    
                else:
                    self.image1 = self.image

    def stampa (self, screen, acc_y):
        screen.blit(self.image1, self.rect.topleft)

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
        
    # def missile_collisione(self, ostacoli):
    #     for ostacolo in ostacoli:
    #         if self.rect.colliderect(ostacolo.rect):
    #             return ostacolo
    #     return None
    
    # def terreno_collisione(self):
    #     if self.rect.y >= 560:
    #         return True
    #     return False

class Bomba:
    def __init__(self, vel_x, vel_y, pos_x, pos_y):
        self.image = pygame.image.load('immagini/bomba.png')
        self.image = pygame.transform.scale(self.image, (15,33))
        self.rect = self.image.get_rect()      
        self.rect.topleft = ((pos_x + 45), (pos_y + 30))
        self.b_vel_x = vel_x
        self.b_vel_y = vel_y
    
    def bomba_y (self, b_vel_y):
        b_vel_y = self.b_vel_y
        b_vel_y += 0.1
        return (b_vel_y)
    
    def bomb_move (self, b_vel_x, b_vel_y):
        self.b_vel_x = b_vel_x
        self.b_vel_y = b_vel_y
        self.rect.x += b_vel_x
        self.rect.y += b_vel_y
    
    def stampa (self, screen):
        screen.blit(self.image, self.rect.topleft)
    
    def controllo (self):
        if self.rect.x > 1250:
            return True
        if self.rect.x < -50:
            return True
        if self.rect.y > 650:
            return True
        return False 

class Casa:
    def __init__ (self, image_case, c_lista):
        self.image_case = image_case
        self.posizione = []
        self.c_lista = c_lista
        self.generazione_pos()
        self.colpita = False

    def generazione_pos (self):
        while True:
            x = randint(10,1000)
            n = randint(1,3)
            self.image = pygame.image.load(self.image_case[n])
            self.crea_rect(n,x)
            
            collision = False
            for cas in self.c_lista:
                if self.rect.colliderect(cas.rect):
                    collision = True
                    break
            if not collision:
                break
            
    def crea_rect(self, n,x):
        if n == 1:
            self.image = pygame.transform.scale(self.image, (120,80))
            self.rect = pygame.Rect(x,470,120,80)
            self.n = n
        elif n==2:
            self.image = pygame.transform.scale(self.image, (70,50))
            self.rect = pygame.Rect(x,510,70,50)
            self.n = n
        else:
            self.image = pygame.transform.scale(self.image, (70,130))
            self.rect = pygame.Rect(x,430,70,130)
            self.n = n
    
    def stampa (self,screen):
        screen.blit(self.image, self.rect.topleft)
    
class Esplosione1:
    def __init__ (self, x, y):
        self.image = pygame.image.load("immagini/esplosione.png")
        self.image = pygame.transform.scale(self.image, (80,80))
        self.rect = pygame.Rect(x,y,80,80)

    def appare (self,screen):
        screen.blit(self.image, self.rect.topleft)
    
class Esplosione2:
    def __init__ (self, x, y):
        self.image = pygame.image.load("immagini/esplosione.png")
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = pygame.Rect(x,y,40,40)

    def appare (self,screen):
        screen.blit(self.image, self.rect.topleft)

class Missile:
    def __init__ (self, pos_x, pos_y):
        self.image = pygame.image.load('immagini/missile2.png')
        self.image = pygame.transform.scale(self.image, (50,25))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)


    def movimento(self, screen):
        self.rect.x -= 5
        screen.blit(self.image, self.rect.topleft)



# image_case = {}
# image_case[1]= "immagini/casa11.png"
# image_case[2]= "immagini/casa22.png"
# image_case[3]= "immagini/casa33.png"

# c_lista = []