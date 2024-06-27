class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        _new_node = Node(value)

        self.head = _new_node
        self.tail = _new_node
        self.length = 1

    def print_linked_list(self):
        print(
            "\nLinkedList"
            + f"\nHead: {ll.head.value}"
            + f" | Tail: {ll.tail.value}"
            + f" | Length: {ll.length}"
        )

        _temp = self.head
        while _temp is not None:
            print(_temp.value)
            _temp = _temp.next

    def append(self, value):
        _new_node = Node(value)

        if self.head is None:
            self.head = _new_node
            self.tail = _new_node
        else:
            self.tail.next = _new_node
            self.tail = _new_node

        self.length += 1

        return True

    def pop(self):
        if self.length == 0:
            return None

        _temp = self.head
        _new_tail = _temp

        while _temp.next is not None:
            _new_tail = _temp
            _temp = _temp.next

        self.tail = _new_tail
        _new_tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return _temp.value


if __name__ == "__main__":
    ll = LinkedList(4)
    ll.print_linked_list()

    ll.append(10)
    ll.append(11)
    ll.append(12)
    ll.append(13)
    ll.append(14)
    ll.append(15)
    ll.print_linked_list()

    gll.pop()
    ll.print_linked_list()
