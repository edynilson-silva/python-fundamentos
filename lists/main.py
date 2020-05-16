from usuario import Usuario

continuar = 1
lista_usuarios = []

while continuar != 0:
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite sua idade: "))
    sobrenome = input("Digite seu sobrenome: ")
    usuario = Usuario(nome, idade, sobrenome)
    lista_usuarios.append(usuario)

    print(f"Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}")

    if usuario.idade <= 17:
        print(f"{usuario.nome} é adolescente")
    elif usuario.idade >= 18 and usuario.idade <= 50:
        print(f"{usuario.nome} é adulto")
    else:
        print(f"{usuario.nome} é idoso")
    continuar = int(input("Deseja continuar cadastrando? 0 - Sair | 1 - Continuar"))
else:
    print("Lista de usuários cadastrados: ")

    for x in lista_usuarios:
        print(f"Nome completo: {x.nome} {x.sobrenome} - Idade {x.idade}")

    print("O loop entrou no else")
