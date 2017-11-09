import pygame
from Personaje import *
from Times import *
from Fondo import *
from Informacion import *
from imagenes import ListaAnimacionesProtagonista
from ImagenesJefe import ListaAnimacionesJefe
from ImagenesMiniJefe import ListaAnimacionesMiniJefe
from Sonidos import *
from NivelJefeFinal import *
from EnemigosInicial import *
from NivelHielo import *

def moverCosasPantalla(personaje,fondo,pantalla,vx,vy,t,suceso,listaFlechas,listaWalls,listaEnemigos,informacion):
    if personaje.esta_furiozo:
        vx = vx*3
        vy = vy*3
    fondo.update(pantalla,vx,vy,personaje)
    vx_enemigo = vx
    vy_enemigo = vy
    colision=False
    for wall in listaWalls:
            if personaje.moviendo:
                wall.move_ip(-vx,-vy)
    for wall in listaWalls:
            if wall.colliderect(personaje.rect):
                if wall.height == 95 and wall.width == 31 and t.puertaAbierta:
                    nivelHielo(listaWalls, listaEnemigos, fondo)
                else:
                    vx,vy=-vx,-vy
                colision=True
                break
            

    if colision==True:
        fondo.update(pantalla,vx,vy,personaje)
        for wall in listaWalls:
            wall.move_ip(-vx,-vy)
        vx_enemigo = 0
        vy_enemigo = 0
    for enemigo in listaEnemigos:
        enemigo.update(pantalla, t, listaEnemigos, personaje, vx_enemigo, vy_enemigo, listaFlechas, colision,listaWalls)

    personaje.update(pantalla, t, False, suceso, vx, vy,listaFlechas,colision)
    for flecha in listaFlechas:
        flecha.update(pantalla,listaFlechas,personaje,vx,vy,t)     
    
    informacion.update(pantalla,personaje)
listaFlechas = []
listaWalls=[]
listaEnemigos=[]
fondo = Fondo(pygame.image.load("Mapa1Final.png"),0,-0)
def main():
    import pygame
    suceso = "no atacando"
    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    salir=False
    reloj = pygame.time.Clock()
    gameover=pygame.image.load("GameOver.png")
    personaje = Personaje.Personaje()
    
    listaWalls = listaWallsInicial
    listaEnemigos = listaEnemigosInicial
    fondo = Fondo(fondoInicial,0,0)

#     listaWalls = listaWallsHielo
#     listaEnemigos = listaEnemigosHielo
#     fondo = Fondo(fondoHielo,0,0)

#     listaWalls = listaWallsJefeFinal
#     listaEnemigos = listaEnemigosJefe
#     fondo = Fondo(fondoJefeFinal,0,0)
    
    informacion = Informacion()

    vx,vy=0,0
    t = Times()
    
    leftsigueapretada,rightsigueapretada,downsigueapretada,upsigueapretada= False,False,False,False
    
  
    
    pantalla.blit(personaje.imagen,personaje.rect)
    while salir!=True:#LOOP PRINCIPAL
        reloj.tick(28)
        suceso = "no atacando"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            else:                                                                                    
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_ESCAPE:
                        return False
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada = True
                        vx = -personaje.velocidad
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada = True
                        vx = personaje.velocidad
                    if event.key == pygame.K_UP:
                        upsigueapretada = True
                        vy = -personaje.velocidad
                    if event.key == pygame.K_DOWN:
                        downsigueapretada = True
                        vy = personaje.velocidad
                    
                    if event.key == pygame.K_a:
                        suceso = "espadazo"

                    if event.key == pygame.K_s:
                        suceso = "flechazo"
                        
                    if event.key == pygame.K_d:
                        suceso = "poder"
                    
                    if event.key == pygame.K_f:
                        suceso = "furia"
                    
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada = False
                        if rightsigueapretada: 
                            vx = personaje.velocidad
                        else:
                            vx = 0
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada = False
                        if leftsigueapretada:
                            vx = -personaje.velocidad
                        else:
                            vx = 0
                    if event.key == pygame.K_UP:
                        upsigueapretada = False
                        if downsigueapretada:
                            vy = personaje.velocidad
                        else:
                            vy = 0
                    if event.key == pygame.K_DOWN:
                        downsigueapretada = False
                        if upsigueapretada:
                            vy = -personaje.velocidad
                        else:
                            vy = 0          
                    
    
        pantalla.fill((0,0,170))
        t.update_times()
        if t.gameover == True:
            gameoversonido.play()
            pantalla.blit(gameover,(0,0))
        else:
            moverCosasPantalla(personaje,fondo,pantalla,vx,vy,t,suceso,listaFlechas,listaWalls,listaEnemigos,informacion)
        pygame.display.update()
    pygame.quit()
    
def nivelInicial(listaWalls,listaEnemigos,fondo):
    listaWalls = listaWallsInicial
    listaEnemigos = listaEnemigosInicial
    fondo = Fondo(fondoInicial,0,0)
    
def nivelHielo(listaWalls,listaEnemigos,fondo):
    listaWalls = listaWallsHielo
    listaEnemigos = listaEnemigosHielo
    fondo = Fondo(fondoHielo,0,0)
    
def nivelJefeFinal(listaWalls,listaEnemigos,fondo):
    listaWalls = []
    listaEnemigos = []
    fondo = Fondo(fondoJefeFinal,0,0)
    
main()