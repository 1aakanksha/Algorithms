import copy



class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList():
    def __init__(self):
        self.head=None
        self.Start=self.head

    def printlist(self):
        while self.head!= None:
            print(self.head.data)
            self.head=self.head.next

        self.head = self.Start

    def insert_begin(self,Node):
        Node.next=self.Start
        self.head=Node
        self.Start=self.head

    def insert_last(self,Node):
        while self.head.next!=None:
            self.head=self.head.next
        self.head.next=Node
        self.head = self.Start

    def insert_after_node(self,Node):
        while self.head.data!=Node.data:
            self.head = self.head.next
        self.head = self.head.next
        Node.next=self.head.next
        self.head.next=Node
        self.head = self.Start

    def delete_from_begin(self):
        self.head=self.head.next
        self.Start=self.head

    def delete_from_last(self):
        while self.head.next.next !=None:
            self.head=self.head.next
        self.head.next=None
        self.head=self.Start

    def delete_given_node(self,Node):
        while self.head.next.data!=Node.data:
            self.head=self.head.next
        self.head.next=self.head.next.next
        self.head=self.Start


    def create_list(self,arr):
        for i in range(len(arr)):
            if self.head is None:
                self.head=Node(arr[i])
                self.Start=self.head
                #print(self.head.data)

            else:
                self.head.next=Node(arr[i])
                self.head=self.head.next
                #print(self.head.data)


        self.head=self.Start

    def reverse_list(self):
        # this is not the best way to reverse a linked lisk

        if self.head is None:
            return None
        Next = copy.copy(self.head.next)
        self.head.next=None

        while Next != None:
            Current = copy.copy(self.head)

            self.head = copy.copy(Next)
            Next = self.head.next
            self.head.next = Current

    def nth_node_from_end(self,n):
        if self.head is None:
            return None
        self.reverse_list()


        while n>1:
            if self.head!=None:
                self.head=self.head.next
                n-=1
            else:
                print(-1)
                return
        if self.head is not None:
            print(self.head.data)
        else: print(-1)
        return

    def nth_node_from_end_without_reverse(self,n):
        if self.head is None:
            return None
        len=1
        while self.head.next!=None:
            self.head=self.head.next
            len+=1
        self.head=self.Start
        print(len)
        if n>len:
            print(-1)
            return
        else:
            while len-n>0:
                self.head=self.head.next
                n+=1

            print(self.head.data)





if __name__ =="__main__":
    
    h1=SinglyLinkedList()
    h2=Node("U")
    h3=Node("Son of a Bitch")

    #Add Nodes to list
    h1.head.next=h2
    h2.next=h3
    print("Add Nodes to list")
    h1.printlist()

    # Insert at Beginning
    h4=Node("_|_")
    h1.insert_begin(h4)
    print("Add Nodes to list")
    h1.printlist()

    # Insert at last
    h5=Node("MotherFucker")
    h1.insert_last(h5)
    print("Add Nodes to list")
    h1.printlist()

    #Insert after given node
    h6=Node("You")
    h1.insert_after_node(h2)
    print("Add Nodes to list")
    h1.printlist()

    #Deletion at Start
    h1.delete_from_begin()
    h1.printlist()
    print("Add Nodes to list")

    # Deletion at Start
    h1.delete_from_last()
    h1.printlist()
    
    
    # try creatinglist using array
    lis=SinglyLinkedList()
    array=[76,82,54,93]
    lis.create_list(array)
    #lis.reverse_list()
    lis.printlist()

    lis.nth_node_from_end_without_reverse(4)








