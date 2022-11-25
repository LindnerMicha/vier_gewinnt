import pygame
import sys

#region      -> Init
pygame.init()
screen = pygame.display.set_mode([1920, 1080])
pygame.display.set_caption("Vier Gewinnt")
clock = pygame.time.Clock()
fps = 60
fps_tick = 0
#endregion
#
#region      -> Fonts
pixel_font60 = pygame.font.Font("fonts/PixeloidSans.ttf", 60)
pixel_font30 = pygame.font.Font("fonts/PixeloidSans.ttf", 30)
pixel_font15 = pygame.font.Font("fonts/PixeloidSans.ttf", 15)
sys_font15 = pygame.font.SysFont(None, 15)
sys_font30 = pygame.font.SysFont(None, 30)
sys_font60 = pygame.font.SysFont(None, 60)
#endregion
#
#region -> Variablem init
rect_cor_x = 0
rect_cor_y = 0
x_num = 1000/100
y_num = 1000/100
i = 0
j = 0
x_if = 0
y_if = 0
re_y = y_num
global player
player = 0

index_x = 0
runtime = True

x_array = [0]*129
x_array_count = 129
o_array = [0]*129
o_array_count = 129
#endregion
#
#region -> Button cluster fuck
but_txt0 = " "
but_txt1 = " "
but_txt2 = " "
but_txt3 = " "
but_txt4 = " "
but_txt5 = " "
but_txt6 = " "
but_txt7 = " "
but_txt8 = " "
but_txt9 = " "
but_txt10 = " "
but_txt11 = " "
but_txt12 = " "
but_txt13 = " "
but_txt14 = " "
but_txt15 = " "
but_txt16 = " "
but_txt17 = " "
but_txt18 = " "
but_txt19 = " "
but_txt20 = " "
but_txt21 = " "
but_txt22 = " "
but_txt23 = " "
but_txt24 = " "
but_txt25 = " "
but_txt26 = " "
but_txt27 = " "
but_txt28 = " "
but_txt29 = " "
but_txt30 = " "
but_txt31 = " "
but_txt32 = " "
but_txt33 = " "
but_txt34 = " "
but_txt35 = " "
but_txt36 = " "
but_txt37 = " "
but_txt38 = " "
but_txt39 = " "
but_txt40 = " "
but_txt41 = " "
but_txt42 = " "
but_txt43 = " "
but_txt44 = " "
but_txt45 = " "
but_txt46 = " "
but_txt47 = " "
but_txt48 = " "
but_txt49 = " "
but_txt50 = " "
but_txt51 = " "
but_txt52 = " "
but_txt53 = " "
but_txt54 = " "
but_txt55 = " "
but_txt56 = " "
but_txt57 = " "
but_txt58 = " "
but_txt59 = " "
but_txt60 = " "
but_txt61 = " "
but_txt62 = " "
but_txt63 = " "
but_txt64 = " "
but_txt65 = " "
but_txt66 = " "
but_txt67 = " "
but_txt68 = " "
but_txt69 = " "
but_txt70 = " "
but_txt71 = " "
but_txt72 = " "
but_txt73 = " "
but_txt74 = " "
but_txt75 = " "
but_txt76 = " "
but_txt77 = " "
but_txt78 = " "
but_txt79 = " "
but_txt80 = " "
but_txt81 = " "
but_txt82 = " "
but_txt83 = " "
but_txt84 = " "
but_txt85 = " "
but_txt86 = " "
but_txt87 = " "
but_txt88 = " "
but_txt89 = " "
but_txt90 = " "
but_txt91 = " "
but_txt92 = " "
but_txt93 = " "
but_txt94 = " "
but_txt95 = " "
but_txt96 = " "
but_txt97 = " "
but_txt98 = " "
but_txt99 = " "
but_txt100 = " "
but_txt101 = " "
but_txt102 = " "
but_txt103 = " "
but_txt104 = " "
but_txt105 = " "
but_txt106 = " "
but_txt107 = " "
but_txt108 = " "
but_txt109 = " "
but_txt110 = " "
but_txt111 = " "
but_txt112 = " "
but_txt113 = " "
but_txt114 = " "
but_txt115 = " "
but_txt116 = " "
but_txt117 = " "
but_txt118 = " "
but_txt119 = " "
but_txt120 = " "
but_txt121 = " "
but_txt122 = " "
but_txt123 = " "
but_txt124 = " "
but_txt125 = " "
but_txt126 = " "
but_txt127 = " "
but_txt128 = " "
but_txt129 = " "
#endregion"
#
#region -> Button
def textObjekt(text, pixel_font15):
    textFlaeche = pixel_font15.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()

def button(but_txt, but_x, but_y, but_laenge, but_hoehe, but_color_0, but_color_1, but_font):
    global maus_aktiv
    global option

    if maus_pos[0] > but_x and maus_pos[0] < but_x + but_laenge and maus_pos[1] > but_y and maus_pos[1] < but_y+but_hoehe:
        pygame.draw.rect(screen, but_color_1, (but_x, but_y, but_laenge, but_hoehe))
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            option = but_txt
        if maus_klick[0] == 0:
            maus_aktiv = False
    else:
        pygame.draw.rect(screen, but_color_0, (but_x, but_y, but_laenge, but_hoehe))
    textGrund, textkasten = textObjekt(but_txt, but_font)
    textkasten.center = ((but_x+(but_laenge/2)),(but_y+(but_hoehe/2)))
    screen.blit(textGrund, textkasten)
