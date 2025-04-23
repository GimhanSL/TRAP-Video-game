import pygame
import sys
import random
from pygame import mixer
pygame.init()
#display---
screen_size = (1000,600)
screen = pygame.display.set_mode(screen_size,0,32)
pygame.display.set_caption('TRAP')

background_image = pygame.image.load('TRAP\\backgrounds\\t_bc1.png').convert()
cloud_rect = background_image.get_rect(topleft = (-250,0))
bc_green = pygame.image.load('TRAP\\backgrounds\green_tile.png').convert()
bc_rect = bc_green.get_rect(topleft=(100,80))

#tiles and objects
ob1 = pygame.image.load('TRAP\\assets\walls\wall1.png').convert_alpha()
player_box = pygame.image.load('TRAP\\assets\objects\player_box.png')
next_lvl = pygame.image.load('TRAP\\backgrounds\\next.png')
next_rect = next_lvl.get_rect(topleft = (0,80))
tree = pygame.image.load('TRAP\\assets\\nature\\trees.png')

def tree_pos(x,y):
    place = tree.get_rect(topleft=(x,y))
    screen.blit(tree,place)

#sounds
menu_sound1 =  pygame.mixer.Sound('TRAP\\sound\\Abstract1.mp3')
music = pygame.mixer.music.load('TRAP\\sound\\game_bac.mp3')
pygame.mixer.music.play(-1)
bg1 = pygame.mixer.Sound('TRAP\\sound\\in.mp3')
walk = pygame.mixer.Sound('TRAP\\sound\\Concrete 1.wav')
hurt = pygame.mixer.Sound('TRAP\\sound\\man_scream.ogg')
gameover = pygame.mixer.Sound('TRAP\\sound\\Game_Over_1.wav')
wins = pygame.mixer.Sound('TRAP\\sound\\sea.wav')

#game won images
won = pygame.image.load('TRAP\plans\won.png')
lost = pygame.image.load('TRAP\plans\lost1.png')
#importent var
game_active = True
game_started = False
win = True

#game font
font1 = pygame.font.Font('TRAP\\fonts\\Boxy.otf',20)


#end and start tiles
start_image = pygame.image.load('TRAP\\assets\start n end\start_red_point.png')
st_image_rect = start_image.get_rect(topleft=(100,380))

end_image = pygame.image.load('TRAP\\assets\start n end\end_blue_point.png')
end_rect = end_image.get_rect(topleft= (100,80))

#menu tiles

menu_screen = pygame.image.load('TRAP\plans\\trap_menu.png')
menu_rect = menu_screen.get_rect(topleft = (0,0))
start_button = pygame.image.load('TRAP\menu\play_button.png')
start_button2 = pygame.image.load('TRAP\menu\play_button2.png')
start_brect = start_button.get_rect(topleft = (70,265) )
start_brect2 = start_button2.get_rect(topleft = (70,265) )
exit_button = pygame.image.load('TRAP\menu\exit_button.png')
exit_button2 = pygame.image.load('TRAP\menu\exit_button2.png')
exit_brect = exit_button.get_rect(topleft= (565,265))
exit_brect2 = exit_button2.get_rect(topleft= (565,265))

bv = 5
rv = 5
def cloud_anime():
    global cloud_rect,bv
    if cloud_rect.right <= 1010:
        cloud_rect.right = 1010
        bv = -5
    if cloud_rect.left >= -5:
        cloud_rect.left = -5
        bv = 5
    cloud_rect.x -= bv

#after game over and won
o_again_button = pygame.image.load('TRAP\\menu\\again_button.png').convert()
o_again_button2 = pygame.image.load('TRAP\\menu\\again_button2.png').convert()
ag_rect = o_again_button.get_rect(topleft = (10,200))
ag_rect2 = o_again_button.get_rect(topleft = (10,200))

o_exit_button = pygame.image.load('TRAP\\menu\\won_exit_button.png').convert()
o_exit_button2 = pygame.image.load('TRAP\\menu\\won_exit_button2.png').convert()
ex_rect = o_exit_button.get_rect(topleft = (780,200))
ex_rect2 = o_exit_button2.get_rect(topleft = (780,200))

#traps
helth = 10
index = 0
trap1 = pygame.image.load('TRAP\\assets\\trap1\\trap_1_2.png')
trap2 = pygame.image.load('TRAP\\assets\\trap1\\trap_1_1.png')
trap3 = pygame.image.load('TRAP\\assets\\trap1\\trap_1_1.png')
trap4 = pygame.image.load('TRAP\\assets\\trap1\\trap_1_1.png')

