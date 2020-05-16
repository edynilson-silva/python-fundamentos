nome_da_lista = [elemento1, elemento2, elemento3]

# Adicionar elementos, usar o append()
lista = ["Arroz", "Feijão"]
lista.append("Macarrão")
print(lista) #Arroz, Feijão, Macarrão

# Para adicionar em determinada posição, usar o insert()
lista.insert(1, "Macarrão")

# Remover elementos, usar o remove(), recebe o parâmetro a ser removido
lista.remove("Macarrão")

# Demais métodos

# pop(indice) remove o elemento da lista
# index(elemento): retorna o índice do elemento na lista
# count(elemento): retorna a quantidade de vezes em que um elemento aparece na lista
# sort(): ordena a lista
# reverse(): inverte a ordem da lista