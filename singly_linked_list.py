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
        
    def insert_at_the_end(self,data):
     # first get the whole linked list
     # take one element one at a time and if  the next element to it exits then,put that next element in itr variable(start at the head)
     # when the last element is found and kept inside the itr last line will execute
                 #--> which is

        if self.head is None:
            self.head = Node(data,None) # since we are inserting at the end that's why we will create a lls with just 1 node with given data
            # print('Linked List is empty')
            # return
        else:
            itr = self.head
            llstr = ''
            while itr.next:
                itr = itr.next
                
            itr.next = Node(data,None)

    def print(self):
        # PRINT_RESULTS FOR INSERT AT THE BEGINNING AND END METHOD
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head # represent each element of the linked list one by one
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print('insert_at_the_end: ',llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        print('count: ',count)
        return count
       

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_the_beginning(1)
    ll.insert_at_the_beginning(2)
    ll.insert_at_the_end(3)
    ll.print()
    ll.get_length()