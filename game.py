import pygame
import sys
import random
from personagem import Personagem
from consts import *

# Inicialização das variáveis globais
experiencia = 0
quiz_resolvido = False
cenario_atual = 1
NUM_CORACOES = 3
experiencia_atual = 0

# Carregar backgrounds e recursos
def carregar_recursos():
    recursos = {}
    recursos['background_inicio'] = pygame.transform.scale(
        pygame.image.load("assets/Recursos/tela_inicial.jpg"), (LARGURA, ALTURA))

    # Cenários e recursos
    recursos['background_primavera_nitido'] = pygame.image.load("assets/Backgrounds/cenario1(primavera-nitido).jpg")
    recursos['bau_primavera'] = pygame.image.load("assets/Recursos/baú fechado.png")
    recursos['ticket_primavera'] = pygame.transform.scale(
        pygame.image.load("assets/Recursos/ticket_primavera.png"), (44, 44))

    recursos['background_verao_nitido'] = pygame.image.load("assets/Backgrounds/cenario2(verao-nitido).jpg")
    recursos['bau_verao'] = pygame.image.load("assets/Recursos/bau_verao.png")
    recursos['ticket_verao'] = pygame.transform.scale(
        pygame.image.load("assets/Recursos/ticket_verao.png"), (44, 44))

    recursos['background_outono_nitido'] = pygame.image.load("assets/Backgrounds/cenario3(outono-nitido).jpg")
    recursos['bau_outono'] = pygame.image.load("assets/Recursos/bau_outono.png")
    recursos['ticket_outono'] = pygame.transform.scale(
        pygame.image.load("assets/Recursos/ticket_outono.png"), (44, 44))

    recursos['background_inverno_nitido'] = pygame.image.load("assets/Backgrounds/cenario4(inverno-nitido).jpg")
    recursos['bau_inverno'] = pygame.image.load("assets/Recursos/bau_inverno.png")
    recursos['ticket_inverno'] = pygame.transform.scale(
        pygame.image.load("assets/Recursos/ticket_inverno.png"), (44, 44))

    recursos['background_pico_nitido'] = pygame.image.load("assets/Backgrounds/cenario5(pico - nitido) (1).jpg")
    recursos['bau_pico'] = pygame.image.load("assets/Recursos/bau_pico.png")
    recursos['ticket_pico'] = pygame.transform.scale(
        pygame.image.load("assets/Recursos/ticket_pico.png"), (44, 44))

    # Outros recursos
    recursos['barra_xp'] = pygame.transform.scale(pygame.image.load("assets/barras_xp/barra_xp_comeco.png"), (200, 50))
    recursos['barra_20xp'] = pygame.transform.scale(pygame.image.load("assets/barras_xp/barra_xp_20%.png"), (200, 50))
    recursos['barra_40xp'] = pygame.transform.scale(pygame.image.load("assets/barras_xp/barra_xp_40%.png"), (200, 50))
    recursos['barra_60xp'] = pygame.transform.scale(pygame.image.load("assets/barras_xp/barra_xp_60%.png"), (200, 50))
    recursos['barra_80xp'] = pygame.transform.scale(pygame.image.load("assets/barras_xp/barra_xp_80%.png"), (200, 50))
    recursos['barra_100xp'] = pygame.transform.scale(pygame.image.load("assets/barras_xp/barra_xp_100%.png"), (200, 50))
    recursos['coracao'] = pygame.transform.scale(pygame.image.load("assets/Recursos/coracao.png"), (30, 30))

    return recursos

