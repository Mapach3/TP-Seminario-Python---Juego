import pygame
from Personaje import *
from Times import *
from Fondo import *
from imagenes import *
from ImagenesJefe import ListaAnimacionesJefe

def moverCosasPantalla(personaje,fondo,pantalla,vx,vy,t,suceso,listaFlechas,listaWalls,listaEnemigos):
    fondo.update(pantalla,vx,vy,personaje)
    vx_enemigo = vx
    vy_enemigo = vy
    colision=False
    for wall in listaWalls:
            if personaje.moviendo:
                wall.move_ip(-vx,-vy)
    for wall in listaWalls:
            if wall.colliderect(personaje.rect):
                vx,vy=-vx,-vy
                colision=True
                break    
    if colision==True:
        fondo.update(pantalla,vx,vy,personaje)
        for wall in listaWalls:
            wall.move_ip(-vx,-vy)
        vx_enemigo = 0
        vy_enemigo = 0
    for enemigo in listaEnemigos:
        enemigo.update(pantalla, t, listaEnemigos, personaje, vx_enemigo, vy_enemigo, listaFlechas, colision)
     
        
   

    personaje.update(pantalla, t, False, suceso, vx, vy,listaFlechas,colision)
    for flecha in listaFlechas:
        flecha.update(pantalla,listaFlechas,personaje,vx,vy,t)


