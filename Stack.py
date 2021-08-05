# Stack data structure using python
# by aminu ahmadh Github@AminuAhmadh


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, number):
        self.stack.append(number)

    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            print('Nothing to pop')

    def peek(self):
        if len(self.stack)  > 0:
            print(self.stack[-1])
        else:
            print('Nothing to peek')

    def contain(self, element):
        if element in self.stack:
            return True
        return False


    