tr_list = [trap1,trap2,trap3,trap4]

def Traps(value,trap_list,recx,recty):
    global helth,index
    traps = [trap1.get_rect(topleft=(recx,recty)),trap2.get_rect(topleft=(recx,recty)),trap3.get_rect(topleft = (recx,recty)),trap4.get_rect(topleft = (recx,recty))]
    index += value
    tr = trap_list[int(index)]
    for trap in traps:
        screen.blit(tr,trap)
    if index >= 3:
        if player_rect.colliderect(traps[0]):
            hurt.play(0)
            helth-= 2
        index = 0
    return helth

tindex = 0
trap_2_1 = pygame.image.load('TRAP\\assets\\trap2\\trap_2_2.png')
trap_2_2 = pygame.image.load('TRAP\\assets\\trap2\\trap_2_1.png')
trap_2_3 = pygame.image.load('TRAP\\assets\\trap2\\trap_2_1.png')
trap_2_4 = pygame.image.load('TRAP\\assets\\trap2\\trap_2_1.png')
tr_list4 = [trap_2_1,trap_2_2,trap_2_3,trap_2_4]
traps_4 = [trap_2_1.get_rect(topleft = (520,400)),trap_2_2.get_rect(topleft = (520,400)),trap_2_3.get_rect(topleft = (520,400)),trap_2_4.get_rect(topleft = (520,400))]

def Traps2(value,trap_list,trap_rect_list):
    global tindex,helth
    tindex += value
    tr = trap_list[int(tindex)]
    for trap in trap_rect_list:
        screen.blit(tr,trap)
    if tindex >= 3 :
        if player_rect.colliderect(trap_rect_list[1]) or player_rect.colliderect(trap_rect_list[2]) or player_rect.colliderect(trap_rect_list[3]):
            helth-= 2
            hurt.play(0)
        tindex = 0
    return helth

trap_3_1 = pygame.image.load('TRAP\\assets\\trap2\\trap_2_2.png')
trap_3_2 = pygame.image.load('TRAP\\assets\\trap2\\trap_2_1.png')
trap_3_3 = pygame.image.load('TRAP\\assets\\trap2\\trap_2_1.png')
trap_3_4 = pygame.image.load('TRAP\\assets\\trap2\\trap_2_1.png')
tr_list5 = [trap_3_1,trap_3_2,trap_3_3,trap_3_4]
traps_5 = [trap_3_1.get_rect(topleft = (290,170)),trap_3_2.get_rect(topleft = (290,170)),trap_3_3.get_rect(topleft = (290,170)),trap_3_4.get_rect(topleft = (290,170))]

tindex2 = 0

def Traps3(value,trap_list,trap_rect_list):
    global tindex2,helth
    tindex2 += value
    tr = trap_list[int(tindex2)]
    for trap in trap_rect_list:
        screen.blit(tr,trap)
    if tindex2 >= 3 :
        if player_rect.colliderect(trap_rect_list[1]) or player_rect.colliderect(trap_rect_list[2]) or player_rect.colliderect(trap_rect_list[3]):
            helth-= 2
            hurt.play(0)
        tindex2 = 0
    return helth

hall1 = pygame.image.load('TRAP\\assets\\hall\\st1.png').convert_alpha()
hall2 = pygame.image.load('TRAP\\assets\\hall\\st2.png').convert_alpha()
hall3 = pygame.image.load('TRAP\\assets\\hall\\st3.png').convert_alpha()
hall4 = pygame.image.load('TRAP\\assets\\hall\\st4.png').convert_alpha()

hall_list = [hall1,hall2,hall3,hall4]

hall_rect_list = [hall1.get_rect(topleft = (640,430)),hall2.get_rect(topleft = (640,430)),hall3.get_rect(topleft = (640,430)),hall4.get_rect(topleft = (640,430)),]

hall_index = 0
def Traps4(value,trap_list,trap_rect_list):
    global hall_index,helth
    hall_index += value
    tr = trap_list[int(hall_index)]
    for trap in trap_rect_list:
        screen.blit(tr,trap)
    if hall_index >= 3 :
        if player_rect.colliderect(trap_rect_list[1]) or player_rect.colliderect(trap_rect_list[2]) or player_rect.colliderect(trap_rect_list[3]):
            helth-= 2
            hurt.play(0)
        hall_index = 0
    return helth

