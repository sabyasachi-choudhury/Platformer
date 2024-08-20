# Imports
from pygame.locals import *
from vars import *

pygame.init()


# Square
class Square(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super(Square, self).__init__()
        self.surf = pygame.transform.smoothscale(img, (2 * block_len, 2 * block_len))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(center=(x, y))
        self.id = 'sq'


# Rect
class Rectangle(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super(Rectangle, self).__init__()
        self.surf = pygame.transform.smoothscale(img, (2*block_len, block_len))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(center=(x, y))
        self.id = 'rc'


# Small Square
class Small(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super(Small, self).__init__()
        self.surf = pygame.transform.smoothscale(img, (block_len, block_len))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(center=(x, y))
        self.id = 'sm'


# Pillar
class Pillar(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super(Pillar, self).__init__()
        self.surf = pygame.transform.smoothscale(img, (block_len, 2*block_len))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(center=(x, y))
        self.id = 'pl'


# Fire
class Fire(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super(Fire, self).__init__()
        self.surf = pygame.transform.smoothscale(img, (2*block_len, block_len))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(center=(x, y))
        self.id = 'fire'


# class Lava
class Lava(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super(Lava, self).__init__()
        self.surf = pygame.transform.smoothscale(img, (2*block_len, block_len))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(center=(x, y))
        self.id = 'lava'


# Spikes
class Spike(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super(Spike, self).__init__()
        self.surf = pygame.transform.smoothscale(img, (2*block_len, 2*block_len))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(center=(x, y))
        self.id = 'spike'


# gem
class Gem(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super(Gem, self).__init__()
        self.surf = pygame.transform.smoothscale(img, (block_len, block_len))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(center=(x, y))
        self.id = 'gem'


# Player
class Player(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super(Player, self).__init__()
        self.surf = pygame.transform.smoothscale(img, (int(1.2*block_len), int(1.8*block_len)))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(center=(x, y))
        self.id = 'player'
        self.guide = pygame.rect.Rect(self.rect.centerx+100, self.rect.centery-130, 200, 200)
        self.vel_x = 9

    def motion(self, press, sc_x_dir, sc_y_dir, p_x):
        if press[K_RIGHT]:
            self.rect.move_ip(self.vel_x, 0)
            p_x = 1
        if press[K_LEFT]:
            self.rect.move_ip(-self.vel_x, 0)
            p_x = -1

        if self.rect.right > self.guide.right:
            self.rect.right = self.guide.right
            sc_x_dir = -1
        if self.rect.left < self.guide.left:
            self.rect.left = self.guide.left
            sc_x_dir = 1
        if self.rect.top < self.guide.top:
            self.rect.top = self.guide.top
            sc_y_dir = 1
        if self.rect.bottom > self.guide.bottom:
            self.rect.bottom = self.guide.bottom
            sc_y_dir = -1

        return sc_x_dir, sc_y_dir, p_x

    def jump(self, event, p_y, g):
        if event.key == K_UP or event.key == K_SPACE:
            g = -13
            p_y = -1

        return p_y, g


# Needed vars
class_list = [Pillar, Pillar, Rectangle, Small, Small, Square, Square, Square, Square, Gem, Lava, Spike, Fire, Player]


# Decipher
def decipher(code):
    return_group = pygame.sprite.Group()
    for para in code:
        for i in range(len(id_list)):
            if para[0] == id_list[i]:
                return_group.add(class_list[i](base_img_list[i], para[1], para[2]))
    return return_group


# Gravity
def gravity(body, vel):
    body.rect.move_ip(0, vel)
    if vel < 13:
        vel += 1
    return vel