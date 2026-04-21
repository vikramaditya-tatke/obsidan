"""
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3

Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1

Constraints:

    0 <= s.length <= 1000
    s may consist of printable ASCII characters.

"""

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         char_set = set()
#         left = 0
#         max_length = 0

#         for right in range(len(s)):
#             # If character is already in the set, remove characters from left
#             while s[right] in char_set:
#                 char_set.remove(s[left])
#                 left += 1

#             # Add the current character to the set
#             char_set.add(s[right])

#             # Update the maximum length
#             max_length = max(max_length, right - left + 1)

#         return max_length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_length = 0
        left = 0
        right = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            max_length = max(max_length, len(char_set))

        return max_length


def main():
    s = "pwwkew"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)


if __name__ == "__main__":
    main()
