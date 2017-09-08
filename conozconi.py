import random
import sys
import time
import pygame
from pygame.locals import *
#from gi.repository import Gtk

pygame.mixer.pre_init(44100, -16, 4, 2048)
pygame.init()

d_width = 1200
d_height = 900

game_display = pygame.display.set_mode((d_width, d_height))

class Nave(pygame.sprite.Sprite):
    def __init__(self,width,height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load("/images/nave.png")
        self.image = pygame.transform.scale(self.image, (width,height))
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
    def explosion(self):
        pass
        #aqui se hace la logica de explosion
    def mover(self, x, y):
        #aqui se realiza el metodo blit para mover  la nave
        game_display.blit(self.image, (x,y))

class Alien(pygame.sprite.Sprite):
    def __init__(self,width,height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.height = height
        self.width = width
        self.image = pygame.image.load("/images/alien.png")
        self.image = pygame.transform.scale(self.image, (width,height))
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
    def alegrarse(self, x,y):
        self.happy = pygame.image.load("/images/alien-happy.png")
        self.happy = pygame.transform.scale(self.happy, (self.width,self.height))
        game_display.blit(self.happy, (x,y))
    def asustarse(self, x,y):
        self.startle = pygame.image.load("/images/alien-fear.png")
        self.startle = pygame.transform.scale(self.startle, (self.width,self.height))
        game_display.blit(self.startle, (x,y))
    def entristecerse(self,x, y):
        self.sad = pygame.image.load("/images/alien-sad.png")
        self.sad = pygame.transform.scale(self.sad, (self.width,self.height))
        game_display.blit(self.sad, (x,y))
    def hablar(self, texto, x, y):
        #toda la logica para producir texto en pygame.
        pass

class Alerta(pygame.sprite.Sprite):
    def __init__(self,width,height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.height = height
        self.width = width
        self.image = pygame.image.load("/images/alerta.png")
        self.image = pygame.transform.scale(self.image, (width,height))
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
    def blink(self, x, y):
        game_display.blit(self.image, (x,y))
        game_display.blit(self.image, (30000,30000))
        game_display.blit(self.image, (x,y))        

class Planeta(pygame.sprite.Sprite):
     def __init__(self,width,height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.height = height
        self.width = width
        self.image = pygame.image.load("/images/planeta.png")
        self.image = pygame.transform.scale(self.image, (width,height))
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

class intro:
    def __init__(self):
        self.alien = Alien(218,268)
        self.planeta = Planeta(500,500)
        self.nave = Nave(200,100)
        self.alerta = Alerta(200,200)
    def run():
        #logica de introduccion
        pass