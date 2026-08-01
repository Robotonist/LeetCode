"""
Problem 133: Clone Graph
Difficulty: Medium
Link: https://leetcode.com/problems/clone-graph/

Description:
Given a reference of a node in a connected undirected graph, return a deep copy (clone) 
of the graph. Each node contains an integer value and a list of its neighbors.

Approach:
Use iterative DFS with a stack to traverse the graph. First pass: visit all nodes and 
create copies (mapping old nodes to new nodes). Second pass: connect the cloned nodes 
by copying the neighbor relationships from the original graph.

Key insight: Use a dictionary to map original nodes to cloned nodes, and a visited set 
to avoid processing the same node twice during traversal.

Complexity:
- Time: O(N + E) where N is the number of nodes and E is the number of edges
- Space: O(N) for the hash map and visited set

Edge Cases:
- Single node with no neighbors
- Single node with self-loop
- Disconnected components (not applicable for connected graph)
- Duplicate edges between nodes
"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Clone an undirected graph using iterative DFS.
        
        Args:
            node: Reference to a node in the connected undirected graph
            
        Returns:
            Reference to the cloned node in the deep copy of the graph
        """
        if not node:
            return None

        start = node
        bck_to_copy = {}  # Maps original nodes to cloned nodes
        stack = [start]
        visited = set()  # Tracks visited nodes during traversal
        visited.add(start)

        # First pass: Visit all nodes and create clones
        while stack:
            node = stack.pop()
            bck_to_copy[node] = Node(val=node.val)
                
            # Add unvisited neighbors to stack
            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)

        # Second pass: Connect cloned nodes with their neighbors
        for old_node, new_node in bck_to_copy.items():
            for nei in old_node.neighbors:
                new_nei = bck_to_copy[nei]
                new_node.neighbors.append(new_nei)

        return bck_to_copy[start]


# Test cases
if __name__ == "__main__":
    # Test case 1: Simple graph with 3 nodes
    # Graph: 1--2
    #        |  |
    #        3--4
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    
    solution = Solution()
    cloned = solution.cloneGraph(node1)
    
    # Verify it's a deep copy
    assert cloned.val == 1
    assert cloned is not node1
    assert cloned.neighbors[0] is not node2
    print("✓ Test case 1 passed: Deep copy verified")
    
    # Test case 2: Single node
    single = Node(1)
    cloned_single = solution.cloneGraph(single)
    assert cloned_single.val == 1
    assert cloned_single is not single
    print("✓ Test case 2 passed: Single node cloned")
    
    # Test case 3: Empty graph
    cloned_empty = solution.cloneGraph(None)
    assert cloned_empty is None
    print("✓ Test case 3 passed: Empty graph handled")
    
    print("\nAll tests passed!")
