# Import the pygame module
from copy import deepcopy
import pygame
import time
import sys
import math
import array
import random

array.array('i')

pygame.init()
screen_size = 1000, 810
screen = pygame.display.set_mode(screen_size)
font = pygame.font.SysFont("comicsans", 80)
fontcas=pygame.font.SysFont("Times New Roman", 40)
font2=pygame.font.SysFont("comicsans", 40)
font3=pygame.font.SysFont("comicsans", 30)
vyhra = pygame.image.load('vyhra.png')
firsttime = time.time()
prazdne = 0
stlacena = 0
Poziciax = -1
Poziciay = -1
poleX = array.array('i', (0 for i in range(0, prazdne)))
poleY = array.array('i', (0 for i in range(0, prazdne)))
clicked = False
pocetkrokov=0
pocetkrokovfs=0
pocetkrokov2=0
#MAPY
mapa1 =[
    [0, 7, 0, 8, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 2, 4, 0, 0],
    [1, 0, 6, 4, 0, 0, 5, 0, 0],
    [0, 0, 1, 9, 0, 0, 0, 4, 0],
    [3, 0, 5, 0, 0, 0, 9, 0, 1],
    [0, 9, 0, 0, 0, 4, 2, 0, 0],
    [0, 0, 3, 0, 0, 6, 1, 0, 4],
    [0, 0, 9, 7, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 5, 0, 6, 0]
    ]
solvemapa1 = [[5, 7, 4, 8, 1, 3, 6, 2, 9],
              [9, 3, 8, 5, 6, 2, 4, 1, 7],
              [1, 2, 6, 4, 7, 9, 5, 8, 3],
              [2, 6, 1, 9, 3, 7, 8, 4, 5],
              [3, 4, 5, 6, 2, 8, 9, 7, 1],
              [8, 9, 7, 1, 5, 4, 2, 3, 6],
              [7, 5, 3, 2, 8, 6, 1, 9, 4],
              [6, 8, 9, 7, 4, 1, 3, 5, 2],
              [4, 1, 2, 3, 9, 5, 7, 6, 8]]
#####################################
mapa2 =[
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ]
solvemapa2=[
    [8, 1, 2, 7, 5, 3, 6, 4, 9],
    [9, 4, 3, 6, 8, 2, 1, 7, 5],
    [6, 7, 5, 4, 9, 1, 2, 8, 3],
    [1, 5, 4, 2, 3, 7, 8, 9, 6],
    [3, 6, 9, 8, 4, 5, 7, 2, 1],
    [2, 8, 7, 1, 6, 9, 5, 3, 4],
    [5, 2, 1, 9, 7, 4, 3, 6, 8],
    [4, 3, 8, 5, 2, 6, 9, 1, 7],
    [7, 9, 6, 3, 1, 8, 4, 5, 2]
    ]
####################################
mapa3=[
    [8, 7, 3, 0, 2, 9, 1, 0, 0],
    [5, 0, 9, 4, 6, 1, 0, 8, 0],
    [6, 4, 1, 0, 0, 0, 2, 9, 0],
    [0, 8, 0, 1, 7, 5, 3, 0, 0],
    [9, 0, 7, 8, 0, 3, 6, 0, 0],
    [3, 0, 4, 0, 9, 0, 8, 5, 7],
    [4, 6, 0, 3, 8, 0, 0, 0, 2],
    [1, 0, 0, 9, 0, 6, 0, 0, 8],
    [7, 0, 8, 2, 0, 0, 0, 0, 0]]

solvemapa3=[
            [8, 7, 3, 5, 2, 9, 1, 6, 4],
            [5, 2, 9, 4, 6, 1, 7, 8, 3],
            [6, 4, 1, 7, 3, 8, 2, 9, 5],
            [2, 8, 6, 1, 7, 5, 3, 4, 9],
            [9, 5, 7, 8, 4, 3, 6, 2, 1],
            [3, 1, 4, 6, 9, 2, 8, 5, 7],
            [4, 6, 5, 3, 8, 7, 9, 1, 2],
            [1, 3, 2, 9, 5, 6, 4, 7, 8],
            [7, 9, 8, 2, 1, 4, 5, 3, 6]]
####################################
mapa4=[
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]

solvemapa4=[[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]
########################################
mapa5=[
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]]

