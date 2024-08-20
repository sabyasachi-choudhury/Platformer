# Imports
from vars import *


# Background class
class Background(pygame.sprite.Sprite):
    def __init__(self, image, x):
        super(Background, self).__init__()
        self.surf = pygame.transform.smoothscale(image, (s_width, s_height))
        self.rect = self.surf.get_rect(center=(x, s_height/2))


# Cave Background
class BgSurface(pygame.sprite.Sprite):
    def __init__(self):
        super(BgSurface, self).__init__()
        self.surf = pygame.Surface((s_width, s_height))
        self.rect = self.surf.get_rect(center=(s_width/2, s_height/2))
        self.surf.fill((144, 156, 156))


# Background stuff
cave_air = BgSurface()
bg_file_list = ["layer1.png", "layer2.png"]
bg_img_list = [pygame.image.load(img).convert_alpha() for img in bg_file_list]
l1 = Background(bg_img_list[0], s_width/2)
l2 = Background(bg_img_list[1], s_width/2)
layer_list = [pygame.sprite.Group(l1), pygame.sprite.Group(l2)]
head_list = [pygame.sprite.Group(l1), pygame.sprite.Group(l2)]


# def parallax(s_xdir, s_ydir):
#     for i in range(len(layer_list)):
#         ind = 0
#         for x in layer_list[i]:
#             ind += 1
#             x.rect.move_ip(s_xdir * vel_list[i], s_ydir * vel_list[1])
#             # Adding to left
#             if x.rect.left > 0 and ind == len(layer_list[i]) and not x.rect.centerx > s_width:
#                 new_bg = Background(bg_img_list[i], x.rect.centerx - s_width)
#                 new_bg.rect.centery = x.rect.centery
#                 layer_list[i].add(new_bg)
#             # Memory optimization
#             if x.rect.left > s_width or x.rect.right < 0:
#                 if x in head_list[i]:
#                     x.kill()
#                     for a in layer_list[i]:
#                         head_list[i] = pygame.sprite.Group(a)
#                 x.kill()
#
#         # Adding to right side
#         for a in head_list[i]:
#             if a.rect.right < s_width:
#                 new_head = Background(bg_img_list[i], a.rect.centerx + s_width)
#                 new_head.rect.centery = a.rect.centery
#                 layer_list[i].add(new_head)
#                 head_list[i] = pygame.sprite.Group(new_head)
#
#         # Experimental deletion of common centers
#         for p in layer_list[i]:
#             for q in layer_list[i]:
#                 if p.rect.centerx == q.rect.centerx and p != q:
#                     p.kill()

def parallax(l_list, h_list, s_xdir, s_ydir):
    for i in range(len(l_list)):
        ind = 0
        for x in l_list[i]:
            ind += 1
            x.rect.move_ip(s_xdir * vel_list[i], s_ydir * vel_list[1])
            # Adding to left
            if x.rect.left > 0 and ind == len(l_list[i]) and not x.rect.centerx > s_width:
                new_bg = Background(bg_img_list[i], x.rect.centerx - s_width)
                new_bg.rect.centery = x.rect.centery
                l_list[i].add(new_bg)
            # Memory optimization
            if x.rect.left > s_width or x.rect.right < 0:
                if x in h_list[i]:
                    x.kill()
                    for a in l_list[i]:
                        h_list[i] = pygame.sprite.Group(a)
                x.kill()

        # Adding to right side
        for a in h_list[i]:
            if a.rect.right < s_width:
                new_head = Background(bg_img_list[i], a.rect.centerx + s_width)
                new_head.rect.centery = a.rect.centery
                l_list[i].add(new_head)
                h_list[i] = pygame.sprite.Group(new_head)

        # Experimental deletion of common centers
        for p in l_list[i]:
            for q in l_list[i]:
                if p.rect.centerx == q.rect.centerx and p != q:
                    p.kill()


def bg_reset(n_layer_list, n_head_list, n_cave_air):
    nl1 = Background(bg_img_list[0], s_width / 2)
    nl2 = Background(bg_img_list[1], s_width / 2)
    n_layer_list = [pygame.sprite.Group(nl1), pygame.sprite.Group(nl2)]
    n_head_list = [pygame.sprite.Group(nl1), pygame.sprite.Group(nl2)]
    n_cave_air = BgSurface()
    return n_layer_list, n_head_list, n_cave_air