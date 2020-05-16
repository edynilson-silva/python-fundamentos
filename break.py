numero = 0
soma = 0
while numero < 20:
    numero = int(input("Digite um número menor que 20"))
    soma = soma + numero
    if numero == 16:
        break
print(soma)

# Encerra ao reeber o valor 16