import pygame
from random import randint
from sys import exit
import time
from classi import Aereo
from classi import Bomba
from classi import Casa
from classi import Esplosione1
from classi import Esplosione2
from classi import Missile
pygame.init()

screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Atomic bomber')

sfondo1 = pygame.image.load('immagini/caricamento.png')
sfondo1 = pygame.transform.scale(sfondo1, (1200,600))

barra_caricamento_colore = ('Orange')

def genera_barra(screen, progresso):
    bar_lar= 400
    bar_alt= 50
    bar_x=(1200-bar_lar)/2
    bar_y=(1000-bar_alt)/2

    pygame.draw.rect(screen, (255, 255, 255), (bar_x, bar_y, bar_lar, bar_alt), 2)
    pygame.draw.rect(screen, barra_caricamento_colore,(bar_x, bar_y, bar_lar*progresso, bar_alt))
    
caricamento = True
progresso = 0

while caricamento:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit()
    screen.blit(sfondo1, (0, 0))

    genera_barra(screen, progresso)
    pygame.display.flip()

    time.sleep(0.1)  
    progresso += 0.05
    if progresso >= 1:
        caricamento = False
# lista_b = []
# b_vel_y = 1
# b_vel_x = 1
# vel_x = 4
# vel_y = 2
# acc_x = 0.5
# acc_y = 0.2


from classi import Aereo
from classi import Bomba
from classi import Casa
from classi import Missile
from classi import Esplosione1
from classi import Esplosione2


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
    def __init__ (self, image_case):
        self.image_case = image_case
        self.posizione = []
        self.generazione_pos()
        self.colpita = False

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

        # ostacoli_rect_lista = []

        # if ostacoli_lista:
        #     for ostacoli_rect in ostacoli_lista:
        #         ostacoli_rect.x -= 5
        #         screen.blit(self.image, ostacoli_rect)
        #         if ostacoli_rect.x > -50:
        #             ostacoli_rect_lista.append(ostacoli_rect)
        # return ostacoli_rect_lista


def mostra_testo(screen, testo, x, y):
    font = pygame.font.SysFont('Eras Demi ITC', 36)
    testo_surf = font.render(testo, True, 'Black')
    screen.blit(testo_surf, (x, y))
    
#-----------------------------------------------------------------
#-----------------------------------------------------------------  
#-----------------------------------------------------------------            

image_case = {}
image_case[1]= "immagini/casa11.png"
image_case[2]= "immagini/casa22.png"
image_case[3]= "immagini/casa33.png"

c_lista = []
ostacoli_rect_lista = []
a_lista = []
aereo = Aereo (1,0,200,200)
a_lista.append(aereo)
# screen = pygame.display.set_mode((1200,600))
# pygame.display.set_caption('Atomic bomb')
clock = pygame.time.Clock()

sfondox = pygame.image.load('immagini/sfondo2.1.png').convert()
sfondo = pygame.transform.scale(sfondox, (1200, 750))

# prova2 = pygame.image.load('immagini/aeroplano.png')
# prova = pygame.transform.scale(prova2, (100, 50))
# prova1 = prova.get_rect()

temp = 0
e_lista_temp = []
e_lista = []
lista_b = []
e1_lista = {}
b_vel_y = 1
b_vel_x = 1
vel_x = 2
vel_y = 0
acc_x = 0
acc_y = 0
b = 0
b_controllo = False
m_lista = []
e_lista_counter = {}

ostacoli_timer = pygame.USEREVENT + 1

livello = 1

