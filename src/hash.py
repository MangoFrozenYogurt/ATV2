class Node(object):

    def __init__(self):
        self.data = None
        self.key = int(0)

    def create(self, data, key):
        self.data = data
        self.key = int(key)


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
        pos = self.function(key, len(self.listElem), 0)
        for i in range(1, len(self.listElem[pos].elem)):
            print("hashelem: chave > ", self.listElem[pos].elem[0].key, " dado > ", self.listElem[pos].elem[i].data)

    def printall(self):
        for i in range(len(self.listElem)):
            print("# pos: ", i, "-----------------------")
            for j in range(len(self.listElem[i].elem)):
                if self.listElem[i].elem[j].data is not None: print("chave: ", self.listElem[i].elem[j].key, "dado: ", self.listElem[i].elem[j].data)

    def remove(self, key, data):
        found = False
        i = int(0)
        j = int(0)
        while not found:
            pos = pos = self.function(key, len(self.listElem), i)
            for j in range(len(self.listElem[pos].elem)):
                if self.listElem[pos].elem[j].key == key and self.listElem[pos].elem[j].data == data:
                    found = True
                    del self.listElem[pos].elem[j]
                    return
                elif j == len(self.listElem[pos].elem) and not found:
                    i += 1
                    break
                elif i > len(self.listElem):
                    print("elemento não encontrado")
                    return