#endregion
#
#region -> Funktionen
def draw_text(text, sys_font15, color, screen, x , y):
    textobj = sys_font15.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)

def show_fps():
    fps_tick = str(int(clock.get_fps()))
    draw_text(str(fps_tick), sys_font30, "green", screen, 0, 0)
#endregion
#
#region -> runtime
while runtime:
    maus_pos = pygame.mouse.get_pos()
    maus_klick = pygame.mouse.get_pressed()
    pressed = pygame.key.get_pressed()
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False
        elif pressed[pygame.K_ESCAPE]:
            runtime = False
        elif pressed[pygame.K_p]:
            if player == 0:
                player = 1
            elif player == 1:
                player = 0
        elif pressed[pygame.K_SPACE]:
#region
            x_array.clear()
            o_array.clear()

            but_txt0 = " "
            but_txt1 = " "
            but_txt2 = " "
            but_txt3 = " "
            but_txt4 = " "
            but_txt5 = " "
            but_txt6 = " "
            but_txt7 = " "
            but_txt8 = " "
            but_txt9 = " "
            but_txt10 = " "
            but_txt11 = " "
            but_txt12 = " "
            but_txt13 = " "
            but_txt14 = " "
            but_txt15 = " "
            but_txt16 = " "
            but_txt17 = " "
            but_txt18 = " "
            but_txt19 = " "
            but_txt20 = " "
            but_txt21 = " "
            but_txt22 = " "
            but_txt23 = " "
            but_txt24 = " "
            but_txt25 = " "
            but_txt26 = " "
            but_txt27 = " "
            but_txt28 = " "
            but_txt29 = " "
            but_txt30 = " "
            but_txt31 = " "
            but_txt32 = " "
            but_txt33 = " "
            but_txt34 = " "
            but_txt35 = " "
            but_txt36 = " "
            but_txt37 = " "
            but_txt38 = " "
            but_txt39 = " "
            but_txt40 = " "
            but_txt41 = " "
            but_txt42 = " "
            but_txt43 = " "
            but_txt44 = " "
            but_txt45 = " "
            but_txt46 = " "
            but_txt47 = " "
            but_txt48 = " "
            but_txt49 = " "
            but_txt50 = " "
            but_txt51 = " "
            but_txt52 = " "
            but_txt53 = " "
            but_txt54 = " "
            but_txt55 = " "
            but_txt56 = " "
            but_txt57 = " "
            but_txt58 = " "
            but_txt59 = " "
            but_txt60 = " "
            but_txt61 = " "
            but_txt62 = " "
            but_txt63 = " "
            but_txt64 = " "
            but_txt65 = " "
            but_txt66 = " "
            but_txt67 = " "
            but_txt68 = " "
            but_txt69 = " "
            but_txt70 = " "
            but_txt71 = " "
            but_txt72 = " "
            but_txt73 = " "
            but_txt74 = " "
            but_txt75 = " "
            but_txt76 = " "
            but_txt77 = " "
            but_txt78 = " "
            but_txt79 = " "
            but_txt80 = " "
            but_txt81 = " "
            but_txt82 = " "
            but_txt83 = " "
            but_txt84 = " "
            but_txt85 = " "
            but_txt86 = " "
            but_txt87 = " "
            but_txt88 = " "
            but_txt89 = " "
            but_txt90 = " "
            but_txt91 = " "
            but_txt92 = " "
            but_txt93 = " "
            but_txt94 = " "
            but_txt95 = " "
            but_txt96 = " "
            but_txt97 = " "
            but_txt98 = " "
            but_txt99 = " "
            but_txt100 = " "
            but_txt101 = " "
            but_txt102 = " "
            but_txt103 = " "
            but_txt104 = " "
            but_txt105 = " "
            but_txt106 = " "
            but_txt107 = " "
            but_txt108 = " "
            but_txt109 = " "
            but_txt110 = " "
            but_txt111 = " "
            but_txt112 = " "
            but_txt113 = " "
            but_txt114 = " "
            but_txt115 = " "
            but_txt116 = " "
            but_txt117 = " "
            but_txt118 = " "
            but_txt119 = " "
            but_txt120 = " "
            but_txt121 = " "
            but_txt122 = " "
            but_txt123 = " "
            but_txt124 = " "
            but_txt125 = " "
            but_txt126 = " "
            but_txt127 = " "
            but_txt128 = " "
            but_txt129 = " "
