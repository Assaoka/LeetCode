class Solution(object):
    def isPalindrome(self, s):
        s = [i for i in s.lower() if i.isalnum()]
        for i in range(len(s)/2):
            if s[i] != s[-i-1]: return False
        return True
        