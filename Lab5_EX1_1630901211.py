class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


    def __repr__(self):
        s = ""
        if self.left:
            s += str(self.left).replace("\n", "\n  ")
        s += "\n" + str(self.key)
        if self.right:
            s += str(self.right).replace("\n", "\n  ")
        return s
    def newchild(self):
        if self.right:
            right = self.right.newchild()
            if right[0] == -1:
                return right
            left = self.left.newchild()
            if left[0] == -1:
                return left
            if left[0] != right[0]:
                return [-1, right[1]]
            return [left[0]+1, left[1]]
        elif self.left:
            return [-1, self]
        return [0, self]

    def push(self,key):
        _, parent = self.newchild()
        if not parent.left:
            parent.left = Node(key)
        else:
            parent.right = Node(key)

    def delete(self, parent,key):
        if  parent is None:
            return  parent
        if key <  parent.key:
            parent.left = Node.delete(self, parent.left,key)
            return  parent
        elif (key> parent.key):
            parent.right = Node.delete(self, parent.right,key)
            return  parent
        if  parent.left and  parent.right is None:
            return None
        elif  parent.right is None:
            return  parent.left



tree = Node(50)
tree.push(25)
tree.push(75)
tree.push(30)
tree.push(60)
tree.push(40)
tree.push(35)
tree.push(70)
tree.push(90)
tree.push(15)
tree.push(45)
tree.push(27)
tree.push(55)
tree.push(85)
tree.push(100)
print(tree)


