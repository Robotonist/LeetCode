"""
Problem 57: Insert Interval
Difficulty: Medium
Link: https://leetcode.com/problems/insert-interval/

Description:
You are given an array of non-overlapping intervals where each interval is [start, end],
sorted by start times. You are also given a new interval [start, end].
Insert newInterval into intervals such that:
1. Overlapping intervals are merged
2. The result is returned as a list of non-overlapping intervals sorted by start time

Approach:
Iterate through the intervals and handle three cases:
1. If the current interval ends before newInterval starts: add current interval (no overlap)
2. If the current interval starts after newInterval ends: add newInterval and return remaining intervals
3. If there's overlap: merge by expanding newInterval's boundaries

This is more efficient than collecting and then merging separately.

Algorithm:
1. Iterate through each interval
2. If interval ends before newInterval starts, add it to result (no overlap)
3. If interval starts after newInterval ends, we're done merging:
   - Add merged newInterval to result
   - Add all remaining intervals
   - Return result
4. If there's overlap, merge by updating newInterval's start and end
5. After loop, add the final merged newInterval

Complexity:
- Time: O(n) - single pass through intervals
- Space: O(n) for the result array (not counting output)

Edge Cases:
- Empty intervals list
- newInterval is contained within an existing interval
- newInterval contains multiple intervals
- newInterval doesn't overlap with any interval
- newInterval overlaps with all intervals
"""

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Insert a new interval into a list of non-overlapping intervals, merging as needed.
        
        Args:
            intervals: List of non-overlapping intervals sorted by start time
            newInterval: New interval to insert
            
        Returns:
            List of non-overlapping intervals after insertion and merging
        """
        result = []

        for i in range(len(intervals)):
            # Case 1: Current interval ends before newInterval starts (no overlap)
            # We can safely add the current interval and check newInterval later
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                # Add all remaining intervals (they also don't overlap with newInterval)
                return result + intervals[i:]

            # Case 2: Current interval starts after newInterval ends (no overlap)
            # Add the current interval to result, continue checking
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            # Case 3: Intervals overlap
            # Merge by expanding newInterval's boundaries
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        # Add the final merged newInterval
        result.append(newInterval)
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: newInterval merges two existing intervals
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    expected = [[1, 5], [6, 9]]
    result = solution.insert(intervals, newInterval)
    assert result == expected
    print("✓ Test case 1 passed: newInterval merges with first interval")
    
    # Test case 2: newInterval doesn't overlap (goes at end)
    intervals = [[1, 2], [3, 5], [6, 7]]
    newInterval = [8, 10]
    expected = [[1, 2], [3, 5], [6, 7], [8, 10]]
    result = solution.insert(intervals, newInterval)
    assert result == expected
    print("✓ Test case 2 passed: newInterval at end, no overlap")
    
    # Test case 3: newInterval doesn't overlap (goes at start)
    intervals = [[3, 5], [6, 7]]
    newInterval = [1, 2]
    expected = [[1, 2], [3, 5], [6, 7]]
    result = solution.insert(intervals, newInterval)
    assert result == expected
    print("✓ Test case 3 passed: newInterval at start, no overlap")
    
    # Test case 4: newInterval merges with multiple intervals
    intervals = [[1, 5], [6, 9]]
    newInterval = [2, 7]
    expected = [[1, 9]]
    result = solution.insert(intervals, newInterval)
    assert result == expected
    print("✓ Test case 4 passed: newInterval merges multiple intervals")
    
    # Test case 5: newInterval contains all existing intervals
    intervals = [[1, 2], [3, 4], [5, 6]]
    newInterval = [0, 10]
    expected = [[0, 10]]
    result = solution.insert(intervals, newInterval)
    assert result == expected
    print("✓ Test case 5 passed: newInterval contains all intervals")
    
    # Test case 6: Empty intervals list
    intervals = []
    newInterval = [5, 7]
    expected = [[5, 7]]
    result = solution.insert(intervals, newInterval)
    assert result == expected
    print("✓ Test case 6 passed: Empty intervals list")
    
    # Test case 7: newInterval is contained within an existing interval
    intervals = [[1, 10]]
    newInterval = [3, 5]
    expected = [[1, 10]]
    result = solution.insert(intervals, newInterval)
    assert result == expected
    print("✓ Test case 7 passed: newInterval contained in existing interval")
    
    # Test case 8: Single interval that doesn't overlap
    intervals = [[1, 2]]
    newInterval = [3, 4]
    expected = [[1, 2], [3, 4]]
    result = solution.insert(intervals, newInterval)
    assert result == expected
    print("✓ Test case 8 passed: Single interval, no overlap")
    
    print("\nAll tests passed!")
