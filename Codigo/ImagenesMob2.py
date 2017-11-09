import pygame
class imagenes(pygame.sprite.Sprite):
    def __init__(self):
        self.nombre="unknown"

imagen1=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\move1.png").convert_alpha()
imagen2=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\move2.png").convert_alpha()
imagen3=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\move3.png").convert_alpha()
imagen4=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\move4.png").convert_alpha()
imagen5=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\move5.png").convert_alpha()
imagen6=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\move6.png").convert_alpha()
imagen7=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\move7.png").convert_alpha()

ImgDCam=[imagen1,imagen2,imagen3,imagen4,imagen5,imagen6,imagen7]
        

imageen1=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\move1.png").convert_alpha()
imageen2=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\move2.png").convert_alpha()
imageen3=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\move3.png").convert_alpha()
imageen4=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\move4.png").convert_alpha()
imageen5=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\move5.png").convert_alpha()
imageen6=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\move6.png").convert_alpha()
imageen7=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\move7.png").convert_alpha()

ImgICam=[imageen1,imageen2,imageen3,imageen4,imageen5,imageen6,imageen7]
        
ImgAt1=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\ataque1.png").convert_alpha()
ImgAt2=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\ataque2.png").convert_alpha()
ImgAt3=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\ataque3.png").convert_alpha()
ImgAt4=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\ataque4.png").convert_alpha()
ImgAt5=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\ataque5.png").convert_alpha()
ImgAt6=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\ataque6.png").convert_alpha()
ImgAt7=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\ataque7.png").convert_alpha()
ImgAt8=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\ataque8.png").convert_alpha()
ImgAt9=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\ataque9.png").convert_alpha()       

ImgAtaquDe=[ImgAt1,ImgAt2,ImgAt3,ImgAt4,ImgAt5,ImgAt6,ImgAt7,ImgAt8,ImgAt9]
        
ImgAt10=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\ataque1.png").convert_alpha()
ImgAt11=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\ataque2.png").convert_alpha()
ImgAt12=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\ataque3.png").convert_alpha()
ImgAt13=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\ataque4.png").convert_alpha()
ImgAt14=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\ataque5.png").convert_alpha()
ImgAt15=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\ataque6.png").convert_alpha()
ImgAt16=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\ataque7.png").convert_alpha()
ImgAt17=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\ataque8.png").convert_alpha()
ImgAt18=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\ataque9.png").convert_alpha()

ImgAtaqueIz=[ImgAt10,ImgAt11,ImgAt12,ImgAt13,ImgAt14,ImgAt15,ImgAt16,ImgAt17,ImgAt18]

imagenQuieto1=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\Standby.png").convert_alpha()

ImgQuietoDe=[imagenQuieto1]

imagenQuieto2=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\Standby.png").convert_alpha()

ImgQuietoIz=[imagenQuieto2]

ImagenDamage=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\damage.png").convert_alpha()
ImgDamageDe=[ImagenDamage]

ImagenDamage1=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\damage.png").convert_alpha()
ImgDamageIz=[ImagenDamage1]


ImgMuDe1=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\muerte1.png").convert_alpha()
ImgMuDe2=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\muerte2.png").convert_alpha()
ImgMuDe3=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\muerte3.png").convert_alpha()
ImgMuDe4=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\muerte4.png").convert_alpha()
ImgMuDe5=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\muerte5.png").convert_alpha()
ImgMuDe6=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Derecha\muerte6.png").convert_alpha()

ImgMuerteDe=[ImgMuDe1,ImgMuDe2,ImgMuDe3,ImgMuDe4,ImgMuDe5,ImgMuDe6]


ImgMuIz1=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\muerte1.png").convert_alpha()
ImgMuIz2=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\muerte2.png").convert_alpha()
ImgMuIz3=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\muerte3.png").convert_alpha()
ImgMuIz4=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\muerte4.png").convert_alpha()
ImgMuIz5=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\muerte5.png").convert_alpha()
ImgMuIz6=pygame.image.load("C:\Users\Ignacio\Desktop\Mob2\Izquierda\muerte6.png").convert_alpha()

ImgMuerteIz=[ImgMuIz1,ImgMuIz2,ImgMuIz3,ImgMuIz4,ImgMuIz5,ImgMuIz6]



ListaImagenesDerecha=[ImgQuietoDe,ImgDCam,ImgAtaquDe,ImgMuerteDe,ImgDamageDe]
ListaImagenesIzquierda=[ImgQuietoIz,ImgICam,ImgAtaqueIz,ImgMuerteIz,ImgDamageIz]

ListaAnimacionesMob2 = [ListaImagenesIzquierda,ListaImagenesDerecha]