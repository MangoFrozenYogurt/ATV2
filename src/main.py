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
        while inp < 7:
            print("AVL-tree >\nEscolha uma opção: \n1 - Inserir\n2 - PreOrdem\n3 - InOrdem\n4 - PosOrdem\n"
                  "5 - Remover\n6 - Pesquisar\n7 - Interromper execução\n")
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
                    mytree.preorder(raiz)
                    print("\n")
                else:
                    print("a arvore está vazia insira um conjunto de elementos\n")

            if inp == 3:
                if inserted:
                    mytree.inorder(raiz)
                    print("\n")
                else:
                    print("a arvore está vazia insira um conjunto de elementos\n")
            if inp == 4:
                if inserted:
                    mytree.posorder(raiz)
                    print("\n")
                else:
                    print("a arvore está vazia insira um conjunto de elementos\n")
            if inp == 5:
                if inserted:
                    val = input("Insira a chave do nodo a ser removido: \n")
                    mytree.delete(raiz, val)
                else:
                    print("a arvore está vazia insira um conjunto de elementos\n")
            if inp == 6:
                if inserted:
                    val = input("Insira a chave do nodo para ser pesquisado: \n")
                    print("chave > ", mytree.search(raiz, val).key, "dado > ", mytree.search(raiz, val).data)

                else:
                    print("a arvore está vazia insira um conjunto de elementos\n")
    # Árvore Rubro-negra -----------------------------------------------------------------------------------------------
    elif chds == 3:
        inserted = False
        mytree = RBtree()
        inp = int(0)
        while inp < 5:
            print("RB-tree >\nEscolha uma opção:\n1 - Inserir\n2 - PreOrdem\n3 - Pesquisar\n4 - Remover\n"
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
                    mytree.preorder(mytree.root)
                    print("\n")
                else:
                    print("a arvore está vazia insira um conjunto de elementos\n")

            if inp == 3:
                if inserted:
                    val = input("Insira a chave do nodo para ser pesquisado: \n")
                    print("chave > ", mytree.search(val).key, "dado > ", mytree.search(val).data)

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
                    print(i, "\n")
                    ne = InNode(i, ordstring(i), occurences(i, arquivo))
                    mytree.insert(ne)
                    inserted = True

            if inp == 2:
                if inserted:
                   mytree.print_order()
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
                    mytree.search(val, ordstring(val))

                else:
                    print("a arvore está vazia insira um conjunto de elementos\n")
addtods()
