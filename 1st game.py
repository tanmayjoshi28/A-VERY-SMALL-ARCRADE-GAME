import pygame
import random
import time



black=(0,0,0)
white=(225,225,225)
pygame.init()
gamewin = pygame.display.set_mode((800,600))
pygame.display.set_caption('bullet to The HEAD')
clock=pygame.time.Clock()

pygame.mixer.music.load('Theme.mp3')
pygame.mixer

target=pygame.image.load('hitler.png')
luger=pygame.image.load('luger.png')
bullet=pygame.image.load('bullet.png')


def hitler(x,y):
    gamewin.blit(target,(x,y))

def gun(p,q):
    gamewin.blit(luger,(p,q))
    
def shoot(t,r):
    gamewin.blit(bullet,(t,r))

def textobj(text,font):
    textsurface=font.render(text,True,white)
    return textsurface,textsurface.get_rect()

def killed():
    largetxt=pygame.font.Font('freesansbold.ttf',100)
    textsurf,textrect=textobj("KILL",largetxt)
    textrect.center=((800/2),(600/2))
    gamewin.blit(textsurf,textrect)
    pygame.display.update()
    

def score(o):
    largetxt=pygame.font.Font('freesansbold.ttf',75)
    textsurf,textrect=textobj("Score="+str(o),largetxt)
    textrect.center=((800/2),(600/2))
    gamewin.blit(textsurf,textrect)   
    pygame.display.update()
    time.sleep(1)

def startintro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    gameloop()
        gamewin.fill(black)
        largetxt=pygame.font.Font('freesansbold.ttf',100)
        textsurf,textrect=textobj("KILL HITLER",largetxt)
        textrect.center=((800/2),(600/2))
        gamewin.blit(textsurf,textrect)
        start()
        pygame.display.update()
        clock.tick(15)
                     
def start():
    largetxt=pygame.font.Font('freesansbold.ttf',25)
    textsurf,textrect=textobj("PRESS ENTER TO START",largetxt)
    textrect.center=((800/2),(500))
    gamewin.blit(textsurf,textrect)
    pygame.display.update()
    clock.tick(15)

def pause():
    pause=True
    while pause==True:
        gamewin.fill(black)
        largetxt=pygame.font.Font('freesansbold.ttf',100)
        smalltxt=pygame.font.Font('freesansbold.ttf',25)
        textsurf,textrect=textobj("PAUSED",largetxt)
        textsurf1,textrect1=textobj("[ Y ] TO CONTINUE | [ N ] TO QUIT",smalltxt)
        textrect.center=((800/2),(600/2))
        gamewin.blit(textsurf1,(190,500))
        gamewin.blit(textsurf,textrect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_n:
                    pygame.quit()
                    quit()
                if event.key==pygame.K_y:
                    pause=False
    
def gameloop():
    pygame.mixer.music.play(-1)
    buletcount=0
    
    a=0
    b=0
    xc=0
    yc=0
    a1=600
    b1=0
    a2=900
    b2=900
    yc1=0
    yc2=0
    point=0
    hit=0
    gamexit=False
    while not gamexit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crash=True
                
            # MOVEMENTS of hitler gun bullet
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    xc=-5
                elif event.key==pygame.K_RIGHT:
                    xc=+5
                elif event.key==pygame.K_UP:
                    yc=-5
                elif event.key==pygame.K_DOWN:
                    yc=5
                elif event.key==pygame.K_w:
                    yc1=-7.5
                elif event.key==pygame.K_s:
                    yc1=7.5
                elif event.key==pygame.K_SPACE:  #FOR SCORE
                    a2=590
                    b2=b1+42
                    buletcount=buletcount+1
                elif event.key==pygame.K_TAB:
                    score(hit)
                elif event.key==pygame.K_ESCAPE: #FOR PAUSE
                    pause()

                    
            if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                        xc=0
                        yc=0
                    elif event.key==pygame.K_s or event.key==pygame.K_w:
                        yc1=0
                                          
        
        a=a+xc
        b=b+yc
        b1=b1+yc1
        gamewin.fill(black)
        shoot(a2,b2)
        a2=a2-7
        hitler(a,b)
        gun(a1,b1)
        shoot(a2,b2)
        
        if a >700 or a<0 or b<0 or b>600:
            gamexit=True
        if (b2>b-10 and b2<b+65 and a2>0 and a2<40):
            point=point+1
            killed()
            hit=point/6
        
        pygame.display.update()
        clock.tick(60)
startintro()
gameloop()
pygame.quit()
quit()

