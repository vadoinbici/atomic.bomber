import pygame
from random import randint
from sys import exit
import time
import ast


from classi import Aereo
from classi import Bomba
from classi import Casa
from classi import Ospedale
from classi import Missile
from classi import Esplosione1
from classi import Esplosione2


pygame.init()

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

def mostra_testo(screen, testo, x, y, dim):
    font = pygame.font.SysFont('Eras Demi ITC', dim)
    testo_surf = font.render(testo, True, 'Black')
    screen.blit(testo_surf, (x, y))

def mostra_testo1(screen, testo, x, y, dim, x_m, y_m):
    surface = pygame.Surface((x_m, y_m))
    surface.fill ("White")
    rect = surface.get_rect(topleft = (x-10,y-5))
    screen.blit(surface, (x-10,y-5))
    pygame.draw.rect(screen, (0,0,0), rect, 4)
    font = pygame.font.SysFont('Eras Demi ITC', dim)
    testo_surf = font.render(testo, True, 'Black')
    screen.blit(testo_surf, (x, y))


def leggi_file(nome_file):
    classifica = {}
    with open(nome_file, 'r', encoding='utf-8') as f:
        for riga in f:
            key, value = riga.strip().split(': ', 1)
            classifica[int(key)] = ast.literal_eval(value)

        return classifica

def scrivi_record(record):
    with open('record.txt', 'r+', encoding='utf-8') as f:
        f.truncate(0)
        f.seek(0)
    with open('record.txt', 'w', encoding='utf-8') as f:
        for key, value in record.items():
            f.write(f"{key}: {value}\n")

def confronto(class_temp, record):
    if record == {}:
        record = class_temp
        scrivi_record(record)
    else:
        for key, value in class_temp.items():
            for key1, value1 in record.items():
                    if key > key1:
                        scrivi_record(class_temp)
                        return True
                    if key == key1:
                        if value['case distrutte'] > value1['case distrutte']:
                            scrivi_record(class_temp)
                            return True
                        if value['case distrutte'] == value1['case distrutte']:
                            if value['precisione'] > value1['precisione']:
                                scrivi_record(class_temp)
                                return True

                
    return False




        

    

#-----------------------------------------------------------------
#-----------------------------------------------------------------  
#-----------------------------------------------------------------            

image_case = {}
image_case[1]= "immagini/casa11.png"
image_case[2]= "immagini/casa22.png"
image_case[3]= "immagini/casa33.png"



image_osp = {}
image_osp[2]= "immagini/ospedale1.png"
image_osp[1]= "immagini/ospedale2.png"


image_osp = {}
image_osp[1]= "immagini/ospedale1.png"
image_osp[2]= "immagini/ospedale2.png"

og_lista = []
o_lista = []
c_lista = []
ostacoli_rect_lista = []
a_lista = []
aereo = Aereo (1,0,200,200)
a_lista.append(aereo)
ostacoli_timer = pygame.USEREVENT + 1
# screen = pygame.display.set_mode((1200,600))
# pygame.display.set_caption('Atomic bomb')
clock = pygame.time.Clock()
sfondox = pygame.image.load('immagini/sfondo2.1.png').convert()
sfondo = pygame.transform.scale(sfondox, (1200, 750))


#-----------------------------------------------------------------
#-----------------------------------------------------------------  
#-----------------------------------------------------------------      

c_lista = []
o_lista = []
og_lista = []
ostacoli_rect_lista = []
a_lista = []
aereo = Aereo (1,0,200,200)
a_lista.append(aereo)
temp = 0
e_lista_temp = []
e_lista_temp1 = []
o_lista_temp = []
e_lista = []
b_lista = []
e1_lista = {}
b_vel_y = 1
b_vel_x = 1
vel_x = 2
vel_y = 0
acc_x = 0
acc_y = 0
b = 0
b_controllo = False
riscrivi = False
m_lista = []
e_lista_counter = {}
bombe_lanciate = 0
case_distrutte = 0
livello = 1
game_over = False
testo_schermo = True
classifica = {}
tempo = True
conta = 0
conta_controllo = False
b_lista_del = []
#-----------------------------------------------------------------
#-----------------------------------------------------------------  
#-----------------------------------------------------------------      