solvemapa5=[[7, 8, 5, 4, 3, 9, 1, 2, 6],
            [6, 1, 2, 8, 7, 5, 3, 4, 9],
            [4, 9, 3, 6, 2, 1, 5, 7, 8],
            [8, 5, 7, 9, 4, 3, 2, 6, 1],
            [2, 6, 1, 7, 5, 8, 9, 3, 4],
            [9, 3, 4, 1, 6, 2, 7, 8, 5],
            [5, 7, 8, 3, 9, 4, 6, 1, 2],
            [1, 2, 6, 5, 8, 7, 4, 9, 3],
            [3, 4, 9, 2, 1, 6, 8, 5, 7]]
##########################################
mapa6=[[5, 1, 7, 6, 0, 0, 0, 3, 4],
       [2, 8, 9, 0, 0, 4, 0, 0, 0],
       [3, 4, 6, 2, 0, 5, 0, 9, 0],
       [6, 0, 2, 0, 0, 0, 0, 1, 0],
       [0, 3, 8, 0, 0, 6, 0, 4, 7],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 9, 0, 0, 0, 0, 0, 7, 8],
       [7, 0, 3, 4, 0, 0, 5, 6, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]]

solvemapa6=[[5, 1, 7, 6, 9, 8, 2, 3, 4],
            [2, 8, 9, 1, 3, 4, 7, 5, 6],
            [3, 4, 6, 2, 7, 5, 8, 9, 1],
            [6, 7, 2, 8, 4, 9, 3, 1, 5],
            [1, 3, 8, 5, 2, 6, 9, 4, 7],
            [9, 5, 4, 7, 1, 3, 6, 8, 2],
            [4, 9, 5, 3, 6, 2, 1, 7, 8],
            [7, 2, 3, 4, 8, 1, 5, 6, 9],
            [8, 6, 1, 9, 5, 7, 4, 2, 3]]
########################################
mapa7=[[0, 1, 4, 0, 0, 7, 0, 0, 8],
       [0, 0, 0, 0, 0, 0, 0, 5, 0],
       [0, 0, 0, 9, 0, 2, 0, 0, 1],
       [9, 4, 5, 0, 0, 0, 8, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 4, 3],
       [0, 0, 7, 0, 0, 0, 2, 9, 5],
       [7, 0, 0, 5, 0, 6, 0, 0, 0],
       [0, 8, 0, 0, 0, 0, 0, 0, 0],
       [4, 0, 0, 7, 0, 0, 3, 2, 0]]

solvemapa7=[[2, 1, 4, 6, 5, 7, 9, 3, 8],
            [6, 9, 8, 3, 4, 1, 7, 5, 2],
            [5, 7, 3, 9, 8, 2, 6, 4, 1],
            [9, 4, 5, 2, 7, 3, 8, 1, 6],
            [1, 6, 2, 8, 9, 5, 4, 7, 3],
            [8, 3, 7, 1, 6, 4, 2, 9, 5],
            [7, 2, 9, 5, 3, 6, 1, 8, 4],
            [3, 8, 1, 4, 2, 9, 5, 6, 7],
            [4, 5, 6, 7, 1, 8, 3, 2, 9]]
##########################################
mapa8=[
       [0, 9, 0, 0, 7, 0, 0, 1, 0],
       [0, 7, 0, 3, 0, 6, 0, 0, 0],
       [0, 5, 0, 0, 4, 0, 0, 0, 0],
       [6, 8, 0, 0, 0, 1, 0, 0, 4],
       [0, 4, 2, 0, 0, 0, 7, 9, 0],
       [5, 0, 7, 2, 0, 0, 0, 6, 1],
       [0, 0, 0, 0, 3, 0, 0, 8, 0],
       [0, 0, 0, 8, 0, 9, 0, 5, 0],
       [0, 1, 0, 0, 2, 0, 0, 7, 0]]

solvemapa8=[[4, 9, 6, 5, 7, 2, 3, 1, 8],
            [2, 7, 8, 3, 1, 6, 5, 4, 9],
            [3, 5, 1, 9, 4, 8, 6, 2, 7],
            [6, 8, 9, 7, 5, 1, 2, 3, 4],
            [1, 4, 2, 6, 8, 3, 7, 9, 5],
            [5, 3, 7, 2, 9, 4, 8, 6, 1],
            [9, 6, 5, 1, 3, 7, 4, 8, 2],
            [7, 2, 4, 8, 6, 9, 1, 5, 3],
            [8, 1, 3, 4, 2, 5, 9, 7, 6]]
