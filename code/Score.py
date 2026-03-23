import pygame
import sys
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window):
        self.window = window
        # Carrega a imagem de fundo da tela de score
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.db = DBProxy()  # Instancia o banco de dados

    def save_score(self, player_name, score):

        self.db.save_score(player_name, score)

    def show_score(self):
        # Carrega e toca a música tema do score
        pygame.mixer_music.load('./asset/som.mp3')
        pygame.mixer_music.play(-1)

        # Busca os Top 10 scores do banco de dados
        top_scores = self.db.get_top_scores()

        while True:
            # Desenha o fundo
            self.window.blit(source=self.surf, dest=self.rect)

            # Título da tela
            self._draw_text(35, "RANKING - TOP 10", (255, 215, 0), (WIN_WIDTH // 2 - 130, 40))

            # Lista as pontuações
            y_offset = 120
            for i, row in enumerate(top_scores):
                # row[0] = nome, row[1] = score, row[2] = data
                name, value, date = row
                txt = f"{i + 1}º {name}: {value:06d} ({date})"
                self._draw_text(18, txt, (255, 255, 255), (WIN_WIDTH // 2 - 180, y_offset))
                y_offset += 30

            self._draw_text(15, "Pressione ESC para voltar ao Menu", (200, 200, 200),
                            (WIN_WIDTH // 2 - 130, WIN_HEIGHT - 40))

            pygame.display.flip()

            # Processamento de eventos para não travar o jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer_music.stop()  # Para a música ao sair
                        return  # Volta para o Game.py

    def _draw_text(self, size, text, color, pos):

        font = pygame.font.SysFont('Lucida Sans Typewriter', size)
        text_surf = font.render(text, True, color).convert_alpha()
        text_rect = text_surf.get_rect(left=pos[0], top=pos[1])
        self.window.blit(text_surf, text_rect)