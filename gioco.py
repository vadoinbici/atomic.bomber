import pygame
from random import randint
from sys import exit
import time
pygame.init()
<<<<<<< HEAD


from classi import Aereo
from classi import Ospedale
from classi import Bomba
from classi import Casa
from classi import Missile
from classi import Esplosione1
from classi import Esplosione2


=======
>>>>>>> 1528609164f994dd48508a9e3cfe822c62ba2eb8

screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Atomic bomber')

sfondo1 = pygame.image.load('immagini/caricamento.png')
sfondo1 = pygame.transform.scale(sfondo1, (1200,600))
sfondo_over = pygame.image.load('immagini/game_over.png')
sfondo_over = pygame.transform.scale(sfondo_over, (1200,600))
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


def libera_gioco(self, r_lista):
    while r_lista:
        for el in r_lista:
            r_lista.remove(el)
    return (r_lista)

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

image_osp = {}
image_osp[1]= "immagini/ospedale1.png"
image_osp[2]= "immagini/ospedale2.png"
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
og_lista = []
o_lista = []
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
o_lista_temp = []
o_lista_counter = {}
classifica = {}
ostacoli_timer = pygame.USEREVENT + 1
case_distrutte = 0
bombe_lanciate = 0
livello = 1
game_over = False
while True:
<<<<<<< HEAD
    screen.blit(sfondo, (0,0))
    if livello <= 3:
        while o_lista:
            for el in o_lista:
                o_lista.remove(el)
        if not c_lista:
            pygame.time.set_timer(ostacoli_timer, 3000)
            n_casa = 3
            n_osp = 0
            bmax = 12
            bombe_rimanenti = bmax

            for i in range(n_casa):
                casa = Casa(image_case, og_lista)
                c_lista.append(casa)
                og_lista.append(casa)
            for i in range(n_osp):
                ospedale = Ospedale(image_osp, og_lista)
                o_lista.append(ospedale)
                og_lista.append(ospedale)
        for casa in og_lista:
            casa.stampa(screen)


    if 4 <= livello <= 7:
        while o_lista:
            for el in o_lista:
                o_lista.remove(el)
        if not c_lista:
            pygame.time.set_timer(ostacoli_timer, 2000)
            n_casa = 4
            n_osp = 1
            bmax = 10
            bombe_rimanenti = bmax

            for i in range(n_casa):
                casa = Casa(image_case,og_lista)
                c_lista.append(casa)
                og_lista.append(casa)
            for i in range(n_osp):
                ospedale = Ospedale(image_osp, og_lista)
                o_lista.append(ospedale)
                og_lista.append(ospedale)
        for casa in og_lista:
            casa.stampa(screen)


    if 8 <= livello <= 10:
        while o_lista:
            for el in o_lista:
                o_lista.remove(el)
        if not c_lista:
            pygame.time.set_timer(ostacoli_timer, 1500)
            n_casa = 4
            bmax = 8
            n_osp = 2
            bombe_rimanenti = bmax
            
            for i in range(n_casa):
                casa = Casa(image_case,og_lista)
                c_lista.append(casa)
                og_lista.append(casa)
            for i in range(n_osp):
                ospedale = Ospedale(image_osp, og_lista)
                o_lista.append(ospedale)
                og_lista.append(ospedale)
            
        for casa in og_lista:
            casa.stampa(screen)


    if livello > 10:
        while o_lista:
            for el in o_lista:
                o_lista.remove(el)
        if not c_lista:
            pygame.time.set_timer(ostacoli_timer, 1000)
            n_casa = 5
            n_osp = 3
            bmax = 5
            bombe_rimanenti = bmax

            for i in range(n_casa):
                casa = Casa(image_case, og_lista)
                c_lista.append(casa)
                og_lista.append(casa)
            for i in range(n_osp):
                ospedale = Ospedale(image_osp, og_lista)
                o_lista.append(ospedale)
                og_lista.append(ospedale)

        for casa in og_lista:
            casa.stampa(screen)
