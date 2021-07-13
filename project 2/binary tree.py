class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.lc = None
        self.rc = None

    def set_lc(self, Node):
        if self.lc is None:
            self.lc = BinaryTree(Node)
        else:
            t = BinaryTree(Node)
            t.lc = self.lc
            self.lc = t

    def set_rc(self, Node):
        if self.rc is None:
            self.rc = BinaryTree(Node)
        else:
            t = BinaryTree(Node)
            t.rc = self.rc
            self.rc = t

    def get_rc(self):
        return self.rc

    def get_lc(self):
        return self.lc

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder_trav(self):
        print(self.getRootVal())
        if self.lc:
            self.lc.preorder_trav()
        if self.rc:
            self.rc.preorder_trav()

    def postorder_trav(self):
        if self.lc:
            self.lc.postorder_trav()
        if self.rc:
            self.rc.postorder_trav()
        print(self.getRootVal())

    def inorder_trav(self):
        if self.lc:
            self.lc.inorder_trav()
        print(self.getRootVal())
        if self.rc:
            self.rc.inorder_trav()


"""
Abbreviation key

lc : left child
rc = right child
"""

r = BinaryTree('a')
r.set_lc('b')
r.set_rc('c')
r.set_lc('d')
r.set_rc('e')
r.lc.set_rc('n')
r.rc.set_lc("m")
r.preorder_trav()
print('---------')
r.postorder_trav()
print('---------')
r.inorder_trav()

