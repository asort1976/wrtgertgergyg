import pygame
import random
pygame.init()
pygame.font.init()
propusk = 0
f1 = pygame.font.SysFont('Arial', 15)
text1 = f1.render('пропущенно '+str(propusk), True,(180, 0, 0))
WW =510
WH = 500
sc = pygame.display.set_mode((WW, WH))
clock = pygame.time.Clock()
back = pygame.transform.scale(pygame.image.load('fon.png'), (510, 500))
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (15, 70))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        sc.blit(self.image, (self.rect.x, self.rect.y))
class GameSprite1(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        sc.blit(self.image, (self.rect.x, self.rect.y))

class cicle1(GameSprite):
    def qwe(self):
        self.random1 = random.randint(0,1)
    def qwe2(self):
        self.random2 = random.randint(0,1)

    def update(self):
        
        if self.random1 == 0:
           self.rect.x-=2
        if self.random1 == 1:
           self.rect.x+=2
        #if self.rect.x <=5:
         #   self.random1 = 1
        #if self.rect.x>=490:
            #self.random1 = 0
        if self.random2 == 0:
            self.rect.y-=2
        if self.random2 == 1:
            self.rect.y+=2
        if self.rect.y <=5:
            self.random2 = 1
        if self.rect.y>=460:
            self.random2 = 0
 
        

class Player(GameSprite):
    def update(self):

        keyp = pygame.key.get_pressed()
        if keyp[pygame.K_DOWN] and self.rect.y <427:
            self.rect.y += 5
        if keyp[pygame.K_UP] and self.rect.y >0:
            self.rect.y -= 5
class Player1(GameSprite):
    def update1(self):
        keyp = pygame.key.get_pressed()
        if keyp[pygame.K_s] and self.rect.y <427:
            self.rect.y += 5
        if keyp[pygame.K_w] and self.rect.y >0:
            self.rect.y -= 5
ball = pygame.image.load('cicle.png')


n2 = Player('shtuka.png',5,5)
n3 = Player1('shtuka.png',495,5)
n4 = cicle1('cicle.png',250,250)
n4.qwe()
n4.qwe2()
run2= True
run = True
while run:
    if run2:
        text1 = f1.render('пропущенно '+str(propusk), True,(180, 0, 0))
        sc.blit(back,(0,0))
        n2.update()
        n2.reset()
        n3.update1()
        n3.reset()
        n4.reset()
        n4.update()
        sc.blit(text1,(20,20))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    pygame.display.update() 