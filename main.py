from pygame import *


class Object(sprite.Sprite):
    def __init__(self,player_image,x,y,w,h,speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = speed
        self.rect  = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

    def move(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 550:
            self.rect.y += self.speed
        if keys[K_d] and self.rect.x < 700:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed

    
    direction = 'right'
    def move2(self):
        if self.rect.x > 600:
            self.direction = 'left'
        if self.rect.x < 100:
            self.direction = 'right'
        
        if self.direction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        # картинка стіни - прямокутник потрібних розмірів і кольору
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
        # кожен спрайт має зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


window = display.set_mode((800,600))
picture = transform.scale(image.load("fon.webp"),(800,600))


player1 = Object("lina.png",100,100,100,50,10)
player2 = Object("crystalmaiden.png",200,200,100,50,10)

wall1 = Wall(3,7,8,100,200,50,200)
wall2 = Wall(3,7,8,350,400,200,250)
wall3 = Wall(3,7,8,350,1,200,250)



clock = time.Clock()

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 





    window.blit(picture,(0,0))
    player1.reset()
    player2.reset()

    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()

    player1.move()
    player2.move2()

    if sprite.collide_rect(player1,player2):
        game = False
    

   

    display.update()
    clock.tick(60)