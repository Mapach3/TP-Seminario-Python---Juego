class Enemigo(pygame.sprite.Sprite):
    def __init__(self,tipo,imagenes,left,top,orientacion,expDrop,hpMax,velocidad,danio,distanciaMax):
        self.tipo = tipo
        self.imagenes = imagenes
        self.animacion = self.imagenes[0][0]
        self.imagen = self.animacion[0]
        self.rect = self.imagen.get_rect()
        self.rect.left, self.rect.top = left,top
        self.vx, self.vy = 0,0
        #seteo imagenes
        self.orientacion = orientacion
        self.movimiento = 1
        self.imagen_actual = 0

        #estados
        self.accion = "no atacando"
        self.estaVivo = True
        self.moviendo = False
        self.atacando = False
        self.vivo = True

        #drop
        self.expDrop = expDrop

        #stats
        self.hpMax = hpMax
        self.hp = self.hpMax
        self.velocidad = velocidad
        self.distancia = 0
        self.distanciaMax = distanciaMax
        self.danio = danio

    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
        
    def terminoAnimar(self):
        return self.movimiento == 1 or self.movimiento == 0 or self.imagen_actual == len(self.animacion)-1
    
    def animar(self):
        self.imagen_actual += 1
        if self.imagen_actual >= len(self.animacion):
            self.imagen_actual = 0
        self.imagen = self.animacion[self.imagen_actual]
        
    def update(self, superficie, t, listaEnemigos, personaje, vx, vy):
        
        if self.hp <= 0:
            self.estaVivo = False
        
        if self.estaVivo == False:
            self.destroy(listaEnemigos)
        else:
            if self.distancia <= distanciaMax:
                if self.orientacion == 0:
                    self.vx = -self.velocidad
                else:
                    self.vy = self.velocidad
                self.distancia += self.velocidad
            else:
                self.orientacion += 1
                if self.orientacion == 2:
                    self.orientacion = 0
                
            if self.terminoAnimar():
                if vx == 0 and vy == 0:
                    self.movimiento = 0
                else:
                    self.movimiento = 1
                    self.moviendo = True

                if self.rect.colliderect(personaje.rect):
                    personaje.hp -= self.danio
                    self.movimiento = 2
                    self.seguir(personaje)
                    if personaje.movimiento == 2:
                        self.hp -= personaje.danio * 2
                
                for flecha in listaFlechas:
                    if self.rect.colliderect(flecha.rect):
                        flecha.destroy(listaFlechas)
                        self.hp -= flecha.danio
                        self.seguir(personaje)
                
            self.animacion = self.imagenes[self.orientacion][self.movimiento]
            
            if t.t == 1:
                self.animar()
                
            ## Ubicar al personaje en el medio de la pantalla
    
            superficie.blit(self.imagen,self.rect)
    
    def seguir(self,personaje):
        pass
        
    