cut1 = pygame.image.load('TRAP\\assets\\trap3\\trap3_1.png').convert_alpha()
cut2 = pygame.image.load('TRAP\\assets\\trap3\\trap3_2.png').convert_alpha()
cut3 = pygame.image.load('TRAP\\assets\\trap3\\trap3_2.png').convert_alpha()
cut4 = pygame.image.load('TRAP\\assets\\trap3\\trap3_2.png').convert_alpha()

cut_list = [cut1,cut2,cut3,cut4]

cut_rect_list = [cut1.get_rect(topleft = (550,190)),cut2.get_rect(topleft = (550,190)),cut3.get_rect(topleft = (550,190)),cut4.get_rect(topleft = (550,190))]

cut_index = 0

def Traps5(value,trap_list,trap_rect_list):
    global cut_index,helth
    cut_index += value
    tr = trap_list[int(cut_index)]
    for trap in trap_rect_list:
        screen.blit(tr,trap)
    if cut_index >= 3 :
        if player_rect.colliderect(trap_rect_list[1]) or player_rect.colliderect(trap_rect_list[2]) or player_rect.colliderect(trap_rect_list[3]):
            helth-= 2
            hurt.play(0)
        cut_index = 0
    return helth

w1 = pygame.image.load('TRAP\\assets\\trap5\\t1.png')
w2 = pygame.image.load('TRAP\\assets\\trap5\\t2.png')
w3 = pygame.image.load('TRAP\\assets\\trap5\\t3.png')
w4 = pygame.image.load('TRAP\\assets\\trap5\\t4.png')
w5 = pygame.image.load('TRAP\\assets\\trap5\\t5.png')

wall_rec1 = w1.get_rect(topleft =(350,260))
wall_rec2 = w1.get_rect(topleft =(350,260))
wall_rec3 = w1.get_rect(topleft =(350,260))
wall_rec4 = w1.get_rect(topleft =(350,260))
wall_rec5 = w1.get_rect(topleft =(350,260))


wl_list = [w1,w2,w3,w4,w5]

wl_rect_list = [wall_rec1,wall_rec2,wall_rec3,wall_rec4,wall_rec5]

wl_index = 0
def wall_trap():
    global  wl_list,wl_rect_list,wl_index,helth
    wl_index += 0.1
    wl = wl_list[int(wl_index)]
    for wall in wl_rect_list:
        screen.blit(wl,wall)
    if wl_index >= 4:
        if player_rect.colliderect(wl_rect_list[1]) or player_rect.colliderect(wl_rect_list[2]) or player_rect.colliderect(wl_rect_list[3]) or player_rect.colliderect(wl_rect_list[4]) :
            helth -= 2
            hurt.play(0)
        wl_index = 0
    return helth

wallt1 = pygame.image.load('TRAP\\assets\\trap4\\tr1.png')
wallt2 = pygame.image.load('TRAP\\assets\\trap4\\tr2.png')
wallt3 = pygame.image.load('TRAP\\assets\\trap4\\tr3.png')
wallt4 = pygame.image.load('TRAP\\assets\\trap4\\tr4.png')

wall_r1 = wallt1.get_rect(topleft =(100,250))
wall_r2 = wallt1.get_rect(topleft =(100,250))
wall_r3 = wallt1.get_rect(topleft =(100,250))
wall_r4 = wallt1.get_rect(topleft =(100,250))


wl_list2 = [wallt1,wallt2,wallt3,wallt4]
wl_rect_list2 = [wall_r1,wall_r2,wall_r3,wall_r4]
wl_index2 = 0

def walltrap2():
    global wl_list2,wl_rect_list2,wl_index2,helth
    wl_index2 += 0.1
    wl = wl_list2[int(wl_index2)]
    for wall in wl_rect_list2:
        screen.blit(wl,wall)
    if wl_index2 >= 3:
        if player_rect.colliderect(wl_rect_list2[0])  :
            helth -= 2
            hurt.play(0)
        wl_index2 = 0
    return helth

wall1 = pygame.image.load('TRAP\\assets\\wall2\\4.png')
wall2 = pygame.image.load('TRAP\\assets\\wall2\\3.png')
wall3 = pygame.image.load('TRAP\\assets\\wall2\\2.png')
wall4 = pygame.image.load('TRAP\\assets\\wall2\\1.png')

wlrect = wall1.get_rect(topleft =(400,80))
wlrect1 = wall2.get_rect(topleft =(400,80))
wlrect2 = wall3.get_rect(topleft =(400,80))
wlrect3 = wall4.get_rect(topleft =(400,80))

wlist = [wall1,wall2,wall3,wall4]
wrlist = [wlrect,wlrect1,wlrect2,wlrect3]

