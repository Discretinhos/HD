import pygame
import sys
import random
from consts import LARGURA, ALTURA, PERSONAGEM_X, PERSONAGEM_Y, PERSONAGEM_LARGURA, PERSONAGEM_ALTURA, BAU_X, BAU_Y, BAR_XP_X, BAR_XP_Y, NUM_CORACOES, RECURSOS, QUESTOES
from personagem import Personagem

pygame.init()

def tela_inicial(RECURSOS):
    """ Exibe a tela inicial do jogo e espera pelo jogador pressionar espaço para começar. """
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Nome do Jogo")
    clock = pygame.time.Clock()

    while True:
        # Preenche a tela com a imagem inicial
        tela.blit(RECURSOS['tela_inicial'], (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Inicia o jogo quando espaço é pressionado
                    return

        clock.tick(60)

def mostrar_mapa(tela, recursos):
    clock = pygame.time.Clock()
    while True:
        tela.blit(recursos['mapa'], (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

def colisao_bau(personagem):
    bau_rect = pygame.Rect(BAU_X, BAU_Y, 44, 44)
    return personagem.rect.colliderect(bau_rect)

def desenhar_fundo_e_bau(tela, recursos):
    global cenario_atual
    tela.blit(recursos['tela_inicial'], (0, 0))
    if cenario_atual == 1:
        tela.blit(recursos['primavera']['ticket'], (BAU_X, BAU_Y))
    elif cenario_atual == 2:
        tela.blit(recursos['verao']['ticket'], (BAU_X, BAU_Y))
    elif cenario_atual == 3:
        tela.blit(recursos['outono']['ticket'], (BAU_X, BAU_Y))
    elif cenario_atual == 4:
        tela.blit(recursos['inverno']['ticket'], (BAU_X, BAU_Y))

def desenhar_coracoes(tela, num_coracoes):

    for i in range(num_coracoes):
        tela.blit(RECURSOS['coracao'], (BAR_XP_X + i * 40, BAR_XP_Y))

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

def quiz(tela):
    tentativas_erradas = 0
    pontos = 0
    respostas_certas = []

    questoes_selecionadas = random.sample(list(QUESTOES.items()), 5)

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
        else:
            tentativas_erradas += 1

    exibir_resultado(tela, pontos, respostas_certas)

    if pontos >= 3:
        return NUM_CORACOES + 1
    else:
        return NUM_CORACOES - tentativas_erradas

def jogo(recursos):
    global coracoes, quiz_resolvido, experiencia, cenario_atual
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    clock = pygame.time.Clock()
    personagem = Personagem()
    ticket_pego = False
    coracoes = NUM_CORACOES
    experiencia = 0
    cenario_atual = 1
    quiz_resolvido = False

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_m:
                    mostrar_mapa(tela, recursos)

        teclas = pygame.key.get_pressed()

        if not colisao_bau(personagem):
            personagem.atualizar(teclas)
        else:
            if teclas[pygame.K_i]:
                coracoes = quiz(tela)
                quiz_resolvido = True  # Atualiza o estado do quiz após a interação

        desenhar_fundo_e_bau(tela, recursos)

        if colisao_bau(personagem):
            fonte = pygame.font.SysFont(None, 30)
            mensagem_interacao = fonte.render(" Aperte I para interagir", True, (255, 255, 255))
            tela.blit(mensagem_interacao, (BAU_X, BAU_Y - 30))

        personagem.desenhar(tela)
        desenhar_coracoes(tela, coracoes)

        if quiz_resolvido and not ticket_pego:
            if cenario_atual == 1:
                tela.blit(recursos['primavera']['ticket'], (BAU_X, BAU_Y))
            elif cenario_atual == 2:
                tela.blit(recursos['verao']['ticket'], (BAU_X, BAU_Y))
            elif cenario_atual == 3:
                tela.blit(recursos['outono']['ticket'], (BAU_X, BAU_Y))
            elif cenario_atual == 4:
                tela.blit(recursos['inverno']['ticket'], (BAU_X, BAU_Y))

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
                    personagem.x = PERSONAGEM_X
                    personagem.y = PERSONAGEM_Y
                    personagem.rect.topleft = (personagem.x, personagem.y)

        pygame.display.flip()
        clock.tick(60)

# Chamada da função para exibir a tela de início
tela_inicial(RECURSOS)
pygame.quit()