from utils import *


class Node(object):

    def __init__(self):
        self.data = None
        self.key = int(0)
        self.occ = int(0)

    def create(self, data, key, occ):
        self.data = data
        self.key = int(key)
        self.occ = int(occ)


class Colection(object):

    def __init__(self):
        self.elem = [Node()]
        self.isFull = bool(False)

    def full(self):
        if len(self.elem) == 5:
            self.isFull = True


class Hash(object):

    def __init__(self, tam):
        self.listElem = []
        for i in range(tam):
            self.listElem.append(Colection())

    def allfull(self):
        j = int(0)
        for i in range(len(self.listElem)):
            if self.listElem[i].isFull:
                j += 1

        if j == len(self.listElem):
            return True
        else:
            return False

    def function(self, key, tam, i):
            return int((key + i) % tam)

    def insert(self, node):
        pos = self.function(node.key, len(self.listElem), 0)
        if not self.allfull():
            if self.listElem[pos].isFull is False:
                self.listElem[pos].elem.append(node)
                self.listElem[pos].full()
            else:
                i = int(0)
                while self.listElem[pos].isFull:
                    i += 1
                    pos = self.function(node.key, len(self.listElem), i)
                self.listElem[pos].elem.append(node)
                self.listElem[pos].full()
        else:
            print("não há mais espaço na tabela para adicionar o elemento")

    def search(self, key, data):
        found = False
        j = int(0)
        while not found:
            pos = self.function(key, len(self.listElem), j)
            for i in range(len(self.listElem[pos].elem)):
                if self.listElem[pos].elem[i].key == key and self.listElem[pos].elem[i].data == data:
                    self.listElem[pos].elem[i].occ += 1
                    print("hashelem: chave > ", self.listElem[pos].elem[i].data, " ocorrencia > ",
                          self.listElem[pos].elem[i].occ)
                    found = True
                elif j >= 3 and not found:
                    print("chave não encontrada, adicionando à tabela...")
                    nw = Node()
                    nw.create(data, ordstring(data), nw.occ + 1)
                    return self.insert(nw)
            j += 1

        pos = self.function(key, len(self.listElem), j - 1)
        return self.listElem[pos].elem[i].key

    def printall(self):
        print("\n")
        for i in range(len(self.listElem)):
            print("# pos: ", i, "-----------------------")
            for j in range(len(self.listElem[i].elem)):
                if self.listElem[i].elem[j].data is not None: print("chave: ", self.listElem[i].elem[j].data,
                                                                    "ocorrencia: ", self.listElem[i].elem[j].occ)

        print("\n")

    def remove(self, key):
        found = False
        i = int(0)
        j = int(0)
        while not found:
            pos = self.function(key, len(self.listElem), i)
            for j in range(len(self.listElem[pos].elem)):
                if self.listElem[pos].elem[j].key == key:
                    found = True
                    del self.listElem[pos].elem[j]
                    return
                elif j == len(self.listElem[pos].elem) and not found:
                    i += 1
                    break
                elif i > len(self.listElem):
                    print("elemento não encontrado")
                    return