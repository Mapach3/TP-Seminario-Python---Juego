import pygame
from pickle import FALSE
from pygame import font


class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        self.imagen=pygame.image.load("TestFondo.png").convert_alpha()
        self.rect=self.imagen.get_rect()
    def update(self,pantalla,vx,vy):
        self.rect.move_ip(-vx,-vy)
        pantalla.blit(self.imagen,self.rect)
        
        
        
        
        
class cursor(pygame.Rect):
    def __init__(self):
        (self.x,self.y)=pygame.mouse.get_pos()
        pygame.Rect.__init__(self,self.x,self.y,0,0)
    def updatecursor(self):
        (self.left,self.top)=pygame.mouse.get_pos()
        
        
        
            
        
        
class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x,y):  
        self.imagen=imagen1
        self.imagennormal=imagen1
        self.imagenseleccion=imagen2
        self.rect= imagen1.get_rect()
        self.rect.left=x
        self.rect.top=y
    def setImage(self,imagen):
        self.imagen=imagen
    def pintar(self,surface,cursor):
        if cursor.colliderect(self.rect): self.setImage(self.imagenseleccion)
        else:self.setImage(self.imagennormal)
        surface.blit(self.imagen,(self.rect.left,self.rect.top))        
        
        
#clase del jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        #creo 4 imagenes
        self.imagen1=pygame.image.load("animacion1.png").convert_alpha()
        self.imagen2=pygame.image.load("animacion2.png").convert_alpha()
        self.imagen3=pygame.image.load("animacion1l.png").convert_alpha()
        self.imagen4=pygame.image.load("animacion2l.png").convert_alpha() 
         
        # creo la lista de las imaganes
        #el primer indice es la orientacion y el segundo la imagen
        # self.imagenes[self.orientacion][self.imagen_actual]      
        self.imagenes=[[self.imagen1,self.imagen2],[self.imagen3,self.imagen4]]
        
        self.imagen_actual=0
        self.imagen=self.imagenes[self.imagen_actual][0]
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(300,400)  		# posicion del jugador
        
        #variable par ver si se esta moviendo
        self.estamoviendo=False
        
        # 0 si va ala derecha 1 si va la izquierda
        self.orientacion=0

    def mover(self,vx,vy):
       self.rect.move_ip(vx,vy)
       
    #funcion principal de actualizacion   
    def update(self,superficie,vx,vy,t):
        
        # si no se mueve self.estamoviendo=FALSE
        if (vx,vy)==(0,0): self.estamoviendo=False
        else:self.estamoviendo=True # si se mueve que este en TRUE
        
        # con estas 2 lineas cambio la orientacion
        if vx>0: self.orientacion=0
        elif vx<0: self.orientacion=1
        
        # si el t==1 (auxiliar) y se esta moviendo entonces cambiar la imagen
        if t==1 and self.estamoviendo:
            self.nextimage()
            
        # mover el rectangulo    
        vx=0
        vy=0
        self.mover(vx, vy)
        
        #self.imagen va ser la imagen que este en la orientacion y en el numero de imagen_actual
        self.imagen=self.imagenes[self.orientacion][self.imagen_actual]
        
        #finalmente pintar en la pantalla
        superficie.blit(self.imagen,self.rect)
        
    #funcion que se encarga de cambiar de imagen    
    def nextimage(self):
        self.imagen_actual+=1
        
        if self.imagen_actual>(len(self.imagenes)-1):# si se fue de rango que lo ponga en 0
            self.imagen_actual=0          
        
