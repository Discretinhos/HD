import pygame
import sys
from consts import MUSICA_FUNDO, SOM_PASSOS, LARGURA, ALTURA, carregar_recursos
from game import tela_inicial

# Inicializa o pygame
pygame.init()
pygame.mixer.init()

# Configura a tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Horizonte Discreto")

# Carrega os recursos
RECURSOS = carregar_recursos()

# Carrega a música de fundo
try:
    pygame.mixer.music.load(MUSICA_FUNDO)
    pygame.mixer.music.play(-1)  # Toca a música em loop
    pygame.mixer.music.set_volume(0.4)
except pygame.error as e:
    print(f"Erro ao carregar a música: {e}")

# Carrega o som dos passos
try:
    passos = pygame.mixer.Sound(SOM_PASSOS)
except pygame.error as e:
    print(f"Erro ao carregar o som dos passos: {e}")

def main():
    # Exibe a tela inicial
    tela_inicial()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        pygame.quit()