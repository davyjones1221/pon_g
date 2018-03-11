import pygame
from defs import *
from var import *
import PyIgnition,pygame,sys,math
from random import randint
from time import sleep
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load(jukebox['music1'])
pygame.mixer.music.play()
pygame.mixer.music.load(jukebox['music2'])
pygame.mixer.music.play()
pygame.mixer.music.load(jukebox['music3'])
pygame.mixer.music.play()
pygame.mixer.music.load(jukebox['music4'])
pygame.mixer.music.play()



while True:
 try:
  gamedisplay.fill(colours['white'])
  image = pygame.transform.rotate(ball,angle)
  try:
    padx_change,pady_change,needed = controller(padx_change,pady_change,needed)
  except:
     pass
  pbouncex,pbouncey = boundry(padx,padx_change,pad_width,0,0,0,0,padspeed)
  bbouncex,bbouncey = boundry(ballx,ballx_change,ball_width,bally,bally_change,28,0,ballspeed)

  try:
      padx_change = pbouncex
    
      if (bally+30) >= pady and (bally+30) < (pady+30) and (ballx+28) in range(padx,padx+267):
            bally_change = -10
            source.CreateKeyframe(source.curframe + 1, pos = (ballx+28,bally+30), particlesperframe = 2)
            source.CreateKeyframe(source.curframe + 2, pos = (ballx+28,bally+30), particlesperframe = 0)
            score += sp
            p = 50
      else:
            bally_change = bbouncey
            ballx_change = bbouncex
  except:
     pass


  fish1x,fish1y,fish2x,fish2y = fish(fish1x,fish1y,fish2x,fish2y)
 
  ballx += ballx_change
  bally += bally_change
 
  padx += padx_change
  pady -= padup
  padup += padupplus

 
  fish1x += f1changex
  fish2x += f2changex
 
 
  draw(gamedisplay,bg,0,0)
  draw(gamedisplay,fish1,fish1x,fish1y)
  draw(gamedisplay,fish2,fish2x,fish2y)
  draw(gamedisplay,image,ballx,bally)
  draw(gamedisplay,bat,padx,pady)
  addtext('Score: %s' % score,(display_width/2),(display_height/30),colours['cream'])
  addtext('Lives: %s' % lives,(display_width/2),(500),(red,green,blue))

        
  if pady < 200:
     padup = 0
     padupplus = 0
     
  sp,ballspeed,padspeed = scores(pady,sp,ballspeed,padspeed)
 
  if p >=1:
     addtext('+%s'% sp,100,150,(250,green,blue))
     
     pygame.display.update()

     red += 20
     if red>255:
         red = red-255

  p-= 1
  effect.Update()
  effect.Redraw()
  pygame.display.update()
  angle += 80
  clock.tick(60)
  if needed == 10:
     secret_message()
  if bally > 605:
     bally = 300
     padx = 400
     lives -= 1
     green += 25
     blue += 25
     if green > 250: 
         green += green - 250
     elif blue > 250:
         blue += blue - 250
  if lives == 0:
     highscore(score)
     lives = 3
     score = 0
     pady = 550
     padx = 400
     bally = 300
     sleep(1)
     padup = 0.00000000001
     padupplus = 0.00001
     scorex = 0
     sp = 5
     ballspeed = 10
     padspeed = 10


 except:
     pass
