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

#To delete a node our function mmust first search for bst to find it 
#after node is found there are three different cases 
#if node is leaf node remove it by remove by removing the link to it
#If the node has only one child node.connect parent node of the node you want to remove to the child node
#If the node has both right and left child nodes.Find nodes in-order successor change values with that node and delete it 


def delete(node,data):
    if node is None:
        return None
    elif data<node.data:
        node.left=delete(node.left,data)
    elif data>node.data:
        node.right=delete(node.right,data)
    else:
        #node with only one child or no child 
        if node.left is None:
            temp=node.data
            node=None
            return node
        elif node.right is None:
            temp=node.right
            node=None
            return node
        
        #node with two child lets find the in-order successor 
        node.data=min_val((node.right).data)
        node.right=delete(node.right,node.data)

    return node




        


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
delete(root,14)
inOrderTraversal(root)
