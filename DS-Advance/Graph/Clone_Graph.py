"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}
        def dfs(node):
            #Base function
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors.append(node2)
    node1.neighbors.append(node4)

    node2.neighbors.append(node1)
    node2.neighbors.append(node3)

    node3.neighbors.append(node2)
    node3.neighbors.append(node4)

    node4.neighbors.append(node1)
    node4.neighbors.append(node3)

    clone_node = Solution().cloneGraph(node1)