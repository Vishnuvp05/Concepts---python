class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
#In In-Order traversal recursive In-Order Traversal of left subtree is done and root node is visited and recursive In-Order Traversal of right subtree is done
#It is mainly used for Binary Search Tree where it returns values in Ascending order 
#The node is visited after in-order traversal of left subtree and before in-order traversal of right subtree hence it is called in-order traversal





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

def InorderTraversal(node):
    if node is None:
        return 
    InorderTraversal(node.left)
    print(node.data,end=", ")
    InorderTraversal(node.right)


InorderTraversal(root)

