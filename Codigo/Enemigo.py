import pygame
from __builtin__ import True
pygame.init()

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,tipo,imagenes,left,top,orientacion,expDrop,hpMax,velocidad,danio,distanciaMax):
        self.tipo = tipo
        self.imagenes = imagenes
        self.animacion = self.imagenes[0][0]
        self.imagen = self.animacion[0]
        self.rect = self.imagen.get_rect()
        self.rect.left, self.rect.top = left,top
        self.vx, self.vy = 0,0
        #seteo imagenes
        self.orientacion = orientacion
        self.movimiento = 0
        self.imagen_actual = 0

        #estados
        self.accion = "no atacando"
        self.estaVivo = True
        self.moviendo = False
        self.atacando = False
        self.vivo = True
        self.siguiendo = False
        #drop
        self.expDrop = expDrop

        #stats
        self.hpMax = hpMax
        self.hp = self.hpMax
        self.velocidad = velocidad
        self.distancia = 0
        self.distanciaMax = distanciaMax
        self.danio = danio

    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
        
    def terminoAnimar(self):
        return self.movimiento == 1 or self.movimiento == 0 or self.imagen_actual == len(self.animacion)-1
    
    def animar(self):
        self.imagen_actual += 1
        if self.imagen_actual >= len(self.animacion):
            self.imagen_actual = 0
        self.imagen = self.animacion[self.imagen_actual]
        
    def update(self, superficie, t, listaEnemigos, personaje, vx, vy, listaFlechas,colision):
        
        if self.siguiendo:
            self.seguir(personaje)
        
        self.mover(-vx + self.vx, -vy + self.vy)
        
        if self.vx < 0: self.orientacion = 1
        if self.vx > 0: self.orientacion = 0
        
        
        if self.terminoAnimar():
            if self.vx == 0 and self.vy == 0:
                self.movimiento = 0
            else:
                self.movimiento = 1
                self.moviendo = True
            if self.rect.colliderect(personaje.rect):
                if personaje.movimiento == 2:
                    self.movimiento = 4
                    self.hp -= personaje.danio * 10
                else:
                    personaje.hp -= self.danio
                    self.movimiento = 2
                    self.siguiendo = True
   
            for flecha in listaFlechas:
                if self.rect.colliderect(flecha.rect):
                    flecha.destroy(listaFlechas)
                    self.hp -= flecha.dano
                    self.siguiendo = True
                    self.movimiento = 4

                if self.estaVivo == False:
                    self.movimiento = 1
            
        self.animacion = self.imagenes[self.orientacion][self.movimiento]
        
        if self.movimiento == 4:
            if t.tde8 == 4:
                self.animar()
        else:
            if t.t == 1:
                self.animar()
        
        if self.hp <= 0 and self.imagen_actual == 6:
            self.destroy(listaEnemigos)
        superficie.blit(self.imagen,self.rect)
    
    def seguir(self,personaje):
        if self.rect.left < personaje.rect.left:
            self.vx = self.velocidad
        else:
            self.vx = -self.velocidad
        if self.rect.top < personaje.rect.top:
            self.vy = self.velocidad
        else:
            self.vy = -self.velocidad
        
    def destroy(self,lista):
        if self in lista:
            lista.remove(self)
            