import pygame
from var import *
from random import randint
import sys
from time import sleep

pygame.init()

Loading = ":-:-:-:-:-:-:-:LOADING:-:-:-:-:-:-:-:-\n01001101 01011001 11110101 01000011 01010010 01010101 01010011 01001000 11110101 01010100 01000001 01001110 01010101\n\n\n"

def draw(screen,obj,x,y):
    screen.blit(obj,(x,y))

def boundry(objx,objx_change,obj_width,objy,objy_change,obj_height,got,speed):
    if objx < 0:
       objx_change = speed
    elif objx > 800 - obj_width:
        objx_change = -speed
    elif objy < 0:
        objy_change = speed
    elif objy > 600 - obj_height:
        if got == 1:
           objy_change = -speed
        else:
            pass
    return objx_change,objy_change

def collison(obj1_y,obj2_y,obj1y_change):
    if (obj1_y + 30 ) > (obj2_y+1):
        obj1y_change = -obj1y_change

def addtext(text,x,y,color): # TEXT DISPLAY KARNE KE LIYE
    font = pygame.font.Font('font/hello.ttf',50)
    TextSurf, TextRect = Text_o(text,font,color)
    TextRect.center  = ((x),(y))
    gamedisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def Text_o(text,font, color):
    textSurface = font.render(text,True,color)
    return textSurface, textSurface.get_rect()

def controller(padx_change,pady_change,needed):
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
            pygame.quit()
    
     elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                padx_change = -10
            elif event.key == pygame.K_RIGHT:
                padx_change = 10
            elif event.key == (pygame.K_t):
                needed += 1
     elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 padx_change = 0

     return padx_change,pady_change,needed


def fish(fish1x,fish1y,fish2x,fish2y):
    if fish1x < -20:
     fish1x = 825
     fish1y += f1changey
     if fish1y > 600:
         fish1y = -25
    if fish2x < -40:
     fish2x = 850
     fish2y += f2changey
     if fish2y > 600:
         fish2y = -200
    return fish1x,fish1y,fish2x,fish2y

def scores(pady,sp,ballspeed,padspeed):
    if pady < 570 and pady> 550:
        sp = 10
        ballspeed = 10
        padspeed = 10
    elif pady <550 and pady > 500:
        sp = 20
        ballspeed = 12
    elif pady <500 and pady > 450:
        sp = 30
    elif pady < 450 and pady > 400:
        sp = 40
        ballspeed = 15
        padspeed = 12
    elif pady < 400 and pady > 350:
        sp = 80
        ballspeed = 17
        padspeed = 15
    elif pady < 350 and pady > 300:
        sp = 160
        ballspeed = 20
        padspeed = 17
    elif pady < 300 and pady > 250:
        sp = 320
        ballspeed = 22
        padspeed = 20
    elif pady < 250:
        sp = 640
        ballspeed = 25
        padspeed = 22
    return sp,ballspeed,padspeed

def highscore(score):
    if score in range(0,100):
        rating = "Damm!Go And think About how to kill yourself"
    elif score in range(101,300):
        rating = "Alright"
    elif score in range(301,500):
        rating = "Hmm, Good"
    elif score in range(501,800):
        rating = "Whoa! Control Yourself Man!! "
    elif score in range(801,1000):
        rating = "O....M....G...."
    elif score in range(1001,1500):
        rating = "[IN JANICE'S VOICE] OH...MY...GOD!!! "
    elif score in range(1501,2000):
        rating = "TO BE HONEST I NEVER THOUGHT ANYONE WOULD BE ABLE TO READ THIS, MAN!"
    elif score > 2000:
        tellem()
    addtext('YOU MADE : %s POINTS'% score,display_width/2,display_height/2,(250,green,blue))
    addtext('RATING: %s '% rating ,display_width/2,display_height/2 + 100,(0,225,252))
    sleep(2)
    

def secret_message():
    pygame.quit()
    for char in Loading:
        sleep(0.04)
        sys.stdout.write(char)
    print "Very Good! you just unlocked a SECRET MSG #1 my friend"
    print "Allright! so do you want to know a secret?"
    print "Here it is then!!"
    print "You really think I'll tell you this easily?"
    print "Well if you know what [ AVAT ] means then you already know the secret......Yeah you are right it's about the MOTIVATORS!!\n"
    q = "01000011 01010010 01010101 01010011 01001000\n"
    for char in q:
        sleep(0.04)
        sys.stdout.write(char)
    print "On the other hand if you don't kwo what [ AVAT ] means...then there is only 0.5% chance that you know the secret"
    print "OK, so I'll tell you some names, ( I REALLY SHOULD SAY HINTS )"
    print "================================"
    print "\t [ 1 ] 8165 [ B /- S E - 2 ] "
    print "\t [ 2 ] /- P"
    print "\t [ 3 ] Grand Theft Auto: 4 [ _ C ] "
    print "\t [ 4 ] Between 0000HOURS and 1159HOURS [ /- \ | ] "
    print "================================"
    print "HAVE FUN  WANDERING, BYE BYE !!"
    input()
    quit()
def tellem():
    pygame.quit()
    msg = "Alright, you deserv this,here you go this is SECRET MESSAGE #2"
    for char in msg:
        sleep(0.4)
        sys.stdout.write(char)

    print "\t [ 1 ] 8165 [ B /- S E - 2 ] #### WELL, I'M NOT TELLING THIS ONE JUST SEE THE BINARY IN \"SECRET MSG #1\" "
    print "\t [ 2 ] /- P #### IT'S [ AP ] "
    print "\t [ 3 ] Grand Theft Auto: 4 [ _ C ] #### IT'S [ LC ] "
    print "\t [ 4 ] Between 0000HOURS and 1200HOURS [ /- \ | ] #### YOU MAY HAVE GUESSED IT , IT'S [ AM ] AS IN [ 12AM TO 11:59AM ] "
    input()
    quit()
