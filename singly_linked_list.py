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
        print('lls: ',llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        print('count: ',count)
        return count
    
    def index_wise_insert(self,data,index):
        # insert 3 at 2 in 1-->2-->4
        # insert the current head in curr, and iterate all element of lls one by one.[1,2,4]
        # if current node index-1 = given index,
           # create a new node with the given data and set the current next element to this new node's next. Node(3,pointer at 4) at 2nd index
        # set this new node as current node's next
        # else upadte curr with curr.next
        # update index count +=1

        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        curr = self.head
        count = 0
        while curr:
            if count == index-1:
                node = Node(data,curr.next)
                curr.next = node
                break
            curr = curr.next
            count+=1

    def index_wise_remove(self,index):
        # remove index 2 from 1-->2-->4
        # insert the current head in curr, and iterate all element of lls one by one.[1,2,4]
        # if current node index-1 = given index,
        # set the next node of the given node as the next node of current node
        # else upadte curr with curr.next
        # update index count +=1

        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        curr = self.head
        count = 0
        while curr:
            if count == index-1:
                curr.next = curr.next.next
                break
            curr = curr.next
            count+=1
            
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_the_end(data)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_the_beginning(1)
    ll.insert_at_the_beginning(2)
    ll.insert_at_the_end(3)
    ll.index_wise_insert(4, 2)
    # ll.index_wise_remove(2)
    # ll.insert_values(["banana","mango","grapes","orange"])
    ll.get_length()
    ll.print()
