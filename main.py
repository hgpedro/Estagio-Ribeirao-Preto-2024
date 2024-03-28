#1 Valor final da variável SOMA:

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA) # Ao final do processamento, o valor da variável SOMA será 91.

#2 Verificação se um número pertence à sequência de Fibonacci:

def fibonacci_sequence(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

numero = int(input("Informe um número: "))

if fibonacci_sequence(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

#3 Próximo elemento nas sequências:

# a) 1, 3, 5, 7, ___
# A lógica é adicionar 2 a cada elemento anterior
# Próximo elemento: 9

# b) 2, 4, 8, 16, 32, 64, ____
# A lógica é multiplicar cada elemento anterior por 2
# Próximo elemento: 128

# c) 0, 1, 4, 9, 16, 25, 36, ____
# A lógica é elevar ao quadrado o índice do elemento (0^2, 1^2, 2^2, ...)
# Próximo elemento: 49

# d) 4, 16, 36, 64, ____
# A lógica é adicionar o próximo quadrado perfeito
# Próximo elemento: 100

# e) 1, 1, 2, 3, 5, 8, ____
# A lógica é a sequência de Fibonacci
# Próximo elemento: 13

# f) 2,10, 12, 16, 17, 18, 19, ____
# A lógica são números que começam com a letra D.
# Próximo elemento: 200

#4 Descobrindo qual interruptor controla cada lâmpada:

# A solução é ligar um interruptor e esperar alguns minutos antes de ligar o segundo, pois sabemos que ao invés de toda a energia elétrica ser convertida em energia luminosa, a resistência absorve parte dela, transformando-a em energia térmica.
# Assim, quando você entrar na sala:
# - A lâmpada que estiver acesa está conectada ao primeiro interruptor
# - A lâmpada que estiver apagada e quente está conectada ao segundo interruptor
# - A lâmpada que estiver apagada e fria está conectada ao terceiro interruptor
# Então, você sabe qual interruptor controla cada lâmpada.

#5 Invertendo os caracteres de uma string:
    
def inverter_string(string):
    inverted_string = ""
    for char in string:
        inverted_string = char + inverted_string
    return inverted_string

texto = input("Informe uma string: ")
print("String invertida:", inverter_string(texto))
