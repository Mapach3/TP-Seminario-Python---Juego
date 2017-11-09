import pygame
from Enemigo import *

pygame.init()

listaWallsInicial = [pygame.Rect(255,290,3,1200),pygame.Rect(256,1533,833,3),
            pygame.Rect(1090,1344,3,200),pygame.Rect(1087,833,3,325),
            pygame.Rect(1088,288,3,360),pygame.Rect(269,244,818,3),
            pygame.Rect(302,332,116,430),pygame.Rect(432,332,43,60),
            pygame.Rect(292,836,188,170),pygame.Rect(305,1100,114,80),
            pygame.Rect(370,1220,26,80),pygame.Rect(299,1389,122,80),
            pygame.Rect(495,1396,80,95),pygame.Rect(578,293,190,160),
            pygame.Rect(873,332,182,60),pygame.Rect(865,875,190,289),
            pygame.Rect(938,1387,119,60),pygame.Rect(1056,1346,219,3),
            pygame.Rect(1056,1150,221,3),pygame.Rect(1088,832,191,3),
            pygame.Rect(1088,640,192,3),pygame.Rect(1279,320,3,308),
            pygame.Rect(1275,275,3427,3),pygame.Rect(4703,320,3,614),
            pygame.Rect(4703,934,180,3),pygame.Rect(4895,800,32,133),
            pygame.Rect(4929,789,577,3),pygame.Rect(5506,800,29,415),
            pygame.Rect(4895,1119,33,19),pygame.Rect(4929,1184,573,30),
            pygame.Rect(4703,1119,192,3),pygame.Rect(4703,1119,3,639),
            pygame.Rect(4600,1601,95,94),pygame.Rect(1330,1596,3126,71),
            pygame.Rect(1319,1759,3096,3),pygame.Rect(1260,1406,1,354),
            pygame.Rect(1279,832,3,311),pygame.Rect(1350,360,309,55),
            pygame.Rect(1637,481,380,90),pygame.Rect(1611,619,405,68),
            pygame.Rect(1636,757,253,50),pygame.Rect(2015,370,2625,44),
            pygame.Rect(1578,1186,1079,90),pygame.Rect(1578,1276,916,104),
            pygame.Rect(2189,492,467,88),pygame.Rect(2189,580,724,70),
            pygame.Rect(2474,705,184,465),pygame.Rect(2883,963,190,637),
            pygame.Rect(2848,1311,30,1),pygame.Rect(3239,484,120,446),
            pygame.Rect(4040,584,560,180),pygame.Rect(4608,705,30,59),
            pygame.Rect(3647,734,159,150),pygame.Rect(3749,1090,252,449),
            pygame.Rect(2016,1567,30,33),pygame.Rect(4549,1794,53,1),
            pygame.Rect(4419,1924,53,1),pygame.Rect(4550,2019,53,1),
            pygame.Rect(4415,1761,3,444),pygame.Rect(4607,1761,3,444),
            pygame.Rect(4414,2208,194,3),pygame.Rect(4640,833,3,106),
            pygame.Rect(4642,1120,3,106),pygame.Rect(5408,895,96,1),
            pygame.Rect(5440,927,63,31),pygame.Rect(5439,1056,63,31),
            pygame.Rect(5408,1088,96,31),pygame.Rect(5440,960,31,95)]

enemigo1 = Enemigo("Enemigo 1",1529,556)
enemigo2 = Enemigo("Enemigo 1",1400,750)
enemigo3 = Enemigo("Enemigo 1",1700,900)
enemigo4 = Enemigo("Enemigo 1",1750,1100)
enemigo5 = Enemigo("Enemigo 1",1500,1200)
enemigo6 = Enemigo("Enemigo 1",2270,800)
enemigo7 = Enemigo("Enemigo 1",2270,900)
enemigo8 = Enemigo("Enemigo 1",2250,1100)
enemigo9 = Enemigo("Enemigo 1",2260,1200)
enemigo10 = Enemigo("Enemigo 1",2000,1500)
enemigo11 = Enemigo("Enemigo 2",2700,1450)
enemigo12 = Enemigo("Enemigo 2",3050,700)
enemigo13 = Enemigo("Enemigo 2",3240,1245)
enemigo14 = Enemigo("Enemigo 2",3100,870)
enemigo15 = Enemigo("Enemigo 2",3240,1123)
enemigo16 = Enemigo("Enemigo 2",3180,1335)
enemigo17 = Enemigo("Enemigo 2",3350,1100)
enemigo18 = Enemigo("Enemigo 2",3550,650)
enemigo19 = Enemigo("Enemigo 2",3500,800)
enemigo20 = Enemigo("Enemigo 2",3600,1000)
enemigo21 = Enemigo("Enemigo 2",4350,540)
enemigo22 = Enemigo("Enemigo 2",3900,800)
enemigo23 = Enemigo("Enemigo 2",3940,940)
enemigo24 = Enemigo("Enemigo 2",4250,900)
enemigo25 = Enemigo("Enemigo 2",4500,900)
enemigo26 = Enemigo("Enemigo 2",4270,1230)
enemigo27 = Enemigo("Enemigo 2",4200,1450)
enemigo28 = Enemigo("Enemigo 2",4500,1200)
enemigo29 = Enemigo("Enemigo 2",4600,1370)
enemigo30 = Enemigo("Enemigo 2",5300,900)
enemigo31 = Enemigo("Enemigo 1",5300,1100)

listaEnemigosInicial = [enemigo1,enemigo2,enemigo3,enemigo4,enemigo5,enemigo6,enemigo7,enemigo8,
                        enemigo9,enemigo10,enemigo11,enemigo12,enemigo13,
                        enemigo14,enemigo15,enemigo16,enemigo17,enemigo18,
                        enemigo19,enemigo20,enemigo21,enemigo22,enemigo23,
                        enemigo24,enemigo25,enemigo26,enemigo27,enemigo28,
                        enemigo29,enemigo30,enemigo31]

fondoInicial = pygame.image.load("Mapa1Final.png")