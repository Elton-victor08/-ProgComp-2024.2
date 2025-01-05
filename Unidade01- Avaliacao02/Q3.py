#aluno: Elton Victor Da Costa - 20241014050024
#aluna: Kaillany Felix Souza - 20242014050021

# Inicialização de variáveis
limite = 10000
numero = 3  
ultimo_primo = 2  
contador_pares = 0 

# Laço principal para verificar todos os números ímpares até o limite
while numero < limite:
    # Verifica se o número atual é primo
    primo = True
    divisor = 2

    # Testa se o número é divisível por algum número menor que ele
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            primo = False
        divisor += 1

    # Se o número for primo e o anterior também, verifica se formam um par consecutivo
    if primo:
        if numero - ultimo_primo == 2: 
            contador_pares += 1
        
        ultimo_primo = numero

    # Incrementa de 2 em 2 para considerar apenas ímpares
    numero += 2

# Exibe o resultado final
print("Quantidade de pares de primos consecutivos ímpares menores que 10000:", contador_pares)

#OBS: coloquei o número máximo até 10 mil devido ao número da questão demorar muito para rodar no python.
