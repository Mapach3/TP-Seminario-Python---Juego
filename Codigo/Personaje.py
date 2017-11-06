import pygame

class Personaje(pygame.sprite.Sprite):
    def __init__(self,imagenes):

        self.imagenes = imagenes
        self.animacion = self.imagenes[0][0]
        self.imagen = self.animacion[0]
        self.rect = self.imagen.get_rect()
        self.rect.height = self.rect.height / 2
        self.rect.top, self.rect.left = (posX,posY)

        #seteo imagenes
        self.orientacion = 0
        self.movimiento = 0
        self.imagen_actual = 0

        #estados
        self.moviendo = False
        self.espadazo = False
        self.flechazo = False
        self.poder = False
        self.vivo = True
        self.subioLvl = False
        self.tienePotas = True

        #inventario
        self.oro = 0
        self.potas = 0

        #stats
        self.hp = 100
        self.hpMax = 100
        self.exp = 0
        self.expParaSubir = 100
        self.velocidad = 1
        self.danio = 1
        self.lvl = 1

    def mover(self,vx,vy):
        if vx == 0 and vy ==0:
            self.moviendo=False
        else: 
            self.moviendo=True
            if vx<0: 
                self.orientacion=0
            else: 
                self.orientacion=1
        self.rect.move_ip(vx*self.velocidad,vy*self.velocidad)
    
    
    def update(self, superficie, t, subioLvl, suceso):
        if self.hp <= 0:
            self.estaVivo = False
        if t.tde8 == 8 and self.subioLvl:
            self.subioLvl = False
        if self.exp >= self.expToNext:
            self.subirLvl(subirLvl, t)
        if suceso == "usar pota":
            self.usarPota()
        if suceso == "espadazo":
            self.movimiento = 2
        if suceso == "poder":
            self.movimiento = 3
        if suceso == "flechazo":
            self.movimiento = 4
        if self.estaVivo == False:
            self.movimiento = 5
        if suceso == "es golpeado":
            self.movimiento = 6
        if t.t == 1:
            self.animar()
        

    def animar(self):
        self.imagen_actual += 1
        if self.imagen_actual == len(self.imagenes[self.orientacion]):
            self.imagen_actual = 0
        self.imagen = self.imagenes[self.orientacion][self.movimiento][self.imagen_actual]

    def subirLvl(self, superficie, subirLvl, t):
        self.subioLvl = True
        self.lvl += 1
        t.tde8 = 0
        self.exp = 0
        self.expParaSubir += self.expParaSubir/4
        subirLvl.play()
        self.danio += self.danio/4
        self.hpMax += self.hpMax/4

    def usarPota(self):
        if self.potas > 0:
            self.potas -= 1
            curacion = self.hpmax / 4
            self.hp += curacion
            usarPota.play()
            if self.hp > self.hpmax:
                self.hp = self.hpmax
            

def main():
    import pygame
    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    salir=False
    reloj= pygame.time.Clock()
    fondo=Fondo(pygame.image.load("ChelinsWorld/fondo2.gif"))
    cursor=cursor()

    personaje=Personaje(listaImagenesProtagonista)

    vx,vy=0,0
    t = Times()

    

    while salir!=True:#LOOP PRINCIPAL
        reloj.tick(28)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            else:                                                                                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada = True
                        vx = -1
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada = True
                        vx = 1
                    if event.key== pygame.K_UP:
                        upsigueapretada=True
                        vy = -1
                    if event.key == pygame.K_DOWN:
                        downsigueapretada = True
                        vy = 1
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada = False
                        if rightsigueapretada: 
                            vx = 1
                        else:
                            vx = 0
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada = False
                        if leftsigueapretada:
                            vx = -1
                        else:
                            vx = 0
                    if event.key == pygame.K_UP:
                        upsigueapretada = False
                        if downsigueapretada:
                            vy = 1
                        else:
                            vy = 0
                    if event.key == pygame.K_DOWN:
                        downsigueapretada = False
                        if upsigueapretada:
                            vy = -1
                        else:
                            vy=0                    


        pantalla.fill((0,0,170))
        personaje.mover(vx, vy)           
        t.update_times()     
        moverCosasPantalla(personaje,fondo,pantalla,vx,vy,t) 
        pygame.display.update()
        
    pygame.quit()
    

def moverCosasPantalla(personaje,fondo,pantalla,vx,vy,t):
    fondo.update(pantalla,vx,vy)


main()
