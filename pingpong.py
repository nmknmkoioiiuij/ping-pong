from pygame import *
from random import randint






FPS = 120
player_speed = 8
win_height = 500
win_width = 700
num_fire = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x,player_y,player_speed, widht,height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (widht,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y -= self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y -= self.speed

back = (235, 103, 52)
win_height = 500
win_width = 700


game = True
finish = False
clock = time.Clock()
fps = 120


racket1 = Player('racket.png',)
racket2 = Player('racket.png',)




font.init()
font1 = font.Font('Arial', 36)
font1 = font.Font('Arial', 36)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180,0,0))
lose2 = font2.render('PLAYER 2 LOSE!', True, (180,0,0))
finish = False
game = True

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('1234')
#background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))




FPS = 120 
score = 0
speed_x = 3
speed_y = 3
while game:
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1

    if ball.rect.x < 0:
        finish = False
        window.blit(lose1, (200, 200))
        window.blit(lose2, (200, 200))
    #window.blit(background, (0, 0))

    clock.tick(FPS)
    display.update()
