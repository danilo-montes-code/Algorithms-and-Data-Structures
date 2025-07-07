# Depth First Search (DFS)
Performed on graphs and trees, DFS starts at a root node and travels through the structure as far into the structure as possible. 
For trees, at each node, the left subtree is managed first, and then the current node is proceeded, ending with the right node being processed.
For graphs, the first node that is found is managed immediately, and becomes the next node to process.
In this way, The tree/graph is searched by going down the height of it first.

BFS is useful for:
* finding friends of friends
* finding the shortest path from point A to B

<div align="center">
    <img src="dfs.gif"/>
    <br/>
    <em>GIF from <a href="https://medium.com/analytics-vidhya/a-quick-explanation-of-dfs-bfs-depth-first-search-breadth-first-search-b9ef4caf952c">Medium</a></em>
</div>



## Step-by-Step

1. Your function signature should include:
    * the root of the tree, or starting vertex for a graph
    * the target value to search for
2. Initialize a **queue with the root** of the tree/starting graph node as the only element
    * If using a graph, initialize a **data structure to mark if the node was visited**, be it a hash map, set, etc.
3. Initialize a **loop that runs until the queue is empty**
4. **Pop the first element** of the queue to get the node/vertex to handle
    * If using a graph, **mark the element as visited**
5. If the element **contains the target value**, return a reference to the node, or True, depending on function goals
6. **Add the children nodes**/unvisited adjacent verticies to the end of the queue
7. If the **entire tree/graph was searched without finding the target**, return None or False depending on function goals



## Complexities

**Time Complexity**: `O(n)`, where n is the number of nodes in the tree, or `O(V + E)`, where V is the number of vertices and E is the number of edges in the graph
- Each node is visited at most once, and the entire tree/graph might be searched

**Space Complexity**: `O(n)` - The entire tree/graph can be loaded into the queue at once