class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1

def get_height(node):
    if node is None:
        return 0
    return node.height

def get_balance(node):
    if node is None:
        return 0
    return get_height(node.left)-get_height(node.right)

def rightrotae(y):
    x=y.left
    z=x.right
    x.right=y
    y.left=z

    y.height=1+max(get_height(y.left),get_height(y.right))
    x.height=1+max(get_height(x.left),get_height(x.right))
    return x

def leftrotate(y):
    x=y.right
    z=x.left
    x.left=y
    y.right=z

    x.height=1+max(get_height(x.left),(x.right))
    y.height=1+max(get_height(y.left),(y.right))

    return x
def insertnode(node,data):
    if node is None:
        return TreeNode(data)
    if data<node.data:
        node.left=insertnode(node.left,data)
    elif data>node.data:
        node.right=insertnode(node.right,data)
    
    node.height=1+max(get_height(node.left),get_height(node.right))
    balance=get_balance(node)

    #LL
    if balance>1 and data<node.left.data:
        return rightrotae(node)
    
    if balance<-1 and data>node.left.data:
        return leftrotate(node)
    
    if balance>1 and data>node.left.data:
        node.left=leftrotate(node.left)
        return rightrotae(node)
    if balance<-1 and data<node.left.data:
        node.right=rightrotae(node.right)
        return leftrotate(node)
    return node
    

def inordeeTraversal(node):
    if node is None:
        return 
    inordeeTraversal(node.left)
    print(node.data,end=", ")
    inordeeTraversal(node.right)

root=None
letters=['C','B','E','A','D','H','G','F']
for letter in letters :
    root=insertnode(root,letter)
    
inordeeTraversal(root)
    



