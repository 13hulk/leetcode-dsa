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
        else:
            self.tail.next = _new_node

        self.tail = _new_node
        self.length += 1

        return True


if __name__ == "__main__":
    ll = LinkedList(4)
    ll.print_linked_list()

    ll.append(10)
    ll.print_linked_list()
