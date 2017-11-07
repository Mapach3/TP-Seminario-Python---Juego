import pygame
from imagenes import *
pygame.init()

class Flecha(pygame.sprite.Sprite):
    def __init__(self,personaje):
        self.lanzo = False
        self.imagenes = [imgFlechaIzq,imgFlechaDer]
        self.imagen = self.imagenes[personaje.orientacion]
        self.rect=self.imagen.get_rect() 
        self.pos_comienzo = [[0,-20],[0,-20]] ## La posicion x,y del comienzo del flechazo para la izquierda y la derecha         
        self.orientacion = personaje.orientacion
        self.rect.top = personaje.rect.top + self.pos_comienzo[self.orientacion][1]
        self.rect.left = personaje.rect.left + self.pos_comienzo[self.orientacion][0]
        self.tiempo_actual = 0
        self.tiempototal = 30
        self.dano = 1 * personaje.danio
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
                
        #         for monster in listamonster:
        #             if   monster.estavivo and monster.active and self.rect.colliderect(monster.rect) and t.t==1 and not monster.human:
        #                 monster.hp-=self.dano+(7*jugador.magic/8)
        #                 self.sound.play()
        #                 pygame.draw.rect(superficie,(250,0,0),monster.rect)
        #                 self.destroy(lista,jugador)
        #             if monster.human and self.rect.colliderect(monster.rect):
        #                 monster.textactive=True
        #                 if  isinstance(monster,Teleporter):
        #                     monster.teleport()
        #                     self.destroy(lista, jugador)
        #  
        #         for shop in listashop:
        #             if self.rect.colliderect(shop.rect) and jugador.gold>=shop.precio:
        #                 jugador.gold-=shop.precio
        #                 shop.comprar(jugador)
        #                 shop.sound.play()
        #                 pygame.draw.rect(superficie,(0,255,0),shop.rect)
        #                 self.destroy(lista,jugador)              
        #         self.imagen=self.imagenes[self.orientacion][self.imagen_numero]
    
        superficie.blit(self.imagen,self.rect)
    def destroy(self,lista):
        if self in lista:                
            lista.remove(self)
