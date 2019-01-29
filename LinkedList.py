

class LinkedListNode(object):
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, val):
        node = LinkedListNode(val)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        self.count += 1

    def prepend(self, val):
        node = LinkedListNode(val)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

        self.count += 1

    def search(self, val):
        temp = self.head
        while temp.next is not None:
            if temp.data == val:
                return temp
            temp = temp.next
        return temp

    def delete(self, val):
        temp = self.head
        
        while temp.next is not None:
            if temp.data == val:
                return temp
            temp = temp.next
        return temp