wlindex = 0

def walltrap3():
    global wlist,wrlist,wlindex,helth
    wlindex += 0.1
    wl = wlist[int(wlindex)]
    for wall in wrlist:
        screen.blit(wl,wall)
    if wlindex >= 3:
        if player_rect.colliderect(wrlist[0])  :
            helth -= 2
            hurt.play(0)
        wlindex = 0
    return helth

walll1 = pygame.image.load('TRAP\\assets\\wall3\\4.png')
walll2 = pygame.image.load('TRAP\\assets\\wall3\\3.png')
walll3 = pygame.image.load('TRAP\\assets\\wall3\\2.png')
walll4 = pygame.image.load('TRAP\\assets\\wall3\\1.png')

wlrectt1 = walll1.get_rect(topleft =(820,140))
wlrectt2 = walll2.get_rect(topleft =(820,140))
wlrectt3 = walll3.get_rect(topleft =(820,140))
wlrectt4 = walll4.get_rect(topleft =(820,140))

wlist2 = [walll1,walll2,walll3,walll4]
wrlist2 = [wlrectt4,wlrectt3,wlrectt2,wlrectt1]

wlindex2 = 0

def walltrap4():
    global wlist2,wrlist2,wlindex2,helth
    wlindex2 += 0.1
    wl = wlist2[int(wlindex2)]
    for wall in wrlist2:
        screen.blit(wl,wall)
    if wlindex2 >= 3:
        if player_rect.colliderect(wrlist2[0])  :
            helth -= 2
            hurt.play(0)
        wlindex2 = 0
    return helth

wa1 = pygame.image.load('TRAP\\assets\\wall5\\1.png')
wa2 = pygame.image.load('TRAP\\assets\\wall5\\3.png')
wa3 = pygame.image.load('TRAP\\assets\\wall5\\2.png')
wa4 = pygame.image.load('TRAP\\assets\\wall5\\1.png')

wlr1 = wa1.get_rect(topleft =(709,80))
wlr2 = wa2.get_rect(topleft =(709,80))
wlr3 = wa3.get_rect(topleft =(709,80))
wlr4 = wa4.get_rect(topleft =(709,80))

wlist3 = [wa1,wa2,wa3,wa4]
wrlist3 = [wlr4,wlr3,wlr2,wlr1]

wlindex3 = 0

def walltrap5():
    global wlist3,wrlist3,wlindex3,helth
    wlindex3 += 0.1
    wl = wlist3[int(wlindex3)]
    for wall in wrlist3:
        screen.blit(wl,wall)
    if wlindex3 >= 3:
        if player_rect.colliderect(wrlist3[0]) or player_rect.colliderect(wrlist3[3]) :
            helth -= 2
            hurt.play(0)
        wlindex3 = 0
    return helth




#helth bar
helth1 = pygame.image.load('TRAP\\helth bar\\h1.png')
helth2 = pygame.image.load('TRAP\\helth bar\\h2.png')
helth3 = pygame.image.load('TRAP\\helth bar\\h3.png')
helth4 = pygame.image.load('TRAP\\helth bar\\h4.png')
helth5 = pygame.image.load('TRAP\\helth bar\\h5.png')
helth_rect = helth1.get_rect(topleft = (0,0))
helth_list = [helth1,helth2,helth3,helth4,helth5]
h_index = 0
def Helth_bar():
    global helth,h_index
    if helth == 10 or helth == 9:
        h_index = 0
        screen.blit(helth_list[h_index],helth_rect)
    if helth == 8 or helth == 7:
        h_index = 1
        screen.blit(helth_list[h_index],helth_rect)
    if helth == 6 or helth == 5:
        h_index = 2
        screen.blit(helth_list[h_index],helth_rect)
    if helth == 4 or helth == 3:
        h_index = 3
        screen.blit(helth_list[h_index],helth_rect)
    if helth == 2 or helth == 1:
        h_index = 4
        screen.blit(helth_list[h_index],helth_rect)

###############################################enemy#####################################################

#Idle position



mud = pygame.image.load("TRAP\\assets\\objects\\mud.png")
mud_rect = mud.get_rect(topleft = (600,310))

def mud_():
    global g,v,by,bx
    if player_rect.colliderect(mud_rect):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                g = -2
                by = -2
            if event.key == pygame.K_DOWN:
                g = 2
                by = 2
            if player_rect.left <= mud_rect.right:
                if event.key == pygame.K_RIGHT:
                    v = 2
                    bx =2
            if player_rect.right >= mud_rect.left:
                if event.key == pygame.K_LEFT:
                    v = -2
                    bx = -2

