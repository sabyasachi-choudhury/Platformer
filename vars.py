import pygame
pygame.init()

run = True
s_width, s_height = 1000, 600
bg_width, bg_height = s_width, s_height
bg_grey = (73, 96, 101)
vel_list = [5, 7]
screen_xdir, screen_ydir = 0, 0
block_len = 40
id_list = ['pl1', 'pl2', 'rc', 'sm1', 'sm2', 'sq1', 'sq2', 'sq3', 'sq4', 'gem', 'lava', 'spike', 'fire', 'player']
base_img_files = ["pl_tile1.png", "pl_tile2.png",
                  "rect_tile1.png",
                  "sm_tile1.png", "sm_tile2.png",
                  "sq_tile1.png", "sq_tile2.png", "sq_tile3.png", "sq_tile4.png",
                  "gem.png",
                  "lava_1.png",
                  "spike_1.png",
                  "fire_1.png",
                  "player_1.png"]

screen = pygame.display.set_mode((s_width, s_height))

base_img_list = [pygame.image.load(s).convert() for s in base_img_files]

current_level = 0
g_vel = 0
player_x, player_y = 0, 1
cross_hair = 17

points = 0
cur_points = 0