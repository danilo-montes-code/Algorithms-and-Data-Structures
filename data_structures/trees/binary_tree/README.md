# Binary Tree
A Binary Tree is a variation of a Tree in which each node can have at most 2 children nodes.
This is the most common form of Tree.

<div align="center">
    <img src="binary-tree.svg" height="500"/>
    <br/>
    <em>By <a href="//commons.wikimedia.org/w/index.php?title=User:Radke7CB&amp;action=edit&amp;redlink=1" class="new" title="User:Radke7CB (page does not exist)">Radke7CB</a> - <span class="int-own-work" lang="en">Own work</span>, <a href="https://creativecommons.org/licenses/by-sa/4.0" title="Creative Commons Attribution-Share Alike 4.0">CC BY-SA 4.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=114167467">Link</a></em>
</div>



## Traversing the Data
To traverse a Binary Tree, given its non-linear structure, there are multiple approaches.

The breadth-first search is the same as the general Tree's breadth-first search, starting at the root and adding its children to the end of a queue.

The depth-first search has more specific variations. The depth-first search can come in three forms: Preorder, Inorder, and Postorder traversal. They differ in where the data held in the node being handled in the function call is processed.
* Preorder - 1. process the current node, 2. recursively traverse the left subtree, 3. recursively traverse the right subtree
* Inorder - 1. recursively traverse the left subtree, 2. process the current node, 3. recursively traverse the right subtree
* Postorder - 1. recursively traverse the left subtree, 2. recursively traverse the right subtree, 3. process the current node


## Variations
* Binary Search Tree - a Binary Tree where every left subtree contains elements that are less than or equal to a given node, and every right subtree contains elements that are greater than the given node