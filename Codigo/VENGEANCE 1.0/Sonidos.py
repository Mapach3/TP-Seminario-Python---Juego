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
podersonido=pygame.mixer.Sound("Sonidos/poder.wav")
podersonido.set_volume(0.3)
flechasonido=pygame.mixer.Sound("Sonidos/flechazo.wav")
furiasonido=pygame.mixer.Sound("Sonidos/furia.wav")
furiasonido.set_volume(0.2)
golpeenemigo=pygame.mixer.Sound("Sonidos/golpeenemigo.wav")
golpeenemigo.set_volume(0.35)

pygame.mixer.music.load("Sonidos/peleaboss.mp3") #Musica boosfight

pygame.mixer.music.play() #Como parametro podes ingresar el N de veces que queres que se repita.

pygame.mixer.music.load("Sonidos/menu.mid") #Musica menu.

pygame.mixer.music.play(20) #Como la musica del menu se repite, que tenga un loop mas extenso.

#pygame.mixer.music.load("Sonidos/nieve.mid") #Nivel de nieve 

#pygame.mixer.music.play(20 )

pygame.mixer.music.load("Sonidos/musicamuerte.mid") # Despues del gameover, hasta reiniciar

