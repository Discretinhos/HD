import pygame
from consts import *
class Personagem:
    def __init__(self, x, y):  # Corrigido de _init_ para __init__
        self.x = x
        self.y = y
        self.velocidade = 5
        self.direcao = 'direita'
        self.moving = False

        # Carregar as imagens do personagem
        self.sprite_parado = pygame.image.load("assets/Recursos/sprites_Ella_prota-standing.png").convert_alpha()
        self.sprite_moving1 = pygame.image.load("assets/Recursos/sprites_Ella_prota-moving1.png").convert_alpha()
        self.sprite_moving2 = pygame.image.load("assets/Recursos/sprites_Ella_prota-moving2.png").convert_alpha()

        # Criar animações de movimento para a direita e esquerda
        self.sprites_direita = [self.sprite_moving1, self.sprite_moving2]
        self.sprites_esquerda = [
            pygame.transform.flip(self.sprite_moving1, True, False),
            pygame.transform.flip(self.sprite_moving2, True, False)
        ]

        # Configuração inicial do sprite
        self.sprite_atual = self.sprite_parado
        self.frame_index = 0
        self.tempo_anterior = pygame.time.get_ticks()
        self.frame_rate = 200

        # Configuração inicial do sprite
        self.sprite_atual = self.sprite_parado
        self.frame_index = 0
        self.tempo_anterior = pygame.time.get_ticks()
        self.frame_rate = 200

    def atualizar(self, teclas):
        # Movimentação com as setas esquerda e direita
        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidade
            self.direcao = 'esquerda'
            self.moving = True
        elif teclas[pygame.K_RIGHT]:
            self.x += self.velocidade
            self.direcao = 'direita'
            self.moving = True
        else:
            self.moving = False

        # Atualiza a animação do personagem
        self.animar()

    def animar(self):
        agora = pygame.time.get_ticks()
        if self.moving:
            if agora - self.tempo_anterior > self.frame_rate:
                self.tempo_anterior = agora
                self.frame_index = (self.frame_index + 1) % 2
                self.sprite_atual = self.sprites_direita[self.frame_index] if self.direcao == 'direita' else self.sprites_esquerda[self.frame_index]
        else:
            self.sprite_atual = self.sprite_parado

    def desenhar(self, tela):
        # Desenhar o sprite atual do personagem na tela
        tela.blit(self.sprite_atual, (self.x, self.y))

