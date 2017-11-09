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


class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x,y):  
        self.imagen=imagen1
        self.imagennormal=imagen1
        self.imagenseleccion=imagen2
        self.rect= imagen1.get_rect()
        self.rect.left=x
        self.rect.top=y
        
    def setImage(self,imagen):
        self.imagen=imagen
    def pintar(self,surface,cursor):
        
        if cursor.colliderect(self.rect): 
            self.setImage(self.imagenseleccion)
            
        else:
            self.setImage(self.imagennormal)
        surface.blit(self.imagen,(self.rect.left,self.rect.top))  
        
        
class cursor(pygame.Rect):
    def __init__(self):
        (self.x,self.y)=pygame.mouse.get_pos()
        pygame.Rect.__init__(self,self.x,self.y,0,0)
    def updatecursor(self):
        (self.left,self.top)=pygame.mouse.get_pos()



def moverCosasPantalla(personaje,fondo,pantalla,vx,vy,t,suceso,listaFlechas,listaWalls,listaEnemigos,informacion):
    if personaje.esta_furiozo:
        vx = vx*1.5
        vy = vy*1.5
    fondo.update(pantalla,vx,vy,personaje)
    vx_enemigo = vx
    vy_enemigo = vy
    colision=False
    for wall in listaWalls:
            if personaje.moviendo:
                wall.move_ip(-vx,-vy)
    for wall in listaWalls:
            if wall.colliderect(personaje.rect):
                if wall == puertaHielo and t.estaNivelInicial == True:
                    t.nivelHielo = True
                if wall == puertaJefeFinal and t.estaNivelHielo == True:
                    t.nivelJefeFinal = True
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
fondo = Fondo(pygame.image.load("Mapa1Final.png"),0,0)

def main(cargar=False):
    
    validaciongameover=False
    import pygame
    suceso = "no atacando"
    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    salir=False
    reloj = pygame.time.Clock()
    gameover=pygame.image.load("GameOver.png")
    personaje = Personaje.Personaje()
#     listaWalls = []
#     listaEnemigos = []
#     for wall in listaWalls:
#         listaWalls.remove(wall)
#     for enemigo in listaEnemigos:
#         listaEnemigos.remove(enemigo)
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
    pygame.mixer.music.load("Sonidos/bosque.mid")
    pygame.mixer.music.play(20)
    pygame.mixer.music.set_volume(0.15)
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
                    
        t.segundos = pygame.time.get_ticks()/1000
        pantalla.fill((0,0,170))
        t.update_times()
        if t.gameover == True:
            pygame.mixer.music.stop()
            pantalla.blit(gameover,(0,0))
            if (validaciongameover == False):
                gameoversonido.play()
                validaciongameover= True
                
            
        else:
            moverCosasPantalla(personaje,fondo,pantalla,vx,vy,t,suceso,listaFlechas,listaWalls,listaEnemigos,informacion)
            if t.nivelHielo == True:
                pygame.mixer.stop()
                pygame.mixer.music.load("Sonidos/nieve.mid")
                pygame.mixer.music.play(20)
                pygame.mixer.music.set_volume(0.3)
                t.estaNivelHielo = True
                t.nivelHielo = False
                listaWalls = listaWallsHielo
                listaEnemigos = listaEnemigosHielo
                fondo = Fondo(fondoHielo,0,0)
                personaje.rect.left,personaje.rect.top = (350,250)
            if t.nivelJefeFinal == True:
                pygame.mixer.music.load("Sonidos/peleaboss.mp3")
                pygame.mixer.music.play(20)
                pygame.mixer.music.set_volume(0.4)
                t.estaNivelJefeFinal = True
                t.nivelJefeFinal = False
                listaWalls = listaWallsJefeFinal
                listaEnemigos = listaEnemigosJefe
                fondo = Fondo(fondoJefeFinal,0,0)
                personaje.rect.left,personaje.rect.top = (350,250)
    
                
        pygame.display.update()
    pygame.quit()
    
