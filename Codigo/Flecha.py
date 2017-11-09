import pygame
from imagenes import imgBolaDer,imgBolaIzq,imgFlechaDer,imgFlechaIzq

pygame.init()

class Flecha(pygame.sprite.Sprite):
    def __init__(self,personaje,tipo):
        self.tipo = tipo
        self.lanzo = False
        if self.tipo == "flecha":
            self.imagenes = [imgFlechaIzq,imgFlechaDer]
        else:
            self.imagenes = [imgBolaIzq,imgBolaDer]
        self.imagen = self.imagenes[personaje.orientacion]
        self.rect=self.imagen.get_rect() 
        if self.tipo == "flecha":
            self.pos_comienzo = [[0,-20],[0,-20]] ## La posicion x,y del comienzo del flechazo para la izquierda y la derecha         
        else:
            self.pos_comienzo = [[0,0],[0,0]]
        self.orientacion = personaje.orientacion
        self.rect.top = personaje.rect.top + self.pos_comienzo[self.orientacion][1]
        self.rect.left = personaje.rect.left + self.pos_comienzo[self.orientacion][0]
        self.tiempo_actual = 0
        self.tiempototal = 15
        self.dano = personaje.danio
        self.velocidad = 50
        self.vx,self.vy = 0,0
        
    def update(self,superficie,lista,personaje,vx,vy,t):
        if self.lanzo == False:
            self.lanzo = personaje.imagen_actual >= len(personaje.animacion) - 2
        if self.lanzo == True:
            if t.t == 1:
                self.tiempo_actual += 1
                if self.orientacion == 0:
                   self.vx = -self.velocidad
                else:
                    self.vx = self.velocidad
                        
                self.rect.move_ip(-vx+self.vx,-vy+self.vy,)
                
                if self.tiempo_actual > self.tiempototal:
                    self.destroy(lista)
                

        superficie.blit(self.imagen,self.rect)
    def destroy(self,lista):
        if self in lista:                
            lista.remove(self)
