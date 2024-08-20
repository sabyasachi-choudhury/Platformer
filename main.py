"""To do: Convert to functions, create checkpoints, and figure out animation"""

# Imports
from background import *
from blocks import *
from level_codes import *
from pygame.locals import *

# Main init
pygame.init()

group = decipher(test_level)
exc_group = pygame.sprite.Group()
for thing in group:
    if thing.id == 'player':
        player = thing
    else:
        exc_group.add(thing)
checkpoint_list = []
for x in group:
    checkpoint_list.append([x.rect.centerx, x.rect.centery])


# Main loop
while run:
    # Fill
    screen.fill((73, 96, 101))
    # Event detection
    presses = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            for sp in exc_group:
                if player.rect.bottom == sp.rect.top:
                    # Player jumps
                    player_y, g_vel = player.jump(event, player_y, g_vel)

    # Player left and right
    screen_xdir, screen_ydir, player_x = player.motion(presses, screen_xdir, screen_ydir, player_x)

    # Background motion and stuff
    parallax(layer_list, head_list, screen_xdir, screen_ydir)
    cave_air.rect.move_ip(0, screen_ydir * vel_list[1])

    # Gravity
    g_vel = gravity(player, g_vel)

    # Bg block motion
    for coll_sprite in exc_group:
        coll_sprite.rect.move_ip(screen_xdir * vel_list[1], screen_ydir * vel_list[1])

    for coll_sprite in exc_group:
        if pygame.sprite.collide_rect(player, coll_sprite):
            if coll_sprite.id not in ['fire', 'lava', 'gem', 'spike']:
                if coll_sprite.rect.top+cross_hair > player.rect.bottom > coll_sprite.rect.top and player_y in [0, 1]:
                    player.rect.bottom = coll_sprite.rect.top
                if coll_sprite.rect.bottom-cross_hair < player.rect.top < coll_sprite.rect.bottom and player_y == -1:
                    player.rect.top = coll_sprite.rect.bottom
                if player.rect.right > coll_sprite.rect.left and player.rect.bottom > coll_sprite.rect.top and player_x == 1 and player.rect.top != coll_sprite.rect.bottom:
                    player.rect.right = coll_sprite.rect.left
                elif player.rect.left < coll_sprite.rect.right and player.rect.bottom > coll_sprite.rect.top and player_x == -1 and player.rect.top != coll_sprite.rect.bottom:
                    player.rect.left = coll_sprite.rect.right
            elif coll_sprite.id == 'gem':
                for ind, b_obj in enumerate(group, 0):
                    if b_obj == coll_sprite:
                        checkpoint_list.remove(checkpoint_list[ind])
                        coll_sprite.kill()
            elif coll_sprite.id in ['fire', 'spike', 'lava']:
                for i, t in enumerate(group, 0):
                    t.rect.center = (checkpoint_list[i][0], checkpoint_list[i][1])
                layer_list, head_list, cave_air = bg_reset(layer_list, head_list, cave_air)

    """------------------------------------------------EVERYTHING BLIT!--------------------------------------------"""

    # Background renders. Remember to put this before other blit statements
    screen.blit(cave_air.surf, cave_air.rect)
    for x in layer_list:
        for b_obj in x:
            screen.blit(b_obj.surf, b_obj.rect)

    # Level blit
    for obj in group:
        screen.blit(obj.surf, obj.rect)

    # Final reset
    screen_xdir = 0
    if screen_ydir != 0:
        cross_hair = 21
    else:
        cross_hair = 17
    if g_vel > 0:
        player_y = 1
    screen_ydir = 0

    # Final flip
    pygame.display.flip()
    pygame.time.Clock().tick(100)

# Quit
pygame.quit()
print(len(layer_list))