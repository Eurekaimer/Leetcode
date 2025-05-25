class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        reverse_list = []
        while x > 0:
            reverse_list.append(x % 10)
            x = x // 10
        return reverse_list == reverse_list[::-1]