###################################################player#################################################
player_pos = (170,430)
#idle position
idle_1 = pygame.image.load('TRAP\player\\idle\\idle_1.png').convert_alpha()
idle_2 = pygame.image.load('TRAP\player\\idle\\idle_2.png').convert_alpha()
idle_3 = pygame.image.load('TRAP\player\\idle\\idle_2.png').convert_alpha()
idle_4 = pygame.image.load('TRAP\player\\idle\\idle_1.png').convert_alpha()
player_idle = [idle_1,idle_2,idle_3,idle_4]
player_index = 0
player_1 = player_idle[player_index]
player_rect = idle_1.get_rect(topleft= player_pos, size = (20,38))

def player_idle_anime():
    global player_idle,player_index,player_1,player_rect
    player_index += 0.1
    player_1 = player_idle[int(player_index)]
    if player_index >= 3:
        player_index = 0
    screen.blit(player_1,player_rect)

#player left position
left_1 = pygame.image.load('TRAP\player\left_down\l1.png').convert_alpha()
left_2 = pygame.image.load('TRAP\player\left_down\l2.png').convert_alpha()
left_3 = pygame.image.load('TRAP\player\left_down\l1.png').convert_alpha()
left_4 = pygame.image.load('TRAP\player\left_down\l3.png').convert_alpha()


move_list=[left_1,left_2,left_3]
move_index = 0
def player_move_anime(sprite_list):
    global move_index,player_1,player_rect
    move_index += 1
    player_1 = sprite_list[int(move_index)]
    screen.blit(player_1,player_rect)
    if move_index>= (len(sprite_list)-1):
        move_index = 0

#player right position
right_1 = pygame.image.load('TRAP\player\\right_up\\r1.png').convert_alpha()
right_2 = pygame.image.load('TRAP\player\\right_up\\r2.png').convert_alpha()
right_3 = pygame.image.load('TRAP\player\\right_up\\r1.png').convert_alpha()
right_4 = pygame.image.load('TRAP\player\\right_up\\r3.png').convert_alpha()

right_index = 0
right_list = [right_1,right_2,right_3]

#player up pos
up1 = pygame.image.load('TRAP\player\\up\\u3.png').convert_alpha()
up2 = pygame.image.load('TRAP\player\\up\\u2.png').convert_alpha()
upidle = pygame.image.load('TRAP\player\\up\\u1.png').convert_alpha()

back_list = [up1,up2,]

#player down pos
down1 = pygame.image.load('TRAP\player\\down\\d2.png').convert_alpha()
down2 = pygame.image.load('TRAP\player\\down\\d3.png').convert_alpha()
doenidle = pygame.image.load('TRAP\player\\down\\d1.png').convert_alpha()

down_list = [down1,down2]
hor_index = 0

def player_hor_move_anime(sprite_list):
    global hor_index,player_1,player_rect,g
    hor_index += 0.4
    player_1 = sprite_list[int(hor_index)]
    screen.blit(player_1,player_rect)
    if hor_index>= (len(sprite_list)-1):
        hor_index = 0
    if g == 0:
        player_1 = sprite_list[0]

def player_side_idle(player_image):
    screen.blit(player_image,player_rect)

#make a rect with x_ps,y_ps, width,height
def make_rect(dimention):
    tile = pygame.Rect((dimention))
    return tile

#draw the rect you make before
def rect_draw(color,rect_name):
    pygame.draw.rect(screen,(color),rect_name)

#make sure are there any collide
def collison(player,object):
    coll = []
    for tile in object:
        if player.colliderect(tile):
            coll.append(tile)
    return coll

#the full collider machanism
def move(player,object):
    global g,v
    player.x += v
    coll = collison(player,object)
    for tile in coll:
        if v > 0:
            player.right = (tile.left)
        if v < 0:
            player.left = tile.right
    player.y += g
    coll = collison(player,object)
    for tile in coll:
        if g > 0 :
            player.bottom = tile.top
        if g < 0:
            player.top = tile.bottom
    return player

###############################################player#######################################################

start_button_played = True
exit_button_played = True

def game_over():
    global helth,game_active,win,g,v
    if helth <= 0:
        game_active = False
        helth = 10
        hurt.stop()
        gameover.play(0)
        g= 0
        v = 0
        walk.stop()

