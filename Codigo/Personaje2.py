import pygame
from Flecha import *
from imagenes import *
from ImagenesMob import *
from sonido import *
from Enemigo import *
from __builtin__ import True

        
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
        
        
class Personaje(pygame.sprite.Sprite):
    def __init__(self,imagenes):
        self.imagenes = imagenes
        self.animacion = self.imagenes[0][0]
        self.imagen = self.animacion[0]
        self.rect = self.imagen.get_rect()
        self.rect.left, self.rect.top = (350,250)

        #seteo imagenes
        self.orientacion = 1
        self.movimiento = 0
        self.imagen_actual = 0

        #estados
        self.accion = "no atacando"
        self.estaVivo = True
        self.moviendo = False
        self.atacando = False
        self.vivo = True
        self.subioLvl = False
        self.tienePotas = True

        #inventario
        self.oro = 0
        self.potas = 0

        #stats
        self.hp = 100
        self.hpMax = 100
        self.exp = 0
        self.expParaSubir = 100
        self.velocidad = 5
        self.danio = 5
        self.lvl = 1

    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
        
    def terminoAnimar(self):
        return self.movimiento == 1 or self.movimiento == 0 or self.imagen_actual == len(self.animacion)-1
    
    def animar(self):
        self.imagen_actual += 1
        if self.imagen_actual >= len(self.animacion):
            self.imagen_actual = 0
        self.imagen = self.animacion[self.imagen_actual]
    def update(self, superficie, t, subioLvl, suceso, vx, vy, listaFlechas):
        
        if self.hp <= 0:
            self.estaVivo = False
    
        if vx < 0:
            self.orientacion = 0
        if vx > 0:
            self.orientacion = 1
            
        if self.terminoAnimar():
            if vx == 0 and vy == 0:
                self.movimiento = 0
            else:
                self.movimiento = 1
                self.moviendo = True
            
            if suceso == "espadazo":
                self.movimiento = 2
            
            if suceso == "flechazo":
                self.movimiento = 4
                flecha = Flecha(self)
                listaFlechas.append(flecha)
            
            if suceso == "poder":
                self.movimiento = 3
            
            if self.movimiento != 1:
                self.moviendo = False
            
        self.animacion = self.imagenes[self.orientacion][self.movimiento]
        
        if t.t == 1:
            self.animar()
            
        ## Ubicar al personaje en el medio de la pantalla

        superficie.blit(self.imagen,self.rect)
        
    def subirLvl(self, superficie, subioLvl, t):
        self.subioLvl = True
        self.lvl += 1
        t.tde8 = 0
        self.exp -= self.expParaSubir 
        self.expParaSubir += self.expParaSubir/4
        ##subirLvl.play()
        self.danio += self.danio/4
        self.hpMax += self.hpMax/4

    def usarPota(self):
        if self.potas > 0:
            ##usarPota.play()
            self.potas -= 1
            curacion = self.hpmax / 4
            self.hp += curacion
            usarPota.play()
            if self.hp > self.hpMax:
                self.hp = self.hpMax
                
                
                
class Fondo(pygame.sprite.Sprite):
    def __init__(self,imagen,x=-250,y=-1370):
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(x,y)
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
    def update(self,superficie,vx,vy,personaje):
        if personaje.moviendo:
            self.mover(-vx, -vy)
        superficie.blit(self.imagen,self.rect)  
              
class Cursor(pygame.Rect):
    def __init__(self):
        (self.x,self.y)=pygame.mouse.get_pos()
        pygame.Rect.__init__(self,self.x,self.y,0,0)
    def updatecursor(self):
        (self.left,self.top)=pygame.mouse.get_pos()

