import pygame
import Personaje

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