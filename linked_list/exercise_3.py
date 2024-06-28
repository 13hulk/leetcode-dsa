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
            print("LinkedList is empty!")
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
        print(f"Appending: {value}...")
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.length += 1

        print(f"Appended: {self.tail.value}")
        self.print_linked_list()
        print()
        return True

    def pop(self):
        print("Popping the last item...")

        if self.head is None:
            print("Nothing to pop!")
            print()
            return None

        elif self.head == self.tail:
            popped = self.tail
            self.head = None
            self.tail = None

        else:
            new_tail = self.head
            while new_tail.next != self.tail:
                new_tail = new_tail.next

            popped = new_tail.next
            self.tail = new_tail
            self.tail.next = None

        self.length -= 1

        print(f"Popped: {popped.value}")
        self.print_linked_list()
        print()
        return popped

    def prepend(self, value):
        print(f"Prepending: {value}...")

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

        print(f"Prepended: {self.head.value}")
        self.print_linked_list()
        print()
        return True

    def pop_first(self):
        print("Popping the first item...")

        if self.head is None:
            print("Nothing to pop!")
            return None

        elif self.head == self.tail:
            popped = self.head
            self.head = None
            self.tail = None

        else:
            popped = self.head
            self.head = self.head.next

        self.length -= 1

        print(f"Popped the first item: {popped.value}")
        self.print_linked_list()
        print()
        return popped


if __name__ == "__main__":
    print("--- Create a new LinkedList ---")
    ll = LinkedList(4)
    ll.print_linked_list()
    print()

    print("--- Append item ---")
    ll.append(10)
    ll.append(11)
    ll.append(12)
    # ll.append(13)
    # ll.append(14)
    # ll.append(15)

    print("--- Pop the last item ---")
    ll.pop()
    ll.pop()
    ll.pop()
    ll.pop()
    ll.pop()

    print("--- Prepend item ---")
    ll.prepend(13)
    ll.prepend(14)
    ll.prepend(15)
    ll.prepend(16)

    print("--- Pop the first item ---")
    ll.pop_first()
    ll.pop_first()
    ll.pop_first()
    ll.pop_first()
    ll.pop_first()
