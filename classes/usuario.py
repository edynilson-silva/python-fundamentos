class Usuario:
    def __init__(self, nome, idade, sobrenome):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome

# import: importa o módulo por completo
# from: importa apenas parte do módulo


# no arquivo main.py
from usuario import Usuario #1° Forma, o nome do recurso que queremos utilizar
import usuario #importa tudo da classe (precisamos definir de onde estamos importando usuario.Usuario)