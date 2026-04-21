"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []

Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]

Explanation: The only possible triplet sums up to 0.

Constraints:

    3 <= nums.length <= 1000
    -10^5 <= nums[i] <= 10^5

"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]):
        result = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add(tuple([nums[i], nums[j], nums[k]]))

        return [list(i) for i in result]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []

        for i, num in enumerate(sorted_nums):
            if i > 0 and num == sorted_nums[i - 1]:
                continue

            left = i + 1
            right = len(sorted_nums) - 1
            while left < right:
                three_sum = sorted_nums[left] + sorted_nums[right] + num
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([num, sorted_nums[left], sorted_nums[right]])
                    left += 1
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1

        return result


def main():
    solution = Solution()
    nums = [-3, 3, 4, -3, 2, 1]
    result = solution.threeSum(nums)
    print(result)


if __name__ == "__main__":
    main()
