"""
Problem 542: 01 Matrix
Difficulty: Medium
Link: https://leetcode.com/problems/01-matrix/

Description:
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Approach:
Use multi-source BFS to compute the shortest distance from each cell to the nearest 0.
Key insight: Instead of running BFS from each 1, start BFS from ALL 0s simultaneously.
This is more efficient because all 0s propagate outward in "waves" to find shortest paths.

Algorithm:
1. Initialize a distance matrix filled with infinity
2. Add all cells containing 0 to the queue and set their distance to 0
3. Perform BFS from all 0s simultaneously:
   - For each cell, check its 4 neighbors (up, down, left, right)
   - If neighbor's distance > current distance + 1, update it and add to queue
   - Continue until queue is empty
4. Return the distance matrix

Why Multi-Source BFS Works:
- BFS finds shortest path in unweighted graphs
- All 0s have distance 0, so they propagate outward in concentric "waves"
- Each wave represents cells at distance 1, 2, 3, etc. from nearest 0
- When a cell is reached, we've found the shortest path to a 0

Complexity:
- Time: O(m*n) - each cell is processed at most once
- Space: O(m*n) - for the distance matrix and queue

Edge Cases:
- Empty matrix
- Matrix with no 0s (all distances remain infinity)
- Matrix with only 0s (all distances are 0)
- Single cell
- Matrix with all 0s or all 1s
"""

from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Find the distance of the nearest 0 for each cell in a binary matrix.
        
        Args:
            mat: m x n binary matrix containing 0s and 1s
            
        Returns:
            Matrix where each cell contains the distance to the nearest 0
        """
        if not mat:
            return mat

        rows, cols = len(mat), len(mat[0])
        
        # Initialize distance matrix with infinity
        dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        queue = deque()

        # Step 1: Add all 0s to queue and set their distance to 0
        # This is the key to multi-source BFS
        for m in range(rows):
            for n in range(cols):
                if mat[m][n] == 0:
                    dist[m][n] = 0
                    queue.append((m, n))

        # Step 2: BFS from all 0s simultaneously
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            x, y = queue.popleft()
            
            # Check all 4 adjacent neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Boundary check
                if 0 <= nx < rows and 0 <= ny < cols:
                    # If we found a shorter path, update and add to queue
                    if dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))

        return dist


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Basic example
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    result = solution.updateMatrix(mat)
    assert result == expected
    print("✓ Test case 1 passed: Basic example with mixed 0s and 1s")
    
    # Test case 2: Single row with 0 at start
    mat = [[0, 0, 0]]
    expected = [[0, 0, 0]]
    result = solution.updateMatrix(mat)
    assert result == expected
    print("✓ Test case 2 passed: Single row with all 0s")
    
    # Test case 3: Single row with 0 at end
    mat = [[1, 1, 0]]
    expected = [[2, 1, 0]]
    result = solution.updateMatrix(mat)
    assert result == expected
    print("✓ Test case 3 passed: Single row with 0 at end")
    
    # Test case 4: Column with single 0
    mat = [[0], [1], [1]]
    expected = [[0], [1], [2]]
    result = solution.updateMatrix(mat)
    assert result == expected
    print("✓ Test case 4 passed: Single column with 0 at top")
    
    # Test case 5: Multiple 0s in matrix
    mat = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    expected = [[0, 1, 0], [1, 2, 1], [0, 1, 0]]
    result = solution.updateMatrix(mat)
    assert result == expected
    print("✓ Test case 5 passed: Multiple 0s forming cross pattern")
    
    # Test case 6: Large distance gradient
    mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    expected = [[2, 1, 2], [1, 0, 1], [2, 1, 2]]
    result = solution.updateMatrix(mat)
    assert result == expected
    print("✓ Test case 6 passed: 0 in center, all 1s around")
    
    # Test case 7: Empty row at beginning
    mat = [[0, 0], [1, 1], [1, 1]]
    expected = [[0, 0], [1, 1], [2, 2]]
    result = solution.updateMatrix(mat)
    assert result == expected
    print("✓ Test case 7 passed: 0s in top row")
    
    print("\nAll tests passed!")
