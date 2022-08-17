class Stack:
    length = 0
    top = None

    class Node:
        def __init__(self, argPrevElement, argValue):
            self.prevElement = argPrevElement
            self.value = argValue

    def input(self, argLength):
        val = int(input())
        prvElement = self.Node(None, val)
        i = 0
        while i < argLength:
            val = int(input())
            curElement = self.Node(prvElement, val)
            prvElement = curElement
            self.top = curElement
            i += 1
        self.length = i + 1

    def output(self):
        tmp = self.top
        while tmp != None:
            print(tmp.value)
            tmp = tmp.prevElement

    def append(self, argValue):
        newElement = self.Node(self.top, argValue)
        self.top = newElement
        self.length += 1

    def remove(self):
        if self.top != None:
            del self.top
            self.length -= 1

    def __getitem__(self, argKey):
        i = self.length - 1
        tmp = self.top
        if argKey <= i:
            while i != argKey:
                tmp = tmp.prevElement
                i -= 1
            return tmp.value
        raise KeyError






