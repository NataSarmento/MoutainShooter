import pygame

from code.Const import GRAVITY, WIN_HEIGHT, JUMP_SIZE
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.vertical_speed = 0

    def update(self):
        pass


    def move(self):
        self.vertical_speed += GRAVITY
        self.rect.y += self.vertical_speed
        if self.rect.bottom > WIN_HEIGHT-50:
            self.rect.bottom= WIN_HEIGHT-50
            self.vertical_speed = 0
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_SPACE]:
                if self.rect.bottom == WIN_HEIGHT-50:
                    self.vertical_speed = JUMP_SIZE
        pass
