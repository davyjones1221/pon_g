import pygame
from defs import *
from var import *
import PyIgnition,pygame,sys,math

pygame.init()

display_width = 800
display_height = 600
gamedisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('P-O-N-G-2.0')

ball = pygame.image.load('sprites/ball.png')
bat = pygame.image.load('sprites/bat.png')
clock = pygame.time.Clock()
fps = 60
white = (255,255,255)
colours = {'white':(255,255,255),'dark_cream':(255,255,200),'cream':(250,200,150),'red':(255,0,0),'green':(0,255,0),'blue':(0,0,255)}
bg = pygame.image.load('sprites/bg.bmp').convert()

fish1 = pygame.image.load('sprites/fish1.png')
fish2 = pygame.image.load('sprites/fish2.png')
""" FISH """
#Fish1 = small black

f1changex = -0.5
f1changey = 200
fish1x = 100
fish1y = 100

#Fish2 = Black shark

f2changex = -1
f2changey = 300
fish2x = 100
fish2y = 500

padx =100
pady = 550

ballx = 400
bally = 300
ballx_change = -10
bally_change = -10
ball_width = 30

padx_change = 0
pady_change = 0
pad_width = 267


angle = 1

effect = PyIgnition.ParticleEffect(gamedisplay,(0,0),(display_width,display_height))
source = effect.CreateSource(initspeed = 1.0, initdirection = 0.0, initspeedrandrange = 0.5, initdirectionrandrange = math.pi, particlelife = 1000, colour = (200, 255, 200), drawtype = PyIgnition.DRAWTYPE_BUBBLE, radius = 4.0)

effect.CreateDirectedGravity(strength = 0.04, direction = [0, -1])

p = 0
score = 0
needed = 0
wow = pygame.image.load('sprites/wow.png')

red = 100
green = 100
blue = 100

padup = 0.00000000001
padupplus = 0.00001
scorex = 0
sp = 5
ballspeed = 10
padspeed = 10
lives = 3


jukebox = {'music1':'music/m1.mp3','music2':'music/m2.mp3','music3':'music/m3.mp3','music4':'music/m4.mp3'}
