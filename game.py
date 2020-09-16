import pygame
import random

pygame.init()
pygame.font.init()
run = True

win_h = 1600
win_w = 900

score = 0
clock = pygame.time.Clock()
win = pygame.display.set_mode((win_h, win_w))
pygame.display.set_caption("CoinCollector")
coin_img = pygame.image.load(r"C:\Users\The Main Character\Videos\Captures\PNG\realcoin.png")
char = pygame.image.load(r"C:\Users\The Main Character\Videos\Captures\PNG\character.png")
bgr = pygame.image.load(r"C:\Users\The Main Character\Videos\Captures\PNG\bgsky.png")
isJump = False

# OOP STUFF _____________________________________________________________________________________
class Player(object):
    def __init__(self, px, py, width, height):
        self.image_s = char
        self.image_b = self.image_s.get_rect()
        self.px = px
        self.py = py
        self.width = width
        self.height = height
        self.vel = 17
        self.jvel = 10
        self.mass = 1
        self.hitbox = (self.px, self.py, self.width, self.height)
    def draw(self, win):
        win.blit(char, (round(timmy.px), round(timmy.py)))
        self.hitbox = (round(self.px), round(self.py), self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox), 2)

class Coin(object):
    def __init__(self, x, y, width, height, radius):
        self.image_s = coin_img
        self.image_b = self.image_s.get_rect()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.mass = 1
        self.radius = radius
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        win.blit(coin_img, (round(coin.x), round(coin.y)))
        self.hitbox = (self.x, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), (self.hitbox), 2)

    def coinfalling(self):
        coin.y = coin.y + coin.vel
        if coin.y > win_h:
            coin.x = random.randrange(0, win_w)
            coin.y = -10






    def hit(self):
        if coin.y - coin.radius < timmy.hitbox[1] + timmy.hitbox[3] and coin.y + coin.radius > timmy.hitbox[1]:
            if coin.x + coin.radius > timmy.hitbox[0] and coin.x - coin.radius < timmy.hitbox[0] + timmy.hitbox[2]:
                coin.y = -10
                coin.x = random.randrange(0, win_w)
                global score
                score += 1
                print(score)

# DISPLAY ________________________________________________________________________________

font = pygame.font.SysFont('Comic Sans MS', 30)

def redrawWindow():
    win.blit(bgr, (0, 0))
    coin.draw(win)
    timmy.draw(win)
    win.blit(score_text, (20, 20))
    pygame.display.update()


# GAME MECHANICS _______________________________________________________________________________
#?????????????????????

# GAMELOOP _______________________________________________________________________________
timmy = Player(500, 600, 70, 140)
coin = Coin(random.randint(0, 1550), 0, 70, 70, 35)
while run:

    clock.tick(45)
   
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    score_text = font.render("Score:" + str(score), 1, (255, 0, 0))
    redrawWindow()
    coin.coinfalling()
    coin.hit()
    #NEED HELP
    if score > 5:
        coin.y += 5
    if score == 50:
        coin.y += 5

    # MOVEMENT ______________________________________________________________________________
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and timmy.px < 1600 - timmy.vel - 40:
        timmy.px += timmy.vel
    elif keys[pygame.K_LEFT] and timmy.px > 10:
        timmy.px -= timmy.vel
    if isJump == False:
        if keys[pygame.K_SPACE]:
            isJump = True
    if isJump:
        F = (1/2)*timmy.mass*(timmy.jvel**2)
        timmy.py-=F
        timmy.jvel = timmy.jvel-1
        if timmy.jvel < 0:
            timmy.mass =-1
        if timmy.jvel == -11:
            isJump = False

            timmy.jvel = 10
            timmy.mass = 1
    pygame.display.flip()