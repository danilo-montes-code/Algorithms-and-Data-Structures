# Linked List
A Linked List is a chain of nodes, each consisting of the data to store and a reference to the next node in the chain.
The first node is called the head, and Linked Lists are usually referenced by passing around the reference where needed.
You can also implement two classes, one for the nodes of the Linked List, to handle data storage and `.next` references, and one for the Linked List itself, to handle operations on the list.

<div align="center">
    <img src="linked-list.svg"/>
    <br/>
    <em>By Vectorization: <a href="//commons.wikimedia.org/w/index.php?title=User:Lasindi&amp;action=edit&amp;redlink=1" class="new" title="User:Lasindi (page does not exist)">Lasindi</a> - Own work based on: <a href="//commons.wikimedia.org/wiki/File:Singly_linked_list.png" title="File:Singly linked list.png">Singly linked list.png</a>&nbsp;by <a href="//commons.wikimedia.org/wiki/User:Dcoetzee" title="User:Dcoetzee">Derrick Coetzee</a>, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=2245162">Link</a></em>
</div>


## Traversing the Data
To traverse a Linked List, initialize a pointer to the `head` node, called the `current` node.
To iterate to the next node, set the `current` variable to `current.next`.
This preserves the chain of the Linked List, since using the `head` of the list would destroy each `.next` reference.
Repeat this until `current` is a null pointer.


## Variations
* Doubly-Linked List - A Linked List with nodes that have a reference to the previous node in the chain also stored within