#endregion -> reset tiles
#region -> reihe 0 beschreiben
    if maus_pos[0] > 0 and maus_pos[0] < 0 + 100 and maus_pos[1] > 0 and maus_pos[1] < 0+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt0 = "O"
            elif player == 1:
                but_txt0 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 100 and maus_pos[0] < 100 + 100 and maus_pos[1] > 0 and maus_pos[1] < 0+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt1 = "O"
            elif player == 1:
                but_txt1 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 200 and maus_pos[0] < 200 + 100 and maus_pos[1] > 0 and maus_pos[1] < 0+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt2 = "O"
            elif player == 1:
                but_txt2 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 300 and maus_pos[0] < 300 + 100 and maus_pos[1] > 0 and maus_pos[1] < 0+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt3 = "O"
            elif player == 1:
                but_txt3 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 400 and maus_pos[0] < 400 + 100 and maus_pos[1] > 0 and maus_pos[1] < 0+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt4 = "O"
            elif player == 1:
                but_txt4 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 500 and maus_pos[0] < 500 + 100 and maus_pos[1] > 0 and maus_pos[1] < 0+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt5 = "O"
            elif player == 1:
                but_txt5 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 600 and maus_pos[0] < 600 + 100 and maus_pos[1] > 0 and maus_pos[1] < 0+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt6 = "O"
            elif player == 1:
                but_txt6 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 700 and maus_pos[0] < 700 + 100 and maus_pos[1] > 0 and maus_pos[1] < 0+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt7 = "O"
            elif player == 1:
                but_txt7 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 800 and maus_pos[0] < 800 + 100 and maus_pos[1] > 0 and maus_pos[1] < 0+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt8 = "O"
            elif player == 1:
                but_txt8 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 900 and maus_pos[0] < 900 + 100 and maus_pos[1] > 0 and maus_pos[1] < 0+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt9 = "O"
            elif player == 1:
                but_txt9 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 1000 and maus_pos[0] < 1000 + 100 and maus_pos[1] > 0 and maus_pos[1] < 0+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt10 = "O"
            elif player == 1:
                but_txt10 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 1100 and maus_pos[0] < 1100 + 100 and maus_pos[1] > 0 and maus_pos[1] < 0+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt11 = "O"
            elif player == 1:
                but_txt11 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 1200 and maus_pos[0] < 1200 + 100 and maus_pos[1] > 0 and maus_pos[1] < 0+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt12 = "O"
            elif player == 1:
                but_txt12 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
#endregion
    #region -> reihe 1 beschreiben
    if maus_pos[0] > 0 and maus_pos[0] < 0 + 100 and maus_pos[1] > 100 and maus_pos[1] < 100+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt13 = "O"
            elif player == 1:
                but_txt13 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 100 and maus_pos[0] < 100 + 100 and maus_pos[1] > 100 and maus_pos[1] < 100+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt14 = "O"
            elif player == 1:
                but_txt14 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 200 and maus_pos[0] < 200 + 100 and maus_pos[1] > 100 and maus_pos[1] < 100+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt15 = "O"
            elif player == 1:
                but_txt15 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 300 and maus_pos[0] < 300 + 100 and maus_pos[1] > 100 and maus_pos[1] < 100+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt16 = "O"
            elif player == 1:
                but_txt16 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 400 and maus_pos[0] < 400 + 100 and maus_pos[1] > 100 and maus_pos[1] < 100+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt17 = "O"
            elif player == 1:
                but_txt17 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 500 and maus_pos[0] < 500 + 100 and maus_pos[1] > 100 and maus_pos[1] < 100+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt18 = "O"
            elif player == 1:
                but_txt18 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 600 and maus_pos[0] < 600 + 100 and maus_pos[1] > 100 and maus_pos[1] < 100+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt19 = "O"
            elif player == 1:
                but_txt19 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 700 and maus_pos[0] < 700 + 100 and maus_pos[1] > 100 and maus_pos[1] < 100+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt20 = "O"
            elif player == 1:
                but_txt20 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 800 and maus_pos[0] < 800 + 100 and maus_pos[1] > 100 and maus_pos[1] < 100+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt21 = "O"
            elif player == 1:
                but_txt21 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 900 and maus_pos[0] < 900 + 100 and maus_pos[1] > 100 and maus_pos[1] < 100+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt22 = "O"
            elif player == 1:
                but_txt22 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 1000 and maus_pos[0] < 1000 + 100 and maus_pos[1] > 100 and maus_pos[1] < 100+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt23 = "O"
            elif player == 1:
                but_txt23 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 1100 and maus_pos[0] < 1100 + 100 and maus_pos[1] > 100 and maus_pos[1] < 100+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt24 = "O"
            elif player == 1:
                but_txt24 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 1200 and maus_pos[0] < 1200 + 100 and maus_pos[1] > 100 and maus_pos[1] < 100+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt25 = "O"
            elif player == 1:
                but_txt25 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    #endregion
    #region -> reihe 0 beschreiben
    if maus_pos[0] > 0 and maus_pos[0] < 0 + 100 and maus_pos[1] > 200 and maus_pos[1] < 200+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt26 = "O"
            elif player == 1:
                but_txt26 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 100 and maus_pos[0] < 100 + 100 and maus_pos[1] > 200 and maus_pos[1] < 200+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt27 = "O"
            elif player == 1:
                but_txt27 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 200 and maus_pos[0] < 200 + 100 and maus_pos[1] > 200 and maus_pos[1] < 200+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt28 = "O"
            elif player == 1:
                but_txt28 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 300 and maus_pos[0] < 300 + 100 and maus_pos[1] > 200 and maus_pos[1] < 200+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt29 = "O"
            elif player == 1:
                but_txt29 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 400 and maus_pos[0] < 400 + 100 and maus_pos[1] > 200 and maus_pos[1] < 200+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt30 = "O"
            elif player == 1:
                but_txt30 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 500 and maus_pos[0] < 500 + 100 and maus_pos[1] > 200 and maus_pos[1] < 200+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt31 = "O"
            elif player == 1:
                but_txt31 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 600 and maus_pos[0] < 600 + 100 and maus_pos[1] > 200 and maus_pos[1] < 200+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt32 = "O"
            elif player == 1:
                but_txt32 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 700 and maus_pos[0] < 700 + 100 and maus_pos[1] > 200 and maus_pos[1] < 200+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt33 = "O"
            elif player == 1:
                but_txt33 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 800 and maus_pos[0] < 800 + 100 and maus_pos[1] > 200 and maus_pos[1] < 200+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt34 = "O"
            elif player == 1:
                but_txt34 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 900 and maus_pos[0] < 900 + 100 and maus_pos[1] > 200 and maus_pos[1] < 200+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt35 = "O"
            elif player == 1:
                but_txt35 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 1000 and maus_pos[0] < 1000 + 100 and maus_pos[1] > 200 and maus_pos[1] < 200+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt36 = "O"
            elif player == 1:
                but_txt36 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 1100 and maus_pos[0] < 1100 + 100 and maus_pos[1] > 200 and maus_pos[1] < 200+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt37 = "O"
            elif player == 1:
                but_txt37 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    if maus_pos[0] > 1200 and maus_pos[0] < 1200 + 100 and maus_pos[1] > 200 and maus_pos[1] < 200+100:
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            if player == 0:
                but_txt38 = "O"
            elif player == 1:
                but_txt38 = "X"
        if maus_klick[0] == 0:
            maus_aktiv = False
    #endregion



