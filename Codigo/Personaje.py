import pygame
from Flecha import *
from imagenes import *
from ImagenesMob import *
from Sonidos import *
from Enemigo import *
from Times import *
from Fondo import *
from __builtin__ import False


class Personaje(pygame.sprite.Sprite):
    def __init__(self):

        self.imagenes = ListaAnimacionesProtagonista
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
        self.esta_furiozo = False
        self.seg_aux = 0
        
        #inventario
        self.oro = 0
        self.potas = 0

        #stats
        self.hp = 500
        self.hpMax = 500
        self.exp = 0
        self.expParaSubir = 100
        self.velocidad = 7
        self.danio = 10
        self.lvl = 1
        self.kills = 0
        self.killsToFuria = 5

    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
        
    def terminoAnimar(self):
        return (self.estaVivo and self.movimiento == 1) or self.movimiento == 0 or self.imagen_actual == len(self.animacion)-1
    
    def animar(self):
        self.imagen_actual += 1
        if self.imagen_actual >= len(self.animacion):
            self.imagen_actual = 0
        self.imagen = self.animacion[self.imagen_actual]
    def update(self, superficie, t, subioLvl, suceso, vx, vy, listaFlechas,colision):
        
        if self.hp > self.hpMax:
            self.hp = self.hpMax
        
        if self.exp >= self.expParaSubir:
            self.subirLvl()
            
        if self.hp <= 0:
            self.estaVivo = False
            t.gameover = True
        
        if colision == False:
            if vx < 0:
                self.orientacion = 0
            if vx > 0:
                self.orientacion = 1
        
        if self.terminoAnimar():
            if self.movimiento != 1:
                self.imagen_actual = 0
            
            if self.estaVivo == False:
                self.movimiento = 5
            else:
                if vx == 0 and vy == 0 and self.movimiento != 4:
                    self.movimiento = 0
                else:
                    self.movimiento = 1
                    self.moviendo = True
                
                if suceso == "espadazo":
                    self.movimiento = 2
                    ataquesonido.play()
                    ataquesonido.set_volume(0.2)
                
                if suceso == "flechazo":
                    self.movimiento = 4
                    flecha = Flecha(self,"flecha")
                    listaFlechas.append(flecha)
                    flechasonido.play()
                    flechasonido.set_volume(0.14)
                
                if suceso == "poder":
                    if self.puedeTirarPoder(listaFlechas):
                        self.movimiento = 3
                        flecha = Flecha(self,"poder")
                        listaFlechas.append(flecha)
                        podersonido.play()
                
                if suceso == "furia" and self.kills >= self.killsToFuria:
                    furiasonido.set_volume(0.4)
                    furiasonido.play()
                    self.esta_furiozo = True
                    self.kills = 0
                    self.danio = self.danio * 2
                    self.seg_aux = t.segundos
                    
                if t.segundos - self.seg_aux >= 5 and self.esta_furiozo == True:
                    self.esta_furiozo = False
                    self.danio = self.danio / 2
                    
                if self.movimiento != 1:
                    self.moviendo = False
            
        self.animacion = self.imagenes[self.orientacion][self.movimiento]
        
        if t.t == 1:
            self.animar()
            
        ## Ubicar al personaje en el medio de la pantalla

        superficie.blit(self.imagen,self.rect)
    
    def puedeTirarPoder(self,listaFlechas):
        for proyectil in listaFlechas:
            if proyectil.tipo == "poder":
                return False
        return True
    
    def subirLvl(self):
        self.lvl += 1
        self.exp -= self.expParaSubir 
        self.expParaSubir += self.expParaSubir/4
        levelupsonido.play()
        self.danio += self.danio/4
        self.hpMax += self.hpMax/4
        self.hp = self.hpMax




    

