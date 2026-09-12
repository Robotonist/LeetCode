"""
Problem 15: 3Sum
Difficulty: Medium
Link: https://leetcode.com/problems/3sum/

Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
The solution set must not contain duplicate triplets.

Approach:
1. Sort the array to enable two-pointer technique and easier duplicate handling
2. Iterate through the array, using each element as the first number (anchor)
3. For each anchor, use two pointers to find pairs that sum to -anchor
4. Skip duplicates at each level to ensure unique triplets
5. Adjust pointers based on whether sum is too small or too large

Key Insights:
- Sorting allows us to skip duplicates efficiently
- Two-pointer approach reduces problem to O(n²) instead of O(n³)
- Early termination when anchor > 0 (rest of array will also be positive)
- Skip duplicate pointers after finding a valid triplet

Algorithm:
1. Sort nums
2. For each index i from 0 to n-3:
   - If nums[i] > 0, break (no valid triplets possible)
   - Skip duplicate values of nums[i]
   - Use two pointers (lo, hi) in remaining array
   - Find triplets that sum to 0
   - Skip duplicates for lo and hi pointers

Complexity:
- Time: O(n²) - sorting is O(n log n), nested loops are O(n²)
- Space: O(1) - excluding the output array (some implementations count output)

Edge Cases:
- Array with all zeros
- Array with negative numbers only
- Array with positive numbers only
- Array smaller than 3 elements
- No valid triplets exist
- Multiple duplicate values
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets in the array that sum to zero.
        
        Args:
            nums: List of integers
            
        Returns:
            List of lists, where each inner list is a triplet that sums to zero
        """
        nums.sort()
        n = len(nums)
        answer = []

        for i in range(n):
            # Optimization: if current number is positive, 
            # all remaining numbers are positive, so no triplets can sum to 0
            if nums[i] > 0:
                break
            
            # Skip duplicate values for the first number (anchor)
            # Only skip if it's not the first iteration
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            # Two-pointer approach for the remaining array
            lo, hi = i + 1, n - 1
            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi]
                
                if summ == 0:
                    # Found a valid triplet
                    answer.append([nums[i], nums[lo], nums[hi]])
                    
                    # Move both pointers
                    lo, hi = lo + 1, hi - 1
                    
                    # Skip duplicate values for the left pointer
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    
                    # Skip duplicate values for the right pointer
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                        
                elif summ < 0:
                    # Sum is too small, need larger numbers
                    lo += 1
                else:
                    # Sum is too large, need smaller numbers
                    hi -= 1

        return answer


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Basic example with negative, zero, and positive
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, -1, 2], [-1, 0, 1]]
    result = solution.threeSum(nums)
    assert result == expected
    print("✓ Test case 1 passed: Basic example with mixed numbers")
    
    # Test case 2: All zeros
    nums = [0, 0, 0, 0]
    expected = [[0, 0, 0]]
    result = solution.threeSum(nums)
    assert result == expected
    print("✓ Test case 2 passed: All zeros")
    
    # Test case 3: No valid triplets
    nums = [1, 2, -2, -1]
    expected = []
    result = solution.threeSum(nums)
    assert result == expected
    print("✓ Test case 3 passed: No valid triplets")
    
    # Test case 4: Multiple duplicates
    nums = [-2, 0, 1, 1, 2]
    expected = [[-2, 0, 2], [-2, 1, 1]]
    result = solution.threeSum(nums)
    assert result == expected
    print("✓ Test case 4 passed: Multiple duplicates handled correctly")
    
    # Test case 5: All negative numbers with zero
    nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    result = solution.threeSum(nums)
    # Check that we have some valid triplets
    assert len(result) > 0
    for triplet in result:
        assert sum(triplet) == 0
    print("✓ Test case 5 passed: Complex array with duplicates")
    
    # Test case 6: Single valid triplet
    nums = [-1, 0, 1]
    expected = [[-1, 0, 1]]
    result = solution.threeSum(nums)
    assert result == expected
    print("✓ Test case 6 passed: Single valid triplet")
    
    # Test case 7: Positive numbers only (no solution)
    nums = [1, 2, 3, 4]
    expected = []
    result = solution.threeSum(nums)
    assert result == expected
    print("✓ Test case 7 passed: Positive numbers only")
    
    # Test case 8: Negative numbers with solution
    nums = [-6, 1, -3, -2, 5, -1, 0, 4]
    result = solution.threeSum(nums)
    # Verify all triplets sum to zero and no duplicates
    for triplet in result:
        assert sum(triplet) == 0
    assert len(result) == len(set(tuple(sorted(t)) for t in result))
    print("✓ Test case 8 passed: Negative and positive numbers")
    
    print("\nAll tests passed!")
