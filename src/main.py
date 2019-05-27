from hash import *
from avl import *


def menu():

    print("Escolha a estrutura de dados: \n")
    ed = int(input("1 - Hash\n2 - Árvore AVL\n"))

    if ed == 1:
        tam = int(input("Insira o tamanho da tabela: \n"))

        hashtable = Hash(tam)
        stop = 0

        while stop < 5:
            stop = int(input("1 - Inserir\n2 - Consultar\n3 - Imprimir tabela\n4 - Remover um elemento\n"))
            if stop == 1:
                elemento = input("Insira o elemento do nó\n")
                chave = int(input("Insita o valor da chave\n"))
                no = Node()
                no.create(elemento, chave)

                hashtable.insert(no)

            elif stop == 2:
                hashtable.search(int(input("Insira a chave para pesquisar o elemento\n")))

            elif stop == 3:
                hashtable.printall()
            elif stop == 4:
                chave = int(input("Insira a chave do nodo que você deseja remover: "))
                elem = input("Insira o elemento do nodo que você deseja remover: ")
                hashtable.remove(chave, elem)

    elif ed == 2:
        mytree = AVLTree()
        raiz = None
        inp = int(0)
        while inp < 5:
            print("Escolha uma opção: \n1 - Inserir\n2 - PreOrdem\n3 - InOrdem\n4 - Remover")
            inp = int(input(""))

            if inp == 1:
                val = int(input("Insira a chave do nodo atual: "))
                dat = input("Insira o conteudo do nodo atual: ")
                raiz = mytree.insert(raiz, val, dat)

            if inp == 2:
                mytree.preorder(raiz)

            if inp == 3:
                mytree.inorder(raiz)

            if inp == 4:
                val = int(input("Insira a chave do nodo a ser removido: "))
                mytree.delete(raiz, val)

    elif ed > 2:
        return

menu()