while True:
    if game_over:
        screen.blit(sfondo_over, (0,0))
        mostra_testo(screen, "Prendi INVIO per ricominciare", 300, 500, 36)
        if riscrivi:
            class_temp = leggi_file('classifica.txt')
            record = leggi_file('record.txt')
            if confronto(class_temp, record):
                record = leggi_file('record.txt')
                

                
                
            
            print(record)
        riscrivi = False
        for key, value in record.items():
            mostra_testo1(screen, f'Livello: {key}', 100, 100, 30, 300, 50)
            mostra_testo1(screen, f"case distrutte: {value['case distrutte']}", 100, 200, 30, 300, 50)
            mostra_testo1(screen, f"precisione: {value['precisione']}", 100, 300, 30, 300, 50)
            mostra_testo1(screen, f"bombe lanciate: {value['bombe lanciate']}", 100, 400, 30, 300, 50)


        mostra_testo1(screen, 'RECORD', 800, 100, 50, 240, 70)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_over = False
                c_lista = []
                o_lista = []
                og_lista = []
                ostacoli_rect_lista = []
                a_lista = []
                aereo = Aereo (1,0,200,200)
                a_lista.append(aereo)
                temp = 0
                e_lista_temp = []
                e_lista_temp1 = []
                o_lista_temp = []
                e_lista = []
                b_lista = []
                e1_lista = {}
                b_vel_y = 1
                b_vel_x = 1
                vel_x = 2
                vel_y = 0
                acc_x = 0
                acc_y = 0
                b = 0
                b_controllo = False
                riscrivi = False
                m_lista = []
                e_lista_counter = {}
                bombe_lanciate = 0
                case_distrutte = 0
                livello = 1
                game_over = False
                testo_schermo = True
                classifica = {}
                tempo = True
                conta = 0
                conta_controllo = False
                b_lista_del = []
                    


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
                n_osp = 1
                bmax = 10
                bombe_rimanenti = bmax
                for i in range(n_casa):
                    casa = Casa(image_case,c_lista)
                    c_lista.append(casa)
                    og_lista.append(casa)
                for i in range(n_osp):

                    osp = Ospedale(image_osp,og_lista)

                    osp = Ospedale(image_osp, og_lista)

                    o_lista.append(osp)
                    og_lista.append(osp)
            for casa in c_lista:
                casa.stampa(screen)
            for osp in o_lista:
                osp.stampa(screen)
        
        if 8 <= livello <= 10:
            if not c_lista:
                pygame.time.set_timer(ostacoli_timer, 1500)
                n_casa = 4
                n_osp = 2
                bmax = 8
                bombe_rimanenti = bmax
                for i in range(n_casa):
                    casa = Casa(image_case,c_lista)
                    c_lista.append(casa)
                    og_lista.append(casa)
                for i in range(n_osp):
                    osp = Ospedale(image_osp, og_lista)
                    o_lista.append(osp)
                    og_lista.append(osp)
            for casa in c_lista:
                casa.stampa(screen)
            for osp in o_lista:
                osp.stampa(screen)
        
        if 11 <= livello <= 15: 
            if not c_lista:
                pygame.time.set_timer(ostacoli_timer, 1000)
                n_casa = 4
                n_osp = 2
                bmax = 7
                bombe_rimanenti = bmax
                for i in range(n_casa):
                    casa = Casa(image_case,c_lista)
                    c_lista.append(casa)
                    og_lista.append(casa)
                for i in range(n_osp):

                    osp = Ospedale(image_osp,og_lista)

                    osp = Ospedale(image_osp, og_lista)

                    o_lista.append(osp)
                    og_lista.append(osp)
            for casa in c_lista:
                casa.stampa(screen)
            for osp in o_lista:
                osp.stampa(screen)
        
        if livello > 15: 
            if not c_lista:
                pygame.time.set_timer(ostacoli_timer, 500)
                n_casa = 4
                n_osp = 2
                bmax = 7
                bombe_rimanenti = bmax
                for i in range(n_casa):
                    casa = Casa(image_case,c_lista)
                    c_lista.append(casa)
                    og_lista.append(casa)
                for i in range(n_osp):

                    osp = Ospedale(image_osp,og_lista)

                    osp = Ospedale(image_osp, og_lista)

                    o_lista.append(osp)
                    og_lista.append(osp)
            for casa in c_lista:
                casa.stampa(screen)
            for osp in o_lista:
                osp.stampa(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                #    vel_x = -4
                    acc_x = -0.5
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                #    vel_x = 4 
                    acc_x = 0.5
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                #    vel_y = 2
                    acc_y = 0.2
                    # if acc_y < 0.2:
                    #     acc_y += 0.1
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                #    vel_y = -2
                    acc_y = -0.2
                    # if acc_y > -0.2:
                    #     acc_y -= 0.1
                elif event.key == pygame.K_SPACE:
                    i = 0
                    bomba = Bomba(aereo.vel_x, aereo.vel_y, aereo.rect.x, aereo.rect.y)
                    if len(b_lista) < 3:
                        if b != bmax:
                            b += 1
                            bombe_rimanenti -= 1 
                            bombe_lanciate += 1
                            b_lista.append(bomba)
                            b_controllo = True
            if event.type == ostacoli_timer:
                y = randint(10,430)
                x = randint(1300,1500)
                missile = Missile(x, y)
                m_lista.append(missile)
                # ostacoli_rect_lista.append(pygame.Rect(randint(1300, 1500), randint(50,430), 50, 25))



        if b_controllo:
            for bomba in b_lista:
                b_vel_y = bomba.bomba_y(b_vel_y)
                bomba.bomb_move(bomba.b_vel_x, b_vel_y)
                bomba.stampa(screen)
                if bomba.controllo():  
                    b_lista_del.append(bomba)
                
                for casa_esp in e_lista_temp:  
                    casa = casa_esp['casa']
                    if bomba.rect.colliderect(casa.rect):
                        b_lista_del.append(bomba)
                        break
                


                else:
                    for casa in c_lista:
                            if bomba.rect.colliderect(casa.rect):
                                casa.colpita = True
                                esplosione = Esplosione1((bomba.rect.x - 25), bomba.rect.y)
                                casa_esp_temp = {'casa': casa, 'esplosione': esplosione}
                                e_lista_temp.append(casa_esp_temp)
                                e_lista_counter[esplosione] = 0
                                b_lista_del.append(bomba)
                                case_distrutte += 1
                                break
                
                for osp_esp in o_lista_temp:  
                    osp = osp_esp['ospedale']
                    if bomba.rect.colliderect(osp.rect):
                        b_lista_del.append(bomba)
                        break
                


                else:
                    for osp in o_lista:
                            if bomba.rect.colliderect(osp.rect):
                                osp.colpita = True
                                esplosione = Esplosione1((bomba.rect.x - 25), bomba.rect.y)
                                osp_esp_temp = {'ospedale': osp, 'esplosione': esplosione}
                                e_lista_temp1.append(osp_esp_temp)
                                e_lista_counter[esplosione] = 0
                                b_lista_del.append(bomba)
                                break








                if bomba.rect.y >= 510:
                    esp1 = Esplosione2((bomba.rect.x), bomba.rect.y)
                    e1_lista[esp1] = 0
                    b_lista_del.append(bomba)

        if e_lista_temp:
            for casa_esp in e_lista_temp:
                esplosione = casa_esp['esplosione']
                casa = casa_esp['casa'] 
                esplosione.appare(screen)
                e_lista_counter[esplosione] += 1

                if e_lista_counter[esplosione] > 20:
                    c_lista.remove(casa)
                    e_lista_temp.remove(casa_esp)
            
        if e_lista_temp1:
            for osp_esp in e_lista_temp1:
                esplosione = osp_esp['esplosione']
                casa = osp_esp['ospedale'] 
                esplosione.appare(screen)
                e_lista_counter[esplosione] += 1

                if e_lista_counter[esplosione] > 20:
                    o_lista.remove(osp)
                    e_lista_temp1.remove(osp_esp)
                    if bombe_lanciate != 0 or case_distrutte != 0:
                        perc = round(case_distrutte/bombe_lanciate, 2)
                    else:
                        perc = 0
                    classifica[livello] = {'case distrutte': case_distrutte, 'precisione': perc*100, 'bombe lanciate': bombe_lanciate,}
                    with open('classifica.txt', 'r+', encoding='utf-8') as f:
                        f.truncate(0)
                        f.seek(0)
                    with open('classifica.txt', 'w', encoding='UTF-8') as f:
                        for key,value in classifica.items():
                            f.write(f"{key}: {value}\n")
                    riscrivi = True
                    m_lista.clear()
                    e_lista.clear()
                    c_lista.clear()
                    o_lista.clear()
                    b_lista_del.clear()
                    b_lista.clear()
                    e_lista_temp1.clear()
                    a_lista.clear()
                    testo_schermo = False
                    game_over = True

        if e1_lista:
            for esp1 in e1_lista:
                e1_lista[esp1] += 1
            if e1_lista[esp1] < 15:
                esp1.appare(screen)
            else:
                del e1_lista[esp1]

    

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
                esp1.appare(screen)
                pygame.display.flip()
                pygame.time.delay(300)
                if bombe_lanciate != 0 or case_distrutte != 0:
                    perc = round(case_distrutte/bombe_lanciate, 2)
                else:
                    perc = 0
                classifica[livello] = {'case distrutte': case_distrutte, 'precisione': perc*100, 'bombe lanciate': bombe_lanciate,}
                with open('classifica.txt', 'r+', encoding='utf-8') as f:
                    f.truncate(0)
                    f.seek(0)
                with open('classifica.txt', 'w', encoding='UTF-8') as f:
                    for key,value in classifica.items():
                        f.write(f"{key}: {value}\n")
                e1_lista.clear()
                m_lista.clear()
                e_lista.clear()
                c_lista.clear()
                b_lista_del.clear()
                o_lista.clear()
                b_lista.clear()
                e_lista_temp1.clear()
                a_lista.clear()
                riscrivi = True
                testo_schermo = False
                game_over= True
                
            for casa in c_lista:
                if aereo.rect.colliderect(casa.rect):
                    esp1 = Esplosione1((aereo.rect.x), aereo.rect.y)
                    esp1.appare(screen)
                    pygame.display.flip()
                    pygame.time.delay(300)
                    a_lista.remove(aereo)
                    if bombe_lanciate != 0 or case_distrutte != 0:
                        perc = round(case_distrutte/bombe_lanciate, 2)
                    else:
                        perc = 0
                    classifica[livello] = {'case distrutte': case_distrutte, 'precisione': perc*100, 'bombe lanciate': bombe_lanciate,}
                    
                    with open('classifica.txt', 'r+', encoding='utf-8') as f:
                        f.truncate(0)
                        f.seek(0)
                    with open('classifica.txt', 'w', encoding='UTF-8') as f:
                        for key,value in classifica.items():
                            f.write(f"{key}: {value}\n")
                    e1_lista.clear()
                    m_lista.clear()
                    b_lista_del.clear()
                    e_lista.clear()
                    c_lista.clear()
                    o_lista.clear()
                    b_lista.clear()
                    e_lista_temp1.clear()
                    a_lista.clear()
                    riscrivi = True
                    testo_schermo = False
                    game_over = True
            
            for osp in o_lista:
                if aereo.rect.colliderect(osp.rect):
                    esp1 = Esplosione1((aereo.rect.x), aereo.rect.y)
                    esp1.appare(screen)
                    pygame.display.flip()
                    pygame.time.delay(300)
                    a_lista.remove(aereo)

                    if not bombe_lanciate and not case_distrutte:
                        perc = round(case_distrutte/bombe_lanciate, 2)
                    else:
                        perc = 0
                    classifica[livello] = {'case distrutte': case_distrutte, 'precisione': perc*100, 'bombe lanciate': bombe_lanciate,}
                    with open('classifica.txt', 'r+', encoding='utf-8') as f:
                        f.truncate(0)
                        f.seek(0)
                    with open('classifica.txt', 'w', encoding='UTF-8') as f:
                        for key,value in classifica.items():
                            f.write(f"{key}: {value}\n")
                    e1_lista.clear()
                    m_lista.clear()
                    b_lista_del.clear()
                    e_lista.clear()
                    c_lista.clear()
                    o_lista.clear()
                    b_lista.clear()
                    e_lista_temp1.clear()
                    a_lista.clear()
                    testo_schermo = False
                    game_over = True
                    

        if testo_schermo:
            mostra_testo(screen, f"Livello: {livello}", 10, 10, 36)
            mostra_testo(screen, f"Bombe rimanenti: {bombe_rimanenti}", 200, 10, 36)
            mostra_testo(screen, f'case distrutte: {case_distrutte}', 750, 15, 26)
            if bombe_lanciate != 0 or case_distrutte != 0:
                perc = round(case_distrutte/bombe_lanciate, 2)
            else:
                perc = 0
            mostra_testo(screen, f'precisione: {perc}', 1000, 15, 26)

        for missile in m_lista:
            missile.movimento(screen)
            if aereo.rect.x<1200:
                if aereo.rect.colliderect(missile.rect):
                    esp1 = Esplosione1((aereo.rect.x), aereo.rect.y)
                    esp1.appare(screen)
                    pygame.display.flip()
                    pygame.time.delay(300)
                    m_lista.remove(missile)
                    a_lista.remove(aereo)

                    if bombe_lanciate != 0 or case_distrutte != 0:
                        perc = round(case_distrutte/bombe_lanciate, 2)
                    else:
                        perc = 0
                    classifica[livello] = {'case distrutte': case_distrutte, 'precisione': perc*100, 'bombe lanciate': bombe_lanciate,}
                    
                    with open('classifica.txt', 'r+', encoding='utf-8') as f:
                        f.truncate(0)
                        f.seek(0)

                    with open('classifica.txt', 'w', encoding='UTF-8') as f:
                        for key,value in classifica.items():
                            f.write(f"{key}: {value}\n")

                    m_lista.clear()
                    e_lista.clear()
                    o_lista.clear()
                    b_lista_del.clear()
                    b_lista.clear()
                    e_lista_temp1.clear()
                    a_lista.clear()
                    e1_lista.clear()
                    riscrivi = True
                    testo_schermo = False
                    game_over = True
                

        if not c_lista:

            livello += 1

            o_lista.clear()
            og_lista.clear()
            b = 0
            o_lista.clear()
            og_lista.clear()
        
        if bombe_rimanenti==0 and not b_lista:
            conta_controllo = True
            if conta > 150:
                if not c_lista:
                    pass
                if not b_lista:
                    pass
                

                
                if bombe_lanciate != 0 or case_distrutte != 0:
                    perc = round(case_distrutte/bombe_lanciate, 2)
                else:
                    perc = 0 
                classifica[livello] = {'case distrutte': case_distrutte, 'precisione': perc*100, 'bombe lanciate': bombe_lanciate,}
                
                with open('classifica.txt', 'r+', encoding='utf-8') as f:
                    f.truncate(0)
                    f.seek(0)
                with open('classifica.txt', 'w', encoding='UTF-8') as f:
                    for key,value in classifica.items():
                        f.write(f"{key}: {value}\n")

                e1_lista.clear()
                m_lista.clear()
                e_lista.clear()
                b_lista_del.clear()
                c_lista.clear()
                o_lista.clear()
                b_lista.clear()
                e_lista_temp1.clear()
                a_lista.clear()
                riscrivi = True
                testo_schermo = False
                mostra_testo(screen, "Hai finito le bombe", 400, 300, 40) 
                pygame.display.flip()
                pygame.time.delay(1000)
                game_over= True
                conta = 0

            else:
                conta += 1
            
            if not conta_controllo:
                if conta != 0:
                    conta = 0
                    conta_controlla = False
            
        for bomba in b_lista_del:
            b_lista.remove(bomba)
        b_lista_del.clear()
            
            


    pygame.display.update()
    clock.tick(60)