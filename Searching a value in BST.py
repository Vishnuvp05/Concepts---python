class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def serach(node,target):
    if node is None:
        return None
    elif target==node.data:
        return node
    elif node.data>target:
        return serach(node.left,target)
    else:
        return serach(node.right,target)
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

a=serach(root,14)
if a:
    print("Found")
else:
    print("Not found")