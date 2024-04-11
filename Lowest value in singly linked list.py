class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
def lowest_value(head):
    minval=head.data
    curr=head.next
    while curr:
        if curr.data<minval:
            minval=curr.data
        curr=curr.next

    return minval
        
node1=Node(4)
node2=Node(7)
node3=Node(8)
node4=Node(7)

node1.next=node2
node2.next=node3
node3.next=node4

print(lowest_value(node1))



