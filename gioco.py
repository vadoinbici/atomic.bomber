import pygame
from sys import exit
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
    
    def cordinate(self):
        return self.rect.topleft
    
    def muoviti (self, vel_x, vel_y):
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def velx (self, vel_x, acc_x):
        if vel_x >= 4:
            if acc_x < 0:
                vel_x += acc_x
                vel_x = round(vel_x, 1)
                return (vel_x)
        elif vel_x <= -4:
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

class Bomba:
    def __init__(self, vel_x, vel_y, pos_x, pos_y):
        self.image = pygame.image.load('immagini/bomba.png')
        self.image = pygame.transform.scale(self.image, (20,50))
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


#-----------------------------------------------------------------
#-----------------------------------------------------------------  
#-----------------------------------------------------------------            

aereo = Aereo (1,0,200,200)
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Atomic bomb')
clock = pygame.time.Clock()

sfondox = pygame.image.load('immagini/sfondo2.png').convert()
sfondo = pygame.transform.scale(sfondox, (1200, 750))

prova2 = pygame.image.load('immagini/aeroplano.png')
prova = pygame.transform.scale(prova2, (100, 50))
prova1 = prova.get_rect()

lista_b = []
b_vel_y = 1
b_vel_x = 1
vel_x = 4
vel_y = 0
acc_x = 1
acc_y = 0.5
b_controllo = False

while True:
    screen.blit(sfondo, (0,0))
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           exit()
       
       elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
            #    vel_x = -4
                acc_x = -0.5
            elif event.key == pygame.K_RIGHT:
            #    vel_x = 4 
                acc_x = 0.5
            elif event.key == pygame.K_DOWN:
            #    vel_y = 2
                acc_y = 0.2
                # if acc_y < 0.2:
                #     acc_y += 0.1
            elif event.key == pygame.K_UP:
            #    vel_y = -2
                acc_y = -0.2
                # if acc_y > -0.2:
                #     acc_y -= 0.1
            elif event.key == pygame.K_SPACE:
                i = 0
                bomba = Bomba(aereo.vel_x, aereo.vel_y, aereo.rect.x, aereo.rect.y)
                if len(lista_b) < 3:
                    lista_b.append(bomba)
                    b_controllo = True



    if b_controllo == True:
        for bomba in lista_b:
            b_vel_y = bomba.bomba_y(b_vel_y)
            bomba.bomb_move(bomba.b_vel_x, b_vel_y)
            bomba.stampa(screen)
            if bomba.controllo() == True:  
                lista_b.remove(bomba)


            
    
    
    
    vel_x = aereo.velx(vel_x, acc_x)
    vel_y = aereo.vely(vel_y, acc_y)
    acc_y = aereo.accy(vel_y, acc_y)
    aereo.controllox()
    vel_y = aereo.controlloy(vel_y)
    aereo.muoviti(vel_x, vel_y) 
    aereo.ruota(acc_y, vel_x)
    aereo.stampa(screen, acc_y)



    pygame.display.update()
    clock.tick(60)