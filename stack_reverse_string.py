#** LIFO ***
from collections import deque
#**** COMPLEXITY --> PUSH/POP == O(1) ****
#**** COMPLEXITY --> SEARCH ELEMENT BY VALUE O(n) ****

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
    
def reverse_string(string):
    stack = Stack() # class object
    # test = ''
    for letter in string:
        # CLALL FUNCTIONS OF STACK CLASS VIA THIS OBJECT
        stack.push(letter)
    reverse_string = ''
    while stack.size()!=0:
        reverse_string += stack.pop()
    return reverse_string
         


if __name__ == '__main__':
    print(reverse_string('My Name is Anika'))




# SECOND METHOD 
import collections
from collections import deque
stack = collections.deque()

def reverse_string(string):
    for letter in string:
        stack.append(letter)
    r_string =''
    while len(stack) != 0:
        r_string += stack.pop()
    return r_string
print('method 2: ',reverse_string('My Name is Anika'))


   
