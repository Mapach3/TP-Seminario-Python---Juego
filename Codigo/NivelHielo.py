import pygame
import Enemigo
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

listaWallsHielo = [pygame.Rect(317,110,3,286),pygame.Rect(315,55,138,3),
                   pygame.Rect(452,112,3,157),pygame.Rect(323,398,606,3),
                   pygame.Rect(453,203,603,3),pygame.Rect(1056,269,3.562),
                   pygame.Rect(927,400,3,1136),pygame.Rect(927,1535,2017,3),
                   pygame.Rect(2944,830,3,705),pygame.Rect(1078,765,1865,1),
                   pygame.Rect(998,771,53,1),pygame.Rect(964,1218,53,1),
                   pygame.Rect(1346,1409,29,1),pygame.Rect(1697,1023,29,1),
                   pygame.Rect(1989,1185,53,1),pygame.Rect(1829,1443,53,1),
                   pygame.Rect(2337,928,29,1),pygame.Rect(2625,928,29,1),
                   pygame.Rect(2241,1504,29,1),pygame.Rect(2593,1471,29,1),
                   pygame.Rect(2882,1377,29,1),pygame.Rect(1026,1007,62,45),
                   pygame.Rect(1347,881,62,45),pygame.Rect(1925,866,84,66),
                   pygame.Rect(1155,1358,62,45),pygame.Rect(1544,1375,84,66),
                   pygame.Rect(2019,1378,84,66),pygame.Rect(2272,1393,62,45),
                   pygame.Rect(2211,879,62,45),pygame.Rect(2533,1122,87,38),
                   pygame.Rect(1653,1076,158,133)]

#fondoHielo = pygame.image.load("MapaHieloFinal.png")            