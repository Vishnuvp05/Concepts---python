class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
node1=Node(4)
node2=Node(7)
node3=Node(8)
node4=Node(7)

node1.next=node2
node1.prev=node4

node2.next=node3
node2.prev=node1

node3.next=node4
node3.prev=node2

node4.next=node1
node4.prev=node3

#forward
curr=node1
start_node=node1
print(curr.data,end="-->")
curr=curr.next

while curr!=start_node:
    print(curr.data,end="-->")
    curr=curr.next
print("Null")

curr=node4
start_node=node4
print(curr.data,end="-->")
curr=curr.prev

while curr!=start_node:
    print(curr.data,end="-->")
    curr=curr.prev

print("Null")

