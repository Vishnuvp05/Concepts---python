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
node2.prev=node1
node2.next=node3
node3.prev=node2
node3.next=node4
node4.prev=node3

#travese forward
curr=node1
while curr:
    print(curr.data,end="-->")
    curr=curr.next
print("Null")

#traverse backward
curr=node4
while curr:
    print(curr.data,end="-->")
    curr=curr.prev
print("Null")