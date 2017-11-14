import pygame
class imagenes(pygame.sprite.Sprite):
    def __init__(self):
        self.nombre="unknown"

imagen1=pygame.image.load("Jefe1\Derecha\move1.png").convert_alpha()
imagen2=pygame.image.load("Jefe1\Derecha\move2.png").convert_alpha()
imagen3=pygame.image.load("Jefe1\Derecha\move3.png").convert_alpha()
imagen4=pygame.image.load("Jefe1\Derecha\move4.png").convert_alpha()
imagen5=pygame.image.load("Jefe1\Derecha\move5.png").convert_alpha()
imagen6=pygame.image.load("Jefe1\Derecha\move6.png").convert_alpha()

ImgDCam=[imagen1,imagen2,imagen3,imagen4,imagen5,imagen6]
        

imageen1=pygame.image.load("Jefe1\Izquierda\move1.png").convert_alpha()
imageen2=pygame.image.load("Jefe1\Izquierda\move2.png").convert_alpha()
imageen3=pygame.image.load("Jefe1\Izquierda\move3.png").convert_alpha()
imageen4=pygame.image.load("Jefe1\Izquierda\move4.png").convert_alpha()
imageen5=pygame.image.load("Jefe1\Izquierda\move5.png").convert_alpha()
imageen6=pygame.image.load("Jefe1\Izquierda\move6.png").convert_alpha()

ImgICam=[imageen1,imageen2,imageen3,imageen4,imageen5,imageen6]
        
ImgAt1=pygame.image.load("Jefe1\Derecha\Ataque1.png").convert_alpha()
ImgAt2=pygame.image.load("Jefe1\Derecha\Ataque2.png").convert_alpha()
ImgAt3=pygame.image.load("Jefe1\Derecha\Ataque3.png").convert_alpha()
ImgAt4=pygame.image.load("Jefe1\Derecha\Ataque4.png").convert_alpha()
ImgAt5=pygame.image.load("Jefe1\Derecha\Ataque5.png").convert_alpha()
ImgAt6=pygame.image.load("Jefe1\Derecha\Ataque6.png").convert_alpha()
ImgAt7=pygame.image.load("Jefe1\Derecha\Ataque7.png").convert_alpha()
ImgAt8=pygame.image.load("Jefe1\Derecha\Ataque8.png").convert_alpha()
ImgAt9=pygame.image.load("Jefe1\Derecha\Ataque9.png").convert_alpha()        
ImgAtaquDe=[ImgAt1,ImgAt2,ImgAt3,ImgAt4,ImgAt5,ImgAt6,ImgAt7,ImgAt8,ImgAt9]
        
ImgAt10=pygame.image.load("Jefe1\Izquierda\Ataque1.png").convert_alpha()
ImgAt11=pygame.image.load("Jefe1\Izquierda\Ataque2.png").convert_alpha()
ImgAt12=pygame.image.load("Jefe1\Izquierda\Ataque3.png").convert_alpha()
ImgAt13=pygame.image.load("Jefe1\Izquierda\Ataque4.png").convert_alpha()
ImgAt14=pygame.image.load("Jefe1\Izquierda\Ataque5.png").convert_alpha()
ImgAt15=pygame.image.load("Jefe1\Izquierda\Ataque6.png").convert_alpha()
ImgAt16=pygame.image.load("Jefe1\Izquierda\Ataque7.png").convert_alpha()
ImgAt17=pygame.image.load("Jefe1\Izquierda\Ataque8.png").convert_alpha()
ImgAt18=pygame.image.load("Jefe1\Izquierda\Ataque9.png").convert_alpha()          

ImgAtaqueIz=[ImgAt10,ImgAt11,ImgAt12,ImgAt13,ImgAt14,ImgAt15,ImgAt16,ImgAt17,ImgAt18]
        
ImgPodDe1=pygame.image.load("Jefe1\Derecha\poder1.png").convert_alpha()
ImgPodDe2=pygame.image.load("Jefe1\Derecha\poder2.png").convert_alpha()
ImgPodDe3=pygame.image.load("Jefe1\Derecha\poder3.png").convert_alpha()
ImgPodDe4=pygame.image.load("Jefe1\Derecha\poder4.png").convert_alpha()
ImgPodDe5=pygame.image.load("Jefe1\Derecha\poder5.png").convert_alpha()
ImgPodDe6=pygame.image.load("Jefe1\Derecha\poder6.png").convert_alpha()
ImgPodDe7=pygame.image.load("Jefe1\Derecha\poder7.png").convert_alpha()
ImgPodDe8=pygame.image.load("Jefe1\Derecha\poder8.png").convert_alpha()


ImgPoderDe=[ImgPodDe1,ImgPodDe2,ImgPodDe3,ImgPodDe4,ImgPodDe5,ImgPodDe6,ImgPodDe7,ImgPodDe8]

ImgPodIz1=pygame.image.load("Jefe1\Izquierda\poder1.png").convert_alpha()
ImgPodIz2=pygame.image.load("Jefe1\Izquierda\poder2.png").convert_alpha()
ImgPodIz3=pygame.image.load("Jefe1\Izquierda\poder3.png").convert_alpha()
ImgPodIz4=pygame.image.load("Jefe1\Izquierda\poder4.png").convert_alpha()
ImgPodIz5=pygame.image.load("Jefe1\Izquierda\poder5.png").convert_alpha()
ImgPodIz6=pygame.image.load("Jefe1\Izquierda\poder6.png").convert_alpha()
ImgPodIz7=pygame.image.load("Jefe1\Izquierda\poder7.png").convert_alpha()
ImgPodIz8=pygame.image.load("Jefe1\Izquierda\poder8.png").convert_alpha()

ImgPoderIz=[ImgPodIz1,ImgPodIz2,ImgPodIz3,ImgPodIz4,ImgPodIz5,ImgPodIz6,ImgPodIz7,ImgPodIz8]


imagen1=pygame.image.load("Jefe1\Derecha\Standby.png").convert_alpha()
ImgQuietoDe=[imagen1]

imageen1=pygame.image.load("Jefe1\Izquierda\Standby.png").convert_alpha()
ImgQuietoIz=[imageen1]

ImgMuDe1=pygame.image.load("Jefe1\Derecha\damageymuerte1.png").convert_alpha()
ImgMuDe2=pygame.image.load("Jefe1\Derecha\muerte2.png").convert_alpha()

ImgMuerteDe=[ImgMuDe1,ImgMuDe2]


ImgMuIz1=pygame.image.load("Jefe1\Izquierda\damageymuerte1.png").convert_alpha()
ImgMuIz2=pygame.image.load("Jefe1\Izquierda\muerte2.png").convert_alpha()

ImgMuerteIz=[ImgMuIz1,ImgMuIz2]

ImagenDamageDe=pygame.image.load("Jefe1\Derecha\damageymuerte1.png").convert_alpha()
ImgDamageDe=[ImagenDamageDe]

ImagenDamageIz=pygame.image.load("Jefe1\Izquierda\damageymuerte1.png").convert_alpha()
ImgDamageIz=[ImagenDamageIz]

ListaImagenesDerecha=[ImgQuietoDe,ImgDCam,ImgAtaquDe,ImgMuerteDe,ImgDamageDe,ImgPoderDe]
ListaImagenesIzquierda=[ImgQuietoIz,ImgICam,ImgAtaqueIz,ImgMuerteIz,ImgDamageIz,ImgPoderIz]

ListaAnimacionesJefe=[ListaImagenesDerecha,ListaImagenesIzquierda]