def menu():
    import pygame
    pygame.init()
    
    pygame.mixer.music.load("Sonidos/menu.mid")
    pantalla=pygame.display.set_mode((900,700))
    pygame.display.set_caption("Vengeance")
    relojmenu = pygame.time.Clock()
    titulo=pygame.image.load("Vengeance/Titulo.png").convert_alpha()
    descripcion=pygame.image.load("Vengeance/descripcion.png").convert_alpha()
    pygame.mixer.music.play(30)
    
    newgame = Boton(pygame.image.load("Vengeance/jugar1.png").convert_alpha(),
                    pygame.image.load("Vengeance/jugar2.png").convert_alpha(),280,290)
    
    controles = Boton(pygame.image.load("Vengeance/controles.png").convert_alpha(),
                     pygame.image.load("Vengeance/controles2.png").convert_alpha(),280,370) # 280 para igualar chaboncito
    
    salir = Boton(pygame.image.load("Vengeance/salir.png").convert_alpha(),
                  pygame.image.load("Vengeance/salir1.png").convert_alpha(),280,460)      #USAR ESTAS POS PARA LOS OTROS BOTONES
    
    
    fuente1=pygame.font.SysFont("Arial", 30, False, False)
    
    selec1=pygame.mixer.Sound("selec.wav")  
    
    cont=False
    
    pygame.mixer.stop()
    
    
    c1=cursor()
    loadgamebool=None
    
    
    
    #Loop Principal!
    while True:
        
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()           # RETURN NONE PARA SALIR
                return None
            if event.type==pygame.MOUSEBUTTONDOWN:
                if c1.colliderect(newgame.rect):
                    selec1.play()
                    pygame.quit()
                    return False
                elif c1.colliderect(controles.rect):
                    selec1.play()
                    cont=True
                elif c1.colliderect(salir.rect):
                    selec1.play()
                    pygame.quit()
                    return None
                
                
                
                
        pantalla.fill((0,0,0))
        relojmenu.tick(15)
        pantalla.blit(titulo,(50,-20)) #Posicion del titulo del juego
        pantalla.blit(descripcion,(170,660))  #Descripcion que va abajo de las opciones
        #TEXTOS PARA CONTROLES
        movim=fuente1.render("-Movimiento: Flechas Direccionales",0,(255,255,255))
        atack1=fuente1.render("-Ataque 1: A",0,(255,255,255))
        atack2=fuente1.render("-Ataque 2: D",0,(255,255,255))
        atack3=fuente1.render("-Ataque 3: F",0,(255,255,255))
        paus= fuente1.render("-Pulsa P para pausar el juego",0,(255,255,255))
        newgame.pintar(pantalla, c1)
        if cont==False:
            controles.pintar(pantalla, c1)
        salir.pintar(pantalla,c1)
        
        c1.updatecursor()
        
        if cont==True:
            pantalla.blit(movim,(230,310))
            pantalla.blit(atack1,(230,350))
            pantalla.blit(atack2,(230,390))
            pantalla.blit(atack3,(230,430))
            pantalla.blit(paus,(230,470))
        
            
    
        
        pygame.display.update()
                    
    
#FUNCION START QUE CONTROLA LOS PASOS DE PANTALLA
        
        
def start(loadbool=None):
    if loadbool==None:
        loadbool=menu()
    if not(loadbool==None):
        a=main(loadbool)
        if a==True:
            start(True)
            
            

