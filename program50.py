class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = Node(data)

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end='->')
            temp = temp.next
        print(None)
    def count1(self):
        count=0
        temp = self.head
        while temp:
            count=count+1
            temp = temp.next
        print(count)
    def even(self):
        temp=self.head
        sum=0
        while temp:
            if temp.data%2==0:
                sum=sum+temp.data
            temp=temp.next
        print(sum)
    def prime(self):
        count=0
        temp=self.head
        while temp:
            for i in range(2,3):
                if temp.data%i==0:
                    count=count+1
            temp=temp.next
            print(count)

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.count1()
ll.even()
ll.prime()
ll.print_list()
