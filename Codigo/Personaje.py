import pygame
Class Personaje():
    def __init__(self,imagenes):
        #imagenes y posicion
        self.imagenes = imagenes
        self.animacion = self.imagenes[0][0]
        self.imagen = self.animacion[0]
        self.rect = self.imagen.get_rect()
        self.rect.top, self.rect.left = (posX,posY)

        #seteo imagenes
        self.orientacion = 0
        self.movimiento = 0
        self.imagen_actual = 0

        #estados
        self.moviendo = False
        self.espadazo = False
        self.flechazo = False
        self.casteando = False
        self.vivo = True

        #inventario
        self.oro = 0
        self.potas = 0

        #stats
        self.hp = 100
        self.hpMax = 100
        self.exp = 0
        self.expToNext = 100
        self.velocidad = 1
        self.danio = 1
        self.lvl = 1

    def mover(self, vx, vy):
        if vx == 0 and vy == 0:
           self.moviendo = False
           self.movimiento = 0
        else:
            self.moviendo = True
            if vx < 0:
               self.orientacion = 0
            else:
                self.orientacion = 1
        self.rect.move_ip(vx*self.velocidad, vy*self.velocidad)

    def setLvl(self):
        if self.exp >= expToNext:
            self.lvl += 1
            self.exp -= self.expToNext
            self.expToNext += self.expToNext/2.0
            subirLvl.play()

    def estaMoviendo(vx,vy)
        self.moviendo = vx == 0 and vy == 0

    def actualizar(self,vx,vy,t,espadazo,flechazo,casteando):
        self.actualizarLvl(self)
        if self.estaMoviendo(vx,vy):
            mover(self,vx,vy)
        else
            quieto(self)
        if espadazo:
            self.movimiento = 2
        if casteando:
            self.movimiento = 3
        if flechazo:
            self.movimiento = 4
        if self.estaVivo(self) == False:
            self.movimiento = 5
        ##
        ##
        ##
        self.setImagen(self)


class Player(pygame.sprite.Sprite):
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
        self.expToNext = 100
        self.velocidad = 1
        self.danio = 1
        self.lvl = 1


    def update(self, listamonster, listagold, superficie, t, hited, subirLvl):
        if self.hp <= 0:
            self.estavivo = False
        if t.tde8 == 8 and self.subioLvl:
            self.subioLvl = False
        if self.exp >= self.expToNext:
            self.subirLvl(subirLvl, t)
        if espadazo:
            self.movimiento = 2
        if casteando:
            self.movimiento = 3
        if flechazo:
            self.movimiento = 4
        if self.estaVivo == False:
            self.movimiento = 5
        if
        if t.t == 1:
            self.animar()
        for monster in listamonster:
            if monster.active and monster.estavivo and self.rect.colliderect(monster.rect) and t.t == 1 and not (
            t.gameover) and not (monster.human):
                self.hp -= monster.dano
                pygame.draw.rect(superficie, (255, 0, 0), self.rect)
                hited.play()
            if isinstance(monster, Teleporter_on_contact):
                if monster.rect.colliderect(self.rect):
                    monster.teleport_on_contact()
        for gold in listagold:
            if self.rect.colliderect(gold.rect):
                self.gold += gold.cantidad
                gold.destroy(listagold)
        self.printText(superficie, self.rect.left, self.rect.top - self.rect.height)
        if not self.estapegando:
            if self.hp <= 0: self.imagen = self.imagendead
            superficie.blit(self.imagen, (self.rect.left, self.rect.top - self.rect.height))

    def printText(self, surface, x, y):
        f1 = pygame.font.SysFont("Terminal", 20, False, False)
        if self.estavivo:
            self.text = str(self.hp) + " / " + str(self.hpmax)
        else:
            self.text = "*DEAD*"
        self.textsurface = f1.render(self.text, 0, (0, 0, 0))
        surface.blit(self.textsurface, (x, y - 10))
        if self.leveledup:
            pygame.draw.rect(surface, (255, 245, 0), self.rect)
            self.textsurface2 = pygame.font.SysFont("Arial", 14, True, False).render("LEVEL UP!", 0, (255, 255, 255))
            surface.blit(self.textsurface2, (x, y - 30))

    def nextimage(self):
        if self.casting:
            self.imagen = self.imagenescasting[self.orientacion]
        else:
            self.imagen_actual += 1
            if self.imagen_actual == len(self.imagenes[self.orientacion]):
                self.imagen_actual = 0
            self.imagen = self.imagenes[self.orientacion][self.imagen_actual]

    def levelup(self, superficie, levelup, t):
        self.leveledup = True
        self.level += 1
        t.tde8 = 0
        self.xp = 0
        if self.level <= 12:
            self.xptonextlevel = (self.level ** (2)) * 1500
        else:
            x = self.level ** 3
            self.xptonextlevel = math.log(x, 2) * 20000 + 10000
        self.xptonextlevel = (round(self.xptonextlevel, 0))
        levelup.play()
        self.dano += 0
        self.magic += 0
        self.hpmax += 20
        self.skillpoints += 10
        if self.hp <= 75:
            self.hp += 25

    def usepot(self):

        if self.pots > 0:
            self.pots -= 1
            heal = self.hpmax / 4 + self.hpmax / 2
            self.hp += heal
            pygame.mixer.Sound("ChelinsWorld/pot.wav").play()
            if self.hp > self.hpmax:
                self.hp = self.hpmax
        self.lockpots()

    def lockpots(self):
        self.enablepots = False

    def unlockpots(self):
        self.enablepots = True

    def setacrono(self):
        imagen1 = pygame.image.load("ChelinsWorld/acronor1.png").convert_alpha()
        imagen2 = pygame.image.load("ChelinsWorld/acronor2.png").convert_alpha()
        imagen1l = pygame.image.load("ChelinsWorld/acronol1.png").convert_alpha()
        imagen2l = pygame.image.load("ChelinsWorld/acronol2.png").convert_alpha()
        imagen1t = pygame.image.load("ChelinsWorld/acronot1.png").convert_alpha()
        imagen2t = pygame.image.load("ChelinsWorld/acronot2.png").convert_alpha()
        imagen1b = pygame.image.load("ChelinsWorld/acronob1.png").convert_alpha()
        imagen2b = pygame.image.load("ChelinsWorld/acronob2.png").convert_alpha()
        self.imagenes = [[imagen1, imagen2], [imagen1l, imagen2l], [imagen1t, imagen2t], [imagen1b, imagen2b]]
        self.imagenescasting = self.imagenescastingacrono