##########################################
mapa9=[  #pre dfsko
            [0, 5, 1, 3, 9, 6, 8, 2, 7],
            [2, 3, 8, 5, 4, 7, 9, 6, 1],
            [9, 0, 7, 1, 8, 2, 3, 4, 5],
            [3, 7, 2, 4, 1, 8, 6, 5, 9],
            [5, 8, 6, 9, 7, 3, 2, 1, 4],
            [1, 4, 9, 6, 2, 5, 7, 3, 8],
            [8, 9, 3, 2, 5, 4, 1, 7, 6],
            [6, 1, 5, 7, 3, 9, 4, 8, 2],
            [7, 2, 4, 0, 6, 1, 5, 9, 3]]

solvemapa9=[[4, 5, 1, 3, 9, 6, 8, 2, 7],
            [2, 3, 8, 5, 4, 7, 9, 6, 1],
            [9, 6, 7, 1, 8, 2, 3, 4, 5],
            [3, 7, 2, 4, 1, 8, 6, 5, 9],
            [5, 8, 6, 9, 7, 3, 2, 1, 4],
            [1, 4, 9, 6, 2, 5, 7, 3, 8],
            [8, 9, 3, 2, 5, 4, 1, 7, 6],
            [6, 1, 5, 7, 3, 9, 4, 8, 2],
            [7, 2, 4, 8, 6, 1, 5, 9, 3]]
##########################################
mapa10=[
       [0, 0, 0, 0, 8, 0, 4, 0, 0],
       [8, 0, 0, 0, 5, 6, 0, 9, 0],
       [3, 5, 0, 4, 0, 0, 0, 0, 2],
       [0, 0, 0, 0, 0, 9, 0, 3, 0],
       [9, 6, 0, 0, 0, 0, 0, 5, 1],
       [0, 2, 0, 8, 0, 0, 0, 0, 0],
       [7, 0, 0, 0, 0, 2, 0, 8, 9],
       [0, 8, 0, 9, 4, 0, 0, 0, 6],
       [0, 0, 6, 0, 3, 0, 0, 0, 0]]

solvemapa10=[[6, 1, 9, 2, 8, 3, 4, 7, 5],
            [8, 4, 2, 7, 5, 6, 1, 9, 3],
            [3, 5, 7, 4, 9, 1, 8, 6, 2],
            [4, 7, 5, 1, 2, 9, 6, 3, 8],
            [9, 6, 8, 3, 7, 4, 2, 5, 1],
            [1, 2, 3, 8, 6, 5, 9, 4, 7],
            [7, 3, 4, 6, 1, 2, 5, 8, 9],
            [5, 8, 1, 9, 4, 7, 3, 2, 6],
            [2, 9, 6, 5, 3, 8, 7, 1, 4]]


completed = deepcopy(solvemapa1)





