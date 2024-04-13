from pygame import *
from random import randint
from time import time as timer

clock1 = time.Clock()


FPS = 120
player_speed = 8
win_height = 500
win_width = 700
num_fire = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x  -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x  < 595:
            self.rect.x  += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(50 ,650)
            self.rect.y = 0
            lost = lost + 1

       




font.init()
font1 = font.Font('Arial', 36)

finish = False
game = True

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('1234')
#background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))




FPS = 120 
score = 0
 
while game:
    #window.blit(background, (0, 0))

    clock1.tick(FPS)
    display.update()
