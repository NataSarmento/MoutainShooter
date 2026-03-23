from code.Const import WIN_WIDTH
from code.Entity import Entity


class Enemy(Entity):
    #PARÂMETRO 'speed'
    def __init__(self, name: str, position: tuple, speed: float):
        super().__init__(name, position)

        # VELOCIDADE DINÂMICA NO INIMIGO:
        self.speed = speed

    def move(self):
        # O MOVIMENTO AGORA É DITADO PELA VELOCIDADE DO LEVEL:
        self.rect.centerx -= self.speed