def pozadie(defaultplocha):
    screen.fill(pygame.Color("White"))
    for i in range (9):
        for j in range (9):
            if defaultplocha[i][j] != 0:
                pygame.draw.rect(screen, pygame.Color((246, 229, 141)),pygame.Rect((j) * 80 + 17, (i) * 80 + 17, 78, 78))

    if Poziciax >= 0:
        pygame.draw.rect(screen, pygame.Color((85, 239, 196)),pygame.Rect((Poziciax - 1) * 80 + 17, (Poziciay - 1) * 80 + 17, 78, 78))
    pygame.draw.rect(screen, pygame.Color("black"), pygame.Rect(15, 15, 720, 720), 8)
    mouse = pygame.mouse.get_pos()


    if 800 + 100 > mouse[0] > 800 and 50 + 50 > mouse[1] > 50:
        pygame.draw.rect(screen, (86, 101, 115), (800, 50, 103, 53))
        pygame.draw.rect(screen, (0, 255, 0), (800, 50, 100, 50))
    else:

        pygame.draw.rect(screen, (0, 200, 0), (800, 50, 100, 50))
    DFS=font2.render("DFS", True, pygame.Color('black'))
    screen.blit(DFS, pygame.Vector2((820), (62)))


    if 800 + 100 > mouse[0] > 800 and 150 + 50 > mouse[1] > 150:
        pygame.draw.rect(screen, (86, 101, 115), (800, 150, 103, 53))
        pygame.draw.rect(screen, (0, 255, 0), (800, 150, 100, 50))
    else:
        pygame.draw.rect(screen, (0, 200, 0), (800, 150, 100, 50))
    DFS = font2.render("BCK", True, pygame.Color('black'))
    screen.blit(DFS, pygame.Vector2((820), (162)))

    if 800 + 100 > mouse[0] > 800 and 250 + 50 > mouse[1] > 250:
        pygame.draw.rect(screen, (86, 101, 115), (800, 250, 103, 53))
        pygame.draw.rect(screen, (0, 255, 0), (800, 250, 100, 50))
    else:
        pygame.draw.rect(screen, (0, 200, 0), (800, 250, 100, 50))
    DFS=font2.render("FF", True, pygame.Color('black'))
    screen.blit(DFS, pygame.Vector2((832), (263)))

    if 800 + 100 > mouse[0] > 800 and 350 + 50 > mouse[1] > 350:
        pygame.draw.rect(screen, (86, 101, 115), (800, 350, 103, 53))
        pygame.draw.rect(screen, (((247, 159, 31))), (800, 350, 100, 50))
    else:
        pygame.draw.rect(screen, ((238, 90, 36)), (800, 350, 100, 50))
    DFS = font2.render("Reset", True, pygame.Color('black'))
    screen.blit(DFS, pygame.Vector2((813), (362)))

    if 800 + 100 > mouse[0] > 800 and 550 + 50 > mouse[1] > 550:
        pygame.draw.rect(screen, (86, 101, 115), (800, 550, 103, 53))
        pygame.draw.rect(screen, ((162, 155, 254)), (800, 550, 100, 50))
    else:
        pygame.draw.rect(screen, ((108, 92, 231)), (800, 550, 100, 50))
    DFS = font3.render("Generuj", True, pygame.Color('black'))
    screen.blit(DFS, pygame.Vector2((810), (564)))


    j = 1
    while (j * 80) < 720:
        line_width = 2 if j % 3 > 0 else 5
        pygame.draw.line(screen, pygame.Color("black"), pygame.Vector2((j * 80) + 15, 15),
                         pygame.Vector2((j * 80) + 15, 735), line_width)
        pygame.draw.line(screen, pygame.Color("black"), pygame.Vector2(15, (j * 80) + 15),
                         pygame.Vector2(735, (j * 80) + 15), line_width)
        j += 1



def vybermapy(mapa):
    if mapa==1:
       return mapa1
    if mapa==2:
       return mapa2
    if mapa==3:
       return mapa3
    if mapa==4:
       return mapa4
    if mapa==5:
       return mapa5
    if mapa==6:
       return mapa6
    if mapa==7:
       return mapa7
    if mapa==8:
       return mapa8
    if mapa==9:
       return mapa9
    if mapa==10:
       return mapa10



def hodinky():
    global firsttime
    text = fontcas.render('Čas' + cas(round(time.time() - firsttime)), False, (0, 0, 0))
    screen.blit(text, (750, 690))


