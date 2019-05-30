from hash import *
from avl import *
from rbtree import *
from utils import *
from btree import *
import math


def addtods():
    arquivo = ''
    chfile = int(input("ESCOLHA UM ARQUIVO: \n1 - teste1.txt\n"))

    # seleção de arquivo -----------------------------------------------------------------------------------------------

    if chfile == 1:
        arquivo = '../textfiles/teste1.txt'

    # seleção de estrutura de dados ------------------------------------------------------------------------------------

    chds = int(input("ESCOLHA UMA OPÇÃO: \n1 - Hash\n2 - AVL-tree\n3 - RB-tree\n4 - B-tree\n"))
    if chds == 1:
        hasht = Hash((int(math.floor(numwords(arquivo)/2) - 5)))

    # opções internas dos algoritmos -----------------------------------------------------------------------------------
        inp = int(0)
    # HASH -------------------------------------------------------------------------------------------------------------
        while inp < 5:
            inp = int(input("HASH > ESCOLHA UMA OPÇÃO: \n1 - Adicionar\n2 - Consultar\n3 - Remover\n4 - Imprimir\n"
                            "5 - Interroper execução\n"))
            if inp == 1:
                list = listwords(arquivo)
                for i in list:
                    no = Node()
                    no.create(i, ordstring(i), occurences(i, arquivo))
                    hasht.insert(no)

            if inp == 2:
                chave = input("Insira uma palavra para ser pesquisada na tabela:\n")
                hasht.search(ordstring(chave), chave)

            if inp == 3:
                chave = ordstring(input("Insira a palavra que você deseja remover:\n"))
                hasht.remove(chave)

            if inp == 4:
                hasht.printall()
    # Árvore AVL -------------------------------------------------------------------------------------------------------
    elif chds == 2:
        inserted = False
        mytree = AVLTree()
        raiz = None
        inp = int(0)
        while inp < 5:
            print("AVL-tree >\nEscolha uma opção: \n1 - Inserir\n2 - Imprimir\n"
                  "3 - Remover\n4 - Pesquisar\n5 - Interromper execução\n")
            inp = int(input(""))

            if inp == 1:
                list = listwords(arquivo)
                for i in list:
                    dat = i
                    oc = occurences(i, arquivo)
                    raiz = mytree.insert(raiz, dat, oc)
                    inserted = True

            if inp == 2:
                if inserted:
                    mytree.sortedlist(raiz)
                    print("\n")
                else:
                    print("a arvore está vazia insira um conjunto de elementos\n")

            if inp == 3:
                if inserted:
                    val = input("Insira a chave do nodo a ser removido: \n")
                    mytree.delete(raiz, val)
                else:
                    print("a arvore está vazia insira um conjunto de elementos\n")
            if inp == 4:
                if inserted:
                    val = input("Insira a chave do nodo para ser pesquisado: \n")
                    if mytree.search(raiz, val):
                        print("A chave está na arvore\n")
                    else:
                        print("chave não encontrada, adicionando...")
                        mytree.insert(raiz, val, 0)
                else:
                    print("a arvore está vazia insira um conjunto de elementos\n")
    # Árvore Rubro-negra -----------------------------------------------------------------------------------------------
    elif chds == 3:
        inserted = False
        mytree = RBtree()
        inp = int(0)
        while inp < 5:
            print("RB-tree >\nEscolha uma opção:\n1 - Inserir\n2 - Imprimir\n3 - Pesquisar\n4 - Remover\n"
                  "5 - Interromper execução\n")
            inp = int(input(""))

            if inp == 1:
                list = listwords(arquivo)
                for i in list:
                    dat = i
                    oc = occurences(i, arquivo)
                    mytree.insert(dat, oc)
                    inserted = True

            if inp == 2:
                if inserted:
                    mytree.sortedlist()
                    print("\n")
                else:
                    print("a arvore está vazia insira um conjunto de elementos\n")

            if inp == 3:
                if inserted:
                    val = input("Insira a chave do nodo para ser pesquisado: \n")
                    if mytree.search(val):
                        print("A chave está na arvore\n")
                    else:
                        print("chave não encontrada, adicionando...")
                        mytree.insert(val, 0)
                else:
                    print("a arvore está vazia insira um conjunto de elementos\n")

            if inp == 4:
                if inserted:
                    val = input("Insira a chave do nodo a ser removido: \n")
                    mytree.delete(val)
                else:
                    print("a arvore está vazia insira um conjunto de elementos\n")
    # Árvore B ---------------------------------------------------------------------------------------------------------
    elif chds == 4:
        inserted = False
        mytree = Btree(3)
        inp = int(0)
        while inp < 4:
            print("B-tree > \nEscolha uma opção: \n1 - Inserir\n2 - Imprimir\n3 - Pesquisar\n4 - Interromper execução\n")
            inp = int(input(""))

            if inp == 1:
                w = listwords(arquivo)
                for i in w:
                    ne = InNode(i, ordstring(i), occurences(i, arquivo))
                    mytree.insert(ne)
                    inserted = True

            if inp == 2:
                if inserted:
                   mytree.sortedlist()
                   print("\n")
                else:
                    print("a arvore está vazia insira um conjunto de elementos\n")

            '''if inp == 5:
                if inserted:
                    val = input("Insira a chave do nodo a ser removido: \n")
                    mytree.delete(raiz, val)
                else:
                    print("a arvore está vazia insira um conjunto de elementos\n")'''
            if inp == 3:
                if inserted:
                    val = input("Insira a chave do nodo para ser pesquisado: \n")
                    if mytree.search(val):
                        print("a chave está na árvore\n")
                    else:
                        print("a chave não foi encontrada, adicionando...")
                        mytree.insert(InNode(val, ordstring(val), 0))

                else:
                    print("a arvore está vazia insira um conjunto de elementos\n")
addtods()
