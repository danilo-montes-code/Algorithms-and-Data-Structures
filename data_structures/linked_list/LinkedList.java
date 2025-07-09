import java.lang.StringBuilder;

/**
 * Represents a Linked List data structure.
 * 
 * @author Danilo Montes
 */
class LinkedList {
    private Node head;

    /**
     * Represents a node in the Linked List.
     * 
     * @author Danilo Montes
     */
    private static class Node {
        int data;
        Node next;
        // Node prev;  // A Doubly-Linked List will have a pointer to the previous node as well

        Node(int data) {
            this.data = data;
            this.next = null;
        }
        Node(int data, Node next) {
            this.data = data;
            this.next = next;
        }
    }

    /**
     * Adds a new node with the specified data to the end of the Linked List.
     * 
     * @param data the data to be added to the Linked List
     */
    public void add(int data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
        } 
        else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    /**
     * Displays the contents of the Linked List.
     */
    public void display() {
        Node current = head;
        StringBuilder linkedListString = new StringBuilder();

        while (current != null) {
            linkedListString.append(current.data)
            if (current.next != null)
                linkedListString.append(" -> ");
            current = current.next;
        }

        System.out.println(linkedListString.toString().trim());
    }
}

class LinkedListDemo {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.add(10);
        list.add(20);
        list.add(30);
        list.display(); // Output: 10 20 30
    }
}