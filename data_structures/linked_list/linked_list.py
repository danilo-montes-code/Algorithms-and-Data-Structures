"""linked_list.py
A class that implements a singly linked list with basic operations.
"""

class LinkedList:
    """
    A class representing a singly linked list.
    
    Attributes
    ----------
    head : LinkedListNode
        The first node in the linked list.
    """
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None


    def append(self, data):
        """Append a new node with the given data to the end of the list."""
        new_node = LinkedListNode(data)

        if not self.head:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    
    def __str__(self):
        """Return a string representation of the linked list."""
        nodes = []
        current_node = self.head

        while current_node:
            nodes.append(str(current_node.data))
            current_node = current_node.next

        return " -> ".join(nodes)



class LinkedListNode:
    """A class representing a node in a linked list."""
    
    def __init__(
        self, 
        data, 
        next_node=None,
        # prev_node=None  # A Doubly-Linked List would have this attribute
    ):
        """Initialize the node with data and a pointer to the next node."""
        self.data = data
        self.next = next_node
        # self.prev = prev_node




def demonstrate_linked_lists():
    """Main function to demonstrate the linked list."""
    
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    print(linked_list)


if __name__ == "__main__":
    demonstrate_linked_lists()