def over_anime():
    global start_button_played,exit_button_played
    mouse_pos = pygame.mouse.get_pos()
    if ag_rect.collidepoint(mouse_pos):
        screen.blit(o_again_button2,ag_rect2)
        if not start_button_played:
            menu_sound1.play(0)
            start_button_played = True
    else:
        start_button_played = False
    if ex_rect.collidepoint(mouse_pos):
        screen.blit(o_exit_button2,ex_rect2)
        if not exit_button_played:
            menu_sound1.play(0)
            exit_button_played = True
    else:
        exit_button_played = False

def menu_Play():
    global start_brect,game_started,exit_brect,menu_rect,time
    if event.type == pygame.MOUSEBUTTONDOWN:
        if start_brect.collidepoint(event.pos):
            game_started = True
            time = 0
    if event.type == pygame.MOUSEBUTTONDOWN:
        if exit_brect.collidepoint(event.pos):
            exit()

def menu_anime():
    global start_button_played,exit_button_played
    mouse_pos = pygame.mouse.get_pos()
    if start_brect.collidepoint(mouse_pos):
        screen.blit(start_button2,start_brect2)
        if not start_button_played:
            menu_sound1.play(0)
            start_button_played = True
    else:
        start_button_played = False

    if exit_brect.collidepoint(mouse_pos):
        screen.blit(exit_button2,exit_brect2)
        if not exit_button_played:
            menu_sound1.play(0)
            exit_button_played = True
    else:
        exit_button_played = False

def over_play():
    global game_active,g,v,helth
    if event.type == pygame.MOUSEBUTTONDOWN:
        if ag_rect.collidepoint(event.pos):
            game_active = True
            helth = 10
            player_rect.topleft = player_pos
    if event.type == pygame.MOUSEBUTTONDOWN:
        if ex_rect.collidepoint(event.pos):
            exit()

def win_play():
    global win,g,v,helth
    if event.type == pygame.MOUSEBUTTONDOWN:
        if ag_rect.collidepoint(event.pos):
            wins.stop()
            win = True
            player_rect.topleft = player_pos
            v = 0
            g = 0
            helth = 10
    if event.type == pygame.MOUSEBUTTONDOWN:
        if ex_rect.collidepoint(event.pos):
            exit()

def move_object(player):
    global obg,obv,ob_list
    for i in ob_list:
        if player.colliderect(i):
            if player.right >= i.left:
                obv = v
            if player.left <= i.right:
                obv = v
            i.x += obv
            if player.top <= i.bottom:
                obg = g
            if player.bottom >= i.top:
                obg = g
            i.y += obg

def border(player):
    if player.x <= 100:
        player.x = 100
    if player.right >= 890:
        player.right = 890
    if player.y <= 80:
        player.y = 80
    if player.y >= 453:
        player.y = 453

def winthe_game(player,end):
    global game_active,win,helth
    if player.colliderect(end):
        wins.play(0)
        walk.stop()
        helth = 10
        win = False


g1 = pygame.image.load("TRAP\\goal bar\\gb1.png")
g2 = pygame.image.load("TRAP\\goal bar\\gb2.png")
g3 = pygame.image.load("TRAP\\goal bar\\gb3.png")
g4 = pygame.image.load("TRAP\\goal bar\\gb4.png")
g5 = pygame.image.load("TRAP\\goal bar\\gb5.png")
g6 = pygame.image.load("TRAP\\goal bar\\gb6.png")
g7 = pygame.image.load("TRAP\\goal bar\\gb7.png")
g8 = pygame.image.load("TRAP\\goal bar\\gb8.png")
g9 = pygame.image.load("TRAP\\goal bar\\gb9.png")
g10 = pygame.image.load("TRAP\\goal bar\\gb10.png")
g11 = pygame.image.load("TRAP\\goal bar\\gb11.png")
g12 = pygame.image.load("TRAP\\goal bar\\gb12.png")
g13 = pygame.image.load("TRAP\\goal bar\\gb13.png")
g14 = pygame.image.load("TRAP\\goal bar\\gb14.png")
g15 = pygame.image.load("TRAP\\goal bar\\gb15.png")
g16 = pygame.image.load("TRAP\\goal bar\\gb16.png")

g1_rect = g1.get_rect(topleft =(500,10))
gb_list = [g1,]

