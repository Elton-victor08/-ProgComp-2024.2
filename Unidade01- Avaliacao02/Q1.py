#aluno: Elton Victor Da Costa - 20241014050024
#aluna: Kaillany Felix Souza - 20242014050021


contador = 0

# Laço para percorrer os números de 10 até 987631
for num in range(10, 987632): 
    num_str = str(num)
    decrescente = True

    # Verificando se o número é decrescente
    for i in range(len(num_str) - 1):
        if num_str[i] < num_str[i + 1]: 
            decrescente = False
            break

    # Se for decrescente, incrementa o contador
    if decrescente:
        contador += 1

# Exibindo a quantidade de números decrescentes
print(f"A quantidade de números decrescentes entre 10 e 987631 é: {contador}")
