class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.child = []
        self.pare = []
        self.sibl = []
        self.leaves = []


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

    def _findMin(self, parent):
        if self.left:
            return self.left._findMin(self)
        else:
            return [parent, self]
    def delete(self, key):

        if self.key == key:
            if self.right and self.left:
                [ps, su] = self.right._findMin(self)
                if ps.left == su:
                    ps.left = su.right
                else:
                    ps.right = su.right


                su.left = self.left
                su.right = self.right
                return su
            else:
                if self.left:
                    return self.left
                else:
                    return self.right
        else:
            if self.key > key:
                if self.left:
                    self.left = self.left.delete(key)
            else:
                if self.right:
                    self.left = self.right.delete(key)
        return self

    def Height(self,Root):
        if Root == None:
            return 0
        left = Node.Height(self,Root.left)
        right = Node.Height(self,Root.right)
        return max(left,right) + 1
    def Childs (self,Root):
        if Root == None:
            return 0
        if Root.left == None and Root.right != None:
            self.child.append(Root.right.key)
        elif Root.left !=None and  Root.right == None:
            self.child.append(Root.left.key)
            self.child.append(Root.right.key)
        Node.Childs(self,Root.left)
        Node.Childs(self, Root.right)
        return self.child
    def Parent(self,Root):
        if Root == None:
            return 0
        if Root.left != None or Root.right != None:
            self.pare.append(Root.key)
        Node.Parent(self,Root.left)
        Node.Parent(self,Root.right)
        return self.pare
    def leave(self,Root):
        if Root == None:
            return 0
        if Root.left == None and Root.right == None:
            self.leaves.append(Root.key)
        Node.leave(self,Root.left)
        Node.leave(self, Root.right)
        return self.leaves

    def Sibling(self,Root):
        if Root == None:
            return 0
        if Root.left != None and Root.right != None:
            self.sibl.append(Root.left.key)
            self.sibl.append(Root.right.key)
        Node.leave(self,Root.left)
        Node.leave(self,Root.right)
        return self.sibl

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

print("BINARY TREE :")
print(tree)
print("==========================")
tree.delete(75)#ลบไม่ได้
tree.delete(30)#ลบได้
tree.delete(35)#ลบไม่ได้
print("BINARY TREE DELETE NODE")
print(tree)#พอลบแล้วBinary Tree ออกมาเพี้ยนเห็นได้จากการนำ100 มาเป็นchildของ2 ตัว

print("==========================")
print ("Height = : ",tree.Height(tree))#ค่าออกมาผิดเนื่องจากเอาค่ามาจากBinary Treeที่printออกมาหลังจากใช้function delete
print ("Child = : ",tree.Childs(tree))#ค่าออกมาผิดเนื่องจากเอาค่ามาจากBinary Treeที่printออกมาหลังจากใช้function delete
print ("Sibling = : ",tree.Sibling(tree))#ค่าออกมาผิดเนื่องจากเอาค่ามาจากBinary Treeที่printออกมาหลังจากใช้function delete
print ("Parent = : ",tree.Parent(tree))#ค่าออกมาผิดเนื่องจากเอาค่ามาจากBinary Treeที่printออกมาหลังจากใช้function delete
print ("Leaves = : ",tree.leave(tree))#ค่าออกมาผิดเนื่องจากเอาค่ามาจากBinary Treeที่printออกมาหลังจากใช้function delete










