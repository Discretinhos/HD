import pygame
import sys
import random
from consts import (LARGURA, ALTURA, PERSONAGEM_LARGURA, PERSONAGEM_X, PERSONAGEM_Y,
                    PERSONAGEM_ALTURA, BAU_X, BAU_Y, BAR_XP_X, BAR_XP_Y, NUM_CORACOES,
                    TAMANHO_BAU, carregar_recursos, QUESTOES)
from personagem import Personagem

# Inicialização do Pygame
pygame.init()

# Carrega os recursos
RECURSOS = carregar_recursos()

# Variáveis globais
quiz_resolvido = False
cenario_atual = 1
experiencia = 0
NUM_CORACOES = 3

def tela_inicial():
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Horizonte Discreto")
    clock = pygame.time.Clock()

    while True:
        tela.blit(RECURSOS['tela_inicial'], (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jogo()

        clock.tick(60)

def mostrar_mapa(tela):
    tela.blit(RECURSOS['mapa', (0,0)])

def tela_game_over(tela):
    tela.fill((0, 0, 0))
    fonte = pygame.font.Font(None, 74)
    texto_game_over = fonte.render("Game Over", True, (255, 0, 0))
    tela.blit(texto_game_over, (LARGURA // 2 - texto_game_over.get_width() // 2, ALTURA // 2 - 50))

    fonte = pygame.font.Font(None, 36)
    texto_reiniciar = fonte.render("Pressione R para reiniciar", True, (255, 255, 255))
    tela.blit(texto_reiniciar, (LARGURA // 2 - texto_reiniciar.get_width() // 2, ALTURA // 2 + 20))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return

def colisao_bau(rect_personagem):
    bau_rect = pygame.Rect(BAU_X, BAU_Y, 44, 44)
    return rect_personagem.colliderect(bau_rect)

def mostrar_pergunta(screen, questao):
    fonte = pygame.font.Font(None, 36)
    linhas_pergunta = quebrar_texto(questao["pergunta"], fonte, 700)

    for i, linha in enumerate(linhas_pergunta):
        texto_linha = fonte.render(linha, True, (0, 0, 0))
        screen.blit(texto_linha, (50, 100 + i * 40))

    for i, opcao in enumerate(questao["opcoes"]):
        texto_opcao = fonte.render(opcao, True, (0, 0, 0))
        screen.blit(texto_opcao, (100, 200 + len(linhas_pergunta) * 40 + i * 40))

def exibir_resultado(tela, pontos, respostas_certas):
    tela.fill((255, 255, 255))
    fonte = pygame.font.Font(None, 48)
    fim_texto = fonte.render(f"Fim do Quiz! Pontuação Final: {pontos}/5", True, (0, 0, 0))
    tela.blit(fim_texto, (200, 300))

    if respostas_certas:
        perguntas_acertadas = ", ".join(map(str, respostas_certas))
        acertos_texto = fonte.render(f"Perguntas acertadas: {perguntas_acertadas}", True, (0, 0, 0))
        tela.blit(acertos_texto, (200, 350))

    pygame.display.flip()
    pygame.time.wait(3000)

def quebrar_texto(texto, fonte, largura_maxima):
    palavras = texto.split()
    linhas = []
    linha_atual = ""
    for palavra in palavras:
        test_line = linha_atual + palavra + " "
        if fonte.size(test_line)[0] < largura_maxima:
            linha_atual = test_line
        else:
            linhas.append(linha_atual)
            linha_atual = palavra + " "
    linhas.append(linha_atual)
    return linhas

def quiz(tela, recursos):
    global quiz_resolvido, NUM_CORACOES
    tentativas_erradas = 0
    pontos = 0
    respostas_certas = []

    questoes_selecionadas = []
    if cenario_atual == 1:
        questoes_selecionadas = random.sample(list(QUESTOES['primavera'].items()), 5)
    elif cenario_atual == 2:
        questoes_selecionadas = random.sample(list(QUESTOES['verao'].items()), 5)

    for numero, questao in questoes_selecionadas:
        tela.fill((255, 255, 255))
        mostrar_pergunta(tela, questao)
        pygame.display.flip()

        resposta_usuario = None
        while resposta_usuario is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        resposta_usuario = "A"
                    elif event.key == pygame.K_b:
                        resposta_usuario = "B"
                    elif event.key == pygame.K_c:
                        resposta_usuario = "C"
                    elif event.key == pygame.K_d:
                        resposta_usuario = "D"

            pygame.time.wait(100)

        if resposta_usuario == questao["resposta"]:
            pontos += 1
            respostas_certas.append(numero)
            print(f"Resposta correta para pergunta {numero}!")
        else:
            tentativas_erradas += 1
            print(f"Resposta incorreta para pergunta {numero}!")

        if tentativas_erradas >= 3:
            tela_game_over(tela)
            return NUM_CORACOES

    exibir_resultado(tela, pontos, respostas_certas)

    if pontos <= 2:
        NUM_CORACOES -= 1
        print(f"Você acertou {pontos} perguntas. Você perdeu um coração! Corações restantes: {NUM_CORACOES}")

        if NUM_CORACOES <= 0:
            tela_game_over(tela)
            return NUM_CORACOES

    if pontos > 2:
        quiz_resolvido = True

    return NUM_CORACOES

def jogo(recursos):
    global experiencia, quiz_resolvido, cenario_atual
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    clock = pygame.time.Clock()
    personagem = Personagem()
    ticket_pego = False
    tentativas_quiz = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_m:
                    mostrar_mapa(tela, recursos)

        teclas = pygame.key.get_pressed()
        personagem.atualizar(teclas)

        if cenario_atual == 1:
            tela.blit(RECURSOS['primavera']['background_nitido'], (0, 0))
            if not ticket_pego and not quiz_resolvido:
                if colisao_bau(personagem.rect):
                    tentativas_quiz += 1
                    quiz(tela, recursos)

        elif cenario_atual == 2:
            tela.blit(RECURSOS['verao']['background_nitido'], (0, 0))
            if not ticket_pego and not quiz_resolvido:
                if colisao_bau(personagem.rect):
                    tentativas_quiz += 1
                    quiz(tela, recursos)

        personagem.desenhar(tela)
        desenhar_coracoes(tela, NUM_CORACOES)

        if quiz_resolvido and not ticket_pego:
            if cenario_atual == 1:
                tela.blit(RECURSOS['primavera']['ticket'], (BAU_X, BAU_Y))
            elif cenario_atual == 2:
                tela.blit(RECURSOS['verao ']['ticket'], (BAU_X, BAU_Y))

            fonte = pygame.font.SysFont(None, 15)
            texto1 = fonte.render("Aperte P para pegar", True, (255, 255, 255))
            tela.blit(texto1, (BAU_X, BAU_Y - 30))

            if teclas[pygame.K_p]:
                ticket_pego = True
                experiencia += 10
                print("Você pegou o ticket! +10 de experiência")

                if cenario_atual < 4:
                    cenario_atual += 1
                    quiz_resolvido = False
                    ticket_pego = False
                    tentativas_quiz = 0
                    personagem.x = PERSONAGEM_X
                    personagem.y = PERSONAGEM_Y
                    personagem.rect.topleft = (personagem.x, personagem.y)

        pygame.display.flip()
        clock.tick(60)

def tela_inicio(recursos):
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    while True:
        tela.blit(RECURSOS['tela_inicial'], (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                jogo(recursos)

# Inicialização do Pygame e execução do jogo
pygame.init()
recursos = carregar_recursos()
tela_inicio(recursos)