def main():
    import pygame
    suceso = "no atacando"
    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    salir=False
    reloj = pygame.time.Clock()
    fondo = Fondo(pygame.image.load("Mapa1Final.png"),0,-0)
    gameover=pygame.image.load("GameOver.png")
    listaFlechas = []
    listaWalls=[]
    listaEnemigos=[]
    listaWalls=[pygame.Rect(255,290,3,1200),pygame.Rect(256,1533,833,3),
                pygame.Rect(1090,1344,3,200),pygame.Rect(1087,833,3,325),
                pygame.Rect(1088,288,3,360),pygame.Rect(269,244,818,3),
                pygame.Rect(302,332,116,430),pygame.Rect(432,332,43,60),
                pygame.Rect(292,836,188,170),pygame.Rect(305,1100,114,80),
                pygame.Rect(370,1220,26,80),pygame.Rect(299,1389,122,80),
                pygame.Rect(495,1396,80,95),pygame.Rect(578,293,190,160),
                pygame.Rect(873,332,182,60),pygame.Rect(865,875,190,289),
                pygame.Rect(938,1387,119,60),pygame.Rect(1056,1346,219,3),
                pygame.Rect(1056,1150,221,3),pygame.Rect(1088,832,191,3),
                pygame.Rect(1088,640,192,3),pygame.Rect(1279,320,3,308),
                pygame.Rect(1275,275,3427,3),pygame.Rect(4703,320,3,614),
                pygame.Rect(4703,934,180,3),pygame.Rect(4895,800,32,133),
                pygame.Rect(4929,789,577,3),pygame.Rect(5506,800,29,415),
                pygame.Rect(4895,1119,33,19),pygame.Rect(4929,1184,573,30),
                pygame.Rect(4703,1119,192,3),pygame.Rect(4703,1119,3,639),
                pygame.Rect(4600,1601,95,94),pygame.Rect(1330,1596,3126,71),
                pygame.Rect(1319,1759,3096,3),pygame.Rect(1260,1406,1,354),
                pygame.Rect(1279,832,3,311),pygame.Rect(1350,360,309,55),
                pygame.Rect(1637,481,380,90),pygame.Rect(1611,619,405,68),
                pygame.Rect(1636,757,253,50),pygame.Rect(2015,370,2625,44),
                pygame.Rect(1578,1186,1079,90),pygame.Rect(1578,1276,916,104),
                pygame.Rect(2189,492,467,88),pygame.Rect(2189,580,724,70),
                pygame.Rect(2474,705,184,465),pygame.Rect(2883,963,190,637),
                pygame.Rect(2848,1311,30,1),pygame.Rect(3239,484,120,446),
                pygame.Rect(4040,584,560,180),pygame.Rect(4608,705,30,59),
                pygame.Rect(3647,734,159,150),pygame.Rect(3749,1090,252,449),
                pygame.Rect(2016,1567,30,33),pygame.Rect(4549,1794,53,1),
                pygame.Rect(4419,1924,53,1),pygame.Rect(4550,2019,53,1),
                pygame.Rect(4415,1761,3,444),pygame.Rect(4607,1761,3,444),
                pygame.Rect(4414,2208,194,3),pygame.Rect(4640,833,3,106),
                pygame.Rect(4642,1120,3,106),pygame.Rect(5408,895,96,1),
                pygame.Rect(5440,927,63,31),pygame.Rect(5439,1056,63,31),
                pygame.Rect(5408,1088,96,31)]
    personaje = Personaje.Personaje()
    enemigo1 = Enemigo("mob1", ListaAnimacionesMob1, 800, 600, 0, 100, 50, 2, 2, 10)
    enemigo2 = Enemigo("Boss 1", ListaAnimacionesJefe, 1000, 1200, 0, 100, 50, 2, 2, 10)
    listaEnemigos = [enemigo1,enemigo2]
    vx,vy=0,0
    t = Times()
    teleport_hielo=pygame.Rect(255,290,400,500)
    leftsigueapretada,rightsigueapretada,downsigueapretada,upsigueapretada= False,False,False,False
    rojo=(250,0,0)
    
    pantalla.blit(personaje.imagen,personaje.rect)
    while salir!=True:#LOOP PRINCIPAL
        reloj.tick(28)
        suceso = "no atacando"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            else:                                                                                    
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_ESCAPE:
                        return False
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada = True
                        vx = -personaje.velocidad
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada = True
                        vx = personaje.velocidad
                    if event.key == pygame.K_UP:
                        upsigueapretada = True
                        vy = -personaje.velocidad
                    if event.key == pygame.K_DOWN:
                        downsigueapretada = True
                        vy = personaje.velocidad
                    
                    if event.key == pygame.K_a:
                        suceso = "espadazo"

                    if event.key == pygame.K_s:
                        suceso = "flechazo"
                        
                    if event.key == pygame.K_d:
                        suceso = "poder"
                        
                    if event.key == pygame.K_q:
                        personaje.usarPota()
                    
                    #CON U PASAS AL MAPA DE HIELO
                    if event.key == pygame.K_u:
                        hielo(personaje)
                     
                    #CON Y PASAS AL MAPA DE BOSSFIGHT
                    if event.key == pygame.K_y:
                        bossfight(personaje)
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada = False
                        if rightsigueapretada: 
                            vx = personaje.velocidad
                        else:
                            vx = 0
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada = False
                        if leftsigueapretada:
                            vx = -personaje.velocidad
                        else:
                            vx = 0
                    if event.key == pygame.K_UP:
                        upsigueapretada = False
                        if downsigueapretada:
                            vy = personaje.velocidad
                        else:
                            vy = 0
                    if event.key == pygame.K_DOWN:
                        downsigueapretada = False
                        if upsigueapretada:
                            vy = -personaje.velocidad
                        else:
                            vy = 0          
                    
                    
                    
                    

        pantalla.fill((0,0,170))
        if t.gameover == True:
            gameoversonido.play()
            pantalla.blit(gameover,(0,0))
        else:
            t.update_times()
            moverCosasPantalla(personaje,fondo,pantalla,vx,vy,t,suceso,listaFlechas,listaWalls,listaEnemigos)
        pygame.draw.rect(pantalla,rojo,teleport_hielo)
        pygame.display.update()
        pygame.draw.rect(pantalla,(255,0,0),puertaHielo)
            
    pygame.quit()
    
    
