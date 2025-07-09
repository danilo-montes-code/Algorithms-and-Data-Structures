# Linked List
A Linked List is a chain of nodes, each consisting of the data to store and a reference to the next node in the chain.
The first node is called the head, and Linked Lists are usually referenced by passing around the reference where needed.
You can also implement two classes, one for the nodes of the Linked List, to handle data storage and `.next` references, and one for the Linked List itself, to handle operations on the list.


## Traversing the Data
To traverse a Linked List, initialize a pointer to the `head` node, called the `current` node.
To iterate to the next node, set the `current` variable to `current.next`.
This preserves the chain of the Linked List, since using the `head` of the list would destroy each `.next` reference.
Repeat this until `current` is a null pointer.


## Variations
* Doubly-Linked List - A Linked List with nodes that have a reference to the previous node in the chain also stored within