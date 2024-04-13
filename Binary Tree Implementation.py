class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

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

print(root.left.right.data)
