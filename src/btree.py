from utils import ordenar
from hash import *


class InNode(object):
    def __init__(self, d, k, o):
        self.data = d
        self.key = k
        self.occ = o


class Bnode(object):
    def __init__(self, t):
        self.keys = []
        self.children = []
        self.leaf = True
        self.t = t

    def split(self, parent, node):
        # dividir o nó e reorganizar as chaves/filhos
        new_node = self.__class__(self.t)
        mid = self.size()//2
        splitval = self.keys[mid]
        parent.add_key(splitval)
        # adicionar chaves e filhos ao nó apropriado
        new_node.children = self.children[mid + 1:]
        self.children = self.children[:mid + 1]
        new_node.keys = self.keys[mid + 1:]
        self.keys = self.keys[:mid]

        # se o novo nó tem filhos, colocar ele como nó interno mudando o seu estado leaf
        if len(new_node.children) > 0:
            new_node.leaf = False

        parent.children = parent.add_child(new_node)

        if node.key < splitval.key:
            return self
        else:
            return new_node

    def isfull(self):
        return self.size == 2 * self.t - 1

    def size(self):
        return len(self.keys)

    def add_key(self, node):
        self.keys.append(node)
        self.keys = ordenar(self.keys)

    def add_child(self, node):
        i = len(self.children) - 1
        while i >= 0 and self.children[i].keys[0].key > node.keys[0].key:
            i -= 1
        return self.children[:i + 1] + [node] + self.children[i + 1:]


class Btree(object):
    def __init__(self, t):
        self.t = t
        if self.t <= 1:
            raise ValueError("A Árvore B precisa tem um valor de grau minimo maior ou igual a 2\n")
        self.root = Bnode(t)

    def insert(self, node):
        if node is None:
            print("node is none\n")
            return
        else:
            print(node.data)
            raiz = self.root

            if raiz.isfull():
                new_root = Bnode(self.t)
                new_root.children.append(self.root)
                new_root.leaf = False

                raiz = raiz.split(new_root, node)

                self.root = new_root

            while not raiz.leaf:
                i = raiz.size() - 1
                while i > 0 and node.key < raiz.keys[i].key:
                    i -= 1
                if node.key > raiz.keys[i].key:
                    i += 1

                next_ = raiz.children[i]
                if next_.isfull():
                    print("entrou aqui next\n")
                    raiz = next_.split(raiz, node)
                else:
                    raiz = next_

            # todos os nós cheios foram divididos, inserir nó
            print("entrou aqui\n")
            raiz.add_key(node)

    def search(self, data, tree=None):
        val = ordstring(data)
        if tree is None:
            tree = self.root
        for j in range(len(tree.keys)):
            if tree.keys[j].key == val and tree.keys[j].data:
                print("Está na árvore\n")
                return True
            elif tree.leaf:
                print("Não está na árvore\n")
                return False
            else:
                i = 0
                while i < tree.size() and val > tree.keys[i].key:
                    i += 1
                return self.search(data, tree.children[i])

    def print_order(self):
        this_level = [self.root]
        while this_level:
            next_level = []
            output = ""
            for node in this_level:
                if node.children:
                    next_level.extend(node.children)
                for i in node.keys:
                    output += "|" + str(i.data) + " " + str(i.occ) + "|\n"
            print(output)
            this_level = next_level
