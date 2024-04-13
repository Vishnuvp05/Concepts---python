class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
#start at root node
#compare each node is value lower? go left 
#is value higher ? go right
#continue to compare nodes with the new value until there is no right or left to compare with . That is where the new node is inserted 
#inserting nodes as described above means that an inserted node will always become a new leaf node 
#all nodes in BST are unique so in case we find the same value as the one we want to insert we do nothing 

def insert(node,data):
    if node is None:
        return TreeNode(data)
    else:
        if data<node.data:
            node.left=insert(node.left,data)
        elif data>node.data:
            node.right=insert(node.right,data)
    return node


def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)
        


root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

# Inserting new value into the BST
insert(root, 10)

# Traverse
inOrderTraversal(root)
