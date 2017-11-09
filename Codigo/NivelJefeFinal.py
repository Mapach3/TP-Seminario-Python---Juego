import pygame
import Enemigo
pygame.init()
pygame.display.set_mode((800,600))

#Aca va un solo enemigo que es el Jefe Final

enemigo1 = Enemigo("Jefe",1680,713)

###pared = pygame.Rect(left,top,alto,ancho)
pared1=pygame.Rect(333,191,134,31) #PARED INICIO NIVEL HORIZONTAL
pared2=pygame.Rect(334,223,53.517) #PARED PASILLO VERTICAL IZQUIERDA
pared3=pygame.Rect(435,223,77,354) #PARED PASILLO VERTICAL DERECHA
pared4=pygame.Rect(367,709,241,32) #PARED PASILLO HORIZONTAL INFERIOR

pared5=pygame.Rect(512,321,70,252) #PARED VERTICAL IZQUIERDA SUPERIOR:
pared6=pygame.Rect(513,743,95,341) #PARED VERTICUAL IZQUIERDA INFERIOR
pared7=pygame.Rect(582,1110,1329,3)#PARED HORIZONTAL INFERIOR
pared8=pygame.Rect(1888,390,23,697)#PARED VERTICAL DERECHA
pared9=pygame.Rect(582,354,1302,3) #PARED VERTICAL DERECHA


listaEnemigosJefe = [enemigo1]

listaWallsJefeFinal = [pared1,pared2,pared3,pared4,pared5,pared6,pared7,pared8,pared9]

#fondoJefeFinal = pygame.image.load("MapaBossFinal.png")  