class Node:
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_the_beginning(self,data):
        if self.head is None:
            node = Node(data,self.head,None)
            self.head = node
        else:
            node = Node(data,self.head,None)
            self.head.prev = node
            self.head = node

    def insert_at_the_end(self,data):
        if self.head is None:
            node = Node(data,None,None) # next is None cz we are adding the last element 
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            node = Node(data,None,curr)
            curr.next = node

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_specific_index(self,data,index):
        if index<0 or index>self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.insert_at_the_beginning(data)
            return
        else:
            count = 0
            curr = self.head

            while curr:
                if count == index-1:
                    node = Node(data,curr.next,curr)
                    curr.next = node
                    if node.next:
                        curr.next.prev = node
                    break
                curr = curr.next
                count += 1

    
    def remove_at_specific_index(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def print_forward_element(self):
        # note: we don't need any data/next/prev arguments here cz we are not creating any new node, we are just iterrating through the
            # existing linked list
        if self.head is None:
            print('Linked list is empty')
            return
        curr = self.head
        llstr = ''
        while curr:
            llstr += str(curr.data)+'-->' if curr.next else str(curr.data)
            curr = curr.next
        print('forward llstr: ', llstr)


    def get_last_node(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr

    def print_backward_element(self):
        if self.head is None:
            print('Linked List is Empty')
            return 
        last_node = self.get_last_node()
        llstr = ''
        while last_node:
            llstr += str(last_node.data) + '-->'
            last_node = last_node.prev
        print('print_backward_element: ',llstr)

    

if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_at_the_beginning(1)
    ll.insert_at_the_beginning(2)
    ll.insert_at_the_end(3)
    ll.insert_at_the_end(4)
    ll.get_length()
    ll.insert_at_specific_index(33, 2)
    # ll.remove_at_specific_index(2)
    ll.print_forward_element()
    ll.print_backward_element()
            