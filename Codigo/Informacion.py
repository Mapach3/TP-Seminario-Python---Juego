import pygame
import Personaje
import Fondo


class Informacion(pygame.sprite.Sprite):
    def __init__(self):
        self.listatexto=[]
        self.fondo=pygame.image.load("Informacion/Fondo.png").convert_alpha() 
        self.botones=pygame.image.load("Informacion/Botones.png").convert_alpha()
       
    def update(self,pantalla,personaje):
        self.maketext(personaje)
        ypad=3
        ypad2=3
        pantalla.blit(self.fondo,(-1,0))        
        for texto in self.listaTextos:
            pantalla.blit(texto,(40,ypad))
            ypad+=25
            
    def maketext(self,personaje):
       
        self.texto1= "Level: " + str(personaje.level)
        self.textoPantalla1 = pygame.font.SysFont("Arial", 14, True, False).render(self.texto1,0,(255,255,255))
       
        self.texto2="Exp: " + str(personaje.exp) + " / " + str(personaje.expToNext)
        self.textoPantalla2= pygame.font.SysFont("Arial", 14, True, False).render(self.texto2,0,(255,255,255))
        
        self.texto3 = str(personaje.hp) + " / " + str(persoanje.hpMax) + " HP"
        self.textoPantalla3= pygame.font.SysFont("Arial", 14, True, False).render(self.texto3,0,(255,255,255))        
        
        self.texto4 = "Danio: " + str(personaje.dano)
        self.textoPantalla4= pygame.font.SysFont("Arial", 14, True, False).render(self.texto4,0,(255,255,255))        

        self.texto5 = "Velocidad: " + str(personaje.velocidad))
        self.textoPantalla5= pygame.font.SysFont("Arial", 14, True, False).render(self.texto5,0,(255,255,255))        


        self.texto6 = "Kills: "+ str(personaje.kills)
        self.textoPantalla6= pygame.font.SysFont("Arial", 14, True, False).render(self.texto6,0,(255,255,255))        

        
        self.texto7="Kills para furia: " + str(personaje.killsToFuria)
        self.textoPantalla7= pygame.font.SysFont("Arial", 14, True, False).render(self.texto7,0,(255,255,255))        
        
        self.listaTextos=[self.textoPantalla1,self.textoPantalla2,
                         self.textoPantalla3,self.textoPantalla4,self.textoPantalla5,
                         self.textoPantalla6,self.textoPantalla7]  