numero = 0
soma = 0
while numero < 20:
    numero = int(input("Digite um número menor que 20"))
    soma = soma + numero
    if numero == 16:
        continue
print(soma)

# "salta" a execução ao receber o valor 16