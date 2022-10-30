class Node:
    # each node consists of two element value of the node and pointer to the next element
    # creating node (data,next memory position of next element)
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    # create and empty head
    def __init__(self):
        self.head = None

    def insert_at_the_beginning(self,data):
        # linked_list has 2 components data and pointer(the position of the second emement)
        # insert(2)---> create node(2,None)--> head = (2,None) --> there's no next element
        # insert(3)--> head.data = 3 (node(3,pointer for the element with val 2))--> next= (2,None)
        # insert(4)--> head.data = 4 (node(4,pointer for the element with val 3))--> next= (node(3,pointer for the element with val 2))
                                    # -->next = (2,None)
        # after building the linked list take each node data (1st header = (4,pointer...3)) then update the variable with next el = (3,pointer..2)
        # result 4-->3-->2
        
        node = Node(data,self.head)
        self.head = node
        if self.head is None:
            print("Linked list is empty")
            return
        # else:
        itr = self.head  # represent each element of the linked list one by one
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_the_beginning(1)
    ll.insert_at_the_beginning(2)