#aluno: Elton Victor Da Costa - 20241014050024
#aluna: Kaillany Felix Souza - 20242014050021

import random

# Lista de palavras para o jogo
palavras = (
    "ADAGA", "ADUBO", "AMIGO", "ANEXO", "ARAME", "ARARA", "ARROZ",
    "ASILO", "ASTRO", "BAILE", "BAIXA", "BALAO", "BALSA", "BARCO",
    "BARRO", "BEIJO", "BICHO", "BORDA", "BORRA", "BRAVO", "BREJO",
    "BURRO", "CAIXA", "CALDO", "CANJA", "CARRO", "CARTA", "CERVO",
    "CESTA", "CLIMA", "COBRA", "COLAR", "COQUE", "COURO", "CRAVO",
    "DARDO", "FAIXA", "FARDO", "FENDA", "FERRO", "FESTA", "FLUOR",
    "FORCA", "FORNO", "FORTE", "FUNDO", "GAITA", "GARRA", "GENIO",
    "GESSO", "GRADE", "GRANA", "GRAMA", "GURIA", "GREVE", "GRUTA",
    "HEROI", "HOTEL", "ICONE", "IMPAR", "IMUNE", "INDIO", "JUNTA",
    "LAPIS", "LARVA", "LAZER", "LENTO", "LESTE", "LIMPO", "LIVRO",
    "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORTE",
    "MORRO", "MURAL", "MOVEL", "NACAO", "NINHO", "NOBRE", "NORMA",
    "NORTE", "NUVEM", "PACTO", "PALHA", "PARDO", "PARTE", "PEDRA",
    "PEDAL", "PEIXE", "PRADO", "PISTA", "POMBO", "POETA", "PONTO",
    "PRATO", "PRECO", "PRESO", "PROSA", "PRUMO", "PULGA", "PULSO",
    "QUEPE", "RAIVA", "RISCO", "RITMO", "ROSTO", "ROUPA", "SABAO",
    "SALTO", "SENSO", "SINAL", "SITIO", "SONHO", "SOPRO", "SURDO",
    "TARDE", "TERNO", "TERMO", "TERRA", "TIGRE", "TINTA", "TOLDO",
    "TORRE", "TRAJE", "TREVO", "TROCO", "TRONO", "TURMA", "URUBU",
    "VALSA", "VENTO", "VERDE", "VISAO", "VINHO", "VIUVO", "ZEBRA"
)

# Escolhendo duas palavras secretas diferentes
palavra_secreta_1 = random.choice(palavras)
palavra_secreta_2 = random.choice(palavras)

# Verificando se as palavras são diferentes
while palavra_secreta_2 == palavra_secreta_1:  
    palavra_secreta_2 = random.choice(palavras)

# Número de tentativas
num_tentativas = 6

# Cores para as letras
verde = "\033[32m"  # Letra correta e na posição certa
amarelo = "\033[33m"  # Letra correta mas na posição errada
cinza = "\033[90m"  # Letra errada
reset = "\033[0m"  # Resetar a cor

# Controle de acertos
acertou_palavra_1 = False
acertou_palavra_2 = False

# Bem-vindo ao jogo
print("Bem-vindo ao jogo Dueto!")
print("Tente adivinhar as duas palavras secretas de 5 letras.")
print("Dica: use SOMENTE letras maiúsculas nas suas respostas.")
print(f"Você tem {num_tentativas} tentativas.\n")

# Jogo
while num_tentativas > 0 and not (acertou_palavra_1 and acertou_palavra_2):
    print(f"Tentativas restantes: {num_tentativas}")
    tentativa = input("Digite uma palavra de 5 letras: ").strip()

    # Validar se a palavra está em maiúsculas
    palavra_maiuscula = True 
    for letra in tentativa:
        if not ('A' <= letra <= 'Z'): 
            palavra_maiuscula = False
            break

    if not palavra_maiuscula:
        print("Por favor, use SOMENTE letras maiúsculas.")
        continue 

    # Validar o tamanho da palavra
    if not (len(tentativa) == 5):
        print("A palavra deve ter exatamente 5 letras!")
        continue

    # Comparação com a primeira palavra
    resultado_1 = ""
    for i in range(5):
        if acertou_palavra_1:  # Se já acertou, manter verde
            resultado_1 += verde + palavra_secreta_1[i] + reset
        elif tentativa[i] == palavra_secreta_1[i]:
            resultado_1 += verde + tentativa[i] + reset
        elif tentativa[i] in palavra_secreta_1:
            resultado_1 += amarelo + tentativa[i] + reset
        else:
            resultado_1 += cinza + tentativa[i] + reset

    # Comparação com a segunda palavra
    resultado_2 = ""
    for i in range(5):
        if acertou_palavra_2:  # Se já acertou, manter verde
            resultado_2 += verde + palavra_secreta_2[i] + reset
        elif tentativa[i] == palavra_secreta_2[i]:
            resultado_2 += verde + tentativa[i] + reset
        elif tentativa[i] in palavra_secreta_2:
            resultado_2 += amarelo + tentativa[i] + reset
        else:
            resultado_2 += cinza + tentativa[i] + reset

    # Mostrar os resultados de forma combinada
    print(f"\nResultado: Palavra 1: {resultado_1} | Palavra 2: {resultado_2}")

    # Atualizar acertos
    if tentativa == palavra_secreta_1:
        acertou_palavra_1 = True
        print("Você acertou a primeira palavra!")

    if tentativa == palavra_secreta_2:
        acertou_palavra_2 = True
        print("Você acertou a segunda palavra!")

    # Reduzir tentativas se não acertou nenhuma
    if not (tentativa == palavra_secreta_1 or tentativa == palavra_secreta_2):
        num_tentativas -= 1

# Fim do jogo
if acertou_palavra_1 and acertou_palavra_2:
    print("Parabéns! Você acertou ambas as palavras!")
else:
    print(f"Fim de jogo! As palavras eram: {palavra_secreta_1} e {palavra_secreta_2}")
    print("Mais sorte na próxima vez!")
