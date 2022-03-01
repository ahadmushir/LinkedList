class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Stack:
    def __init__(self, node):
        n = Node(node)
        self.tail = n
        self.head = n

    def push(self, n):
        if self.head:

            n_node = Node(n)
            temp = self.head
            self.head.next = n_node
            self.head = self.head.next
            n_node.prev = temp

        else:
            n1 = Node(n)
            self.tail = n1
            self.head = n1

    def pop(self):
        if self.head is None and self.tail is None:
            print("No Value")

        if self.head == self.tail:
            temp = self.head
            self.tail = None
            self.head = None
            return temp
        elif self.head:
            res = self.head
            self.head = self.head.prev
            return res
        else:
            print("No Data, please push in the stack")


if __name__ == "__main__":

    ST = Stack(5)
    ST.push(10)
    ST.push(15)
    ST.push(20)

    ST.pop()
    ST.pop()
    ST.pop()
    ST.pop()
    ST.push(54)
    v = ST.pop()

    print(v.data)