#region
    if but_txt0 == "X":
        x_array[0] = 1
    if but_txt0 == "O":
        o_array[0] = 1
    if but_txt1 == "X":
        x_array[1] = 1
    if but_txt1 == "O":
        o_array[1] = 1
    if but_txt2 == "X":
        x_array[2] = 1
    if but_txt2 == "O":
        o_array[2] = 1
    if but_txt3 == "X":
        x_array[3] = 1
    if but_txt3 == "O":
        o_array[3] = 1
    if but_txt4 == "X":
        x_array[4] = 1
    if but_txt4 == "O":
        o_array[4] = 1
    if but_txt5 == "X":
        x_array[5] = 1
    if but_txt5 == "O":
        o_array[5] = 1
    if but_txt6 == "X":
        x_array[6] = 1
    if but_txt6 == "O":
        o_array[6] = 1
    if but_txt7 == "X":
        x_array[7] = 1
    if but_txt7 == "O":
        o_array[7] = 1
    if but_txt8 == "X":
        x_array[8] = 1
    if but_txt8 == "O":
        o_array[8] = 1
    if but_txt9 == "X":
        x_array[9] = 1
    if but_txt9 == "O":
        o_array[9] = 1
    if but_txt10 == "X":
        x_array[10] = 1
    if but_txt10 == "O":
        o_array[10] = 1
    if but_txt11 == "X":
        x_array[11] = 1
    if but_txt11 == "O":
        o_array[11] = 1
    if but_txt12 == "X":
        x_array[12] = 1
    if but_txt12 == "O":
        o_array[12] = 1
    if but_txt13 == "X":
        x_array[13] = 1
    if but_txt13 == "O":
        o_array[13] = 1
    if but_txt14 == "X":
        x_array[14] = 1
    if but_txt14 == "O":
        o_array[14] = 1
    if but_txt15 == "X":
        x_array[15] = 1
    if but_txt15 == "O":
        o_array[15] = 1
    if but_txt16 == "X":
        x_array[16] = 1
    if but_txt16 == "O":
        o_array[16] = 1
    if but_txt17 == "X":
        x_array[17] = 1
    if but_txt17 == "O":
        o_array[17] = 1
    if but_txt18 == "X":
        x_array[18] = 1
    if but_txt18 == "O":
        o_array[18] = 1
    if but_txt19 == "X":
        x_array[19] = 1
    if but_txt19 == "O":
        o_array[19] = 1
    if but_txt20 == "X":
        x_array[20] = 1
    if but_txt20 == "O":
        o_array[20] = 1
    if but_txt21 == "X":
        x_array[21] = 1
    if but_txt21 == "O":
        o_array[21] = 1
    if but_txt22 == "X":
        x_array[22] = 1
    if but_txt22 == "O":
        o_array[22] = 1
    if but_txt23 == "X":
        x_array[23] = 1
    if but_txt23 == "O":
        o_array[23] = 1
    if but_txt24 == "X":
        x_array[24] = 1
    if but_txt24 == "O":
        o_array[24] = 1
    if but_txt25 == "X":
        x_array[25] = 1
    if but_txt25 == "O":
        o_array[25] = 1
    if but_txt26 == "X":
        x_array[26] = 1
    if but_txt26 == "O":
        o_array[26] = 1
    if but_txt27 == "X":
        x_array[27] = 1
    if but_txt27 == "O":
        o_array[27] = 1
    if but_txt28 == "X":
        x_array[28] = 1
    if but_txt28 == "O":
        o_array[28] = 1
    if but_txt29 == "X":
        x_array[29] = 1
    if but_txt29 == "O":
        o_array[29] = 1
    if but_txt30 == "X":
        x_array[30] = 1
    if but_txt30 == "O":
        o_array[30] = 1
    if but_txt31 == "X":
        x_array[31] = 1
    if but_txt31 == "O":
        o_array[31] = 1
    if but_txt32 == "X":
        x_array[32] = 1
    if but_txt32 == "O":
        o_array[32] = 1
    if but_txt33 == "X":
        x_array[33] = 1
    if but_txt33 == "O":
        o_array[33] = 1
    if but_txt34 == "X":
        x_array[34] = 1
    if but_txt34 == "O":
        o_array[34] = 1
    if but_txt35 == "X":
        x_array[35] = 1
    if but_txt35 == "O":
        o_array[35] = 1
    if but_txt36 == "X":
        x_array[36] = 1
    if but_txt36 == "O":
        o_array[36] = 1
    if but_txt37 == "X":
        x_array[37] = 1
    if but_txt37 == "O":
        o_array[37] = 1
    if but_txt38 == "X":
        x_array[38] = 1
    if but_txt38 == "O":
        o_array[38] = 1
    if but_txt39 == "X":
        x_array[39] = 1
    if but_txt39 == "O":
        o_array[39] = 1
    if but_txt40 == "X":
        x_array[40] = 1
    if but_txt40 == "O":
        o_array[40] = 1
    if but_txt41 == "X":
        x_array[41] = 1
    if but_txt41 == "O":
        o_array[41] = 1
    if but_txt42 == "X":
        x_array[42] = 1
    if but_txt42 == "O":
        o_array[42] = 1
    if but_txt43 == "X":
        x_array[43] = 1
    if but_txt43 == "O":
        o_array[43] = 1
    if but_txt44 == "X":
        x_array[44] = 1
    if but_txt44 == "O":
        o_array[44] = 1
    if but_txt45 == "X":
        x_array[45] = 1
    if but_txt45 == "O":
        o_array[45] = 1
    if but_txt46 == "X":
        x_array[46] = 1
    if but_txt46 == "O":
        o_array[46] = 1
    if but_txt47 == "X":
        x_array[47] = 1
    if but_txt47 == "O":
        o_array[47] = 1
    if but_txt48 == "X":
        x_array[48] = 1
    if but_txt48 == "O":
        o_array[48] = 1
    if but_txt49 == "X":
        x_array[49] = 1
    if but_txt49 == "O":
        o_array[49] = 1
    if but_txt50 == "X":
        x_array[50] = 1
    if but_txt50 == "O":
        o_array[50] = 1
    if but_txt51 == "X":
        x_array[51] = 1
    if but_txt51 == "O":
        o_array[51] = 1
    if but_txt52 == "X":
        x_array[52] = 1
    if but_txt52 == "O":
        o_array[52] = 1
    if but_txt53 == "X":
        x_array[53] = 1
    if but_txt53 == "O":
        o_array[53] = 1
    if but_txt54 == "X":
        x_array[54] = 1
    if but_txt54 == "O":
        o_array[54] = 1
    if but_txt55 == "X":
        x_array[55] = 1
    if but_txt55 == "O":
        o_array[55] = 1
    if but_txt56 == "X":
        x_array[56] = 1
    if but_txt56 == "O":
        o_array[56] = 1
    if but_txt57 == "X":
        x_array[57] = 1
    if but_txt57 == "O":
        o_array[57] = 1
    if but_txt58 == "X":
        x_array[58] = 1
    if but_txt58 == "O":
        o_array[58] = 1
    if but_txt59 == "X":
        x_array[59] = 1
    if but_txt59 == "O":
        o_array[59] = 1
    if but_txt60 == "X":
        x_array[60] = 1
    if but_txt60 == "O":
        o_array[60] = 1
    if but_txt61 == "X":
        x_array[61] = 1
    if but_txt61 == "O":
        o_array[61] = 1
    if but_txt62 == "X":
        x_array[62] = 1
    if but_txt62 == "O":
        o_array[62] = 1
    if but_txt63 == "X":
        x_array[63] = 1
    if but_txt63 == "O":
        o_array[63] = 1
    if but_txt64 == "X":
        x_array[64] = 1
    if but_txt64 == "O":
        o_array[64] = 1
    if but_txt65 == "X":
        x_array[65] = 1
    if but_txt65 == "O":
        o_array[65] = 1
    if but_txt66 == "X":
        x_array[66] = 1
    if but_txt66 == "O":
        o_array[66] = 1
    if but_txt67 == "X":
        x_array[67] = 1
    if but_txt67 == "O":
        o_array[67] = 1
    if but_txt68 == "X":
        x_array[68] = 1
    if but_txt68 == "O":
        o_array[68] = 1
    if but_txt69 == "X":
        x_array[69] = 1
    if but_txt69 == "O":
        o_array[69] = 1
    if but_txt70 == "X":
        x_array[70] = 1
    if but_txt70 == "O":
        o_array[70] = 1
    if but_txt71 == "X":
        x_array[71] = 1
    if but_txt71 == "O":
        o_array[71] = 1
    if but_txt72 == "X":
        x_array[72] = 1
    if but_txt72 == "O":
        o_array[72] = 1
    if but_txt73 == "X":
        x_array[73] = 1
    if but_txt73 == "O":
        o_array[73] = 1
    if but_txt74 == "X":
        x_array[74] = 1
    if but_txt74 == "O":
        o_array[74] = 1
    if but_txt75 == "X":
        x_array[75] = 1
    if but_txt75 == "O":
        o_array[75] = 1
    if but_txt76 == "X":
        x_array[76] = 1
    if but_txt76 == "O":
        o_array[76] = 1
    if but_txt77 == "X":
        x_array[77] = 1
    if but_txt77 == "O":
        o_array[77] = 1
    if but_txt78 == "X":
        x_array[78] = 1
    if but_txt78 == "O":
        o_array[78] = 1
    if but_txt79 == "X":
        x_array[79] = 1
    if but_txt79 == "O":
        o_array[79] = 1
    if but_txt80 == "X":
        x_array[80] = 1
    if but_txt80 == "O":
        o_array[80] = 1
    if but_txt81 == "X":
        x_array[81] = 1
    if but_txt81 == "O":
        o_array[81] = 1
    if but_txt82 == "X":
        x_array[82] = 1
    if but_txt82 == "O":
        o_array[82] = 1
    if but_txt83 == "X":
        x_array[83] = 1
    if but_txt83 == "O":
        o_array[83] = 1
    if but_txt84 == "X":
        x_array[84] = 1
    if but_txt84 == "O":
        o_array[84] = 1
    if but_txt85 == "X":
        x_array[85] = 1
    if but_txt85 == "O":
        o_array[85] = 1
    if but_txt86 == "X":
        x_array[86] = 1
    if but_txt86 == "O":
        o_array[86] = 1
    if but_txt87 == "X":
        x_array[87] = 1
    if but_txt87 == "O":
        o_array[87] = 1
    if but_txt88 == "X":
        x_array[88] = 1
    if but_txt88 == "O":
        o_array[88] = 1
    if but_txt89 == "X":
        x_array[89] = 1
    if but_txt89 == "O":
        o_array[89] = 1
    if but_txt90 == "X":
        x_array[90] = 1
    if but_txt90 == "O":
        o_array[90] = 1
    if but_txt91 == "X":
        x_array[91] = 1
    if but_txt91 == "O":
        o_array[91] = 1
    if but_txt92 == "X":
        x_array[92] = 1
    if but_txt92 == "O":
        o_array[92] = 1
    if but_txt93 == "X":
        x_array[93] = 1
    if but_txt93 == "O":
        o_array[93] = 1
    if but_txt94 == "X":
        x_array[94] = 1
    if but_txt94 == "O":
        o_array[94] = 1
    if but_txt95 == "X":
        x_array[95] = 1
    if but_txt95 == "O":
        o_array[95] = 1
    if but_txt96 == "X":
        x_array[96] = 1
    if but_txt96 == "O":
        o_array[96] = 1
    if but_txt97 == "X":
        x_array[97] = 1
    if but_txt97 == "O":
        o_array[97] = 1
    if but_txt98 == "X":
        x_array[98] = 1
    if but_txt98 == "O":
        o_array[98] = 1
    if but_txt99 == "X":
        x_array[99] = 1
    if but_txt99 == "O":
        o_array[99] = 1
    if but_txt100 == "X":
        x_array[100] = 1
    if but_txt100 == "O":
        o_array[100] = 1
    if but_txt101 == "X":
        x_array[101] = 1
    if but_txt101 == "O":
        o_array[101] = 1
    if but_txt102 == "X":
        x_array[102] = 1
    if but_txt102 == "O":
        o_array[102] = 1
    if but_txt103 == "X":
        x_array[103] = 1
    if but_txt103 == "O":
        o_array[103] = 1
    if but_txt104 == "X":
        x_array[104] = 1
    if but_txt104 == "O":
        o_array[104] = 1
    if but_txt105 == "X":
        x_array[105] = 1
    if but_txt105 == "O":
        o_array[105] = 1
    if but_txt106 == "X":
        x_array[106] = 1
    if but_txt106 == "O":
        o_array[106] = 1
    if but_txt107 == "X":
        x_array[107] = 1
    if but_txt107 == "O":
        o_array[107] = 1
    if but_txt108 == "X":
        x_array[108] = 1
    if but_txt108 == "O":
        o_array[108] = 1
    if but_txt109 == "X":
        x_array[109] = 1
    if but_txt109 == "O":
        o_array[109] = 1
    if but_txt110 == "X":
        x_array[110] = 1
    if but_txt110 == "O":
        o_array[110] = 1
    if but_txt111 == "X":
        x_array[111] = 1
    if but_txt111 == "O":
        o_array[111] = 1
    if but_txt112 == "X":
        x_array[112] = 1
    if but_txt112 == "O":
        o_array[112] = 1
    if but_txt113 == "X":
        x_array[113] = 1
    if but_txt113 == "O":
        o_array[113] = 1
    if but_txt114 == "X":
        x_array[114] = 1
    if but_txt114 == "O":
        o_array[114] = 1
    if but_txt115 == "X":
        x_array[115] = 1
    if but_txt115 == "O":
        o_array[115] = 1
    if but_txt116 == "X":
        x_array[116] = 1
    if but_txt116 == "O":
        o_array[116] = 1
    if but_txt117 == "X":
        x_array[117] = 1
    if but_txt117 == "O":
        o_array[117] = 1
    if but_txt118 == "X":
        x_array[118] = 1
    if but_txt118 == "O":
        o_array[118] = 1
    if but_txt119 == "X":
        x_array[119] = 1
    if but_txt119 == "O":
        o_array[119] = 1
    if but_txt120 == "X":
        x_array[120] = 1
    if but_txt120 == "O":
        o_array[120] = 1
    if but_txt121 == "X":
        x_array[121] = 1
    if but_txt121 == "O":
        o_array[121] = 1
    if but_txt122 == "X":
        x_array[122] = 1
    if but_txt122 == "O":
        o_array[122] = 1
    if but_txt123 == "X":
        x_array[123] = 1
    if but_txt123 == "O":
        o_array[123] = 1
    if but_txt124 == "X":
        x_array[124] = 1
    if but_txt124 == "O":
        o_array[124] = 1
    if but_txt125 == "X":
        x_array[125] = 1
    if but_txt125 == "O":
        o_array[125] = 1
    if but_txt126 == "X":
        x_array[126] = 1
    if but_txt126 == "O":
        o_array[126] = 1
    if but_txt127 == "X":
        x_array[127] = 1
    if but_txt127 == "O":
        o_array[127] = 1
    if but_txt128 == "X":
        x_array[128] = 1
    if but_txt128 == "O":
        o_array[128] = 1
    if but_txt129 == "X":
        x_array[129] = 1
    if but_txt129 == "O":
        o_array[129] = 1
