import pygame
from Flecha import *
from imagenes import *
from __builtin__ import True
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

def moverCosasPantalla(personaje,fondo,pantalla,vx,vy,t,suceso,listaFlechas,listaWalls):
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
    personaje.update(pantalla, t, False, suceso, vx, vy,listaFlechas)
    for flecha in listaFlechas:
        flecha.update(pantalla,listaFlechas,personaje,vx,vy,t)
    

def main():
    import pygame
    suceso = "no atacando"
    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    salir=False
    reloj = pygame.time.Clock()
    fondo = Fondo(pygame.image.load("Mapa1Final.png"),0,0)
    cursor = Cursor()
    listaFlechas = []
    listaWalls=[]
    listaWalls=[pygame.Rect(255,290,3,1200)]
    personaje=Personaje(ListaAnimacionesProtagonista)

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
        moverCosasPantalla(personaje,fondo,pantalla,vx,vy,t,suceso,listaFlechas,listaWalls)
        cursor.updatecursor()  
        pygame.display.update()
        print 
    pygame.quit()
    

main()
