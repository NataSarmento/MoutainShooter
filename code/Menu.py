import pygame.image

from code.Const import WIN_WIDTH, COLOR_BLACK, MENU_OPTION, COLOR_BLUE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/background.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/som.mp3')
        pygame.mixer_music.play(-1)
        while True:
            #DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=100, text="THE", text_color=COLOR_BLACK, text_center_pos=((WIN_WIDTH / 2.3), 70))
            self.menu_text(text_size=100, text="VAMPIRE", text_color=COLOR_BLACK,
                           text_center_pos=((WIN_WIDTH / 2.3), 200))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=50, text=MENU_OPTION[i], text_color=COLOR_BLUE,
                                   text_center_pos=((WIN_WIDTH / 2.3), 400 + 70 * i))

                else:
                    self.menu_text(text_size=50, text=MENU_OPTION[i], text_color=COLOR_YELLOW,
                                   text_center_pos=((WIN_WIDTH / 2.3), 400 + 70 * i))
            pygame.display.flip()
            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN: #down key
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: #up key
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # enter
                        return MENU_OPTION[menu_option]


    def menu_text(self, text_size, text, text_color, text_center_pos):
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