#endregion



#region -> reihenclusterfuck
#region -> row 0
    but0 =button(but_txt0, 0, 0, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but1 =button(but_txt1, 100, 0, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but2 =button(but_txt2, 200, 0, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but3 =button(but_txt3, 300, 0, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but4 =button(but_txt4, 400, 0, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but5 =button(but_txt5, 500, 0, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but6 =button(but_txt6, 600, 0, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but7 =button(but_txt7, 700, 0, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but8 =button(but_txt8, 800, 0, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but9 =button(but_txt9, 900, 0, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but10 =button(but_txt10, 1000, 0, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but11 =button(but_txt11, 1100, 0, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but12 =button(but_txt12, 1200, 0, 100, 100, (255,0,0), (0,255,0), pixel_font30)
#endregion
#region -> row 1
    but13 =button(but_txt13, 0, 100, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but14 =button(but_txt14, 100, 100, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but15 =button(but_txt15, 200, 100, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but16 =button(but_txt16, 300, 100, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but17 =button(but_txt17, 400, 100, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but18 =button(but_txt18, 500, 100, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but19 =button(but_txt19, 600, 100, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but20 =button(but_txt20, 700, 100, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but21 =button(but_txt21, 800, 100, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but22 =button(but_txt22, 900, 100, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but23 =button(but_txt23, 1000, 100, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but24 =button(but_txt24, 1100, 100, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but25 =button(but_txt25, 1200, 100, 100, 100, (255,0,0), (0,255,0), pixel_font30)
#endregion
#region -> row 2
    but26 =button(but_txt26, 0, 200, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but27 =button(but_txt27, 100, 200, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but28 =button(but_txt28, 200, 200, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but29 =button(but_txt29, 300, 200, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but30 =button(but_txt30, 400, 200, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but31 =button(but_txt31, 500, 200, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but32 =button(but_txt32, 600, 200, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but33 =button(but_txt33, 700, 200, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but34 =button(but_txt34, 800, 200, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but35 =button(but_txt35, 900, 200, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but36 =button(but_txt36, 1000, 200, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but37 =button(but_txt37, 1100, 200, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but38 =button(but_txt38, 1200, 200, 100, 100, (255,0,0), (0,255,0), pixel_font30)
#endregion
#region -> row 3
    but39 =button(but_txt39, 0, 300, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but40 =button(but_txt40, 100, 300, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but41 =button(but_txt41, 200, 300, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but42 =button(but_txt42, 300, 300, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but43 =button(but_txt43, 400, 300, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but44 =button(but_txt44, 500, 300, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but45 =button(but_txt45, 600, 300, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but46 =button(but_txt46, 700, 300, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but47 =button(but_txt47, 800, 300, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but48 =button(but_txt48, 900, 300, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but49 =button(but_txt49, 1000, 300, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but50 =button(but_txt50, 1100, 300, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but51 =button(but_txt51, 1200, 300, 100, 100, (255,0,0), (0,255,0), pixel_font30)
#endregion
#region -> row 4
    but52 =button(but_txt52, 0, 400, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but53 =button(but_txt53, 100, 400, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but54 =button(but_txt54, 200, 400, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but55 =button(but_txt55, 300, 400, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but56 =button(but_txt56, 400, 400, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but57 =button(but_txt57, 500, 400, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but58 =button(but_txt58, 600, 400, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but59 =button(but_txt59, 700, 400, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but60 =button(but_txt60, 800, 400, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but61 =button(but_txt61, 900, 400, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but62 =button(but_txt62, 1000, 400, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but63 =button(but_txt63, 1100, 400, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but64 =button(but_txt64, 1200, 400, 100, 100, (255,0,0), (0,255,0), pixel_font30)
#endregion
#region -> row 5
    but65 =button(but_txt65, 0, 500, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but66 =button(but_txt66, 100, 500, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but67 =button(but_txt67, 200, 500, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but68 =button(but_txt68, 300, 500, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but69 =button(but_txt69, 400, 500, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but70 =button(but_txt70, 500, 500, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but71 =button(but_txt71, 600, 500, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but72 =button(but_txt72, 700, 500, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but73 =button(but_txt73, 800, 500, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but74 =button(but_txt74, 900, 500, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but75 =button(but_txt75, 1000, 500, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but76 =button(but_txt76, 1100, 500, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but77 =button(but_txt77, 1200, 500, 100, 100, (255,0,0), (0,255,0), pixel_font30)
#endregion
#region -> row 6
    but78 =button(but_txt78, 0, 600, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but79 =button(but_txt79, 100, 600, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but80 =button(but_txt80, 200, 600, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but81 =button(but_txt81, 300, 600, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but82 =button(but_txt82, 400, 600, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but83 =button(but_txt83, 500, 600, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but84 =button(but_txt84, 600, 600, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but85 =button(but_txt85, 700, 600, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but86 =button(but_txt86, 800, 600, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but87 =button(but_txt87, 900, 600, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but88 =button(but_txt88, 1000, 600, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but89 =button(but_txt89, 1100, 600, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but90 =button(but_txt90, 1200, 600, 100, 100, (255,0,0), (0,255,0), pixel_font30)
#endregion
#region -> row 7
    but91 =button(but_txt91, 0, 700, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but92 =button(but_txt92, 100, 700, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but93 =button(but_txt93, 200, 700, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but94 =button(but_txt94, 300, 700, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but95 =button(but_txt95, 400, 700, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but96 =button(but_txt96, 500, 700, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but97 =button(but_txt97, 600, 700, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but98 =button(but_txt98, 700, 700, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but99 =button(but_txt99, 800, 700, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but100 =button(but_txt100, 900, 700, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but101 =button(but_txt101, 1000, 700, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but102 =button(but_txt102, 1100, 700, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but103 =button(but_txt103, 1200, 700, 100, 100, (255,0,0), (0,255,0), pixel_font30)
#endregion
#region -> row 8
    but104 =button(but_txt104, 0, 800, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but105 =button(but_txt105, 100, 800, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but106 =button(but_txt106, 200, 800, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but107 =button(but_txt107, 300, 800, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but108 =button(but_txt108, 400, 800, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but109 =button(but_txt109, 500, 800, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but110 =button(but_txt110, 600, 800, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but111 =button(but_txt111, 700, 800, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but112 =button(but_txt112, 800, 800, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but113 =button(but_txt113, 900, 800, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but114 =button(but_txt114, 1000, 800, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but115 =button(but_txt115, 1100, 800, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but116 =button(but_txt116, 1200, 800, 100, 100, (255,0,0), (0,255,0), pixel_font30)
#endregion
#region -> row 9
    but117 =button(but_txt117, 0, 900, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but118 =button(but_txt118, 100, 900, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but119 =button(but_txt119, 200, 900, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but120 =button(but_txt120, 300, 900, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but121 =button(but_txt121, 400, 900, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but122 =button(but_txt122, 500, 900, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but123 =button(but_txt123, 600, 900, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but124 =button(but_txt124, 700, 900, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but125 =button(but_txt125, 800, 900, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but126 =button(but_txt126, 900, 900, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but127 =button(but_txt127, 1000, 900, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but128 =button(but_txt128, 1100, 900, 100, 100, (255,0,0), (0,255,0), pixel_font30)
    but129 =button(but_txt129, 1200, 900, 100, 100, (255,0,0), (0,255,0), pixel_font30)
#endregion
#endregion

#region -> UI Text
    draw_text("Vier Gewinnt", sys_font60, "green", screen, 1500, 40)
    pygame.draw.rect(screen, "white", [1450, 90, 370, 40], 1)
    if player == 0:
        draw_text("Spieler O ist dran", sys_font30, "green", screen, 1550, 100)
    elif player == 1:
        draw_text("Spieler 1 ist dran", sys_font30, "green", screen, 1550, 100)
#endregion
    print(player)
    show_fps()
    pygame.display.flip()
    clock.tick(fps)
#endregion
#