while True:
    screen.blit(sfondo, (0,0))
    if livello <= 3:
        if not c_lista:
            pygame.time.set_timer(ostacoli_timer, 3000)
            n_casa = 3
            bmax = 12
            bombe_rimanenti = bmax
            for i in range(n_casa):
                casa = Casa(image_case, c_lista)
                c_lista.append(casa)
        for casa in c_lista:
            casa.stampa(screen)
    if 4 <= livello <= 7:
        if not c_lista:
            pygame.time.set_timer(ostacoli_timer, 2000)
            n_casa = 4
            bmax = 10
            bombe_rimanenti = bmax
            for i in range(n_casa):
                casa = Casa(image_case,c_lista)
                c_lista.append(casa)
        for casa in c_lista:
            casa.stampa(screen)
    if 8 <= livello <= 10:
        if not c_lista:
            pygame.time.set_timer(ostacoli_timer, 1500)
            n_casa = 4
            bmax = 8
            bombe_rimanenti = bmax
            for i in range(n_casa):
                casa = Casa(image_case,c_lista)
                c_lista.append(casa)
        for casa in c_lista:
            casa.stampa(screen)
    if livello > 10:
        if not c_lista:
            pygame.time.set_timer(ostacoli_timer, 1000)
            n_casa = 5
            bmax = 5
            bombe_rimanenti = bmax
            for i in range(n_casa):
                casa = Casa(image_case.c_lista)
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
                    if b != bmax:
                        b += 1
                        bombe_rimanenti -= 1 
                        lista_b.append(bomba)
                        b_controllo = True
        if event.type == ostacoli_timer:
            y = randint(50,430)
            x = randint(1300,1500)
            missile = Missile(x, y)
            m_lista.append(missile)
            # ostacoli_rect_lista.append(pygame.Rect(randint(1300, 1500), randint(50,430), 50, 25))



    if b_controllo:
        for bomba in lista_b:
            b_vel_y = bomba.bomba_y(b_vel_y)
            bomba.bomb_move(bomba.b_vel_x, b_vel_y)
            bomba.stampa(screen)
            if bomba.controllo():  
                lista_b.remove(bomba)
            
            for casa_esp in e_lista_temp:  # Controlla solo le case che sono in attesa di essere rimosse
                casa = casa_esp['casa']
                if bomba.rect.colliderect(casa.rect):
                    lista_b.remove(bomba)
                    break
            
            else:
                for casa in c_lista:
                        if bomba.rect.colliderect(casa.rect):
                            casa.colpita = True
                            esplosione = Esplosione1((bomba.rect.x - 50), bomba.rect.y)
                            casa_esp_temp = {'casa': casa, 'esplosione': esplosione}
                            e_lista_temp.append(casa_esp_temp)
                            e_lista_counter[esplosione] = 0
                            lista_b.remove(bomba)
                            break


            if bomba.rect.y >= 510:
                esp1 = Esplosione2((bomba.rect.x), bomba.rect.y)
                e1_lista[esp1] = 0
                lista_b.remove(bomba)

    if e_lista_temp:
        for casa_esp in e_lista_temp:
            esplosione = casa_esp['esplosione']
            casa = casa_esp['casa'] 
            esplosione.appare(screen)
            e_lista_counter[esplosione] += 1

            if e_lista_counter[esplosione] > 20:
                c_lista.remove(casa)
                e_lista_temp.remove(casa_esp)

    if e1_lista:
        for esp1 in e1_lista:
            e1_lista[esp1] += 1
        if e1_lista[esp1] < 15:
            esp1.appare(screen)
        else:
            del e1_lista[esp1]


    # missile = Missile(1300, 100)
    # m_lista.append(missile)
    # ostacoli_rect_lista = missile.movimento(ostacoli_rect_lista)
 

    for aereo in a_lista:
        vel_x = aereo.velx(vel_x, acc_x)
        vel_y = aereo.vely(vel_y, acc_y)
        acc_y = aereo.accy(vel_y, acc_y)
        aereo.controllox()
        vel_y = aereo.controlloy(vel_y)
        aereo.muoviti(vel_x, vel_y) 
        aereo.ruota(acc_y, vel_x)
        aereo.stampa(screen, acc_y)
    mostra_testo(screen, f"Livello: {livello}", 10, 10)
    mostra_testo(screen, f"Bombe rimanenti: {bombe_rimanenti}", 200, 10)

    for missile in m_lista:
        missile.movimento(screen)
        if aereo.rect.colliderect(missile.rect):
            esp1 = Esplosione1((aereo.rect.x), aereo.rect.y)

            e1_lista[esp1] = 0
            m_lista.remove(missile)
            a_lista.remove(aereo)



    




    if not c_lista:
        livello += 1
        b = 0

    pygame.display.update()
    clock.tick(60)