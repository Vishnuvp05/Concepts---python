class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

def min_val(node):
    curr=node
    while curr.left:
        curr=curr.left
    return curr.data

def max_val(node):
    curr=node
    while curr.right:
        curr=curr.right
    return curr.data
        


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


# Traverse
inOrderTraversal(root)
a=min_val(root)
b=max_val(root)

print("lowest value is : " ,a)
print("Highest value is : " ,b)