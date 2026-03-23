import pygame
import sys
from code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.Menu import Menu
from code.Score import Score
from code.level import Level


class Game:
    def __init__(self):
        """Inicializa o motor gráfico e configura a janela principal do jogo."""
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Vampire Shooter - Project")

    def run(self):
        """Loop principal de orquestração do jogo. Gerencia a transição entre telas."""

        # Instanciação das classes de interface (Menu e Score)
        # Fazemos isso fora do loop para otimização de recursos
        menu = Menu(self.window)
        score_screen = Score(self.window)

        while True:
            # Invoca o menu e captura a opção selecionada pelo usuário
            menu_return = menu.run()

            # Lógica de roteamento baseada no retorno do Menu
            if menu_return == MENU_OPTION[0]:
                # Inicia a fase principal do jogo (New Game)
                level = Level(self.window, 'Level1', menu_return)
                level.run()

            elif menu_return == MENU_OPTION[1]:
                # Acessa a tela de Ranking (Score) e busca dados no DBProxy
                score_screen.show_score()

            elif menu_return == MENU_OPTION[2]:
                # Procedimento de encerramento seguro do sistema
                pygame.quit()
                sys.exit()

            else:
                # Fallback para entradas não tratadas
                pass


# Ponto de entrada do script
if __name__ == "__main__":
    game = Game()
    game.run()


