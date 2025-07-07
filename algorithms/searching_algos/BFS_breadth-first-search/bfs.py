"""
Breadth-First Search (BFS)

Time Complexity: O(n) where n is the number of nodes in the tree, or O(V + E), where V is the number of vertices and E is the number of edges in the graph
Space Complexity: O(V)
"""

from collections import deque

class TreeNode:

    def __init__(self, value, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right



def BFS(root: TreeNode, target: int) -> bool:
    if not root:
        return False
    
    queue = deque([root])

    while queue:
        node = queue.popleft()
        
        if node.value == target:
            return True
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return False



def example_BFS():
    """
    Example usage of BFS
    """
    root = TreeNode(1,
                    TreeNode(2,
                             TreeNode(4),
                             TreeNode(5)),
                    TreeNode(3))
    
    print(BFS(root, 4))  # Output: True
    print(BFS(root, 6))  # Output: False

if __name__ == "__main__":
    example_BFS()