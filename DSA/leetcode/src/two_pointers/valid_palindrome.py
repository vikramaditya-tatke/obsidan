"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true

Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false

Explanation: "tabacat" is not a palindrome.

Constraints:

    1 <= s.length <= 1000
    s is made up of only printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s) - 1
        while left_pointer < right_pointer:
            while left_pointer < right_pointer and not s[left_pointer].isalnum():
                left_pointer += 1

            while left_pointer < right_pointer and not s[right_pointer].isalnum():
                right_pointer -= 1

            if s[left_pointer].lower() != s[right_pointer].lower():
                return False

            left_pointer += 1
            right_pointer -= 1

        return True


def main():
    solution = Solution()
    result = solution.isPalindrome("Was it a car or a cat I saw?")
    print(result)


if __name__ == "__main__":
    solution = Solution()
    s = "Was it a car or a cat I saw?"
    result = solution.isPalindrome(s)
    print(result)
    main()