class Times(object):
    def __init__(self):
        self.t=0
        self.tde2=0
        self.tde4=0
        self.tde8=0
        self.tde40=0
        self.trespawn=[]
        self.gameover=False
        self.tiempoanterior=0
    def update_times(self):
        self.t+=1
        self.tde2+=1
        self.tde4+=1
        self.tde8+=1
        self.tde40+=1
        if self.t>1: self.t=0
        if self.tde2>2: self.tde2=0
        if self.tde4>4: self.tde4=0
        if self.tde8>8: self.tde8=0
        if self.tde40>140: self.tde40=0
        for respawntimes in self.trespawn:
            respawntimes.update()

def moverCosasPantalla(personaje,fondo,pantalla,vx,vy,t,suceso,listaFlechas,listaWalls,listaEnemigos):
    fondo.update(pantalla,vx,vy,personaje)
    colision=False
    for wall in listaWalls:
            if personaje.moviendo:
                wall.move_ip(-vx,-vy)
    for wall in listaWalls:
            if wall.colliderect(personaje.rect):
                vx,vy=-vx,-vy
                colision=True
                break    
    if colision==True:
        fondo.update(pantalla,vx,vy,personaje)
        for wall in listaWalls:
            wall.move_ip(-vx,-vy)
    for enemigo in listaEnemigos:
        enemigo.update(pantalla, t, listaEnemigos, personaje, vx, vy, listaFlechas)
    personaje.update(pantalla, t, False, suceso, vx, vy, listaFlechas)
    for flecha in listaFlechas:
        flecha.update(pantalla,listaFlechas,personaje,vx,vy,t)
    



def main(cargar=False):
    import pygame
    suceso = "no atacando"
    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    salir=False
    reloj = pygame.time.Clock()
    fondo = Fondo(pygame.image.load("Mapa1Final.png"),0,-0)
    pygame.mixer.music.load("Sonidos/bosque.mid")
    pygame.mixer.music.play(300)
    pygame.mixer.music.set_volume(0.15)
    cursor = Cursor()
    listaFlechas = []
    listaWalls=[]
    listaWalls=[pygame.Rect(255,290,3,1200),pygame.Rect(256,1533,833,3),
                pygame.Rect(1090,1344,3,200),pygame.Rect(1087,833,3,325),
                pygame.Rect(1088,288,3,360),pygame.Rect(269,244,818,3),
                pygame.Rect(302,332,116,430),pygame.Rect(432,332,43,60),
                pygame.Rect(292,836,188,170),pygame.Rect(305,1100,114,80),
                pygame.Rect(370,1220,26,80),pygame.Rect(299,1389,122,80),
                pygame.Rect(495,1396,80,95),pygame.Rect(578,293,190,160),
                pygame.Rect(873,332,182,60),pygame.Rect(865,875,190,289),
                pygame.Rect(938,1387,119,60),pygame.Rect(1056,1346,219,3),
                pygame.Rect(1056,1150,221,3),pygame.Rect(1088,832,191,3),
                pygame.Rect(1088,640,192,3)]
    personaje=Personaje(ListaAnimacionesProtagonista)
    enemigo1 = Enemigo("mob1", ListaAnimacionesMob1, 100, 100, 0, 100, 50, 3, 3, 30)
    listaEnemigos = [enemigo1]
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
                        ataquesonido.play()
                        ataquesonido.set_volume(0.2)
                        
                        
                    if event.key == pygame.K_s:
                        suceso = "flechazo"
                        flechasonido.play()
                        flechasonido.set_volume(0.14)
                        
                    if event.key == pygame.K_d:
                        suceso = "poder"
                        podersonido.play()
                        
                    if event.key == pygame.K_q:
                        personaje.usarPota()
                    
                        
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
        moverCosasPantalla(personaje,fondo,pantalla,vx,vy,t,suceso,listaFlechas,listaWalls,listaEnemigos)
        cursor.updatecursor()  
        pygame.display.update()
        print 
    pygame.quit()
    
def menu():
    import pygame
    pygame.init()
    
    pygame.mixer.music.load("Sonidos/menu.mid")
    pygame.mixer.music.set_volume(0.24)
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
    
    
    c1=Cursor()
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
        
start()

