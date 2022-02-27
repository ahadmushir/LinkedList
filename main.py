# Main

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            temp = self.head
            while self.head.next is not None:
                self.head = self.head.next
            self.head.next = Node(val)
            self.head = temp

        return self.head

    def __len__(self):
        count = 0
        temp = self.head
        if self.head is None:
            return count
        else:
            while self.head is not None:
                count += 1
                self.head = self.head.next
            self.head = temp
            return count

    def print(self):
        temp = self.head
        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next
        self.head = temp


def reverse_ll(LL):
    visited = []
    head = LL.head

    while head is not None:
        visited.append(head)
        head = head.next


    head = visited.pop()
    temp = head

    while visited:
        n = visited.pop()
        n.next = None
        head.next = n
        head = head.next
    head = temp
    return head



if __name__ == "__main__":
    LL = LinkedList()
    LL.insert(4)
    LL.insert(45)
    LL.insert(200)
    LL.insert(2)
    LL.print()
    print("The length of the LL is %s" % len(LL))

    # Printing Reversed LL
    newHead = reverse_ll(LL)
    while newHead is not None:
        print(newHead.data)
        newHead = newHead.next






