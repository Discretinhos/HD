import pygame
from consts import PERSONAGEM_X, PERSONAGEM_Y, PERSONAGEM_LARGURA, PERSONAGEM_ALTURA, LARGURA, ALTURA, RECURSOS

class Personagem:
    def __init__(self, x=PERSONAGEM_X, y=PERSONAGEM_Y):
        self.x = x
        self.y = y
        self.velocidade = 5
        self.direcao = 'direita'
        self.moving = False
        self.carregar_sprites()

    def carregar_sprites(self):
        self.sprite_parado = RECURSOS['sprites_parado']
        self.sprite_moving1 = RECURSOS['sprites_moving1']
        self.sprite_moving2 = RECURSOS['sprites_moving2']

        self.sprites_direita = [self.sprite_moving1, self.sprite_moving2]
        self.sprites_esquerda = [pygame.transform.flip(self.sprite_moving1, True , False),
                                 pygame.transform.flip(self.sprite_moving2, True, False)]

        self.sprite_atual = self.sprite_parado
        self.frame_index = 0
        self.tempo_anterior = pygame.time.get_ticks()
        self.frame_rate = 200
        self.rect = pygame.Rect(self.x, self.y, PERSONAGEM_LARGURA, PERSONAGEM_ALTURA)

    def atualizar(self, teclas):
        """Atualiza a posição e animação do personagem com base nas teclas pressionadas."""
        self.moving = False  # Reseta o estado de movimento

        # Movimentação do personagem
        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidade
            self.direcao = 'esquerda'
            self.moving = True
        elif teclas[pygame.K_RIGHT]:
            self.x += self.velocidade
            self.direcao = 'direita'
            self.moving = True

        # Limitar o movimento do personagem dentro da tela
        self.x = max(0, min(self.x, LARGURA - PERSONAGEM_LARGURA))

        # Se o personagem está no chão, limita a posição y
        self.y = max(0, min(self.y, ALTURA - PERSONAGEM_ALTURA))

        # Atualiza a animação e a posição do retângulo
        self.animar()
        self.rect.topleft = (self.x, self.y)  # Atualiza a posição do retângulo

    def animar(self):
        agora = pygame.time.get_ticks()
        if self.moving:
            if agora - self.tempo_anterior > self.frame_rate:
                self.tempo_anterior = agora
                self.frame_index = (self.frame_index + 1) % len(self.sprites_direita)
                self.sprite_atual = self.sprites_direita[self.frame_index] if self.direcao == 'direita' else \
                                    self.sprites_esquerda[self.frame_index]
        else:
            self.sprite_atual = self.sprite_parado

    def desenhar(self, tela):
        tela.blit(self.sprite_atual, (self.x, self.y))