goal_count = 10
def goal():
    global goal_count
    if player_rect.x >= 200 and player_rect.y <= 460:
        screen.blit(g2,g1_rect)
    if player_rect.x >= 490 and player_rect.y <= 460:
        screen.blit(g3,g1_rect)
    if player_rect.x >= 600 and player_rect.y <= 460:
        screen.blit(g4,g1_rect)
    if player_rect.x <= 800 and player_rect.y <= 340:
        screen.blit(g5,g1_rect)
    if player_rect.x <= 500 and player_rect.y <= 340:
        screen.blit(g6,g1_rect)
    if player_rect.x <= 300 and player_rect.y <= 340:
        screen.blit(g7,g1_rect)
    if player_rect.x >= 200 and player_rect.y <= 250:
        screen.blit(g8,g1_rect)
    if player_rect.x >= 400 and player_rect.y <= 250:
        screen.blit(g9,g1_rect)
    if player_rect.x >= 600 and player_rect.y <= 250:
        screen.blit(g10,g1_rect)
    if player_rect.x <= 800 and player_rect.y <= 100:
        screen.blit(g11,g1_rect)
    if player_rect.x <= 600 and player_rect.y <= 100:
        screen.blit(g12,g1_rect)
    if player_rect.x <= 500 and player_rect.y <= 100:
        screen.blit(g13,g1_rect)
    if player_rect.x <= 400 and player_rect.y <= 100:
        screen.blit(g14,g1_rect)
    if player_rect.x <= 300 and player_rect.y <= 100:
        screen.blit(g15,g1_rect)
    if player_rect.x <= 350 and player_rect.y <= 100:
        screen.blit(g16,g1_rect)

ret_but = pygame.image.load('TRAP\\sub menu icons\\retry.png')
ret_but2 = pygame.image.load('TRAP\\sub menu icons\\retry2.png')
ret_but_rect = ret_but.get_rect(topleft = (920,320))

sound_but1 = pygame.image.load('TRAP\\sub menu icons\\sound.png')
sound_but2 = pygame.image.load('TRAP\\sub menu icons\\sound2.png')
s_rect = sound_but1.get_rect(topleft = (920,240))

poi_but = pygame.image.load('TRAP\\sub menu icons\\poitioin_button.png')
poi_but2 = pygame.image.load('TRAP\\sub menu icons\\poitioin_button2.png')
po_rect = poi_but.get_rect(topleft=(10,180))

sw_but = pygame.image.load('TRAP\\sub menu icons\\sword_button.png')
sw_but2 = pygame.image.load('TRAP\\sub menu icons\\sword_button2.png')
sw_rect = sw_but.get_rect(topleft = (10,300))

sub_button = pygame.image.load('TRAP\\sub menu icons\\sub_menu.png')
sub_button2 = pygame.image.load('TRAP\\sub menu icons\\sub_menu2.png')
sub_rect = sub_button.get_rect(topleft = (920,150))

def REstart():
    global win,helth,idle
    if event.type == pygame.MOUSEBUTTONDOWN:
        if ret_but_rect.collidepoint(event.pos):
            player_rect.x,player_rect.y = player_pos
            helth = 10

def sub_anime(rect_img,rect):
    mouse_p = pygame.mouse.get_pos()
    if rect.collidepoint(mouse_p):
        screen.blit(rect_img,rect)

def sub_menu():
    global sub_rect
    if event.type == pygame.MOUSEBUTTONDOWN:
        if sub_rect.collidepoint(event.pos):
            exit()


#tiles
tiles= [
    ob1.get_rect(topleft=(100,370),size = (720,60)),
    ob1.get_rect(topleft = (180,250),size = (720,60)),
    ob1.get_rect(topleft = (100,140),size = (720,60))
]
ob_list=[
    player_box.get_rect(topleft=(270,450), size=(30,30))
          ]
#gravity and velosity
v = 0
g = 0
tile_count = 0
obv = 0
obg = 0
up = False
down = False
right = False
left = False
keyup = False
idle = False