def mostrar_mapa(tela, recursos):
    clock = pygame.time.Clock()
    while True:
        tela.blit(recursos['mapa'], (0,  0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

def tela_game_over(tela, recursos):
    tela.fill((0, 0, 0))
    fonte = pygame.font.Font(None, 74)
    texto_game_over = fonte.render("Game Over", True, (255, 0, 0))
    tela.blit(texto_game_over, (LARGURA // 2 - texto_game_over.get_width() // 2, ALTURA //  2 - 50))

    fonte = pygame.font.Font(None , 36)
    texto_reiniciar = fonte.render("Pressione R para reiniciar", True, (255, 255, 255))
    tela.blit(texto_reiniciar, (LARGURA // 2 - texto_reiniciar.get_width() // 2, ALTURA // 2 + 20))

    desenhar_coracoes(tela, NUM_CORACOES, recursos['coracao'])

    pygame.display.flip()

def desenhar_coracoes(tela, num_coracoes, coracao_img):
    for i in range(num_coracoes):
        tela.blit(coracao_img, (LARGURA - 40 * (i + 1), 10))

def desenhar_barra_experiencia(tela, experiencia_atual, largura_maxima=200, altura=20):
    pygame.draw.rect(tela, (255, 255, 255), (barra_xp_x, barra_xp_y, largura_maxima, altura))  # Barra de fundo
    proporcao = min(experiencia_atual / 100, 1)  # Supondo que 100 é a experiência máxima
    pygame.draw.rect(tela, (0, 255, 0), (barra_xp_x, barra_xp_y, largura_maxima * proporcao, altura))  # Barra de experiência

def colisao_bau(personagem):
    bau_rect = pygame.Rect(bau_x, bau_y, 64, 64)  # Ajuste o tamanho do baú se necessário
    personagem_rect = pygame.Rect(personagem.x, personagem.y, personagem_largura, personagem_altura)  # Cria o retângulo do personagem
    return personagem_rect.colliderect(bau_rect)

def proximidade_bau(personagem):
    distancia_interacao = 100  # Ajuste conforme necessário
    bau_rect = pygame.Rect(bau_x, bau_y, 64, 64)  # Ajuste o tamanho do baú se necessário
    personagem_rect = pygame.Rect(personagem.x, personagem.y, personagem_largura, personagem_altura)  # Cria o retângulo do personagem

    return personagem_rect.colliderect(bau_rect.inflate(distancia_interacao, distancia_interacao))

def mostrar_pergunta(screen, questao):
    fonte = pygame.font.Font(None, 36)
    linhas_pergunta = quebrar_texto(questao["pergunta"], fonte, 700)

    for i, linha in enumerate(linhas_pergunta):
        texto_linha = fonte.render(linha, True, (0, 0, 0))
        screen.blit(texto_linha, (50, 100 + i * 40))

    for i, opcao in enumerate(questao["opcoes"]):
        texto_opcao = fonte.render(opcao, True , (0, 0, 0))
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
    global quiz_resolvido, NUM_CORACOES, cenario_atual
    tentativas_erradas = 0
    pontos = 0
    respostas_certas = []

    questoes_selecionadas = []
    if cenario_atual == 1:
        questoes_selecionadas = random.sample(list(QUESTOES['primavera'].items()), 5)
    elif cenario_atual == 2:
        questoes_selecionadas = random.sample(list(QUESTOES['verao'].items()), 5)
    elif cenario_atual == 3:
        questoes_selecionadas = random.sample(list(QUESTOES['outono'].items()), 5)
    elif cenario_atual == 4:
        questoes_selecionadas = random.sample(list(QUESTOES['inverno'].items()), 5)
    elif cenario_atual == 5:
        questoes_selecionadas = random.sample(list(QUESTOES['pico'].items()), 5)

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
            NUM_CORACOES -= 1
            print(f"Você perdeu um coração! Corações restantes: {NUM_CORACOES}")

            if NUM_CORACOES <= 0:
                tela_game_over(tela, recursos)
                return NUM_CORACOES

            # Finaliza o quiz se o jogador perder um coração
            return NUM_CORACOES

    exibir_resultado(tela, pontos, respostas_certas)

    if pontos <= 2:
        NUM_CORACOES -= 1
        print(f"Você acertou {pontos} perguntas. Você perdeu um coração! Corações restantes: {NUM_CORACOES}")

        if NUM_CORACOES <= 0:
            tela_game_over(tela, recursos)
            return NUM_CORACOES

    if pontos > 2:
        quiz_resolvido = True

    return NUM_CORACOES

def jogo(recursos):
    global experiencia, quiz_resolvido, cenario_atual, NUM_CORACOES
    cenario_atual = 1
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    clock = pygame.time.Clock()
    personagem = Personagem(personagem_x, personagem_y)
    ticket_pego = False
    NUM_CORACOES = 3

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_m:
                    mostrar_mapa(tela, recursos)
                elif evento.key == pygame.K_r:
                    cenario_atual = 1
                    NUM_CORACOES = 3
                    experiencia = 0
                    quiz_resolvido = False
                    ticket_pego = False
                    personagem.x, personagem.y = 20, 440

        teclas = pygame.key.get_pressed()

        if not colisao_bau(personagem):
            personagem.atualizar(teclas)

        desenhar_barra_experiencia(tela, experiencia_atual)
        desenhar_coracoes(tela, NUM_CORACOES, recursos['coracao'])

        if cenario_atual == 1:
            tela.blit(recursos['background_primavera_nitido'], (0, 0))
            if not quiz_resolvido:
                tela.blit(recursos['bau_primavera'], (bau_x, bau_y))

        elif cenario_atual == 2:
            tela.blit(recursos ['background_verao_nitido'], (0, 0))
            if not quiz_resolvido:
                tela.blit(recursos['bau_verao'], (bau_x, bau_y))
        elif cenario_atual == 3:
            tela.blit(recursos['background_outono_nitido'], (0, 0))
            if not quiz_resolvido:
                tela.blit(recursos['bau_outono'], (bau_x, bau_y))
        elif cenario_atual == 4:
            tela.blit(recursos['background_inverno_nitido'], (0, 0))
            if not quiz_resolvido:
                tela.blit(recursos['bau_inverno'], (bau_x, bau_y))
        elif cenario_atual == 5:
            tela.blit(recursos['background_pico_nitido'], (0, 0))
            if not quiz_resolvido:
                tela.blit(recursos['bau_pico'], (bau_x, bau_y))

        if proximidade_bau(personagem) and not ticket_pego:
            fonte = pygame.font.SysFont(None, 30)
            if not quiz_resolvido:  # Exibe a mensagem de interação apenas se o quiz não foi resolvido
                mensagem_interacao = fonte.render("Aperte I", True, (255, 255, 255))
                tela.blit(mensagem_interacao, (bau_x, bau_y - 30))

                if teclas[pygame.K_i]:
                    coracoes = quiz(tela)

        personagem.desenhar(tela)

        if quiz_resolvido and not ticket_pego:
            if cenario_atual == 1:
                tela.blit(recursos['ticket_primavera'], (bau_x, bau_y))
            elif cenario_atual == 2:
                tela.blit(recursos['ticket_verao'], (bau_x, bau_y))
            elif cenario_atual == 3:
                tela.blit(recursos['ticket_outono'], (bau_x, bau_y))
            elif cenario_atual == 4:
                tela.blit(recursos['ticket_inverno'], (bau_x, bau_y))
            elif cenario_atual == 5:
                tela.blit(recursos['ticket_pico'], (bau_x, bau_y))

            fonte = pygame.font.SysFont(None, 15)
            texto1 = fonte.render("Aperte P", True, (255, 255, 255))
            tela.blit(texto1, (bau_x, bau_y - 30))

            if teclas[pygame.K_p]:
                ticket_pego = True
                experiencia += 10
                print("Você pegou o ticket! +10 de experiência")

                transicao(tela)

                if cenario_atual < 5:
                    cenario_atual += 1
                    quiz_resolvido = False
                    ticket_pego = False
                    personagem.x, personagem.y = 20, 440

        pygame.display.flip()
        clock.tick(60)

def transicao(tela):
    duracao_transicao = 1000
    for i in range(3):
        tela.fill((0, 0, 0))
        pygame.display.update()
        pygame.time.delay(duracao_transicao)

def tela_inicio(tela, recursos):
    while True:
        tela.blit(recursos['background_inicio'], (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

pygame.init()
recursos = carregar_recursos()
tela = pygame.display.set_mode((LARGURA, ALTURA))
tela_inicio(tela, recursos)
jogo(recursos)
