import random
import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.DBProxy import DBProxy  # Importação do gerenciador de banco de dados


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.bg_list = EntityFactory.get_entity('Level1Bg')

        # Atributos de controle dinâmico de gameplay e escalonamento
        self.enemy_speed = 5.0
        self.last_spawn_time = 0
        self.spawn_delay = 2000
        self.score = 0  # Accumulative scoring system

    def run(self):
        """Ciclo principal de execução do nível (Main Loop)."""
        clock = pygame.time.Clock()
        while True:
            clock.tick(120)  # Mantém a fluidez em altas taxas de atualização
            current_time = pygame.time.get_ticks()

            # Renderização das camadas de fundo para garantir o 'buffer clear'
            for bg in self.bg_list:
                bg.move()
                self.window.blit(bg.surf, bg.rect)

            # Algoritmo de Spawn: Controle de densidade via tempo e proximidade física
            if current_time - self.last_spawn_time > self.spawn_delay:
                can_spawn = True
                for ent in self.entity_list:
                    if 'Enemy' in ent.name:
                        # Mantém uma janela de segurança de 400px para evitar sobreposição
                        if ent.rect.right > (WIN_WIDTH - 400):
                            can_spawn = False
                            break

                if can_spawn:
                    choice = random.choice(['Enemy', 'Enemy2'])
                    novo = EntityFactory.get_entity(choice, speed=self.enemy_speed)
                    self.entity_list.append(novo)
                    self.last_spawn_time = current_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Iteração de entidades: Processamento de física, desenho e lógica de pontuação
            player = self.entity_list[0]
            for ent in self.entity_list:
                ent.move()
                self.window.blit(ent.surf, ent.rect)

                # Detecção de colisão AABB com redução de hitbox para maior precisão visual
                if ent != player:
                    if player.rect.inflate(-20, -20).colliderect(ent.rect.inflate(-20, -20)):
                        # Persistência de dados e encerramento da sessão
                        self.display_game_over()
                        return "MENU"

                # Lógica de remoção e incremento de dificuldade (Score Trigger)
                if ent.rect.right < 0:
                    self.entity_list.remove(ent)
                    if 'Enemy' in ent.name:
                        self.score += 100  # Pontuação por inimigo superado
                        self.enemy_speed += 0.2
                        if self.spawn_delay > 800:
                            self.spawn_delay -= 50

            # Atualização do Heads-Up Display (HUD)
            self.level_text(20, f'SCORE: {self.score:06d}', (255, 255, 255), (WIN_WIDTH - 180, 20))
            self.level_text(14, f'VELOCIDADE: {self.enemy_speed:.1f}', (255, 255, 0), (10, 20))

            pygame.display.flip()

    def display_game_over(self):
        """Gerencia a transição de Game Over, persistência de score e bloqueio de interface."""

        # Salvamento persistente no Banco de Dados SQLite
        db = DBProxy()
        db.save_score('Player 1', self.score)  # Player 1 como valor default

        # Composição visual da tela de encerramento
        self.window.fill((0, 0, 0))  # Overlay preto para destaque de texto
        self.level_text(40, "GAME OVER", (255, 0, 0), (WIN_WIDTH // 2 - 100, WIN_HEIGHT // 2 - 60))
        self.level_text(25, f"PONTUAÇÃO FINAL: {self.score}", (255, 255, 255), (WIN_WIDTH // 2 - 130, WIN_HEIGHT // 2))
        self.level_text(16, "Pressione qualquer tecla para retornar ao menu", (200, 200, 200),
                        (WIN_WIDTH // 2 - 180, WIN_HEIGHT // 2 + 70))

        pygame.display.flip()

        # Loop de bloqueio para garantir a leitura do score final pelo usuário
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False
            pygame.time.delay(100)

    def level_text(self, text_size: int, text: str, text_color: tuple, tex_pos: tuple):
        """Renderizador utilitário de texto com suporte a anti-aliasing (convert_alpha)."""
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=tex_pos[0], top=tex_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)