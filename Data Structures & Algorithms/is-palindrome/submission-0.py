class Solution:
    def isPalindrome(self, s: str) -> bool:
        empty_spaces = ""
        vl_pd = ""

        for i in s:
            if i.isalnum():
                empty_spaces = empty_spaces + i.lower()

        for j in empty_spaces:
            vl_pd = j + vl_pd

        if vl_pd == empty_spaces:
            return True
        else:
            return False