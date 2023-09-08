from random import randint
import tree_2 as tree

#inserindo valores aleatórios na árvore
qtd_valor = int(input('Digite quantos números você deseja inserir aleatóriamente: '))
arv = tree.tree(randint(1,25))
for i in range(qtd_valor):
    arv.insert(randint(1,15))

# Implemente um método na classe `Arvore` que verifica se um valor está presente na árvore.
valor = int(input('Digite um valor para verificar na árvore: '))
if arv.binary_search(valor):
    print('Valor presente')
else:
    print('Valor ausente')

#Crie uma função que calcula a altura de uma árvore binária.
print(f'altura da árvore: {arv.tree_height()}')

#Implemente uma função que realiza uma travessia inordem (esquerda-raiz-direita) em uma árvore binária e retorna os valores dos nós visitados.
print('Árvore percorrida in-ordem:')
arv.in_order()

#Implemente uma função que realiza uma travessia pré-ordem (raiz-esquerda-direita) em uma árvore binária e retorna os valores dos nós visitados.
print('Árvore percorrida pré-ordem:')
arv.pre_order()

#Implemente uma função que realiza uma travessia pós-ordem (esquerda-direita-raiz) em uma árvore binária e retorna os valores dos nós visitados.
print('Árvore percorrida pos-ordem: ')
arv.post_order()

#Implemente uma função que realiza uma travessia em níveis em uma árvore binária e retorna os valores dos nós visitados.
print('Árvore percorrida em ordem de níveis:')
arv.level_order()

#Escreva uma função para contar o número total de nós em uma árvore binária.
print(f'Número total de nós: {arv.count_nos()}')

#Escreva uma função que encontre o valor máximo armazenado em uma árvore binária.
print(f'Valor máximo armazenado na árvore: {arv.max_value()}')

#Escreva uma função que verifica se uma árvore binária é uma árvore de busca válida.
if arv.is_valid_bst():
    print('É uma árvore de busca válida')
else:
    print('Não é uma árvore de busca válida')

#Implemente um método na classe `Arvore` que permite a remoção de um nó específico da árvore.
valor_rem = int(input('Digite um valor para remover: '))
arv.remove_value(valor_rem)
print('Árvore após valor removido em ordem de niveis')
arv.level_order()

#Escreva uma função que retorna todos os nós em um determinado nível da árvore.
no = int(input('Digite um nível da árvore para retornar os nós desse nível: '))
print(arv.nivel_node_descendent(no))

#Escreva uma função que encontre o caminho da raiz até um nó específico na árvore.
node = int(input('Digite um nó para buscar seu caminho até a raiz: '))
print(arv.root_node(node))

#Escreva uma função que, dado um nó, retorne todos os nós filhos do nó fornecido.
nodo = int(input('Digite outro nó para retornar os nós filhos dele: '))
print(arv.descendant_node(nodo))