import pygame
import time
from pygame import font



class Fondo(pygame.sprite.Sprite):
    import pygame
    
    def __init__(self):
        self.imagen=pygame.image.load("Mapa1Final.png").convert_alpha()
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
        
        if cursor.colliderect(self.rect): 
            self.setImage(self.imagenseleccion)
            
        else:
            self.setImage(self.imagennormal)
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
    import time
    pygame.init()

    
    pygame.mixer.music.load("Sonidos/bosque.mid")
    pygame.mixer.music.play(300)
    
    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Vengeance")
    salir=False
    reloj1= pygame.time.Clock()
    
    #creo un player
    player1=Player()
    
    fondo1=Fondo()
    vx,vy=0,0
    velocidad=32
    
    #COLORCITOS
    rojo=(250,0,0)
    
    time.sleep(2)
    pygame.mixer.music.load("Sonidos/bosque.mid")
    pygame.mixer.music.play(300)
   
    
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
                
                #PAUSA WORK IN PROGRESS
                if event.key == pygame.K_p: #PAUSA WORK IN PROGRESS
                    estaPausado=True
                    pausa(pantalla,estaPausado)    
                    
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
        
       
        
        #actualizar pantalla
        pygame.display.update()
        
        

        

                
    pygame.quit()




## Menu que seria la pantalla principal antes de iniciar el juego. La principal es MAIN. FALTA HACERLO MAS LINDO

def menu():
    import pygame
    pygame.init()
    
    pygame.mixer.music.load("Sonidos/menu.mid")
    pantalla=pygame.display.set_mode((900,700))
    pygame.display.set_caption("Vengeance")
    relojmenu = pygame.time.Clock()
    titulo=pygame.image.load("Vengeance/Titulo.png").convert_alpha()
    descripcion=pygame.image.load("Vengeance/descripcion.png").convert_alpha()
    pygame.mixer.music.play(30)
    
    newgame = Boton(pygame.image.load("Vengeance/jugar1.png").convert_alpha(),
                    pygame.image.load("Vengeance/jugar2.png").convert_alpha(),280,290)
    
    controles = Boton(pygame.image.load("Vengeance/controles.png").convert_alpha(),
                     pygame.image.load("Vengeance/controles2.png").convert_alpha(),280,370) # 280 para igualar chaboncito
    
    salir = Boton(pygame.image.load("Vengeance/salir.png").convert_alpha(),
                  pygame.image.load("Vengeance/salir1.png").convert_alpha(),280,460)      #USAR ESTAS POS PARA LOS OTROS BOTONES
    
    
    fuente1=pygame.font.SysFont("Arial", 30, False, False)
    
    selec1=pygame.mixer.Sound("selec.wav")  
    
    cont=False
    
    pygame.mixer.stop()
    
    
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
                    selec1.play()
                    pygame.quit()
                    return False
                elif c1.colliderect(controles.rect):
                    selec1.play()
                    cont=True
                elif c1.colliderect(salir.rect):
                    selec1.play()
                    pygame.quit()
                    return None
                
                
                
                
        pantalla.fill((0,0,0))
        relojmenu.tick(15)
        pantalla.blit(titulo,(50,-20)) #Posicion del titulo del juego
        pantalla.blit(descripcion,(170,660))  #Descripcion que va abajo de las opciones
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
            
            

def pausa(pantalla,estaPausado):
    import pygame
    fondopausa = pygame.image.load("Vengeance/menupausa.png")
    while estaPausado == True:
        pantalla.blit(fondopausa,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        estaPausado=False
        pygame.display.update()            
    return                
        
    



  
start()


        


    
    
