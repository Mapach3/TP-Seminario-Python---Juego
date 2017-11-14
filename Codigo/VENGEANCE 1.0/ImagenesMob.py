import pygame
class imagenes(pygame.sprite.Sprite):
    def __init__(self):
        self.nombre="unknown"

imagen1=pygame.image.load("Mob1\Derecha\move1.png").convert_alpha()
imagen2=pygame.image.load("Mob1\Derecha\move2.png").convert_alpha()
imagen3=pygame.image.load("Mob1\Derecha\move3.png").convert_alpha()
imagen4=pygame.image.load("Mob1\Derecha\move4.png").convert_alpha()
imagen5=pygame.image.load("Mob1\Derecha\move5.png").convert_alpha()
imagen6=pygame.image.load("Mob1\Derecha\move6.png").convert_alpha()

ImgDCam=[imagen1,imagen2,imagen3,imagen4,imagen5,imagen6]
        

imageen1=pygame.image.load("Mob1\Izquierda\move1.png").convert_alpha()
imageen2=pygame.image.load("Mob1\Izquierda\move2.png").convert_alpha()
imageen3=pygame.image.load("Mob1\Izquierda\move3.png").convert_alpha()
imageen4=pygame.image.load("Mob1\Izquierda\move4.png").convert_alpha()
imageen5=pygame.image.load("Mob1\Izquierda\move5.png").convert_alpha()
imageen6=pygame.image.load("Mob1\Izquierda\move6.png").convert_alpha()

ImgICam=[imageen1,imageen2,imageen3,imageen4,imageen5,imageen6]
        
ImgAt1=pygame.image.load("Mob1\Derecha\\ataque1.png").convert_alpha()
ImgAt2=pygame.image.load("Mob1\Derecha\\ataque2.png").convert_alpha()
ImgAt3=pygame.image.load("Mob1\Derecha\\ataque3.png").convert_alpha()
ImgAt4=pygame.image.load("Mob1\Derecha\\ataque4.png").convert_alpha()

        
ImgAtaquDe=[ImgAt1,ImgAt2,ImgAt3,ImgAt4]
        
ImgAt6=pygame.image.load("Mob1\Izquierda\\ataque1.png").convert_alpha()
ImgAt7=pygame.image.load("Mob1\Izquierda\\ataque2.png").convert_alpha()
ImgAt8=pygame.image.load("Mob1\Izquierda\\ataque3.png").convert_alpha()
ImgAt9=pygame.image.load("Mob1\Izquierda\\ataque4.png").convert_alpha()

ImgAtaqueIz=[ImgAt6,ImgAt7,ImgAt8,ImgAt9]

imagenQuieto1=pygame.image.load("Mob1\Derecha\Standby.png").convert_alpha()
ImgQuietoDe=[imagenQuieto1]

imagenQuieto2=pygame.image.load("Mob1\Izquierda\Standby.png").convert_alpha()
ImgQuietoIz=[imagenQuieto2]

ImgMuDe1=pygame.image.load("Mob1\Derecha\damageymuerte1.png").convert_alpha()
ImgMuDe2=pygame.image.load("Mob1\Derecha\muerte2.png").convert_alpha()
ImgMuDe3=pygame.image.load("Mob1\Derecha\muerte3.png").convert_alpha()
ImgMuDe4=pygame.image.load("Mob1\Derecha\muerte4.png").convert_alpha()

ImgMuerteDe=[ImgMuDe1,ImgMuDe2,ImgMuDe3,ImgMuDe4]


ImgMuIz1=pygame.image.load("Mob1\Izquierda\damageymuerte1.png").convert_alpha()
ImgMuIz2=pygame.image.load("Mob1\Izquierda\muerte2.png").convert_alpha()
ImgMuIz3=pygame.image.load("Mob1\Izquierda\muerte3.png").convert_alpha()
ImgMuIz4=pygame.image.load("Mob1\Izquierda\muerte4.png").convert_alpha()

ImgMuerteIz=[ImgMuIz1,ImgMuIz2,ImgMuIz3,ImgMuIz4]

ImagenDamageDe=pygame.image.load("Mob1\Derecha\damageymuerte1.png").convert_alpha()
ImgDamageDe=[ImagenDamageDe,ImgMuDe1]

ImagenDamageIz=pygame.image.load("Mob1\Izquierda\damageymuerte1.png").convert_alpha()
ImgDamageIz=[ImagenDamageIz,ImgMuIz1]

ListaImagenesDerecha=[ImgQuietoDe,ImgDCam,ImgAtaquDe,ImgMuerteDe,ImgDamageDe]
ListaImagenesIzquierda=[ImgQuietoIz,ImgICam,ImgAtaqueIz,ImgMuerteIz,ImgDamageIz]

ListaAnimacionesMob1=[ListaImagenesDerecha,ListaImagenesIzquierda]