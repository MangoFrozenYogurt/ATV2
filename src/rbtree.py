from utils import *


class RBNode(object):

    def __init__(self, data, key, occ, color):
        self.data = data
        self.key = key
        self.occ = int(occ)
        self.right = None
        self.left = None
        self.parent = None
        self.red = color


class RBtree(object):
    def __init__(self):
        self.nil = RBNode(None, None, 0, False)
        self.root = self.nil

    def search(self, data):
        return self.search_helper(self.root, data)

    def search_helper(self, root, data):
        key = ordstring(data)
        if root == self.nil or data == root.data:
            return root
        elif key < root.key:
            return self.search_helper(root.left, data)
        else:
            return self.search_helper(root.right, data)

    def getminkeynode(self, root):
        if root is None or root.left is None:
            return root

        return self.getminkeynode(root.left)

    def getmaxkeynode(self, root):
        if root is None or root.right is None:
            return root
        return self.getmaxkeynode(root.right)

    def leftRotate(self, node):
        y = node.right
        node.right = y.left
        if y.left != self.nil:
            y.left.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.left = node
        node.parent = y
        return

    def rightRotate(self, node):
        y = node.left
        node.left = y.right
        if y.right != self.nil:
            y.right.parent = node

        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y

        y.right = node
        node.parent = y
        return

    def successor(self, node):
        if node.right != self.nil:
            return self.getminkeynode(node.right)

        y = node.parent
        while y != self.nil and node == y.right:
            node = y
            y = y.parent
        return y

    def predecessor(self, node):
        if node.left != self.nil:
            return self.getmaxkeynode(node.left)

        y = node.parent
        while y != self.nil and node == y.left:
            node = y
            y = y.parent
        return y

    def insert_fixup(self, node):
        while node.parent.red:
            if node.parent == node.parent.parent.right:
                # em busca do tio
                uncle = node.parent.parent.left
                if uncle.red:
                    # caso 3.1
                    uncle.red = False
                    node.parent.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # caso 3.2.2
                        node = node.parent
                        self.rightRotate(node)
                    # caso 3.2.1
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.leftRotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right
                if uncle.red:
                    # analogo ao caso 3.1
                    uncle.red = False
                    node.parent.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # caso analogo ao caso 3.2.2
                        node = node.parent
                        self.leftRotate(node)
                    node.parent.red = False
                    node.parent.parent.red = True

                    self.rightRotate(node.parent.parent)
            if node == self.root:
                break
        self.root.red = False

    def delete_fixup(self, node):
        while node != self.root and not node.red:
            if node == node.parent.left:
                s = node.parent.right
                if s.red:
                    # caso 3.1
                    s.red = False
                    node.parent.red = True
                    self.leftRotate(node.parent)
                    s = node.parent.right

                if not s.left.red and not s.right.red:
                    # caso 3.2
                    s.red = True
                    node = node.parent
                else:
                    if not s.right.red:
                        # caso 3.3
                        s.left.red = False
                        s.red = True
                        self.rightRotate(s)
                        s = node.parent.right

                    # caso 3.4
                    s.red = node.parent.red
                    node.parent.red = False
                    s.right.red = False
                    self.leftRotate(node.parent)
                    node = self.root
            else:
                s = node.parent.left
                if s.red:
                    # caso 3.1
                    s.red = False
                    node.parent.red = True
                    self.rightRotate(node.parent)
                    s = node.parent.left
                    if not s.right.red and not s.left.red:
                        # case 3.2
                        s.red = True
                        node = node.parent
                    else:
                        if not s.left.red:
                            # caso 3.3
                            s.right.red = False
                            s.red = True
                            self.leftRotate(s)
                            s = node.parent.left
                        # caso 3.4
                        s.red = node.parent.red
                        node.parent.red = False
                        s.left.red = False
                        self.rightRotate(node.parent)
                        node = self.root
        node.red = False

    def insert(self, data, occ):
        key = ordstring(data)
        node = RBNode(data, key, occ, True)
        node.parent = None
        node.left = self.nil
        node.right = self.nil

        y = None
        x = self.root

        while x != self.nil:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        # se o nó é uma raiz
        if node.parent is None:
            node.red = False
            return
        # se o avõ é nulo
        if node.parent.parent is None:
            return

        # resolver possiveis violações

        self.insert_fixup(node)

    def getroot(self):
        return self.root

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, data):
        self.delete_helper(self.root, data)

    def delete_helper(self, node, data):
        key = ordstring(data)
        z = self.nil
        while node != self.nil:
            if node.key == key and node.data == data:
                z = node

            if node.key <= key:
                node = node.right
            else:
                node = node.left

        if z == self.nil:
            print("nó não encontrado\n")
            return

        y = z

        y_original_color = y.red

        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.getminkeynode(z.right)
            y_original_color = y.red
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if not y_original_color:
            self.delete_fixup(x)

    def preorder(self, root):
        x = root
        if x == self.nil:
            return
        print("{0} ".format(x.key), "{0} ".format(x.data), end="")
        self.preorder(x.left)
        self.preorder(x.right)
