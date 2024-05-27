import pygame
from random import randint
from sys import exit
pygame.init()

# lista_b = []
# b_vel_y = 1
# b_vel_x = 1
# vel_x = 4
# vel_y = 2
# acc_x = 0.5
# acc_y = 0.2

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
    def __init__ (self, image_case):
        self.image_case = image_case
        self.posizione = []
        self.generazione_pos()

    def generazione_pos (self):
        while True:
            x = randint(10,1000)
            n = randint(1,3)
            self.image = pygame.image.load(self.image_case[n])
            self.crea_rect(n,x)
            
            collision = False
            for cas in c_lista:
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
    


    
   
            

#-----------------------------------------------------------------
#-----------------------------------------------------------------  
#-----------------------------------------------------------------            

image_case = {}
image_case[1]= "immagini/casa11.png"
image_case[2]= "immagini/casa22.png"
image_case[3]= "immagini/casa33.png"

# rett = pygame.Surface((90,160))
# rett.fill("Blue")

# rett1 = pygame.Surface((90,60))
# rett1.fill("Red")

# rett2 = pygame.Surface((150,100))
# rett2.fill("Black")
c_lista = []
# n_casa = randint(3,4)
# for i in range(n_casa):
#     casa = Casa(image_case)
#     c_lista.append(casa)

    # else:
    #     casa = Casa(image_case)
    #     while casa.controllo_coll(casa.rect):
    #     if not self.controllo_coll(rect):
    #             self.posizione.append((x, n))
    #             break

aereo = Aereo (1,0,200,200)
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Atomic bomb')
clock = pygame.time.Clock()

sfondox = pygame.image.load('immagini/sfondo2.1.png').convert()
sfondo = pygame.transform.scale(sfondox, (1200, 750))

prova2 = pygame.image.load('immagini/aeroplano.png')
prova = pygame.transform.scale(prova2, (100, 50))
prova1 = prova.get_rect()

lista_b = []
b_vel_y = 1
b_vel_x = 1
vel_x = 2
vel_y = 0
acc_x = 0
acc_y = 0
b_controllo = False

while True:
    screen.blit(sfondo, (0,0))

    if not c_lista:
        n_casa = randint(3,4)
        for i in range(n_casa):
            casa = Casa(image_case)
            c_lista.append(casa)
    for casa in c_lista:
        casa.stampa(screen)

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
            if bomba.controllo():  
                lista_b.remove(bomba)
            for casa in c_lista:
                    if bomba.rect.colliderect(casa.rect):
                       c_lista.remove(casa)
                       lista_b.remove(bomba)
            if bomba.rect.y >= 510 :
                lista_b.remove(bomba)


    
    vel_x = aereo.velx(vel_x, acc_x)
    vel_y = aereo.vely(vel_y, acc_y)
    acc_y = aereo.accy(vel_y, acc_y)
    aereo.controllox()
    vel_y = aereo.controlloy(vel_y)
    aereo.muoviti(vel_x, vel_y) 
    aereo.ruota(acc_y, vel_x)
    aereo.stampa(screen, acc_y)







                                                                    # for bomba in lista_b:
                                                                    #     if bomba.rect.colliderect(casa.rect) == True:
                                                                    #         pygame.quit()
                                                                    #         exit()
                                                                    # screen.blit(rett, (100,400))
                                                                    # screen.blit(rett1, (500,500))
                                                                    # screen.blit(rett2, (1000,460))
    pygame.display.update()
    clock.tick(60)