def main(cargar=False):
    import pygame
    
    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    salir=False
    reloj1= pygame.time.Clock()
    
    #creo un player
    player1=Player()
    
    fondo1=Fondo()
    vx,vy=0,0
    velocidad=32
    
    #COLORCITOS
    rojo=(250,0,0)
    
    #Rectangulos para paredes MAPA INICIAL
    r1 = pygame.Rect(50,50,45,45)
    
    #auxiliares para el movimiento
    leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada=False,False,False,False
    t=0
    while salir!=True:#LOOP PRINCIPAL
        for event in pygame.event.get():
            #control de eventos
            if event.type == pygame.QUIT:
                salir=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leftsigueapretada=True
                    vx=-velocidad
                if event.key == pygame.K_RIGHT:
                    rightsigueapretada=True
                    vx=velocidad
                if event.key== pygame.K_UP:
                    upsigueapretada=True
                    vy=-velocidad
                if event.key == pygame.K_DOWN:
                    downsigueapretada=True
                    vy=velocidad
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    leftsigueapretada=False
                    if rightsigueapretada:vx=velocidad
                    else:vx=0
                if event.key == pygame.K_RIGHT:
                    rightsigueapretada=False
                    if leftsigueapretada:vx=-velocidad
                    else:vx=0
                if event.key== pygame.K_UP:
                    upsigueapretada=False
                    if downsigueapretada:vy=velocidad
                    else:vy=-0
                if event.key == pygame.K_DOWN:
                    downsigueapretada=False
                    if upsigueapretada:vy=-velocidad
                    else:vy=0 
                    
                         
        reloj1.tick(25)# 25 fps
        
        #auxiliar de la animacion
        t+=1
        if t>1:
            t=0            
         
        # pintar el fondo            
        pantalla.fill((255,255,255))
        
        #pinto fondo
        fondo1.update(pantalla,vx,vy)
        
        # actualizar jugador
        player1.update(pantalla,vx,vy,t)
        
       
        #poner rectangulos
        pygame.draw.rect(pantalla,rojo,r1)
        
        #actualizar pantalla
        pygame.display.update()
        
        

        

                
    pygame.quit()




## Menu que seria la pantalla principal antes de iniciar el juego. La principal es MAIN. FALTA HACERLO MAS LINDO

def menu():
    import pygame
    pygame.init()
    
    
    pantalla=pygame.display.set_mode((900,700))
    pygame.display.set_caption(": EL TRABAJO PRACTICO : ")
    relojmenu = pygame.time.Clock()
    titulo=pygame.image.load("placeholder.png").convert_alpha()
    
    newgame = Boton(pygame.image.load("jugar1.png").convert_alpha(),
                    pygame.image.load("jugar2.png").convert_alpha(),300,195)
    
    controles = Boton(pygame.image.load("controles1.png").convert_alpha(),
                     pygame.image.load("controles2.png").convert_alpha(),300,370)
    
    salir = Boton(pygame.image.load("salir1.png").convert_alpha(),
                  pygame.image.load("salir2.png").convert_alpha(),300,545)      #USAR ESTAS POS PARA LOS OTROS BOTONES
    
    
    fuente1=pygame.font.SysFont("Arial", 30, False, False)
    
    
    cont=False
    
    c1=cursor()
    loadgamebool=None
    
    #Loop Principal!
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()           # RETURN NONE PARA SALIR
                return None
            if event.type==pygame.MOUSEBUTTONDOWN:
                if c1.colliderect(newgame.rect):
                    pygame.quit()
                    return False
                elif c1.colliderect(controles.rect):
                    cont=True
                elif c1.colliderect(salir.rect):
                    pygame.quit()
                    return None
                
                
                
                
        pantalla.fill((0,0,0))
        relojmenu.tick(15)
        pantalla.blit(titulo,(300,5)) #Posicion del titulo del juego
        #TEXTOS PARA CONTROLES
        movim=fuente1.render("-Movimiento: Flechas Direccionales",0,(255,255,255))
        atack1=fuente1.render("-Ataque 1: A",0,(255,255,255))
        atack2=fuente1.render("-Ataque 2: D",0,(255,255,255))
        atack3=fuente1.render("-Ataque 3: F",0,(255,255,255))
        paus= fuente1.render("-Pulsa P para pausar el juego",0,(255,255,255))
        newgame.pintar(pantalla, c1)
        if cont==False:
            controles.pintar(pantalla, c1)
        salir.pintar(pantalla,c1)
        
        c1.updatecursor()
        
        if cont==True:
            pantalla.blit(movim,(230,310))
            pantalla.blit(atack1,(230,350))
            pantalla.blit(atack2,(230,390))
            pantalla.blit(atack3,(230,430))
            pantalla.blit(paus,(230,470))
        
            
    
        
        pygame.display.update()
                    
    
#FUNCION START QUE CONTROLA LOS PASOS DE PANTALLA
        
        
def start(loadbool=None):
    if loadbool==None:
        loadbool=menu()
    if not(loadbool==None):
        a=main(loadbool)
        if a==True:
            start(True)
        
start()


        
        

    
    
