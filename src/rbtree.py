class RBtree:
    def __init__(self):
        self.root = None


class RBNode:

    def __init__(self):
        self.data = None
        self.key = None
        self.right = None
        self.left = None
        self.parent = None
        self.color = None

    def create(self):
        root = RBtree()

    def insert(self, key, data):
        node = RBNode()
        node.key = key
        node.data = data

