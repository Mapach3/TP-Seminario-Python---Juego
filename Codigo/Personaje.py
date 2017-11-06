import pygame
from imagenes import *
class Personaje(pygame.sprite.Sprite):
    def __init__(self,imagenes):

        self.imagenes = imagenes
        self.animacion = self.imagenes[0][0]
        self.imagen = self.animacion[0]
        self.rect = self.imagen.get_rect()
        self.rect.height = self.rect.height / 2
        self.rect.top, self.rect.left = (0,0)

        #seteo imagenes
        self.orientacion = 0
        self.movimiento = 0
        self.imagen_actual = 0

        #estados
        self.estaVivo = True
        self.moviendo = False
        self.espadazo = False
        self.flechazo = False
        self.poder = False
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
        if vx == 0 and vy ==0:
            self.moviendo=False
        else: 
            self.moviendo=True
            if vx < 0: 
                self.orientacion = 0
            if vx > 0:
                self.orientacion = 1
        self.rect.move_ip(vx*self.velocidad,vy*self.velocidad)
    
    
    def update(self, superficie, t, subioLvl, suceso):
        if self.hp <= 0:
            self.estaVivo = False
        if t.tde8 == 8 and self.subioLvl:
            self.subioLvl = False
        if self.exp >= self.expParaSubir:
            self.subirLvl(subirLvl, t)
        if suceso == "usar pota":
            self.usarPota()
        if suceso == "espadazo":
            self.movimiento = 2
        if suceso == "poder":
            self.movimiento = 3
        if suceso == "flechazo":
            self.movimiento = 4
        if self.estaVivo == False:
            self.movimiento = 5
        if suceso == "es golpeado":
            self.movimiento = 6
        if t.t == 1 and self.moviendo == True:
            self.animar()
        superficie.blit(self.imagen,self.rect)

    def animar(self):
        self.imagen_actual += 1
        if self.imagen_actual == len(self.animacion):
            self.imagen_actual = 0
        self.imagen = self.imagenes[self.orientacion][self.movimiento][self.imagen_actual]

    def subirLvl(self, superficie, subirLvl, t):
        self.subioLvl = True
        self.lvl += 1
        t.tde8 = 0
        self.exp = 0
        self.expParaSubir += self.expParaSubir/4
        subirLvl.play()
        self.danio += self.danio/4
        self.hpMax += self.hpMax/4

    def usarPota(self):
        if self.potas > 0:
            self.potas -= 1
            curacion = self.hpmax / 4
            self.hp += curacion
            usarPota.play()
            if self.hp > self.hpmax:
                self.hp = self.hpmax
                
class Fondo(pygame.sprite.Sprite):
    def __init__(self,imagen,x=-250,y=-1370):
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(x,y)
    def mover(self,vx,vy):
        self.rect.move_ip(vx*10,vy*10)
    def update(self,superficie,vx,vy):
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
        self.tde4=0
        self.tde8=0
        self.tde40=0
        self.trespawn=[]
        self.gameover=False
        self.tiempoanterior=0
    def update_times(self):
        self.t+=1
        self.tde4+=1
        self.tde8+=1
        self.tde40+=1
        if self.t>1: self.t=0
        if self.tde4>4: self.tde4=0
        if self.tde8>8: self.tde8=0
        if self.tde40>140: self.tde40=0
        for respawntimes in self.trespawn:
            respawntimes.update()

def moverCosasPantalla(personaje,fondo,pantalla,vx,vy,t,suceso):
    fondo.update(pantalla,vx,vy)
    personaje.update(pantalla, t, False, suceso)

def main():
    import pygame
    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    salir=False
    reloj = pygame.time.Clock()
    fondo = Fondo(pygame.image.load("C:\Users\matiste\Documents\GitHub\TP-Seminario-Python---Juego\Documentacion\Mapas Finales\MAPAS FINALES JUEGO SEMINARIO\Mapa1Final.png"))
    cursor = Cursor()

    personaje=Personaje(ListaAnimacionesProtagonista)

    vx,vy=0,0
    t = Times()
    
    leftsigueapretada,rightsigueapretada,downsigueapretada,upsigueapretada= False,False,False,False
    
    pantalla.blit(personaje.imagen,personaje.rect)
    while salir!=True:#LOOP PRINCIPAL
        reloj.tick(28)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            else:                                                                                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada = True
                        vx = -1
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada = True
                        vx = 1
                    if event.key == pygame.K_UP:
                        upsigueapretada = True
                        vy = -1
                    if event.key == pygame.K_DOWN:
                        downsigueapretada = True
                        vy = 1
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada = False
                        if rightsigueapretada: 
                            vx = 1
                        else:
                            vx = 0
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada = False
                        if leftsigueapretada:
                            vx = -1
                        else:
                            vx = 0
                    if event.key == pygame.K_UP:
                        upsigueapretada = False
                        if downsigueapretada:
                            vy = 1
                        else:
                            vy = 0
                    if event.key == pygame.K_DOWN:
                        downsigueapretada = False
                        if upsigueapretada:
                            vy = -1
                        else:
                            vy=0                    


        pantalla.fill((0,0,170))
        personaje.mover(vx, vy)
        suceso = "x"
        t.update_times()
        moverCosasPantalla(personaje,fondo,pantalla,vx,vy,t,suceso)   
        cursor.updatecursor()  
        pygame.display.update()
        
    pygame.quit()
    

main()
