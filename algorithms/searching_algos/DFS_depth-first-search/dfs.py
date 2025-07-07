"""
Depth-First Search (DFS)

Time Complexity: O(n) where n is the number of nodes in the tree, or O(V + E), where V is the number of vertices and E is the number of edges in the graph
Space Complexity: O(V)
"""

class TreeNode:

    def __init__(self, value, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right



def DFS(root: TreeNode, target: int) -> bool:
    if not root:
        return False
    
    if DFS(root=root.left, target=target):
        return True

    if root.value == target:
        return True

    if DFS(root=root.right, target=target):
        return True

    return False



def example_DFS():
    """
    Example usage of DFS
    """
    root = TreeNode(1,
                    TreeNode(2,
                             TreeNode(4),
                             TreeNode(5)),
                    TreeNode(3))
    
    print(DFS(root, 4))  # Output: True
    print(DFS(root, 6))  # Output: False

if __name__ == "__main__":
    example_DFS()