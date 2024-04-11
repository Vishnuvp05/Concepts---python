class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        
node1=Node(4)
node2=Node(7)
node3=Node(8)
node4=Node(7)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node1

curr=node1
start_node=node1
print(curr.data,end="-->")
curr=curr.next

while curr!=start_node:
    print(curr.data,end="-->")
    curr=curr.next
print("Null")