#main game loop---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
        if game_started:
            if game_active :
                if win:
                    if event.type == pygame.KEYDOWN:
                        keyup = False
                        if event.key == pygame.K_LEFT and  pygame.K_DOWN:
                            v = 0
                            g = 0
                        if event.key ==  pygame.K_DOWN and pygame.K_LEFT :
                            v = 0
                            g = 0
                        if event.key == pygame.K_DOWN and pygame.K_RIGHT:
                            v = 0
                            g = 0
                        if event.key == pygame.K_RIGHT and pygame.K_DOWN:
                            v = 0
                            g = 0
                        if event.key == pygame.K_RIGHT and pygame.K_UP:
                            v = 0
                            g = 0
                        if event.key == pygame.K_UP and pygame.K_RIGHT:
                            v = 0
                            g = 0
                        if event.key == pygame.K_UP and pygame.K_LEFT:
                            v = 0
                            g = 0
                        if event.key == pygame.K_LEFT and pygame.K_UP:
                            v,g = 0,0
                        if event.key == pygame.K_UP:
                            g = -5
                            by = -5
                            walk.play(-1)
                        if event.key == pygame.K_DOWN:
                            g = 5
                            by = 5
                            walk.play(-1)
                        if event.key == pygame.K_RIGHT:
                            v = 5
                            bx = 5
                            walk.play(-1)
                        if event.key == pygame.K_LEFT:
                            v = -5
                            bx =-5
                            walk.play(-1)
                    if event.type == pygame.KEYUP:
                        keyup = True
                        if event.key == pygame.K_UP:
                            g = 0

                            up = True
                            down = False
                            right = False
                            left = False

                        if event.key == pygame.K_DOWN:
                            g = 0
                            down = True
                            right = False
                            left = False
                            up = False

                        if event.key == pygame.K_RIGHT:
                            v = 0
                            right = True
                            left = False
                            up = False
                            down = False

                        if event.key == pygame.K_LEFT:
                            v = 0
                            left =True
                            right = False
                            up = False
                            down = False
                        bx = 0
                        by = 0
                        walk.stop()

                else:
                    win_play()
                    helth = 5
            else:
                over_play()
        else:
            menu_Play()

    if game_started:
        pygame.mixer.music.stop()
        if  game_active:
            if win:

                time = (pygame.time.get_ticks()//1000)

                screen.fill((0,25,0))
                screen.blit(background_image,cloud_rect)
                cloud_anime()
                screen.blit(bc_green,bc_rect)
                screen.blit(mud,mud_rect)
                screen.blit(end_image,end_rect)
                move(player_rect,tiles)
                screen.blit(g1,g1_rect)
                screen.blit(ret_but,ret_but_rect)
                screen.blit(sub_button,sub_rect)
                screen.blit(sound_but1,s_rect)
                sub_anime(ret_but2,ret_but_rect)
                sub_anime(sub_button2,sub_rect)
                sub_anime(sound_but2,s_rect)
                move_object(player_rect)
                for tile in tiles:
                    screen.blit(ob1,tile)

                Traps(0.1,tr_list,360,420)
                Traps4(0.1,hall_list,hall_rect_list)
                Traps5(0.05,cut_list,cut_rect_list)
                wall_trap()
                walltrap3()
                mud_()
                walltrap2()
                walltrap4()
                walltrap5()
                screen.blit(next_lvl,next_rect)
                REstart()

                if keyup == True :
                    if right == True:
                        screen.blit(right_list[0],player_rect)
                    if left == True:
                        screen.blit(move_list[0],player_rect)
                    if up == True:
                        screen.blit(upidle,player_rect)
                    if down == True:
                        screen.blit(doenidle,player_rect)
                if keyup == False:
                    if  v == -5 or v== -2:
                        player_move_anime(move_list)
                    if  v == 5 or v== 2:
                        player_move_anime(right_list)
                    if  g == -5 or g== -2:
                        player_hor_move_anime(back_list)
                    if  g == 5 or g== 2:
                        player_hor_move_anime(down_list)
                Traps2(0.1,tr_list4,traps_4)
                Traps3(0.1,tr_list5,traps_5)
                #for ob in ob_list:
                    #screen.blit(player_box,ob)

                tree_pos(100,170)
                tree_pos(210,20)
                tree_pos(860,410)
                tree_pos(860,250)
                tree_pos(500,240)
                tree_pos(860,90)
                tree_pos(90,300)
                screen.blit(start_image,st_image_rect)
                font_surf = font1.render(str(time),False,(255,207,50))
                #screen.blit(font_surf,(290,20))
                sub_menu()
                border(player_rect)
                winthe_game(player_rect,end_rect)
                Helth_bar()
                goal()
                game_over()

            else:
                screen.blit(background_image,cloud_rect)
                cloud_anime()
                screen.blit(won,(0,0))
                screen.blit(o_again_button,ag_rect)
                screen.blit(o_exit_button,ex_rect)
                over_anime()


        else:
            screen.blit(background_image,cloud_rect)
            cloud_anime()
            screen.blit(lost,(0,0))
            screen.blit(o_again_button,ag_rect)
            screen.blit(o_exit_button,ex_rect)
            over_anime()

    else:
        screen.blit(background_image,cloud_rect)
        cloud_anime()
        screen.blit(menu_screen,menu_rect)
        screen.blit(start_button,start_brect)
        screen.blit(exit_button,exit_brect)
        menu_anime()

    pygame.display.update()
    pygame.time.delay(27)