=======
    if game_over:
        screen.blit(sfondo_over, (0,0))
        mostra_testo(screen, "Prendi INVIO per ricominciare", 300, 500)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_over = False
                livello = 1
                a_lista = []
                aereo = Aereo (1,0,200,200)
                a_lista.append(aereo)
                e_lista_temp = []
                e_lista = []
                lista_b = []
                e1_lista = {}
                vel_x = 2
                vel_y = 0
                acc_x = 0
                acc_y = 0
                b = 0
                m_lista = []
                e_lista_counter = {}


    else:
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
>>>>>>> 1528609164f994dd48508a9e3cfe822c62ba2eb8

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
                for osp in o_lista:
                        if bomba.rect.colliderect(osp.rect):
                            osp.colpita = True
                            esplosione = Esplosione1((bomba.rect.x - 50), bomba.rect.y)
                            osp_esp_temp = {'casa': casa, 'esplosione': esplosione}
                            o_lista_temp.append(osp_esp_temp)
                            o_lista_counter[esplosione] = 0
                            lista_b.remove(bomba)
                            perc = round(case_distrutte/bombe_lanciate, 2)
                            classifica[livello] = {'case distrutte': case_distrutte, 'precisione': perc*100, 'bombe lanciate': bombe_lanciate,}
                            with open('classifica.txt', 'w', encoding='utf-8') as f:
                                for key,value in classifica.items():
                                    f.write(f"{key}: {value}\n")
                            c_lista = libera_gioco(c_lista)
                            o_lista = libera_gioco(o_lista)
                            m_lista = libera_gioco(m_lista)
                            lista_b = libera_gioco(lista_b)
                        # METTERE LA SCHERMATA GAME OVER ////////////////////////////////////////////////////////////////////////////////


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

        if aereo.rect.y >= 490:
            esp1 = Esplosione1((aereo.rect.x), aereo.rect.y)
            e1_lista[esp1] = 0
            a_lista.remove(aereo)
<<<<<<< HEAD

            perc = round(case_distrutte/bombe_lanciate, 2)
            classifica[livello] = {'case distrutte': case_distrutte, 'precisione': perc*100, 'bombe lanciate': bombe_lanciate,}
            for key,value in classifica.items():
                f.write(f"{key}: {value}\n")

            c_lista = libera_gioco(c_lista)
            o_lista = libera_gioco(o_lista)
            m_lista = libera_gioco(m_lista)
            lista_b = libera_gioco(lista_b)
             # METTERE LA SCHERMATA GAME OVER ////////////////////////////////////////////////////////////////////////////////

        for osp in o_lista:
            if aereo.rect.colliderect(osp.rect):
                esp1 = Esplosione1((aereo.rect.x), aereo.rect.y)
                e1_lista[esp1] = 0
                a_lista.remove(aereo)
            
            perc = round(case_distrutte/bombe_lanciate, 2)
            classifica[livello] = {'case distrutte': case_distrutte, 'precisione': perc*100, 'bombe lanciate': bombe_lanciate,}
            for key,value in classifica.items():
                f.write(f"{key}: {value}\n")

            c_lista = libera_gioco(c_lista)
            o_lista = libera_gioco(o_lista)
            m_lista = libera_gioco(m_lista)
            lista_b = libera_gioco(lista_b)
        # METTERE LA SCHERMATA GAME OVER ////////////////////////////////////////////////////////////////////////////////
=======
            game_over= True
            
>>>>>>> 1528609164f994dd48508a9e3cfe822c62ba2eb8
        for casa in c_lista:
            if aereo.rect.colliderect(casa.rect):
                esp1 = Esplosione1((aereo.rect.x), aereo.rect.y)
                e1_lista[esp1] = 0
                a_lista.remove(aereo)
<<<<<<< HEAD
            
            perc = round(case_distrutte/bombe_lanciate, 2)
            classifica[livello] = {'case distrutte': case_distrutte, 'precisione': perc*100, 'bombe lanciate': bombe_lanciate,}
            for key,value in classifica.items():
                f.write(f"{key}: {value}\n")

                c_lista = libera_gioco(c_lista)
                o_lista = libera_gioco(o_lista)
                m_lista = libera_gioco(m_lista)
                lista_b = libera_gioco(lista_b)
                # METTERE LA SCHERMATA GAME OVER ////////////////////////////////////////////////////////////////////////////////
=======
                game_over = True
                
>>>>>>> 1528609164f994dd48508a9e3cfe822c62ba2eb8


    mostra_testo(screen, f"Livello: {livello}", 10, 10)
    mostra_testo(screen, f"Bombe rimanenti: {bombe_rimanenti}", 200, 10)

    for missile in m_lista:
        missile.movimento(screen)
        if aereo.rect.colliderect(missile.rect):
            esp1 = Esplosione1((aereo.rect.x), aereo.rect.y)

            e1_lista[esp1] = 0
            m_lista.remove(missile)
            a_lista.remove(aereo)
<<<<<<< HEAD
             # METTERE LA SCHERMATA GAME OVER ////////////////////////////////////////////////////////////////////////////////

=======
            game_over = True
            
>>>>>>> 1528609164f994dd48508a9e3cfe822c62ba2eb8

    if not c_lista:
        case_distrutte += n_casa
        bombe_lanciate += b
        livello += 1
        b = 0
    if bombe_rimanenti==0 and not lista_b:
        game_over= True

    pygame.display.update()
    clock.tick(60)