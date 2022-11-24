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
but_txt = " "
player = 0
but_txt = [" "]*120000
but_txt_ind = 0

img = pygame.image.load("test.png")

recht_x = ["0", "100", "200", "300", "400", "500", "600", "700", "800", "900", "1000", "1100", "1200"]
recht_y = ["0", "100", "200", "300", "400", "500", "600", "700", "800", "900", "1000"]


#region -> Button
def textObjekt(text, pixel_font15):
    textFlaeche = pixel_font15.render(text, True, (0, 0, 0))C-PNQA4894
    return textFlaeche, textFlaeche.get_rect()

def button(img, but_x, but_y, but_laenge, but_hoehe, but_color_0, but_color_1, but_font):
    global maus_aktiv
    global option

    if maus_pos[0] > but_x and maus_pos[0] < but_x + but_laenge and maus_pos[1] > but_y and maus_pos[1] < but_y+but_hoehe:
        pygame.draw.rect(screen, but_color_1, (but_x, but_y, but_laenge, but_hoehe))
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
        if maus_klick[0] == 0:
            maus_aktiv = False
    else:
        pygame.draw.rect(screen, but_color_0, (but_x, but_y, but_laenge, but_hoehe))
    textGrund, textkasten = textObjekt(but_txt, but_font)
    textkasten.center = ((but_x+(but_laenge/2)),(but_y+(but_hoehe/2)))
    screen.blit(img, textkasten)
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
index_x = 0
runtime = True
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
            else:
                player = 0



    for x in recht_x:
        for y in recht_y:
            rect_cor_y += 100
            if rect_cor_y > 1000:
                rect_cor_x = rect_cor_x + 100
                rect_cor_y = 0
            if rect_cor_x > 1200:
                rect_cor_x = 0

            if player == 0:
                but_txt_ind = (int(x) * int(y)) / int(1000)
                print(int(but_txt_ind))
                but_txt[int(but_txt_ind)] = "O"

            if player == 1:
                but_txt_ind = (int(x) * int(y)) / int (1000)
                print(int(but_txt_ind))
                but_txt[int(but_txt_ind)] = "X"

            button(img, rect_cor_x, rect_cor_y, 100, 100, (255,0,0), (0,255,0), pixel_font60)








#region -> UI Text
    draw_text("Vier Gewinnt", sys_font60, "green", screen, 1500, 40)

#endregion

    show_fps()
    pygame.display.flip()
    clock.tick(fps)