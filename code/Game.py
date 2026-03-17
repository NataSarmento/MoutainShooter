import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # check for all events
        # for events in pygame.event.get():
        #    if events.type == pygame.QUIT:
        #       pygame.quit()  # close window
        #      quit()  # end pygame
