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
        if len(self.elem) == 4:
            self.isFull = True


class Hash(object):

    def __init__(self, tam):
        self.listElem = []
        for i in range(tam):
            self.listElem.append(Colection())

    def function(self, key, tam, i):
            return int((key + i) % tam)

    def insert(self, node):
        pos = self.function(node.key, len(self.listElem), 0)
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

    def search(self, key):
        found = False
        j = int(0)
        while not found:
            pos = self.function(key, len(self.listElem), j)
            for i in range(len(self.listElem[pos].elem)):
                if self.listElem[pos].elem[i].key == key:
                    print("hashelem: chave > ", self.listElem[pos].elem[i].data, " ocorrencia > ",
                          self.listElem[pos].elem[i].occ)
                    found = True
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