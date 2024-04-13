#Biinary tree can bbe started in an array starting with root node 'R' on index 0
#The rest of the tree can be built 

binary_tree_array=['R','A','B','C','D','E','F',None,None,None,None,None,None,'G']

def left_child_index(index):
    return 2*index+1
def right_child_index(index):
    return 2*index+2
def get_data(index):
    if 0 <= index and len(binary_tree_array):
        return  binary_tree_array[index]
    return None

#traversal 

def PreOrder(index):
    if index>=len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return [binary_tree_array[index]]+PreOrder(left_child_index(index))+PreOrder(right_child_index(index))

def InOrder(index):
    if index>=len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return InOrder(left_child_index(index))+[binary_tree_array[index]]+InOrder(right_child_index(index))

def PostOrder(index):
    if index>=len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return PostOrder(left_child_index(index))+PostOrder(right_child_index(index))+[binary_tree_array[index]]    
#let us access the element 'F' which is located in  right of root's right 

right_child=right_child_index(0)
right_of_right_child=right_child_index(right_child)
data=get_data(right_of_right_child)
print(data)

print("Pre-Order Traversal : ",PreOrder(0))
print("In-Order Traversal :",InOrder(0))
print("Post-Order Traversal : ",PostOrder(0))

