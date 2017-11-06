import pygame
class Imagenes(object):
    def __init__(self):
        self.nombre="Unknown"
pygame.init()
pygame.display.set_mode((0,0))


ataquesonido=pygame.mixer.Sound("Sonidos/espadazo.wav")
ataquesonido.set_volume(0.4)
levelupsonido=pygame.mixer.Sound("Sonidos/levelup.wav")
gameoversonido=pygame.mixer.Sound("Sonidos/gameover.wav")
golpeadosonido=pygame.mixer.Sound("Sonidos/golpeado.wav")
podersonido=pygame.mixer.Sound("Sonidos/poder")
podersonido.set_volume(0.3)
flechasonido=pygame.mixer.Sound("Sonidos/flechazo)

pygame.music.load("Sonidos/peleaboss.mp3") #Musica boosfight

pygame.music.play() #Como parametro podes ingresar el N de veces que queres que se repita.

pygame.music.load("Sonidos/menu.mid") #Musica menu.

pygame.music.play(20) #Como la musica del menu se repite, que tenga un loop mas extenso.

pygame.music.load("Sonidos/nieve.mid") #Nivel de nieve 

pygame.music.play(20 )

pygame.music.load("Sonidos/musicamuerte.mid") # Despues del gameover, hasta reiniciar