def hielo(personaje):
    import pygame
    pygame.init()
    suceso = "no atacando"
    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    pygame.display.set_caption("::: Vengeance :::")
    salir=False
    reloj = pygame.time.Clock()
    fondo = Fondo(pygame.image.load("MapaHieloFinal.png"),0,-0)
    gameover=pygame.image.load("GameOver.png")
    listaFlechas = []
    listaWalls=[]
    listaEnemigos=[]
    listaWalls=[pygame.Rect(255,290,3,1200),pygame.Rect(256,1533,833,3),
                pygame.Rect(1090,1344,3,200),pygame.Rect(1087,833,3,325),
                pygame.Rect(1088,288,3,360),pygame.Rect(269,244,818,3),
                pygame.Rect(302,332,116,430),pygame.Rect(432,332,43,60),
                pygame.Rect(292,836,188,170),pygame.Rect(305,1100,114,80),
                pygame.Rect(370,1220,26,80),pygame.Rect(299,1389,122,80),
                pygame.Rect(495,1396,80,95),pygame.Rect(578,293,190,160),
                pygame.Rect(873,332,182,60),pygame.Rect(865,875,190,289),
                pygame.Rect(938,1387,119,60),pygame.Rect(1056,1346,219,3),
                pygame.Rect(1056,1150,221,3),pygame.Rect(1088,832,191,3),
                pygame.Rect(1088,640,192,3),pygame.Rect(1279,320,3,308),
                pygame.Rect(1275,275,3427,3),pygame.Rect(4703,320,3,614),
                pygame.Rect(4703,934,180,3),pygame.Rect(4895,800,32,133),
                pygame.Rect(4929,789,577,3),pygame.Rect(5506,800,29,415),
                pygame.Rect(4895,1119,33,19),pygame.Rect(4929,1184,573,30),
                pygame.Rect(4703,1119,192,3),pygame.Rect(4703,1119,3,639),
                pygame.Rect(4600,1601,95,94),pygame.Rect(1330,1596,3126,71),
                pygame.Rect(1319,1759,3096,3),pygame.Rect(1260,1406,1,354),
                pygame.Rect(1279,832,3,311),pygame.Rect(1350,360,309,55),
                pygame.Rect(1637,481,380,90),pygame.Rect(1611,619,405,68),
                pygame.Rect(1636,757,253,50),pygame.Rect(2015,370,2625,44),
                pygame.Rect(1578,1186,1079,90),pygame.Rect(1578,1276,916,104),
                pygame.Rect(2189,492,467,88),pygame.Rect(2189,580,724,70),
                pygame.Rect(2474,705,184,465),pygame.Rect(2883,963,190,637),
                pygame.Rect(2848,1311,30,1),pygame.Rect(3239,484,120,446),
                pygame.Rect(4040,584,560,180),pygame.Rect(4608,705,30,59),
                pygame.Rect(3647,734,159,150),pygame.Rect(3749,1090,252,449),
                pygame.Rect(2016,1567,30,33),pygame.Rect(4549,1794,53,1),
                pygame.Rect(4419,1924,53,1),pygame.Rect(4550,2019,53,1),
                pygame.Rect(4415,1761,3,444),pygame.Rect(4607,1761,3,444),
                pygame.Rect(4414,2208,194,3),pygame.Rect(4640,833,3,106),
                pygame.Rect(4642,1120,3,106),pygame.Rect(5408,895,96,1),
                pygame.Rect(5440,927,63,31),pygame.Rect(5439,1056,63,31),
                pygame.Rect(5408,1088,96,31)]
    personaje = Personaje.Personaje()
    enemigo1 = Enemigo("mob1", ListaAnimacionesMob1, 800, 600, 0, 100, 50, 2, 2, 10)
    enemigo2 = Enemigo("Boss 1", ListaAnimacionesJefe, 1000, 1200, 0, 100, 50, 2, 2, 10)
    listaEnemigos = [enemigo1,enemigo2]
    vx,vy=0,0
    t = Times()
    vx,vy=0,0
    t = Times()
    
    leftsigueapretada,rightsigueapretada,downsigueapretada,upsigueapretada= False,False,False,False
    
    pantalla.blit(personaje.imagen,personaje.rect)
    
    while salir!=True:#LOOP PRINCIPAL
        reloj.tick(28)
        suceso = "no atacando"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            else:                                                                                    
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_ESCAPE:
                        return False
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada = True
                        vx = -personaje.velocidad
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada = True
                        vx = personaje.velocidad
                    if event.key == pygame.K_UP:
                        upsigueapretada = True
                        vy = -personaje.velocidad
                    if event.key == pygame.K_DOWN:
                        downsigueapretada = True
                        vy = personaje.velocidad
                    
                    if event.key == pygame.K_a:
                        suceso = "espadazo"

                    if event.key == pygame.K_s:
                        suceso = "flechazo"
                        
                    if event.key == pygame.K_d:
                        suceso = "poder"
                        
                    if event.key == pygame.K_q:
                        personaje.usarPota()
                        
                    if event.key == pygame.K_o:
                        main()    
                    
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada = False
                        if rightsigueapretada: 
                            vx = personaje.velocidad
                        else:
                            vx = 0
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada = False
                        if leftsigueapretada:
                            vx = -personaje.velocidad
                        else:
                            vx = 0
                    if event.key == pygame.K_UP:
                        upsigueapretada = False
                        if downsigueapretada:
                            vy = personaje.velocidad
                        else:
                            vy = 0
                    if event.key == pygame.K_DOWN:
                        downsigueapretada = False
                        if upsigueapretada:
                            vy = -personaje.velocidad
                        else:
                            vy = 0   
   
    
    
        pantalla.fill((0,0,170))
        if t.gameover == True:
            gameoversonido.play()
            pantalla.blit(gameover,(0,0))
        else:
            t.update_times()
            moverCosasPantalla(personaje,fondo,pantalla,vx,vy,t,suceso,listaFlechas,listaWalls,listaEnemigos)
        pygame.display.update()
    pygame.quit()
    
    
