"""linked_list.py
A class that implements a singly linked list with basic operations.
"""

class LinkedListNode:
    """A class representing a node in a linked list."""
    
    def __init__(self, data, next_node=None):
        """Initialize the node with data and a pointer to the next node."""
        self.data = data
        self.next = next_node




def demonstrate_linked_lists():
    """Main function to demonstrate the linked list."""
    
    head = LinkedListNode(1, 
        next_node=LinkedListNode(2,
            next_node=LinkedListNode(3)
        )
    )

    current_node = head
    while current_node:
        print(current_node.data)
        current_node = current_node.next


if __name__ == "__main__":
    demonstrate_linked_lists()