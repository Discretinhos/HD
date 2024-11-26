# consts.py

# Dimensões da tela
LARGURA = 1365
ALTURA = 510

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Posições iniciais e dimensões
personagem_x, personagem_y = 20, 440
personagem_largura, personagem_altura = 64, 64
bau_x, bau_y = 1280, 432  # Ajuste a posição do baú
barra_xp_x, barra_xp_y = 25, 10
coracao_x, coracao_y = 60, 80  # Posição Y dos corações

QUESTOES = {
    'primavera': {
        1: {
            "pergunta": "Qual técnica de demonstração se utiliza para provar uma afirmação ao demonstrar que o contrário levaria a uma contradição?",
            "opcoes": ["A) Indução", "B) Contrapositivo", "C) Contradição", "D) Prova Direta"],
            "resposta": "C"
        },
        2: {
            "pergunta": "Em uma prova por contrapositivo, para provar P=>Q qual afirmação é provada?",
            "opcoes": ["A) Q=>P", "B) ¬P⇒¬Q", "C) ¬Q⇒¬P", "D) P^Q=>¬Q"],
            "resposta": "B"
        },
        3: {
            "pergunta": "Qual técnica de prova é mais apropriada para provar uma afirmação da forma “para todo n, se n é par, então n^2 é par”?",
            "opcoes": ["A) Contrapositiva", "B) Indução", "C) Contradição", "D) Prova Direta"],
            "resposta": "D"
        },
        4: {
            "pergunta": "A técnica de indução matemática é frequentemente usada para provar proposições sobre...",
            "opcoes": ["A) Números Racionais", "B) Números Naturais", "C) Números Complexos", "D) Números Irracionais"],
            "resposta": "B"
        },
        5: {
            "pergunta": "Para provar que 'se um número é ímpar, então seu quadrado também é ímpar', qual técnica seria mais adequada?",
            "opcoes": ["A) Contradição", "B) Prova Direta", "C) Contrapositivo", "D) Indução"],
            "resposta": "B"
        },
        6: {
            "pergunta": "Na indução matemática, qual é o primeiro passo?",
            "opcoes": ["A) Provar a afirmação para n+1", "B) Provar a afirmação para n=1",
                       "C) Assumir a afirmação para n e n+1", "D) Refutar a afirmação para valores ímpares"],
            "resposta": "B"
        },
        7: {
            "pergunta": "Para provar uma proposição para todos os números naturais, qual método é mais eficiente?",
            "opcoes": ["A) Contrapositivo", "B) Indução", "C) Contradição", "D) Prova Direta"],
            "resposta": "B"
        },
        8: {
            "pergunta": "Ao provar uma afirmação por contradição, assumimos...",
            "opcoes": ["A) Que a afirmação é falsa", "B) Que a afirmação é verdadeira", "C) Que ambas são verdadeiras",
                       "D) Que nenhuma delas é verdadeira"],
            "resposta": "A"
        },
        9: {
            "pergunta": "Para provar que a raiz quadrada de 2 é irracional, qual técnica é geralmente utilizada?",
            "opcoes": ["A) Contrapositivo", "B) Prova Direta", "C) Indução", "D) Contradição"],
            "resposta": "D"
        },
        10: {
            "pergunta": "Na prova por contrapositivo, qual proposição alternativa você assume para provar P=>Q?",
            "opcoes": ["A) P=>Q", "B) ¬P=>¬Q", "C) ¬Q⇒¬P", "D) Q=>P"],
            "resposta": "C"
        },
        11: {
            "pergunta": "Qual técnica de demonstração é mais útil para provar a fórmula da soma dos primeiros n números naturais?",
            "opcoes": ["A) Contradição", "B) Indução", "C) Contrapositivo", "D) Redução ao absurdo"],
            "resposta": "B"
        },
        12: {
            "pergunta": "Para provar uma implicação “Se A, então B” usando contrapositivo, devemos provar...",
            "opcoes": ["A) Se B é falso , então A é falso", "B) Se B é verdadeiro, então A é falso",
                       "C) Se A é verdadeiro, então B é falso", "D) Se A é falso, então B é falso"],
            "resposta": "A"
        },
        13: {

            "pergunta": "Qual técnica envolve assumir o oposto de uma afirmação e derivar uma contradição?",
            "opcoes": ["A) Indução", "B) Contradição", "C) Contrapositivo", "D) Prova Direta"],
            "resposta": "B"
        },
        14: {
            "pergunta": "Para provar que a soma de dois números ímpares é par, a técnica recomendada é...",
            "opcoes": ["A) Contradição", "B) Contrapositiva", "C) Prova Direta", "D) Indução"],
            "resposta": "C"
        },
        15: {
            "pergunta": "Uma prova que demonstra uma proposição ao verificar que a negação leva a uma conclusão impossível é chamada de...",
            "opcoes": ["A) Indução", "B) Contrapositivo", "C) Contradição", "D) Prova Direta"],
            "resposta": "C"
        },
        16: {
            "pergunta": "Para mostrar que uma proposição P implica Q em uma prova direta, qual suposição inicial fazemos?",
            "opcoes": ["A) Q é falso", "B) Q é verdadeiro", "C) P é verdadeiro", "D) P é falso"],
            "resposta": "C"
        },
        17: {
            "pergunta": "Qual dos seguintes é um exemplo de prova por contrapositivo?",
            "opcoes": ["A) Suponha que P e Q sejam verdadeiros", "B) Suponha que ¬Q e derive ¬P",
                       "C) Suponha Q e prove P", "D) Suponha que ¬P é falso"],
            "resposta": "B"
        },
        18: {
            "pergunta": "Para provar que não existe número racional cuja raiz quadrada seja 3, utilizamos...",
            "opcoes": ["A) Indução", "B) Prova Direta", "C) Contradição", "D) Contrapositivo"],
            "resposta": "C"
        },
        19: {
            "pergunta": "Qual técnica é frequentemente utilizada em proposições do tipo 'para todo número natural n'?",
            "opcoes": ["A) Contrapositivo", "B) Indução", "C) Prova Direta", "D) Contradição"],
            "resposta": "B"
        },
        20: {
            "pergunta": "Qual técnica requer a demonstração de uma base e um passo de indução?",
            "opcoes": ["A) Contradição", "B) Contrapositivo", "C) Indução", "D) Prova Direta"],
            "resposta": "C"
        },
        21: {
            "pergunta": "Para provar que o produto de dois números racionais é racional, qual técnica é mais adequada?",
            "opcoes": ["A) Prova Direta", "B) Contrapositivo", "C) Contradição", "D) Indução"],
            "resposta": "A"
        },
        22: {
            "pergunta": "Qual técnica é utilizada para provar que se um número é divisível por 4, então seu quadrado é divisível por 16?",
            "opcoes": ["A) Prova Direta", "B) Indução", "C) Contrapositivo", "D) Contradição"],
            "resposta": "A"
        },
        23: {
            "pergunta": "A afirmação 'se um número é par, então seu sucessor é ímpar' pode ser provada usando...",
            "opcoes": ["A) Indução", "B) Prova Direta", "C) Contrapositivo", "D) Contradição"],
            "resposta": "B"
        },
        24: {
            "pergunta": "Para provar que n² − n é par para todo número natural n, a técnica sugerida é...",
            "opcoes": ["A) Contrapositivo", "B) Indução", "C) Contradição", "D) Prova Direta"],
            "resposta": "B"
        },
        25: {
            "pergunta": "Qual técnica de demonstração seria melhor para provar que a soma de um número par com um ímpar é ímpar?",
            "opcoes": ["A) Contradição", "B) Prova Direta", "C) Indução", "D) Contrapositivo"],
            "resposta": "B"
        },
        26: {
            "pergunta": "Para provar que o mínimo divisor de um número primo é ele mesmo, usamos...",
            "opcoes": ["A) Contradição", "B) Indução", "C) Contrapositivo", "D) Prova Direta"],
            "resposta": "D"
        },
        27: {
            "pergunta": "Para provar que um número natural n é divisível por 3, assumimos que n≡0(mod3) e mostramos que...",
            "opcoes": ["A) n=3k+1", "B) n=3k", "C) n≡2(mod3)", "D) n=k+3"],
            "resposta": "B"
        },
        28: {
            "pergunta": "Para provar que um conjunto finito tem um número de subconjuntos que é uma potência de 2, usamos...",
            "opcoes": ["A) Contrapositivo", "B) Indução", "C) Contradição", "D) Prova Direta"],
            "resposta": "B"
        },
        29: {
            "pergunta": "Para mostrar que um número par multiplicado por outro número par é par, usamos...",
            "opcoes": ["A) Contradição", "B) Indução", "C) Contrapositiva", "D) Prova Direta"],
            "resposta": "D"
        },
        30: {
            "pergunta": "Provar que a soma de dois múltiplos de um número é múltiplo desse número é um exemplo de...",
            "opcoes": ["A) Indução", "B) Contradição", "C) Contrapositivo", "D) Prova Direta"],
            "resposta": "D"
        }
    },
    'verao': {
        1: {
            "pergunta": "Quantas maneiras diferentes há para escolher 2 pessoas de um grupo de 5?",
            "opcoes": ["A) 5", "B) 10", "C) 15", "D) 20"],
            "resposta": "B"
        },
        2: {
            "pergunta": "Quantos anagramas podem ser formados a partir da palavra 'COMBINAÇÃO'?",
            "opcoes": ["A) 10!", "B) 11!", "C) 11!/2!", "D) 10!/2!"],
            "resposta": "C"
        },
        3: {
            "pergunta": "Quantas formas existem para organizar 3 bolas vermelhas e 2 bolas azuis em uma linha?",
            "opcoes": ["A) 10", "B) 6", "C) 8", "D) 12"],
            "resposta": "A"
        },
        4: {
            "pergunta": "Em uma eleição com 3 candidatos, quantas maneiras diferentes existem para escolher uma ordem dos vencedores?",
            "opcoes": ["A) 6", "B) 8", "C) 9", "D) 12"],
            "resposta": "A"
        },
        5: {
            "pergunta": "Quantos subconjuntos com exatamente 3 elementos podem ser formados a partir de um conjunto de 6 elementos?",
            "opcoes": ["A) 15", "B) 18", "C) 20", "D) 10"],
            "resposta": "A"
        },
        6: {
            "pergunta": "Se você tem 5 livros e quer organizá-los em uma prateleira, quantas sequências diferentes são possíveis?",
            "opcoes": ["A) 60", "B) 120", "C) 80", "D) 100"],
            "resposta": "B"
        },
        7: {
            "pergunta": "Quantas maneiras há de escolher um presidente e um vice-presidente de um grupo de 7 pessoas?",
            "opcoes": ["A) 21", "B) 35", "C) 42", "D) 56"],
            "resposta": "C"
        },
        8: {
            "pergunta": "Quantas maneiras existem para escolher 2 pessoas de um grupo de 8?",
            "opcoes": ["A) 28", "B) 36", "C) 16", "D) 20"],
            "resposta": "A"
        },
        9: {
            "pergunta": "Quantas maneiras diferentes há de organizar as letras na palavra 'BANANA'",
            "opcoes": ["A) 60", "B) 120", "C) 720", "D) 360"],
            "resposta": "D"
        },
        10: {
            "pergunta": "De quantas maneiras diferentes é possível escolher 3 frutas em uma caixa com 5 frutas diferentes?",
            "opcoes": ["A) 5", "B) 10", "C) 20", "D) 15"],
            "resposta": "D"
        },
        11: {
            "pergunta": "Qual é o valor de 7! (fatorial de 7)?",
            "opcoes": ["A) 5040", "B) 720", "C) 2520", "D) 40320"],
            "resposta": "A"
        },
        12: {
            "pergunta": "Quantas maneiras existem para organizar 4 pessoas em 4 cadeiras?",
            "opcoes": ["A) 16", "B) 64", "C) 24", "D) 36"],
            "resposta": "C"
        },
        13: {
            "pergunta": "De quantas maneiras podemos escolher 3 elementos de um conjunto com 8 elementos?",
            "opcoes": ["A) 28", "B) 56", "C) 16", "D) 35"],
            "resposta": "A"
        },
        14: {
            "pergunta": "Quantas maneiras diferentes existem para distribuir 5 bolas em 3 caixas, onde cada caixa pode receber qualquer número de bolas?",
            "opcoes": ["A) 125", "B) 243", "C) 15", "D) 45"],
            "resposta": "A"
        },
        15: {
            "pergunta": "Quantos subconjuntos de tamanho 2 podem ser formados a partir de um conjunto de 6 elementos?",
            "opcoes": ["A) 10", "B) 15", "C) 6", "D) 20"],
            "resposta": "B"
        },
        16: {
            "pergunta": "Quantas permutações diferentes das letras na palavra 'LIVRO' existem?",
            "opcoes": ["A) 60", "B) 120", "C) 24", "D) 36"],
            "resposta": "B"
        },
        17: {
            "pergunta": "Quantas maneiras existem para escolher uma equipe de 3 pessoas de um grupo de 9?",
            "opcoes": ["A) 84", "B) 120", "C) 36", "D) 28"],
            "resposta": "D"
        },
        18: {
            "pergunta": "Se você tem 10 opções e quer escolher 3 sem importar a ordem, quantas escolhas possíveis existem?",
            "opcoes": ["A) 120", "B) 720", "C) 30", "D) 36"],
            "resposta": "A"
        },
        19: {
            "pergunta": "Quantas maneiras diferentes existem para escolher 2 membros de um grupo de 7?",
            "opcoes": ["A) 21", "B) 42", "C) 35", "D) 14"],
            "resposta": "A"
        },
        20: {
            "pergunta": "Quantos subconjuntos podem ser formados a partir de um conjunto com 4 elementos?",
            "opcoes": ["A) 4", "B) 8", "C) 16", "D) 32"],
            "resposta": "C"
        },
        21: {
            "pergunta": "Quantas maneiras existem para distribuir 4 bolas em 2 caixas, onde cada caixa pode conter qualquer número de bolas?",
            "opcoes": ["A) 8", "B) 10", "C) 16", "D) 6"],
            "resposta": "A"
        },
        22: {
            "pergunta": "Quantas permutações podem ser feitas com as letras da palavra 'MELANCIA'?",
            "opcoes": ["A) 40,320", "B) 20,160", "C) 80,640", "D) 90,720"],
            "resposta": "B"
        },
        23: {
            "pergunta": "Qual é o número de maneiras de organizar as letras na palavra 'ELEFANTE'?",
            "opcoes": ["A) 40,320", " B)20,160", "C) 80,640", "D) 60,480"],
            "resposta": "D"
        },
        24: {
            "pergunta": "Quantas formas existem de escolher uma equipe de 2 pessoas de um grupo de 8?",
            "opcoes": ["A) 28", "B) 16", "C) 36", "D) 21"],
            "resposta": "A"
        },
        25: {
            "pergunta": "Quantas maneiras existem para escolher 4 objetos de um conjunto de 6?",
            "opcoes": ["A) 15", "B) 20", "C) 30", "D) 12"],
            "resposta": "B"
        },
        26: {
            "pergunta": "Quantos subconjuntos de tamanho 3 podem ser escolhidos de um conjunto com 5 elementos?",
            "opcoes": ["A) 5", "B) 6", "C) 10", "D) 15"],
            "resposta": "B"
        },
        27: {
            "pergunta": "Quantas maneiras diferentes existem para arranjar as letras da palavra 'FATORIAL'?",
            "opcoes": ["A) 40,320", "B) 20,160", "C) 90,720", "D) 45,360"],
            "resposta": "C"
        },
        28: {
            "pergunta": "De quantas maneiras podem ser organizadas as letras da palavra 'ESCOLA'?",
            "opcoes": ["A) 720", "B) 1,080", "C) 2,520", "D) 840"],
            "resposta": "A"
        },
        29: {
            "pergunta": "Quantas combinações podem ser feitas escolhendo 3 pessoas de um grupo de 6?",
            "opcoes": ["A) 15", "B) 20", "C) 10", "D) 12"],
            "resposta": "A"
        },
        30: {
            "pergunta": "Quantas permutações podem ser feitas com as letras da palavra 'COMBINA'?",
            "opcoes": ["A) 40,320", "B) 20,160", "C) 5,040", "D) 10,080"],
            "resposta": "C"
        }
    },
    'outono': {
        1: {
            "pergunta": "Qual é a definição de uma função?",
            "opcoes": ["A) Um conjunto de pares ordenados",
                       "B) Uma relação que associa cada elemento de um conjunto a um único elemento de outro conjunto",
                       "C) Uma equação matemática", "D) Um gráfico"],
            "resposta": "B"
        },
        2: {
            "pergunta": "Qual dos seguintes não é um exemplo de função?",
            "opcoes": ["A) f(x) = x^2", "B) g(x) = 2x + 3", "C) h(x) = { (1,2), (1,3) }", "D) j(x) = sin(x)"],
            "resposta": "C"
        },
        3: {
            "pergunta": "O que é uma função injetora?",
            "opcoes": ["A) Uma função onde cada valor de saída é associado a um único valor de entrada",
                       "B) Uma função onde dois valores de entrada podem ter o mesmo valor de saída",
                       "C) Uma função que não tem valores de saída repetidos",
                       "D) Uma função que não é definida para todos os números"],
            "resposta": "A"
        },
        4: {
            "pergunta": "Qual é a imagem da função f(x) = 2x + 1 quando x = 3?",
            "opcoes": ["A) 5", "B) 6", "C) 7", "D) 8"],
            "resposta": "C"
        },
        5: {
            "pergunta": "Uma função é dita ser sobrejetora se...",
            "opcoes": ["A) Cada elemento do domínio é mapeado para um único elemento do contradomínio",
                       "B) Cada elemento do contradomínio é atingido por pelo menos um elemento do domínio",
                       "C) Não há elementos repetidos no domínio",
                       "D) A função é injetora"],
            "resposta": "B"
        },
        6: {
            "pergunta": "Qual é o domínio da função f(x) = 1/x?",
            "opcoes": ["A) Todos os números reais", "B) Todos os números reais, exceto zero",
                       "C) Números inteiros positivos", "D) Números inteiros não-negativos"],
            "resposta": "B"
        },
        7: {
            "pergunta": "Uma função bijetora é...",
            "opcoes": ["A) Apenas injetora", "B) Apenas sobrejetora",
                       "C) Tanto injetora quanto sobrejetora", "D) Não é injetora nem sobrejetora"],
            "resposta": "C"
        },
        8: {
            "pergunta": "Se f(x) = x², qual é o contradomínio de f?",
            "opcoes": ["A) Todos os números reais", "B) Todos os números reais não-negativos",
                       "C) Números inteiros positivos", "D) Todos os números inteiros"],
            "resposta": "B"
        },
        9: {
            "pergunta": "Qual é a composição das funções f(x) = x + 2 e g(x) = 3x?",
            "opcoes": ["A) (f ∘ g)(x) = 3x + 2", "B) (f ∘ g)(x) = 3x + 6",
                       "C) (f ∘ g)(x) = x + 2", "D) (f ∘ g)(x) = 9x + 2"],
            "resposta": "A"
        },
        10: {
            "pergunta": "Qual é o valor da função inversa f^-1(x) se f(x) = 2x + 3?",
            "opcoes": ["A) (x - 3)/2", "B) 2x - 3", "C) x/2 + 3", "D) x + 3/2"],
            "resposta": "A"
        },
        11: {
            "pergunta": "Se f(x) = x² e g(x) = √x, qual é (g ∘ f)(x)?",
            "opcoes": ["A) x", "B) x²", "C) √x", "D) x^4"],
            "resposta": "A"
        },
        12: {
            "pergunta": "A função f(x) = sin(x) é...",
            "opcoes": ["A) Injetora e sobrejetora", "B) Apenas sobrejetora",
                       "C) Apenas injetora", "D) Nem injetora nem sobrejetora no domínio dos reais"],
            "resposta": "D"
        },
        13: {
            "pergunta": "O que é o zero de uma função?",
            "opcoes": ["A) Um valor de x onde f(x) = 0", "B) Um valor de x onde f(x) é infinito",
                       "C) Um valor de f(x) onde x = 0", "D) Um ponto de máximo da função"],
            "resposta": "A"
        },
        14: {
            "pergunta": "Se f(x) = x² + 1, f é injetora no domínio dos reais?",
            "opcoes": ["A) Sim", "B) Não", "C) Apenas para x > 0", "D) Apenas para x < 0"],
            "resposta": "B"
        },
        15: {
            "pergunta": "Se f(x) = 2x e g(x) = x + 1, qual é (f ∘ g)(x)?",
            "opcoes": ["A) 2x + 2", "B) 2x + 1", "C) x + 3", "D) x + 2"],
            "resposta": "A"
        },
        16: {
            "pergunta": "Qual é a definição do domínio de uma função?",
            "opcoes": ["A) O conjunto de valores de saída",
                       "B) O conjunto de valores para os quais a função é definida",
                       "C) O conjunto de pares ordenados",
                       "D) O conjunto de números inteiros"],
            "resposta": "B"
        },
        17: {
            "pergunta": "Se f(x) = 1/x e g(x) = x + 1, qual é (f ∘ g)(x)?",
            "opcoes": ["A) 1/(x + 1)", "B) 1/x + 1", "C) x + 1", "D) 1/x"],
            "resposta": "A"
        },
        18: {
            "pergunta": "Qual é a definição de uma função sobrejetora?",
            "opcoes": ["A) Uma função onde cada valor de saída é associado a um único valor de entrada",
                       "B) Uma função onde dois valores de entrada podem ter o mesmo valor de saída",
                       "C) Uma função que não tem valores de saída repetidos",
                       "D) Uma função que não é definida para todos os números"],
            "resposta": "B"
        },
        19: {
            "pergunta": "Se f(x) = x^2 e g(x) = √x, qual é (f ∘ g)(x)?",
            "opcoes": ["A) x", "B) x²", "C) √x", "D) x^4"],
            "resposta": "A"
        },
        20: {
            "pergunta": "Qual é a definição de uma função bijetora?",
            "opcoes": ["A) Apenas injetora", "B) Apenas sobrejetora",
                       "C) Tanto injetora quanto sobrejetora", "D) Não é injetora nem sobrejetora"],
            "resposta": "C"
        },
        21: {
            "pergunta": "Se f(x) = 2x + 3 e g(x) = x - 1, qual é (f ∘ g)(x)?",
            "opcoes": ["A) 2x + 1", "B) 2x + 2", "C) 2x + 3", "D) 2x + 4"],
            "resposta": "A"
        },
        22: {
            "pergunta": "Qual é a definição de uma função injetora?",
            "opcoes": ["A) Uma função onde cada valor de saída é associado a um único valor de entrada",
                       "B) Uma função onde dois valores de entrada podem ter o mesmo valor de saída",
                       "C) Uma função que não tem valores de saída repetidos",
                       "D) Uma função que não é definida para todos os números"],
            "resposta": "A"
        },
        23: {
            "pergunta": "Se f(x) = x^2 e g(x) = 1/x, qual é (f ∘ g)(x)?",
            "opcoes": ["A) 1/x²", "B) x²", "C) 1/x", "D) x"],
            "resposta": "A"
        },
        24: {
            "pergunta": "Qual é a definição de uma função sobrejetora?",
            "opcoes": ["A) Uma função onde cada valor de saída é associado a um único valor de entrada",
                       "B) Uma função onde dois valores de entrada podem ter o mesmo valor de saída",
                       "C) Uma função que não tem valores de saída repetidos",
                       "D) Uma função que não é definida para todos os números"],
            "resposta": "B"
        },
        25: {
            "pergunta": "Se f(x) = 2x + 1 e g(x) = x - 2, qual é (f ∘ g)(x)?",
            "opcoes": ["A) 2x - 3", "B) 2x - 2", "C) 2x - 1", "D) 2x + 1"],
            "resposta": "A"
        },
        26: {
            "pergunta": "Qual é a definição de uma função constante?",
            "opcoes": ["A) Uma função que não muda seu valor", "B) Uma função que muda seu valor",
                       "C) Uma função que é sempre zero", "D) Uma função que é linear"],
            "resposta": "A"
        },
        27: {
            "pergunta": "Qual é a definição de uma função linear?",
            "opcoes": ["A) Uma função que pode ser representada por uma linha reta", "B) Uma função que não é contínua",
                       "C) Uma função que tem um máximo e um mínimo", "D) Uma função que não tem raízes"],
            "resposta": "A"
        },
        28: {
            "pergunta": "Qual é a definição de uma função quadrática?",
            "opcoes": ["A) Uma função que pode ser representada por uma parábola", "B) Uma função que é linear","C) Uma função que não tem raízes", "D) Uma função que é constante"],
            "resposta": "A"
        },
        29: {
            "pergunta": "Qual é a definição de uma função exponencial?",
            "opcoes": ["A) Uma função onde a variável está no expoente", "B) Uma função que é linear",
                       "C) Uma função que não tem raízes", "D) Uma função que é constante"],
            "resposta": "A"
        },
        30: {
            "pergunta": "Qual é a definição de uma função logarítmica?",
            "opcoes": ["A) A inversa de uma função exponencial", "B) Uma função que é linear",
                       "C) Uma função que não tem raízes", "D) Uma função que é constante"],
            "resposta": "A"
        }
    },
    'inverno': {
        1: {
            "pergunta": "Qual é a definição básica de recursão em ciência da computação?",
            "opcoes": ["A) Uma função que chama a si mesma", "B) Uma função que nunca termina",
                       "C) Uma função que chama outra função", "D) Um loop infinito"],
            "resposta": "A"
        },
        2: {
            "pergunta": "Qual das seguintes é uma condição necessária para uma função recursiva?",
            "opcoes": ["A) Uma variável global", "B) Uma condição base", "C) Um loop", "D) Um contador"],
            "resposta": "B"
        },
        3: {
            "pergunta": "Qual função recursiva é frequentemente usada para calcular o valor de n! (fatorial de n)?",
            "opcoes": ["A) Soma", "B) Potência", "C) Multiplicação", "D) Fatorial"],
            "resposta": "D"
        },
        4: {
            "pergunta": "Qual é o resultado da função recursiva para fatorial de 0?",
            "opcoes": ["A) 0", "B) 1", "C) 2", "D) Indefinido"],
            "resposta": "B"
        },
        5: {
            "pergunta": "Qual é a principal vantagem do uso de recursão?",
            "opcoes": ["A) Menor uso de memória", "B) Código mais simples e legível", "C) Reduz o tempo de execução",
                       "D) Evita o uso de funções"],
            "resposta": "B"
        },
        6: {
            "pergunta": "O que é um caso base em uma função recursiva?",
            "opcoes": ["A) O caso que faz a função repetir", "B) O caso em que a função chama outra função",
                       "C) O caso que termina a recursão", "D) O caso que nunca é alcançado"],
            "resposta": "C"
        },
        7: {
            "pergunta": "Qual das seguintes estruturas é mais usada para implementar recursão?",
            "opcoes": ["A) Pilha", "B) Fila", "C) Lista", "D) Tabela Hash"],
            "resposta": "A"
        },
        8: {
            "pergunta": "O que é 'recursão direta'?",
            "opcoes": ["A) Quando uma função chama outra função", "B) Quando uma função chama a si mesma",
                       "C) Quando uma função chama duas outras funções", "D) Quando uma função nunca termina"],
            "resposta": "B"
        },
        9: {
            "pergunta": "O que ocorre se uma função recursiva não tiver um caso base?",
            "opcoes": ["A) A função termina normalmente", "B) A função entra em um loop infinito",
                       "C) A função retorna zero", "D) A função é ignorada pelo compilador"],
            "resposta": "B"
        },
        10: {
            "pergunta": "Qual é o papel de uma condição de parada em recursão?",
            "opcoes": ["A) Iniciar a recursão", "B) Reduzir o valor de uma variável", "C) Parar a recursão",
                       "D) Duplicar a função"],
            "resposta": "C"
        },
        11: {
            "pergunta": "Qual é o uso da recursão na resolução de problemas?",
            "opcoes": ["A) Para problemas que requerem repetição", "B) Para problemas lineares",
                       "C) Para problemas que podem ser divididos em subproblemas menores",
                       "D) Para problemas que não possuem solução base"],
            "resposta": "C"
        },
        12: {
            "pergunta": "Qual das seguintes é uma aplicação comum de recursão?",
            "opcoes": ["A) Calculadora", "B) Fatorial e sequência de Fibonacci", "C) Processador de texto",
                       "D) Planilha eletrônica"],
            "resposta": "B"
        },
        13: {
            "pergunta": "Qual das alternativas define 'recursão indireta'?",
            "opcoes": ["A) Uma função que chama outra função que eventualmente chama a função original",
                       "B) Uma função que nunca chama outra função", "C) Uma função que chama a si mesma",
                       "D) Uma função que retorna um valor fixo"],
            "resposta": "A"
        },
        14: {
            "pergunta": "Qual é a saída da função recursiva que calcula Fibonacci de 5?",
            "opcoes": ["A) 5", "B) 8", "C) 13", "D) 21"],
            "resposta": "B"
        },
        15: {
            "pergunta": "A recursão pode ser substituída por qual estrutura de controle?",
            "opcoes": ["A) Estrutura de seleção", "B) Estrutura de repetição (loops)", "C) Estrutura condicional",
                       "D) Estrutura de interrupção"],
            "resposta": "B"
        },
        16: {
            "pergunta": "Quantas chamadas recursivas são feitas para calcular o fatorial de 4?",
            "opcoes": ["A) 2", "B) 3", "C) 4", "D) 5"],
            "resposta": "D"
        },
        17: {
            "pergunta": "Quais dos seguintes problemas podem ser resolvidos usando recursão?",
            "opcoes": ["A) Ordenação de listas", "B) Somar duas variáveis", "C) Multiplicação", "D) Filtragem de dados"],
            "resposta": "A"
        },
        18: {
            "pergunta": "Qual das seguintes não é uma característica da recursão?",
            "opcoes": ["A) Uso de chamadas de função", "B) Uso de caso base", "C) Uso de variáveis globais",
                       "D) Uso de pilha para armazenar chamadas"],
            "resposta": "C"
        },
        19: {
            "pergunta": "Recursão pode ser mais eficiente do que loops?",
            "opcoes": ["A) Sempre", "B) Em problemas que podem ser divididos em subproblemas", "C) Nunca",
                       "D) Em cálculos matemáticos simples"],
            "resposta": "B"
        },
        20: {
            "pergunta": "Qual das seguintes é uma vantagem da recursão?",
            "opcoes": ["A) Menor tempo de execução", "B) Menor uso de memória", "C) Simplificação de problemas complexos",
                       "D) Necessidade de mais código"],
            "resposta": "C"
        },
        21: {
            "pergunta": "Como a função recursiva fatorial de um número n é geralmente escrita?",
            "opcoes": ["A) f(n) = n + f(n-1)", "B) f(n) = n * f(n-1)", "C) f(n) = f(n-1)", "D) f(n) = n - f(n-1)"],
            "resposta": "B"
        },
        22: {
            "pergunta": "Recursão é uma abordagem natural para resolver problemas de qual natureza?",
            "opcoes": ["A) Iterativos", "B) Lineares", "C) Dividir para conquistar", "D) Aleatórios"],
            "resposta": "C"
        },
        23: {
            "pergunta": "Qual é uma desvantagem da recursão?",
            "opcoes": ["A) Aumenta a complexidade", "B) Consome mais memória devido à pilha de chamadas", "C) É mais lento",
                       "D) Não pode ser usado em problemas grandes"],
            "resposta": "B"
        },
        24: {
            "pergunta": "Qual das seguintes é uma aplicação prática da recursão?",
            "opcoes": ["A) Contar caracteres em uma string", "B) Multiplicação",
            "C) Processamento de árvores binárias", "D) Processamento de matrizes"],
            "resposta": "C"
        },
        25: {
            "pergunta": "Na recursão, o que acontece com cada chamada recursiva?",
            "opcoes": ["A) É armazenada em uma fila", "B) É armazenada na pilha", "C) É descartada imediatamente",
                       "D) É processada em ordem reversa"],
            "resposta": "B"
        },
        26: {
            "pergunta": "Para qual estrutura de dados é mais adequada a recursão?",
            "opcoes": ["A) Fila", "B) Lista", "C) Pilha", "D) Dicionário"],
            "resposta": "C"
        },
        27: {
            "pergunta": "Quais são os casos mais comuns onde recursão é útil?",
            "opcoes": ["A) Jogos", "B) Algoritmos de busca e ordenação", "C) Processamento de dados",
                       "D) Edição de imagens"],
            "resposta": "B"
        },
        28: {
            "pergunta": "Qual é uma limitação da recursão em sistemas com pilha limitada?",
            "opcoes": ["A) Processamento lento", "B) Excesso de variáveis", "C) Estouro de pilha",
                       "D) Uso de função global"],
            "resposta": "C"
        },
        29: {
            "pergunta": "A profundidade de uma chamada recursiva refere-se a...",
            "opcoes": ["A) Número de vezes que a função é chamada", "B) A quantidade de memória usada",
                       "C) O número de parâmetros", "D) A estrutura de dados usada"],
            "resposta": "A"
        },
        30: {
            "pergunta": "A recursão de cauda é...",
            "opcoes": ["A) Uma função que termina em um loop", "B) Uma recursão onde a chamada recursiva é a última operação", "C) Uma função sem caso base",
                       "D) Uma função que nunca termina"],
            "resposta": "B"
        }
    },
    'pico': {
        1: {
            "pergunta": "O que é um grafo em teoria dos grafos?",
            "opcoes": ["A) Um conjunto de pontos e linhas conectando pares de pontos", "B) Um conjunto de números",
                       "C) Uma sequência de passos", "D) Um tipo de matriz"],
            "resposta": "A"
        },
        2: {
            "pergunta": "O que significa dizer que um grafo é conexo?",
            "opcoes": ["A) Todos os vértices têm o mesmo grau", "B) Há um caminho entre qualquer par de vértices",
                       "C) O grafo contém um ciclo", "D) O grafo é completo"],
            "resposta": "B"
        },
        3: {
            "pergunta": "Qual é o número mínimo de arestas em um grafo conexo com n vértices?",
            "opcoes": ["A) n", "B) n - 1", "C) n + 1", "D) n * (n - 1) / 2"],
            "resposta": "B"
        },
        4: {
            "pergunta": "Qual dos seguintes é um exemplo de grafo não direcionado?",
            "opcoes": ["A) Grafo de rede de computadores", "B) Diagrama de fluxo de controle",
                       "C) Grafo de rede de estradas bidirecionais", "D) Árvore genealógica"],
            "resposta": "C"
        },
        5: {
            "pergunta": "Qual o nome dado a um grafo sem ciclos?",
            "opcoes": ["A) Conexo", "B) Ciclo", "C) Árvore", "D) Completo"],
            "resposta": "C"
        },
        6: {
            "pergunta": "Qual estrutura de dados é mais comumente usada para representar grafos em memória?",
            "opcoes": ["A) Pilha", "B) Lista de adjacência", "C) Fila", "D) Árvore binária"],
            "resposta": "B"
        },
        7: {
            "pergunta": "Qual algoritmo é frequentemente utilizado para encontrar o caminho mais curto em um grafo?",
            "opcoes": ["A) Algoritmo de Dijkstra", "B) Algoritmo de Kruskal", "C) Algoritmo de Prim", "D) Algoritmo de Bellman-Ford"],
            "resposta": "A"
        },
        8: {
            "pergunta": "O que é um vértice de corte em um grafo?",
            "opcoes": ["A) Um vértice que aumenta o grau de outros vértices", "B) Um vértice cuja remoção desconecta o grafo",
                       "C) Um vértice sem arestas conectadas", "D) Um vértice que forma um ciclo"],
            "resposta": "B"
        },
        9: {
            "pergunta": "Em um grafo ponderado, o que as arestas possuem além de vértices?",
            "opcoes": ["A) Peso", "B) Cor", "C) Número de ciclos", "D) Grafo completo"],
            "resposta": "A"
        },
        10: {
            "pergunta": "Qual dos seguintes grafos tem o maior número de arestas?",
            "opcoes": ["A) Grafo conexo", "B) Grafo completo", "C) Grafo ciclo", "D) Árvore"],
            "resposta": "B"
        },
        11: {
            "pergunta": "Um grafo direcionado é caracterizado por...",
            "opcoes": ["A) Arestas sem direção", "B) Arestas com direção específica", "C) Conexões que não formam ciclos",
                       "D) Nenhuma aresta"],
            "resposta": "B"
        },
        12: {
            "pergunta": "Em teoria dos grafos, o que é um circuito?",
            "opcoes": ["A) Um caminho que começa e termina no mesmo vértice", "B) Um caminho com vértices adjacentes",
                       "C) Um ciclo sem vértices repetidos", "D) Um grafo completo"],
            "resposta": "A"
        },
        13: {
            "pergunta": "Qual é a complexidade do algoritmo de busca em largura (BFS) em um grafo com V vértices e E arestas?",
            "opcoes": ["A) O(V)", "B) O(E)", "C) O(V + E)", "D) O(V * E)"],
            "resposta": "C"
        },
        14: {
            "pergunta": "Qual algoritmo é utilizado para encontrar uma árvore geradora mínima?",
            "opcoes": ["A) Algoritmo de Dijkstra", "B) Algoritmo de Prim", "C) Algoritmo de Bellman-Ford",
                       "D) Busca em profundidade"],
            "resposta": "B"
        },
        15: {
            "pergunta": "O que é um grafo completo?",
            "opcoes": ["A) Um grafo onde todos os vértices têm o mesmo grau", "B) Um grafo em que todos os vértices estão conectados entre si",
                       "C) Um grafo com um ciclo", "D) Um grafo com número ímpar de arestas"],
            "resposta": "B"
        },
        16: {
            "pergunta": "Em um grafo, o grau de um vértice é...",
            "opcoes": ["A) O número de arestas conectadas ao vértice", "B) A soma dos pesos das arestas do grafo",
                       "C) O número de vértices", "D) O comprimento do maior caminho"],
            "resposta": "A"
        },
        17: {
            "pergunta": "Qual é a complexidade do algoritmo de Dijkstra usando uma fila de prioridade?",
            "opcoes": ["A) O(V^2)", "B) O(V + E)", "C) O(E log V)", "D) O(E^2)"],
            "resposta": "C"
        },
        18: {
            "pergunta": "O que é um grafo bipartido?",
            "opcoes": ["A) Um grafo com duas cores", "B) Um grafo com vértices divididos em dois conjuntos onde arestas conectam apenas vértices de conjuntos diferentes",
                       "C) Um grafo completo", "D) Um grafo com dois ciclos"],
            "resposta": "B"
        },
        19: {
            "pergunta": "O que é um grafo planar?",
            "opcoes": ["A) Um grafo que pode ser desenhado no plano sem arestas cruzadas",  "B)Um grafo com apenas três vértices", "C) Um grafo que possui ciclos", "D) Um grafo completo"],
            "resposta": "A"
        },
        20: {
            "pergunta": "Qual é a diferença entre um caminho e um circuito em um grafo?",
            "opcoes": ["A) Caminho é fechado, circuito é aberto", "B) Caminho não tem ciclos, circuito é um caminho fechado",
                       "C) Caminho é maior que o circuito", "D) Caminho é completo, circuito é bipartido"],
            "resposta": "B"
        },
        21: {
            "pergunta": "Qual algoritmo é usado para encontrar o caminho mínimo em grafos com arestas de pesos negativos?",
            "opcoes": ["A) Algoritmo de Dijkstra", "B) Algoritmo de Prim", "C) Algoritmo de Bellman-Ford",
                       "D) Algoritmo de Kruskal"],
            "resposta": "C"
        },
        22: {
            "pergunta": "Em qual estrutura de dados é baseada a busca em profundidade (DFS)?",
            "opcoes": ["A) Fila", "B) Pilha", "C) Lista", "D) Árvore binária"],
            "resposta": "B"
        },
        23: {
            "pergunta": "Qual é o número máximo de arestas em um grafo simples com n vértices?",
            "opcoes": ["A) n - 1", "B) n^2", "C) n * (n - 1) / 2", "D) 2^n"],
            "resposta": "C"
        },
        24: {
            "pergunta": "O que é um subgrafo?",
            "opcoes": ["A) Uma parte de um grafo", "B) Um grafo completo", "C) Um grafo desconexo", "D) Um ciclo no grafo"],
            "resposta": "A"
        },
        25: {
            "pergunta": "O algoritmo de Kruskal é usado para...",
            "opcoes": ["A) Encontrar o caminho mais curto", "B) Ordenar vértices", "C) Encontrar a árvore geradora mínima",
                       "D) Detectar ciclos"],
            "resposta": "C"
        },
        26: {
            "pergunta": "Como um grafo denso é definido?",
            "opcoes": ["A) Tem mais arestas que vértices", "B) Tem mais vértices que arestas", "C) É um grafo completo",
                       "D) Possui um único ciclo"],
            "resposta": "A"
        },
        27: {
            "pergunta": "Qual é o grau de um vértice isolado?",
            "opcoes": ["A) 0", "B) 1", "C) n", "D) 2"],
            "resposta": "A"
        },
        28: {
            "pergunta": "O que define um ciclo Hamiltoniano?",
            "opcoes": ["A) Um caminho que percorre todos os vértices uma vez e retorna ao inicial",
                       "B) Um caminho sem vértices repetidos", "C) Uma árvore geradora mínima", "D) Um grafo planar"],
            "resposta": "A"
        },
        29: {
            "pergunta": "Qual é a principal característica de um grafo direcionado acíclico?",
            "opcoes": ["A) Possui ciclos", "B) Não possui ciclos", "C) Todos os vértices têm o mesmo grau", "D) É um grafo completo"],
            "resposta": "B"
        },
        30: {
            "pergunta": "Qual dos seguintes é um exemplo de aplicação de grafos?",
            "opcoes": ["A) Redes sociais", "B) Calendário", "C) Funções matemáticas", "D) Pilhas de execução"],
            "resposta": "A"
        }
    }
}
