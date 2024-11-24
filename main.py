import pygame
import sys
from consts import MUSICA_FUNDO, SOM_PASSOS, LARGURA, ALTURA, RECURSOS
from game import tela_inicial, jogo

# Inicializa o pygame
pygame.init()
pygame.mixer.init()

# Configura a tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Horizonte Discreto")

def carregar_imagens():
    """Carrega todas as imagens e recursos necessários."""
    # Aqui você deve garantir que o dicionário RECURSOS seja preenchido corretamente
    # Exemplo:
    # RECURSOS['sprites_parado'] = pygame.image.load("assets/Recursos/sprites_Ella_prota-standing.png").convert_alpha()
    pass  # Remova isso e implemente a função

# Carrega os recursos
carregar_imagens()  # Garante que o dicionário RECURSOS esteja preenchido

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
    tela_inicial(RECURSOS)

    # Inicia o jogo após a tela inicial
    jogo(RECURSOS)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        pygame.quit()