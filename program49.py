class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)

temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print(None)
