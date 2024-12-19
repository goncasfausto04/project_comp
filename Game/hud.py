import pygame
import os
import config
from utils import *

class HUD:
    def __init__(self, screen, config, player):
        self.screen = screen
        self.config = config
        self.player = player
        self.font = pygame.font.Font(None, 30)  # Default font
        self.deep_black = (0, 0, 0)
        self.green = (0, 255, 0)
        self.white = (255, 255, 255)

   
        # Positioning and size for level-up bar
        self.bar_x = 0.1 * config.width
        self.bar_y = 0.05 * config.height
        self.bar_width = 0.8 * config.width
        self.bar_height = 20

     
    def draw_weapon_slots(self):
        slot_size = 50  # Diminuir o tamanho dos slots
        spacing = 10  # Diminuir o espaçamento
        start_x = self.bar_x + 130
        y_position = self.config.height - 95  # Ajuste a posição vertical

        weapon_names = ["1", "2", "3", "4", "5"]  # Nomes das armas
        bullet_type_slot = {"1": "Basic Spell", "2": "Shatterblast", "3": "Arcane Cascade", "4": "Rebound Rune", "5": "Astral Beam"}  # Mapeamento de tipos de balas"}

        for i in range(5):
            slot_rect = pygame.Rect(start_x + i * (slot_size + spacing), y_position, slot_size, slot_size)

            # Retângulo de fundo do slot
            pygame.draw.rect(self.screen, (80, 80, 80), slot_rect)

            # Nome da arma
            if i < len(weapon_names):
                weapon_text = self.font.render(weapon_names[i], True, self.white)
                self.screen.blit(weapon_text, (slot_rect.x + 5, slot_rect.y + 15))

            # Borda do slot
            pygame.draw.rect(self.screen, self.white, slot_rect, 2)
            # Borda do slot selecionado
            if bullet_type_slot[weapon_names[i]] == self.player.bullet_type:
                pygame.draw.rect(self.screen, self.green, slot_rect, 2)
            
            

    def draw_level_up_bar(self):
        bar_width = 0.6 * self.config.width  # Reduzindo a largura
        bar_height = 15  # Reduzindo a altura
        bar_x = 0.2 * self.config.width
        bar_y = self.config.height - 40  # Ajustando a posição vertical

        # Desenho da borda
        pygame.draw.rect(self.screen, (255, 255, 255), (bar_x - 2, bar_y - 2, bar_width + 4, bar_height + 4), 2)
        # Desenho do preenchimento
        fill_width = (self.player.exp / self.player.exp_required) * bar_width
        pygame.draw.rect(self.screen, self.green, (bar_x, bar_y, fill_width, bar_height))

        # Texto da barra de XP
        # Criando uma fonte menor
        small_font = pygame.font.Font(None, 24)  # Tamanho 24 (ajuste conforme necessário)

        level_text = small_font.render(
            f"EXP: {self.player.exp}/{int(self.player.exp_required)}", True, self.white
        )

        # Exibindo o texto no centro da barra de XP

        self.screen.blit(level_text,
                         (self.config.width // 2 - level_text.get_width() // 2, bar_y))  # Ajuste vertical
        
    def draw_health_bar(self):
        """
        Draw the health bar below the player's sprite.
        """
        bar_width = 50  # Width of the health bar
        bar_height = 8  # Height of the health bar
        health_ratio = self.player.health / self.player.max_health

        # Positioning the health bar just below the player
        bar_x = self.player.rect.centerx - bar_width // 2
        bar_y = self.player.rect.bottom + 5

        pygame.draw.rect(self.screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(self.screen, (0, 255, 0), (bar_x, bar_y, int(bar_width * health_ratio), bar_height))

    def draw_player_level(self):
        """
        Draw the player's current level as a large number just above the end of the Level-Up bar.
        """
        large_font = pygame.font.Font(None, 30)
        # Position the level number at the end of the Level-Up bar
        level_text = large_font.render(f"Level: {self.player.level}", True, (255, 255, 255))

        text_x = config.width * 0.62
        text_y = self.config.height * 0.912# Above the Level-Up bar

        self.screen.blit(level_text, (text_x, text_y))

    def draw_best_time(self):
        """
        Draw the player's best time on the HUD.
        """
        # Fonte para o texto do tempo
        time_font = pygame.font.Font(None, 30)
        minutes, seconds = self.player.best_time[0], self.player.best_time[1]

        # Formatação do texto
        time_text = time_font.render(f"Record: {minutes:02}:{seconds:02}", True, (255, 255, 255))

        # Posiciona o texto acima do lado direito da barra de Level-Up
        text_x = config.width * 0.697
        text_y = self.config.height *0.912  # Ajuste vertical

        # Desenha o texto na tela
        self.screen.blit(time_text, (text_x, text_y))

  
    def draw_player_money(self):
        """
        Draw the player's current coins on the HUD.
        """
        # Fonte para o texto das moedas
        money_font = pygame.font.Font(None, 30)  # Um pouco maior para destaque
        money_text = money_font.render(f"Coins: {self.player.coins}", True, (255, 223, 0))  # Texto em amarelo ouro

        # Posiciona o texto acima do lado esquerdo da barra de Level-Up
        text_x = config.width * 0.62
        text_y = self.config.height - 90 

        # Desenha o texto na tela
        self.screen.blit(money_text, (text_x, text_y))

    def draw_slot(self,screen,player):
        # Cooldown bar dimensions and position
        smaller_font = pygame.font.Font(None, 20)  # Smaller font for the "Dash" text
        bar_y = 0.9 * config.height  # Closer to the bottom
        bar_width = 0.15 * config.width  # Smaller width
        bar_x = 0.53 * config.width - (bar_width /2 ) # Centered horizontally
        bar_height = 0.01 * config.height  # Very thin bar

        dash_text = self.font.render("Dash", True, (255, 255, 255))
        space_use = smaller_font.render("Space to Dash", True, (255, 255, 255))
        
        # Draw the background of the bar (gray)
        background_color = (50, 50, 50)  # Gray background
        pygame.draw.rect(screen, background_color, (bar_x, bar_y, bar_width, bar_height))
        # Draw the text "Dash" above the bar
        text_rect = dash_text.get_rect(center=(bar_x * 1.04, bar_y - bar_height * 2))
        space_rect = space_use.get_rect(center=(bar_x *1.17, bar_y - bar_height * 2))
        screen.blit(dash_text, text_rect)
        
        
        # Calculate the cooldown progress
        timer = player.dash_cooldown
        max_cooldown = fps * 2  # Adjust based on your game's cooldown duration
        if timer > 0:
            # Draw the cooldown progress 
            progress_width = bar_width * (timer / max_cooldown)
            progress_color = (0, 255, 0)  # Green bar
            pygame.draw.rect(screen, progress_color, (bar_x, bar_y, progress_width, bar_height))
        
        # display the remaining time as text
        if timer > 0:
            text_color = (255, 255, 255)  # White text
            time_remaining = f"{timer / fps:.1f}"  # Format as seconds
            text_surface = self.font.render(time_remaining, True, text_color)
            text_rect = text_surface.get_rect(center=(bar_x *1.13, bar_y - bar_height * 2))
            screen.blit(text_surface, text_rect)
        else:
            screen.blit(space_use, space_rect)

    def draw(self,screen,player):
        self.draw_health_bar()  # Player health bar that follows the player
        self.draw_level_up_bar()  # Level-up progress bar at the bottom
        self.draw_weapon_slots()
        self.draw_player_level()
        self.draw_player_money()
        self.draw_slot(screen,player) if player.has_dash else None
        self.draw_best_time()

