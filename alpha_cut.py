import numpy as np


class Node:
    def __init__(self, data=None, degree=None, next=None):
        self.data = data
        self.degree = degree
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # insertion method for the linked list
    def insert(self, data, degree):
        newNode = Node(data, degree)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # print method for the linked list
    def printLL(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next

    # Get membership degree of element x based on data structure
    def get_membership(self, x):
        current = self.head
        mem = 0.0
        while(current):
            if x in np.arange(current.data[0], current.data[1], 0.5).tolist():
                mem = current.degree
                break
            current = current.next
        return mem


LL = LinkedList()

L = list(map(float, input("Enter subset of relevant degree of membership[0,1]: ").split()))

print(L)


for l in reversed(L):
    inp = list(map(float, input("Enter alpha cut value for {}: ".format(l)).split()))
    if len(inp) == 1:
        inp.append(inp[0])
    LL.insert(inp, l)

LL.printLL()

while(True):
    x = input("Enter value of x(Enter x to exit): ")
    if x == 'x':
        break
    x = float(x)
    mem = LL.get_membership(x)
    print('Membership Degree of {} is '.format(x), mem)
