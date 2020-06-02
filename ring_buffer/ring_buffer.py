from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Need to check if ring buffer has enough capacity
        # If there is enough capacity:
        if self.storage.length < self.capacity:
            # Add item to end of buffer
            self.storage.add_to_tail(item)
            # Have to set our current to start at head since defaults to None
            self.current = self.storage.head

        # If the length has reached capacity:
        elif self.storage.length == self.capacity:
            self.current.value = item
            # If our current pointer is at the tail, move back to head
            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                # if not we can set item to next spot
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        item = self.storage.head
        # While our item is not None, prevents returning None values:
        while item:
            # Add to []
            list_buffer_contents.append(item.value)
            # Keep going through our storage
            item = item.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