def pausa(pantalla,estaPausado):
    import pygame
    fondopausa = pygame.image.load("Vengeance/menupausa.png")
    while estaPausado == True:
        pantalla.blit(fondopausa,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        estaPausado=False
        pygame.display.update()            
    return                
        
     
    
def nivelInicial(listaWalls,listaEnemigos,fondo):
    listaWalls = listaWallsInicial
    listaEnemigos = listaEnemigosInicial
    fondo = Fondo(fondoInicial,0,0)
    
def nivelJefeFinal(listaWalls,listaEnemigos,fondo):
    listaWalls = []
    listaEnemigos = []
    fondo = Fondo(fondoJefeFinal,0,0)
    
# def nivelHielo(personaje):
#     validaciongameover=False
#     import pygame
#     suceso = "no atacando"
#     pygame.init()
#     pantalla=pygame.display.set_mode((800,600))
#     salir=False
#     reloj = pygame.time.Clock()
#     gameover=pygame.image.load("GameOver.png")
#     personaje = Personaje.Personaje()
#     
#     listaWalls = listaWallsHielo
#     listaEnemigos = listaEnemigosHielo
#     fondo = Fondo(fondoHielo,0,0)
#     
# #     listaWalls = listaWallsHielo
# #     listaEnemigos = listaEnemigosHielo
# #     fondo = Fondo(fondoHielo,0,0)
# 
# #     listaWalls = listaWallsJefeFinal
# #     listaEnemigos = listaEnemigosJefe
# #     fondo = Fondo(fondoJefeFinal,0,0)
#     
#     informacion = Informacion()
# 
#     vx,vy=0,0
#     t = Times()
#     
#     leftsigueapretada,rightsigueapretada,downsigueapretada,upsigueapretada= False,False,False,False
#     
#     pantalla.blit(personaje.imagen,personaje.rect)
#     pygame.mixer.music.load("Sonidos/bosque.mid")
#     pygame.mixer.music.play()
#     pygame.mixer.music.set_volume(0.15)
#     while salir!=True:#LOOP PRINCIPAL
#         reloj.tick(28)
#         suceso = "no atacando"
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 salir=True
#             else:                                                                                    
#                 if event.type == pygame.KEYDOWN:
#                     
#                     if event.key == pygame.K_ESCAPE:
#                         return False
#                     if event.key == pygame.K_LEFT:
#                         leftsigueapretada = True
#                         vx = -personaje.velocidad
#                     if event.key == pygame.K_RIGHT:
#                         rightsigueapretada = True
#                         vx = personaje.velocidad
#                     if event.key == pygame.K_UP:
#                         upsigueapretada = True
#                         vy = -personaje.velocidad
#                     if event.key == pygame.K_DOWN:
#                         downsigueapretada = True
#                         vy = personaje.velocidad
#                     
#                     if event.key == pygame.K_a:
#                         suceso = "espadazo"
# 
#                     if event.key == pygame.K_s:
#                         suceso = "flechazo"
#                         
#                     if event.key == pygame.K_d:
#                         suceso = "poder"
#                     
#                     if event.key == pygame.K_f:
#                         suceso = "furia"
#                     
#                         
#                 if event.type == pygame.KEYUP:
#                     if event.key == pygame.K_LEFT:
#                         leftsigueapretada = False
#                         if rightsigueapretada: 
#                             vx = personaje.velocidad
#                         else:
#                             vx = 0
#                     if event.key == pygame.K_RIGHT:
#                         rightsigueapretada = False
#                         if leftsigueapretada:
#                             vx = -personaje.velocidad
#                         else:
#                             vx = 0
#                     if event.key == pygame.K_UP:
#                         upsigueapretada = False
#                         if downsigueapretada:
#                             vy = personaje.velocidad
#                         else:
#                             vy = 0
#                     if event.key == pygame.K_DOWN:
#                         downsigueapretada = False
#                         if upsigueapretada:
#                             vy = -personaje.velocidad
#                         else:
#                             vy = 0          
#                     
#     
#         pantalla.fill((0,0,170))
#         t.update_times()
#         if t.gameover == True:
#             pygame.mixer.music.stop()
#             if(validaciongameover==False):
#                 gameoversonido.play()
#                 validaciongameover=True
#             pantalla.blit(gameover,(0,0))
#         else:
#             moverCosasPantalla(personaje,fondo,pantalla,vx,vy,t,suceso,listaFlechas,listaWalls,listaEnemigos,informacion)
#             if t.nivelInicial == True:
#                 t.nivelInicial = False
#                 t.estaNivelHielo = False
#                 t.estaNivelInicial = True
#                 main()
#     
#                 
#         pygame.display.update()
#     pygame.quit()


    
start()