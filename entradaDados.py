nome = input("Digite o seu nome: ") #frase opcional
idade = int(input("Digite sua idade: "))
sobrenome = input("Digite seu sobrenome: ")

print(type(idade)) #por padrão o input: salva no formato string 'str'

print(f"Olá, {nome} {sobrenome}, sua idade é {idade}")