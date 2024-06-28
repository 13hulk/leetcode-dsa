class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)

        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_linked_list(self):
        if self.head is None:
            print(
                "LinkedList: "
                + f"Head: {None}"
                + f" | Tail: {None}"
                + f" | Length: {ll.length}"
            )
            return

        print(
            "LinkedList: "
            + f"Head: {ll.head.value}"
            + f" | Tail: {ll.tail.value}"
            + f" | Length: {ll.length}"
        )

        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def append(self, value):
        print(f"\nAppending: {value}..")
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.length += 1

        self.print_linked_list()
        print(f"Append successful: {new_node.value}")
        return True

    def pop(self):
        print("\nPopping last item..")

        if self.head is None:
            raise ValueError("LinkedList is empty")

        elif self.head == self.tail:
            popped = self.tail
            self.tail = None
            self.head = None
            self.length = 0

        else:
            new_tail = self.head
            while new_tail.next != self.tail:
                new_tail = new_tail.next

            self.tail = new_tail
            self.tail.next = None
            self.length -= 1

            popped = new_tail

        self.print_linked_list()
        print(f"Pop successful: {popped.value}")
        return popped.value


if __name__ == "__main__":
    ll = LinkedList(4)
    ll.print_linked_list()

    ll.append(10)
    ll.append(11)
    ll.append(12)
    # ll.append(13)
    # ll.append(14)
    # ll.append(15)

    ll.pop()
    ll.pop()
    ll.pop()
    ll.pop()
    ll.pop()
