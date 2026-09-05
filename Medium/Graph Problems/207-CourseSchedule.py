"""
Problem 207: Course Schedule
Difficulty: Medium
Link: https://leetcode.com/problems/course-schedule/

Description:
You are given numCourses (numbered from 0 to numCourses-1) and a list of prerequisite pairs,
where prerequisites[i] = [a, b] means to take course a, you must first take course b.
Return true if you can finish all courses; otherwise, return false.

Approach:
Use iterative DFS with verification states to detect cycles in a directed graph:
- UNVERIFIED (0): Node has not been visited
- VERIFYING (1): Node is currently being processed (in the DFS path)
- VERIFIED (2): Node has been fully processed

Key insight: If we encounter a node in VERIFYING state, it means we've found a cycle
(we're revisiting a node in the current DFS path).

Algorithm:
1. Build an adjacency list where graph[a] contains all prerequisites b for course a
2. For each course, run DFS to check for cycles
3. During DFS, mark nodes as VERIFYING before exploring neighbors
4. If we find a VERIFYING node, return False (cycle detected)
5. After exploring all neighbors, mark node as VERIFIED
6. If all nodes can be verified without cycles, return True

Complexity:
- Time: O(N + E) where N is numCourses and E is the number of prerequisites
- Space: O(N + E) for the graph and states array

Edge Cases:
- No prerequisites (all courses independent)
- Single course
- Self-loop (course prerequisite to itself)
- Circular dependencies between multiple courses
"""

from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determine if all courses can be finished without circular dependencies.
        
        Args:
            numCourses: Total number of courses
            prerequisites: List of [course, prerequisite] pairs
            
        Returns:
            True if all courses can be finished, False if there's a cycle
        """
        # Build adjacency list mapping each course to its prerequisites
        graph = defaultdict(list)
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        # Verification states for cycle detection
        UNVERIFIED = 0
        VERIFYING = 1
        VERIFIED = 2
        states = [UNVERIFIED] * numCourses
        
        def dfs(node):
            """
            DFS to detect cycles using verification states.
            
            Args:
                node: Current course being verified
                
            Returns:
                True if no cycle found in this path, False if cycle detected
            """
            state = states[node]
            
            # If already verified, no cycle in this path
            if state == VERIFIED:
                return True
            
            # If currently verifying, we've found a cycle!
            # (revisiting a node in the current DFS path)
            if state == VERIFYING:
                return False
            
            # Mark as currently verifying
            states[node] = VERIFYING
            
            # Check all prerequisites of this course
            for prerequisite in graph[node]:
                if not dfs(prerequisite):
                    return False
            
            # Mark as verified (no cycles found in this subtree)
            states[node] = VERIFIED
            return True
        
        # Check each course for cycles
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: No cycles, can finish all courses
    numCourses = 2
    prerequisites = [[1, 0]]
    assert solution.canFinish(numCourses, prerequisites) == True
    print("✓ Test case 1 passed: Linear dependency, can finish")
    
    # Test case 2: Cycle detected, cannot finish all courses
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    assert solution.canFinish(numCourses, prerequisites) == False
    print("✓ Test case 2 passed: Circular dependency detected")
    
    # Test case 3: No prerequisites
    numCourses = 3
    prerequisites = []
    assert solution.canFinish(numCourses, prerequisites) == True
    print("✓ Test case 3 passed: No prerequisites, can finish all")
    
    # Test case 4: Complex graph with no cycles
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    assert solution.canFinish(numCourses, prerequisites) == True
    print("✓ Test case 4 passed: Complex graph with no cycles")
    
    # Test case 5: Complex graph with cycle
    numCourses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2], [0, 3]]
    assert solution.canFinish(numCourses, prerequisites) == False
    print("✓ Test case 5 passed: Complex graph with cycle")
    
    # Test case 6: Self-loop
    numCourses = 1
    prerequisites = [[0, 0]]
    assert solution.canFinish(numCourses, prerequisites) == False
    print("✓ Test case 6 passed: Self-loop detected")
    
    print("\nAll tests passed!")
