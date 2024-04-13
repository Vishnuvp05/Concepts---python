class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

#It is a type of Depth-First-Search where root node is visited and recursive traversal for left subtree and right subtree is done
#root node is visited before recursive left subtree and right subtree hence it is called pre order 
#it is mainly used for creating a copy of tree

def preordertraversal(node):
    if node is None:
        return 
    print(node.data,end=", ")
    preordertraversal(node.left)
    preordertraversal(node.right)

root=Node('R')
nodeA=Node('A')
nodeB=Node('B')
nodeC=Node('C')
nodeD=Node('D')
nodeE=Node('E')
nodeF=Node('F')
nodeG=Node('G')


root.left=nodeA
root.right=nodeB

nodeA.left=nodeC
nodeA.right=nodeD

nodeB.left=nodeE
nodeB.right=nodeF

nodeF.left=nodeG

preordertraversal(root)
