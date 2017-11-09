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
        self.es_golpeado = False
        self.esta_golpeando = False
        self.poderBoss1 = False
        
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
        
        if self.poderBoss1 == True:
            self.mover(-vx + self.vx*7, -vy + self.vy*7)
        else:
            if self.moviendo:
                self.mover(self.vx , self.vy)
            if personaje.moviendo:
                self.mover(-vx,-vy)

        if self.vx < 0: self.orientacion = 1
        if self.vx > 0: self.orientacion = 0
        
        if self.tipo == "Mini Jefe":
            if self.vx < 0: self.orientacion = 0
            if self.vx > 0: self.orientacion = 1
        
        self.es_golpeado = False
        self.esta_golpeando = False
        
        if self.rect.colliderect(personaje.rect):
            if personaje.movimiento == 2:
                self.es_golpeado = True
            else:
                self.esta_golpeando = True
        
        if self.terminoAnimar():
            if self.vx == 0 and self.vy == 0:
                self.movimiento = 0
                self.moviendo = False
            else:
                self.movimiento = 1
                self.moviendo = True
                
            if self.es_golpeado:  
                self.movimiento = 4
                self.hp -= personaje.danio
                self.moviendo = False 
            if self.esta_golpeando:
                personaje.hp -= self.danio
                personaje.movimiento = 6
                self.movimiento = 2
                self.siguiendo = True
            if self.poderBoss1 == True:
                self.movimiento = 2
                ##poderBoss1.play()
   
            for flecha in listaFlechas:
                if self.rect.colliderect(flecha.rect):
                    if flecha.tipo == "flecha":
                        flecha.destroy(listaFlechas)
                        self.hp -= flecha.dano
                    else:
                        self.hp -= flecha.dano*1.5
                    self.siguiendo = True
                    self.movimiento = 4
            
            if self.estaVivo == False:
                self.movimiento = 1
            if self.hp <= 0:
                self.movimiento = 3
                    
 
        self.animacion = self.imagenes[self.orientacion][self.movimiento]
        
        if self.tipo == "Mini Jefe":
            if t.tde80 == 80 and self.poderBoss1 == False:
                self.poderBoss1 = True
            if t.tde40 == 40 and self.poderBoss1 == True:
                self.poderBoss1 = False
        
        if self.tipo == "Boss 2":
            if t.tde80 == 80:
                self.poderBoss2()
        
        if self.movimiento == 4:
            if t.tde8 == 8:
                self.animar()
        else:
            if t.t == 1:
                self.animar()
                
        if self.hp <= 0 and self.movimiento == 3 and self.imagen_actual == 3:
            if self.tipo == "Jefe Final":
                t.winner == True
            else:
                personaje.hp += self.hpMax/10.0
                if self.tipo == "mob1":
                    personaje.exp += 20
                if self.tipo == "mob2":
                    personaje.exp += 60
                if self.tipo == "Mini Jefe":
                    personaje.exp += 200
                if not personaje.esta_furiozo:
                    personaje.kills += 1
            self.destroy(listaEnemigos)
                
        
        if self.hp <= 0 and self.movimiento == 3 and self.imagen_actual == 2 and self.tipo == "Boss 1":
            personaje.hp += self.hpMax/10.0
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
            
    def poderBoss2(self):
        pass
     
    def destroy(self,lista):
        if self in lista:
            lista.remove(self)
            