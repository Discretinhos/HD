import pygame
import sys
from consts import LARGURA, ALTURA
from game import carregar_recursos, tela_inicio, jogo

def main():
    pygame.init()
    pygame.display.set_caption("Horizonte Discreto")
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    recursos = carregar_recursos()
    tela_inicio(tela, recursos)
    jogo(recursos)

if __name__ == "__main__":
    main()
    pygame.quit()
