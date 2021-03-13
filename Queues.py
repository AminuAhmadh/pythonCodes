from collections import deque


class Queue:
    def __init__(self) -> None:
        self.queue = deque()

    # used to add an element to a queue
    def enqueue(self, element):
        self.queue.append(element)

    # used to dequeue/remove an element from a queue
    def dequeue(self):
        if len(self.queue) > 0:
            print(self.queue.popleft()) 
        else:
            print('nothing to dequeue')
