import pygame
class imagenes(pygame.sprite.Sprite):
    def __init__(self):
        self.nombre="unknown"

imagen1=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\move1.png").convert_alpha()
imagen2=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\move2.png").convert_alpha()
imagen3=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\move3.png").convert_alpha()
imagen4=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\move4.png").convert_alpha()
imagen5=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\move5.png").convert_alpha()
imagen6=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\move6.png").convert_alpha()
imagen7=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\move7.png").convert_alpha()
imagen8=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\move8.png").convert_alpha()
imagen9=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\move9.png").convert_alpha()
imagen10=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\move10.png").convert_alpha()
        
ImgDCam=[imagen1,imagen2,imagen3,imagen4,imagen5,imagen6,imagen7,imagen8,imagen9,imagen10]
        

imageen1=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\move1.png").convert_alpha()
imageen2=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\move2.png").convert_alpha()
imageen3=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\move3.png").convert_alpha()
imageen4=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\move4.png").convert_alpha()
imageen5=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\move5.png").convert_alpha()
imageen6=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\move6.png").convert_alpha()
imageen7=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\move7.png").convert_alpha()
imageen8=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\move8.png").convert_alpha()
imageen9=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\move9.png").convert_alpha()
imageen10=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\move10.png").convert_alpha()

ImgICam=[imageen1,imageen2,imageen3,imageen4,imageen5,imageen6,imageen7,imageen8,imageen9,imageen10]
        
ImgAt1=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\ataque1.png").convert_alpha()
ImgAt2=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\ataque2.png").convert_alpha()
ImgAt3=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\ataque3.png").convert_alpha()
ImgAt4=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\ataque4.png").convert_alpha()
ImgAt5=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\ataque5.png").convert_alpha()
        
ImgAtaquDe=[ImgAt1,ImgAt2,ImgAt3,ImgAt4,ImgAt5]
        
ImgAt6=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\ataque1.png").convert_alpha()
ImgAt7=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\ataque2.png").convert_alpha()
ImgAt8=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\ataque3.png").convert_alpha()
ImgAt9=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\ataque4.png").convert_alpha()
ImgAt10=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\ataque5.png").convert_alpha()
        
ImgAtaqueIz=[ImgAt6,ImgAt7,ImgAt8,ImgAt9,ImgAt10]
        
ImgPodDe1=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\poder1.png").convert_alpha()
ImgPodDe2=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\poder2.png").convert_alpha()
ImgPodDe3=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\poder3.png").convert_alpha()
ImgPodDe4=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\poder4.png").convert_alpha()

ImgPoderDe=[ImgPodDe1,ImgPodDe2,ImgPodDe3,ImgPodDe4]

ImgPodIz1=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\poder1.png").convert_alpha()
ImgPodIz2=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\poder2.png").convert_alpha()
ImgPodIz3=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\poder3.png").convert_alpha()
ImgPodIz4=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\poder4.png").convert_alpha()

ImgPoderIz=[ImgPodIz1,ImgPodIz2,ImgPodIz3,ImgPodIz4]

ImgArcIz1=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\Arco1.png").convert_alpha()
ImgArcIz2=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\Arco2.png").convert_alpha()
ImgArcIz3=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\Arco3.png").convert_alpha()
ImgArcIz4=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\Arco4.png").convert_alpha()
ImgArcIz5=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\Arco5.png").convert_alpha()
ImgArcIz6=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\Arco6.png").convert_alpha()
ImgArcIz7=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\Arco7.png").convert_alpha()
ImgArcIz8=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\Arco8.png").convert_alpha()
ImgArcIz9=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\Arco9.png").convert_alpha()

ImgArcoIz=[ImgArcIz1,ImgArcIz2,ImgArcIz3,ImgArcIz4,ImgArcIz5,ImgArcIz6,ImgArcIz7,ImgArcIz8,ImgArcIz9]


ImgArcDe1=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\Arco1.png").convert_alpha()
ImgArcDe2=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\Arco2.png").convert_alpha()
ImgArcDe3=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\Arco3.png").convert_alpha()
ImgArcDe4=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\Arco4.png").convert_alpha()
ImgArcDe5=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\Arco5.png").convert_alpha()
ImgArcDe6=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\Arco6.png").convert_alpha()
ImgArcDe7=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\Arco7.png").convert_alpha()
ImgArcDe8=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\Arco8.png").convert_alpha()
ImgArcDe9=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\Arco9.png").convert_alpha()

ImgArcoDe=[ImgArcDe1,ImgArcDe2,ImgArcDe3,ImgArcDe4,ImgArcDe5,ImgArcDe6,ImgArcDe7,ImgArcDe8,ImgArcDe9]

imagenQuieto1=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\Standby.png").convert_alpha()
ImgQuietoDe=[imagenQuieto1]

imagenQuieto2=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\Standby.png").convert_alpha()
ImgQuietoIz=[imagenQuieto2]



ImgMuDe1=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\damageymuerte1.png").convert_alpha()
ImgMuDe2=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\Muerte2.png").convert_alpha()
ImgMuDe3=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\muerte3.png").convert_alpha()
ImgMuDe4=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\muerte4.png").convert_alpha()
ImgMuDe5=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\muerte5.png").convert_alpha()
ImgMuDe6=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\muerte6.png").convert_alpha()
ImgMuDe7=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\muerte7.png").convert_alpha()

ImgMuerteDe=[ImgMuDe1,ImgMuDe2,ImgMuDe3,ImgMuDe4,ImgMuDe5,ImgMuDe6,ImgMuDe7]


ImgMuIz1=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\damageymuerte1.png").convert_alpha()
ImgMuIz2=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\Muerte2.png").convert_alpha()
ImgMuIz3=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\muerte3.png").convert_alpha()
ImgMuIz4=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\muerte4.png").convert_alpha()
ImgMuIz5=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\muerte5.png").convert_alpha()
ImgMuIz6=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\muerte6.png").convert_alpha()
ImgMuIz7=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\muerte7.png").convert_alpha()

ImgMuerteIz=[ImgMuIz1,ImgMuIz2,ImgMuIz3,ImgMuIz4,ImgMuIz5,ImgMuIz6,ImgMuIz7]

ImagenDamageDe=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Derecha\damageymuerte1.png").convert_alpha()
ImgDamageDe=[ImagenDamageDe]

ImagenDamageIz=pygame.image.load("C:\Users\Ignacio\Desktop\Personaje\Izquierda\damageymuerte1.png").convert_alpha()
ImgDamageIz=[ImagenDamageIz]

ListaImagenesDerecha=[ImgQuietoDe,ImgDCam,ImgAtaquDe,ImgPoderDe,ImgArcoDe,ImgMuerteDe,ImgDamageDe]
ListaImagenesIzquierda=[ImgQuietoIz,ImgICam,ImgAtaqueIz,ImgPoderIz,ImgArcoIz,ImgMuerteIz,ImgDamageIz]

ListaAnimacionesProtagonista=[ListaImagenesDerecha,ListaImagenesIzquierda]