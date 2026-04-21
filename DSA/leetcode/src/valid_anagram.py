"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true

Example 2:

Input: s = "jar", t = "jam"

Output: false

Constraints:

    s and t consist of lowercase English letters.

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}
        for char in s:
            if char in seen_s:
                seen_s[char] += 1
            else:
                seen_s[char] = 1

        for char in t:
            if char in seen_t:
                seen_t[char] += 1
            else:
                seen_t[char] = 1
        print(f"seen_s: {seen_s}")
        print(f"seen_t: {seen_t}")

        if sorted(seen_s) == sorted(seen_t):
            return True

        return False


def main():
    s = "racecar"
    t = "carrace"
    solution = Solution()
    result = solution.isAnagram(s, t)
    print(result)


if __name__ == "__main__":
    main()
