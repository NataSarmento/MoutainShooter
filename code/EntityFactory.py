import random
import pygame
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player
from code.Enemy import Enemy


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0), speed=5):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(1, 3):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player':
                return Player('Player', (10, WIN_HEIGHT - 150))

            case 'Enemy':
                y_pos = WIN_HEIGHT - 120
                x_pos = WIN_WIDTH + 100

                ent = Enemy(name='Enemy', position=(x_pos, y_pos), speed=speed)
                ent.surf = pygame.transform.scale(ent.surf, (80, 80))
                ent.rect = ent.surf.get_rect(topleft=(x_pos, y_pos))
                return ent

            case 'Enemy2':

                y_pos = 150
                x_pos = WIN_WIDTH + 100

                ent = Enemy(name='Enemy2', position=(x_pos, y_pos), speed=speed + 2)
                ent.surf = pygame.transform.scale(ent.surf, (70, 70))
                ent.rect = ent.surf.get_rect(topleft=(x_pos, y_pos))
                return ent
