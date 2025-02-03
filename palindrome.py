class Solution(object):
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1 # right pointer at the end of the string 

        while l < r:
            if not s[l].isalnum(): # if the left pointer is not alphanumeric
                l+=1
            elif not s[r].isalnum(): # if the right pointer is not alphanumeric
                r-=1
            elif s[l].lower() == s[r].lower(): # if the left pointer is equal to the right pointer
                l+=1
                r-=1
            else:
                return False # if the left pointer is not equal to the right pointer
        return True