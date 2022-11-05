## FIFO *********
## USED IN MEMORY BUFFER

import collections
from collections import deque

#** METHOD ONE **
class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]

def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print("   ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()


if __name__ == '__main__':
    produce_binary_numbers(10)

#*** METHOD TWO **
binary_queue = collections.deque()
binary_queue.appendleft('1')
def print_binary(n):
    for i in range(n):
        front = binary_queue[-1]
        print(' ',front)
        binary_queue.appendleft(front+'0')
        binary_queue.appendleft(front+'1')
        if len(binary_queue) != 0:
            binary_queue.pop()
        else:
            print('Queue is empty')    

print_binary(10)
