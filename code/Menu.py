import pygame.image

from code.Const import WIN_WIDTH, COLOR_BLACK, MENU_OPTION, COLOR_BLUE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/background.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/som.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=100, text="THE", text_color=COLOR_BLACK, text_center_pos=((WIN_WIDTH / 2.3), 70))
            self.menu_text(text_size=100, text="VAMPIRE", text_color=COLOR_BLACK, text_center_pos=((WIN_WIDTH / 2.3), 200))

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=50, text=MENU_OPTION[i], text_color=COLOR_BLUE,
                              text_center_pos=((WIN_WIDTH / 2.3), 400 + 70 * i))



            pygame.display.flip()
            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame


    def menu_text(self, text_size, text, text_color, text_center_pos):
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)