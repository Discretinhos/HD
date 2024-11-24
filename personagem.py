import pygame
from consts import LARGURA, ALTURA,PERSONAGEM_X, PERSONAGEM_Y, PERSONAGEM_LARGURA, PERSONAGEM_ALTURA, carregar_recursos

# Carrega os recursos
RECURSOS = carregar_recursos()

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
        self.sprites_esquerda = [pygame.transform.flip(self.sprite_moving1, True, False),
                                 pygame.transform.flip(self.sprite_moving2, True, False)]

        self.sprite_atual = self.sprite_parado
        self.frame_index = 0
        self.tempo_anterior = pygame.time.get_ticks()
        self.frame_rate = 200
        self.rect = pygame.Rect(self.x, self.y, PERSONAGEM_LARGURA, PERSONAGEM_ALTURA)

    def atualizar(self, teclas):
        self.moving = False

        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidade
            self.direcao = 'esquerda'
            self.moving = True
        elif teclas[pygame.K_RIGHT]:
            self.x += self.velocidade
            self.direcao = 'direita'
            self.moving = True

        self.x = max(0, min(self.x, LARGURA - PERSONAGEM_LARGURA))
        self.y = max(0, min(self.y, ALTURA - PERSONAGEM_ALTURA))

        self.animar()
        self.rect.topleft = (self.x, self.y)

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