def bossfight(personaje):
    import pygame
    pygame.init()
    suceso = "no atacando"
    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    pygame.display.set_caption("::: Vengeance :::")
    salir=False
    reloj = pygame.time.Clock()
    fondo = Fondo(pygame.image.load("MapaBossFinal.png"),0,-0)
    gameover=pygame.image.load("GameOver.png")
    listaFlechas = []
    listaWalls=[]
    listaEnemigos=[]
    listaWalls=[pygame.Rect(255,290,3,1200),pygame.Rect(256,1533,833,3),
                pygame.Rect(1090,1344,3,200),pygame.Rect(1087,833,3,325),
                pygame.Rect(1088,288,3,360),pygame.Rect(269,244,818,3),
                pygame.Rect(302,332,116,430),pygame.Rect(432,332,43,60),
                pygame.Rect(292,836,188,170),pygame.Rect(305,1100,114,80),
                pygame.Rect(370,1220,26,80),pygame.Rect(299,1389,122,80),
                pygame.Rect(495,1396,80,95),pygame.Rect(578,293,190,160),
                pygame.Rect(873,332,182,60),pygame.Rect(865,875,190,289),
                pygame.Rect(938,1387,119,60),pygame.Rect(1056,1346,219,3),
                pygame.Rect(1056,1150,221,3),pygame.Rect(1088,832,191,3),
                pygame.Rect(1088,640,192,3),pygame.Rect(1279,320,3,308),
                pygame.Rect(1275,275,3427,3),pygame.Rect(4703,320,3,614),
                pygame.Rect(4703,934,180,3),pygame.Rect(4895,800,32,133),
                pygame.Rect(4929,789,577,3),pygame.Rect(5506,800,29,415),
                pygame.Rect(4895,1119,33,19),pygame.Rect(4929,1184,573,30),
                pygame.Rect(4703,1119,192,3),pygame.Rect(4703,1119,3,639),
                pygame.Rect(4600,1601,95,94),pygame.Rect(1330,1596,3126,71),
                pygame.Rect(1319,1759,3096,3),pygame.Rect(1260,1406,1,354),
                pygame.Rect(1279,832,3,311),pygame.Rect(1350,360,309,55),
                pygame.Rect(1637,481,380,90),pygame.Rect(1611,619,405,68),
                pygame.Rect(1636,757,253,50),pygame.Rect(2015,370,2625,44),
                pygame.Rect(1578,1186,1079,90),pygame.Rect(1578,1276,916,104),
                pygame.Rect(2189,492,467,88),pygame.Rect(2189,580,724,70),
                pygame.Rect(2474,705,184,465),pygame.Rect(2883,963,190,637),
                pygame.Rect(2848,1311,30,1),pygame.Rect(3239,484,120,446),
                pygame.Rect(4040,584,560,180),pygame.Rect(4608,705,30,59),
                pygame.Rect(3647,734,159,150),pygame.Rect(3749,1090,252,449),
                pygame.Rect(2016,1567,30,33),pygame.Rect(4549,1794,53,1),
                pygame.Rect(4419,1924,53,1),pygame.Rect(4550,2019,53,1),
                pygame.Rect(4415,1761,3,444),pygame.Rect(4607,1761,3,444),
                pygame.Rect(4414,2208,194,3),pygame.Rect(4640,833,3,106),
                pygame.Rect(4642,1120,3,106),pygame.Rect(5408,895,96,1),
                pygame.Rect(5440,927,63,31),pygame.Rect(5439,1056,63,31),
                pygame.Rect(5408,1088,96,31)]
    personaje = Personaje.Personaje()
    enemigo1 = Enemigo("mob1", ListaAnimacionesMob1, 800, 600, 0, 100, 50, 2, 2, 10)
    enemigo2 = Enemigo("Boss 1", ListaAnimacionesJefe, 1000, 1200, 0, 100, 50, 2, 2, 10)
    listaEnemigos = [enemigo1,enemigo2]
    vx,vy=0,0
    t = Times()
    vx,vy=0,0
    t = Times()
    
    leftsigueapretada,rightsigueapretada,downsigueapretada,upsigueapretada= False,False,False,False
    
    pantalla.blit(personaje.imagen,personaje.rect)
    
    while salir!=True:#LOOP PRINCIPAL
        reloj.tick(28)
        suceso = "no atacando"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            else:                                                                                    
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_ESCAPE:
                        return False
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada = True
                        vx = -personaje.velocidad
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada = True
                        vx = personaje.velocidad
                    if event.key == pygame.K_UP:
                        upsigueapretada = True
                        vy = -personaje.velocidad
                    if event.key == pygame.K_DOWN:
                        downsigueapretada = True
                        vy = personaje.velocidad
                    
                    if event.key == pygame.K_a:
                        suceso = "espadazo"

                    if event.key == pygame.K_s:
                        suceso = "flechazo"
                        
                    if event.key == pygame.K_d:
                        suceso = "poder"
                        
                    if event.key == pygame.K_q:
                        personaje.usarPota()
                        
                    if event.key == pygame.K_o:
                        main()    
                    
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada = False
                        if rightsigueapretada: 
                            vx = personaje.velocidad
                        else:
                            vx = 0
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada = False
                        if leftsigueapretada:
                            vx = -personaje.velocidad
                        else:
                            vx = 0
                    if event.key == pygame.K_UP:
                        upsigueapretada = False
                        if downsigueapretada:
                            vy = personaje.velocidad
                        else:
                            vy = 0
                    if event.key == pygame.K_DOWN:
                        downsigueapretada = False
                        if upsigueapretada:
                            vy = -personaje.velocidad
                        else:
                            vy = 0   
   
    
    
        pantalla.fill((0,0,170))
        if t.gameover == True:
            gameoversonido.play()
            pantalla.blit(gameover,(0,0))
        else:
            t.update_times()
            moverCosasPantalla(personaje,fondo,pantalla,vx,vy,t,suceso,listaFlechas,listaWalls,listaEnemigos)
        pygame.display.update()
    pygame.quit()    
    

main()
