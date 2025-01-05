#aluno: Elton Victor Da Costa - 20241014050024
#aluna: Kaillany Felix Souza - 20242014050021

# Inicializa o contador de números palíndromos
contador_palindromos = 0

# Itera pelos números de 10 a 100000
numero = 10 
while numero <= 100000:
    
    # Variáveis para verificar se o número é palíndromo
    original = numero
    reverso = 0

    # Calcula o número reverso
    while original > 0:
        resto = original % 10  
        reverso = reverso * 10 + resto  
        original = original // 10  
    
    # Verifica se o número é palíndromo
    if numero == reverso:
        contador_palindromos += 1  

    numero += 1

# Exibe o resultado final
print("Quantidade de números palíndromos entre 10 e 100000:", contador_palindromos)