def fadeout(plocha,width, height,defaultplocha):
    fade = pygame.Surface((width, height))
    fade.fill((0, 0, 0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        pozadie(defaultplocha)
        nakresli_cisla(plocha)
        hodinky()
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)


def nakresli_cisla(plocha):
    offset = 35
    riadok = 0
    while riadok < 9:
        stlpec = 0
        while stlpec < 9:
            vystup = plocha[riadok][stlpec]
            if vystup == 0:
                vystup = ' '
            if vystup!=0:
               cisla = font.render(str(vystup), True, pygame.Color('black'))
               screen.blit(cisla, pygame.Vector2((stlpec * 80) + offset + 5, (riadok * 80) + offset - 2))
            stlpec += 1

        riadok += 1



def novecislo(plocha,defaultplocha):
    if stlacena > 0:
        if plocha[Poziciay - 1][Poziciax - 1] == 0:
            plocha[Poziciay - 1][Poziciax - 1] = stlacena

    if stlacena == -1:

        if defaultplocha[Poziciay - 1][Poziciax - 1] == 0:
            plocha[Poziciay - 1][Poziciax - 1] = 0


def stlacene(x, y):
    global Poziciax
    global Poziciay
    if x > 15 and x < 735 and y < 735 and y > 15:
        x
        POLEX = (730 - x) / 80
        y
        POLEY = (730 - y) / 80

        Poziciax = 9 - math.floor(POLEX / 1)
        Poziciay = 9 - math.floor(POLEY / 1)

        print(POLEX, POLEY, Poziciax, Poziciay)


def cas(sekundy):
    sek = sekundy % 60
    minuta = sekundy // 60
    hodina = minuta // 60
    čas = " " + str(minuta).zfill(2) + ":" + str(sek).zfill(2)
    return čas


def bckmoznost(plocha,riadok,stlpec,cislo):
    for i in range(0,9):
        if plocha[riadok][i] == cislo:
            return False
    for j in range(0,9):
        if plocha[j][stlpec] == cislo:
            return False
    square_row = (riadok//3)*3
    square_col = (stlpec//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if plocha[square_row+i][square_col+j] == cislo:
                return False
    return True


def isWon(plocha):
    pocet0=0
    for i in range(9):
        for j in range(9):
            if plocha[i][j]==0:
                pocet0+=1
    return pocet0


def backtracking(plocha,defaultplocha):

        global pocetkrokov
        for riadky in range(9):
            for stlpce in range(9):
                if plocha[riadky][stlpce] == 0:
                    for cislo in range(1,10):
                        pocetkrokov = pocetkrokov + 1
                        if bckmoznost(plocha,riadky,stlpce,cislo):
                            plocha[riadky][stlpce] = cislo
                            pozadie(defaultplocha)
                            nakresli_cisla(plocha)
                            hodinky()
                            pygame.display.flip()
                            backtracking(plocha,defaultplocha)
                            if isWon(plocha) == 0:
                                print("vyhra")

                                print(isWon(plocha))
                            else:
                                plocha[riadky][stlpce] = 0

                    return False


def doprednakontrola(plocha, defaultplocha):
    k=[1,2,3,4,5,6,7,8,9]
    global pocetkrokov2
    l=deepcopy(k)
    for riadky in range(9):
            l=deepcopy(k)
            for kontrola in range(9):
               if defaultplocha[riadky][kontrola] != 0:
                   l.remove(plocha[riadky][kontrola])
                   print("vymazany riadok",riadky,l)
            for stlpce in range(9):
                if plocha[riadky][stlpce] == 0:
                    for cislo in l:
                        pocetkrokov2 = pocetkrokov2 + 1
                        if bckmoznost(plocha, riadky, stlpce, cislo):
                            plocha[riadky][stlpce] = cislo
                            pozadie(defaultplocha)
                            nakresli_cisla(plocha)
                            hodinky()
                            pygame.display.flip()
                            print(plocha)
                            doprednakontrola(plocha, defaultplocha)
                            if isWon(plocha) == 0:
                                print("vyhra")

                                print(isWon(plocha))
                            else:
                                plocha[riadky][stlpce] = 0
                    return False



def DFSsolveSudoku(plocha,defaultplocha):
    global pocetkrokovfs
    global prazdne
    global poleX
    global poleY
    win = False
    for j in range(9):
        for i in range(9):
            if plocha[j][i] == 0:
                prazdne = prazdne + 1
    cislo1 = 0
    poleX = array.array('i', (0 for i in range(0, prazdne)))
    poleY = array.array('i', (0 for i in range(0, prazdne)))
    k = 0

    for j in range(9):
        for i in range(9):
            if plocha[j][i] == 0:
                x = i + 1
                y = j + 1
                poleX[k] = x
                poleY[k] = y
                k = k + 1

    for j in range(prazdne):
        cislo1 = cislo1 + pow(10, j)

    while win != True:
        for i in range(prazdne):
            velkeprevodene=str(cislo1)
            x=poleX[i]
            y=poleY[i]
            plocha[y-1][x-1] = int(velkeprevodene[i])
            pozadie(defaultplocha)
            nakresli_cisla(plocha)
            hodinky()
            pygame.display.flip()
            pocetkrokovfs=pocetkrokovfs+1

        cislo1 = cislo1 + 1

        if solvemapa1 == plocha or solvemapa2 == plocha or solvemapa3 == plocha or solvemapa4 == plocha or \
           solvemapa5 == plocha or solvemapa6 == plocha or solvemapa7 == plocha or solvemapa8 == plocha or \
           solvemapa9 == plocha or solvemapa1 == plocha:
            win = True

        for event in pygame.event.get():
            hraciaplocha = deepcopy(defaultplocha)
            w, z = pygame.mouse.get_pos()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("QUIT")
                    fadeout(plocha,1000, 810, hraciaplocha)
                    pygame.quit()
                    exit(0)
            if event.type == pygame.MOUSEBUTTONUP:
                if 800 < w < 900 and 300 < z < 400:
                    # print("Klikol si RESET")
                    print(plocha)
                    for i in range(9):
                        for j in range(9):
                            plocha[i][j] = hraciaplocha[i][j]
                            if plocha==hraciaplocha:
                               win=True
                               cislo1 = 0
                               poleX = array.array('i', (0 for i in range(0, prazdne)))
                               poleY = array.array('i', (0 for i in range(0, prazdne)))
                               k = 0
                               cislo1=cislo1*0
                               print(plocha)
                               prazdne=prazdne*0
                # print(hraciaplocha)
"""
        if win == True:
            print("VYHRA")
            pygame.time.delay(200)
            screen.blit(vyhra, (0, 0))
            pygame.display.update()
            pygame.time.delay(2000)
"""

def hra():
    prvecislo=0
    mapa = random.randint(1, 10)
    prvecislo=prvecislo + mapa
    plocha=deepcopy(vybermapy(mapa))
    hraciaplocha=deepcopy(plocha)
    defaultplocha = deepcopy(plocha)
    global clicked
    global stlacena
    bezi = True
    pygame.display.set_caption("Sudoku")
    while bezi:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT")
                fadeout(plocha,1000, 810, hraciaplocha)
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONUP:
                if 800 < x < 900 and 550 < y < 600:
                   while mapa==prvecislo:
                         mapa = random.randint(1, 10)

                   prvecislo = mapa
                   plocha = deepcopy(vybermapy(mapa))
                   hraciaplocha = deepcopy(plocha)
                   defaultplocha = deepcopy(plocha)

            if event.type == pygame.MOUSEBUTTONUP:
                if 800 < x < 900 and 350 < y < 400:
                    global pocetkrokov2
                    global pocetkrokovfs
                    global pocetkrokov
                    for i in range(9):
                        for j in range(9):
                            plocha[i][j]=hraciaplocha[i][j]
                            pocetkrokov=0
                            pocetkrokovfs=0
                            pocetkrokov2=0
            if event.type == pygame.MOUSEBUTTONUP:
                if x < 750 and y < 810:
                    print(x, y)
                    stlacene(x, y)
            if event.type == pygame.MOUSEBUTTONUP:
                if 800 < x < 900 and 50 < y < 100:
                    DFSsolveSudoku(plocha,defaultplocha)
                    print("VYHRA")
                    print("Pocet krokov = ", pocetkrokovfs)
                    
            if event.type == pygame.MOUSEBUTTONUP:
                if 800 < x < 900 and 150 < y < 200:
                    backtracking(plocha,defaultplocha)
                    print("VYHRA")
                    print("Pocet krokov = ",pocetkrokov)

            if event.type == pygame.MOUSEBUTTONUP:
                if 800 < x < 900 and 250 < y < 300:
                    doprednakontrola(plocha,defaultplocha)
                    print("VYHRA")
                    print("Pocet krokov = ", pocetkrokov2)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("QUIT")
                    fadeout(plocha,1000, 810)
                    pygame.quit()
                    exit(0)
                if event.key == pygame.K_1:
                    stlacena = 1
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_KP_1:
                    stlacena = 1
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_2:
                    stlacena = 2
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_KP_2:
                    stlacena = 2
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_3:
                    stlacena = 3
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_KP_3:
                    stlacena = 3
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_4:
                    stlacena = 4
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_KP_4:
                    stlacena = 4
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_5:
                    stlacena = 5
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_KP_5:
                    stlacena = 5
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_6:
                    stlacena = 6
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_KP_6:
                    stlacena = 6
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_7:
                    stlacena = 7
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_KP_7:
                    stlacena = 7
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_8:
                    stlacena = 8
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_KP_8:
                    stlacena = 8
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_9:
                    stlacena = 9
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_KP_9:
                    stlacena = 9
                    novecislo(plocha,defaultplocha)
                    print(stlacena)
                if event.key == pygame.K_BACKSPACE:
                    stlacena = -1
                    novecislo(plocha,defaultplocha)
                    print(stlacena)

        pozadie(defaultplocha)
        nakresli_cisla(plocha)
        hodinky()
        pygame.display.flip()

hra()
pygame.quit()
sys.exit()
