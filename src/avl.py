# Arvore AVL


class AVLNode(object):
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):

    def createnode(self, key, data):
        return AVLNode(key, data)

    def getheight(self, root):
        if not root:
            return 0
        return root.height

    def rightRotate(self, k2):
        k1 = k2.left
        k2.left = k1.right
        k1.right = k2
        k2.height = int(1 + max(self.getheight(k2.left), self.getheight(k2.right)))
        k1.height = int(1 + max(self.getheight(k1.left), self.getheight(k1.right)))
        return k1

    def leftRotate(self, k2):
        k1 = k2.right
        k2.right = k1.left
        k1.left = k2
        k2.height = int(1 + max(self.getheight(k2.left), self.getheight(k2.right)))
        k1.height = int(1 + max(self.getheight(k1.left), self.getheight(k1.right)))
        return k1

    def doubleRight(self, k3):
        k3.left = self.leftRotate(k3.left)
        return self.rightRotate(k3)

    def doubleLeft(self, k3):
        k3.right = self.rightRotate(k3)
        return self.leftRotate(k3)

    def search(self, tree, node):
        if node.key is None:
            return AVLTree()

        if node.key == tree.key:
            return node
        elif node.key < tree.key:
            return self.search(tree, node.left)
        else:
            return self.search(tree, node.right)

    def insert(self, root, key, data):
        # passo 1
        if not root:
            return AVLNode(key, data)
        elif key < root.key:
            root.left = self.insert(root.left, key, data)
        else:
            root.right = self.insert(root.right, key, data)
        # passo 2 atualizando a altura do nó anterior
        root.height = 1 + max(self.getheight(root.left), self.getheight(root.right))
        # passo 3 determinando o balanceamento
        balance = self.balance(root)
        # passo 4 se o nó está desbalanceado
        # caso 1: esquerda esquerda
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)
        # caso 2: dir dir
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)
        # caso 3: esq dir
        if balance > 1 and key > root.left.key:
            return self.doubleRight(root)
        # caso 4: dir esq
        if balance < -1 and key < root.right.key:
            return self.doubleLeft(root)

        return root

    def delete(self, root, key):
        # passo 1 remoção em arvore binaria de busca
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                aux = root.right
                root = None
                return aux
            elif root.right is None:
                aux = root.left
                root = None
                return aux

            aux = self.getminkeynode(root.right)
            root.key = aux.key
            root.right = self.delete(root.right, aux.key)

        # se a arvore só tem a raiz

        if root is None:
            return root

        # passo 2 atualizar a altura do nodo antecessor

        root.height = int(1 + max(self.getheight(root.left), self.getheight(root.right)))

        # passo 3 pegar o fator de balanciamento

        balance = self.getbalance(root)

        # passo 4 se o nodo está balanceado
        # testar os 4 casos

        # caso 1 - desbalanceada à esquerda > rotação simples à direita
        if balance > 1 and self.getbalance(root.left) >= 0:
            return self.rightRotate(root)
        # caso 2 - desbalanceada à direita > rotação simples à esquerda
        if balance < -1 and self.getbalance(root.right) <= 0:
            return self.leftRotate(root)
        # caso 3 - rotação dupla à direita
        if balance > 1 and self.getbalance(root.left) < 0:
            return self.doubleRight(root)
        # caso 4 - rotação dupla à esquerda
        if balance < -1 and self.getbalance(root.right) > 0:
            return self.doubleLeft(root)

        return root

    def getminkeynode(self, root):
        if root is None or root.left is None:
            return root

        return self.getminkeynode(root.left)

    def balance(self, root):
        if not root:
            return 0
        return int(self.getheight(root.left) - self.getheight(root.right))

    def getbalance(self, root):
        if not root:
            return 0
        return int(self.getheight(root.left) - self.getheight(root.right))

    def preorder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if not root:
            return
        self.preorder(root.left)
        print("{0} ".format(root.key), end="")
        self.preorder(root.right)