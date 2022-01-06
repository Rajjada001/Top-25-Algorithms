'''
This is basically to check to check whether a cycle exists or not
'''

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        NewNode = Node(data,self.head)
        if self.head == None:
            self.head = NewNode
            return self.head
        else:
            itr = self.head
            while itr.next:
                itr = itr.next

            itr.next = NewNode
            NewNode.next = None
            return NewNode

    def printList(self):
        # base case
        if self.head == None:
            print("LinkedList is empty")
        else:
            itr = self.head
            concat = ''
            while itr:
                concat += str(itr.data)+'->'
                itr = itr.next
            
            print(concat)

    
    def detectLoop(self):
            low=high=self.head
            while(low and high and high.next):
                low = low.next
                high = high.next.next
                # print(low.data,high.data,sep=" ")
                if low==high:
                    return True
            return False
    
    def removeLoop(self):
            low=high=self.head
            prev = None
            while(low and high and high.next):
                low = low.next
                prev = high.next
                high = high.next.next
                print(low.data,high.data,sep=" ")
                if low == high:
                    low = self.head

                    if(low == high):
                        prev.next = None

                    else:
                        while(low.next != high.next):
                            low = low.next
                            high = high.next
                        high.next = None
                        print("Removed")
                    
            return prev.data


if __name__ == "__main__":
    list1 = LinkedList()
    list1.insert_at_end(1)
    list1.insert_at_end(2)
    list1.insert_at_end(3)
    list1.insert_at_end(4)
    list1.insert_at_end(5)
    list1.insert_at_end(2)
    list1.printList()
    list1.head.next.next.next = list1.head
    print(list1.detectLoop())
    print(list1.removeLoop())
    list1.printList()
    print(list1.detectLoop())
    
