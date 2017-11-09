import pygame
from Enemigo import *
pygame.init()
pygame.display.set_mode((800,600))

#creo y ubico los enemigos

###enemigo = Enemigo(tipo,posx,posy)
### tipos: Enemigo 1, Enemigo 2, Mini Jefe, Jefe
# HACER 14 ENEMIGOS
enemigo1 = Enemigo("Enemigo 1",2809,1300)
enemigo2 = Enemigo("Enemigo 2",2773,1051)
enemigo3 = Enemigo("Enemigo 1",2696,870)
enemigo4 = Enemigo("Enemigo 2",2671,1296)
enemigo5 = Enemigo("Enemigo 1",2487,870)
enemigo6 = Enemigo("Enemigo 1",2506,1038)
enemigo7 = Enemigo("Enemigo 2",2537,1374)
enemigo8 = Enemigo("Enemigo 2",2352,1215)
enemigo9 = Enemigo("Enemigo 1",2257,1100)
enemigo10 = Enemigo("Enemigo 2",1938,1337)
enemigo11 = Enemigo("Enemigo 1",1490,1040)
enemigo12 = Enemigo("Enemigo 2",1463,1275)
enemigo13 = Enemigo("Enemigo 1",1158,1311)
enemigo14 = Enemigo("Enemigo 2",1219,935)

###pared = pygame.Rect(left,top,alto,ancho)

listaEnemigosHielo = [enemigo1,enemigo2,enemigo3,enemigo4,enemigo5,enemigo6,enemigo7,enemigo8,enemigo9,enemigo10,enemigo11,enemigo12,enemigo13,enemigo14]

listaWallsHielo = []

fondoHielo = pygame.image.load("MapaHieloFinal.png")            