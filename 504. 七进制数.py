class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        is_negative = num < 0
        num = abs(num)
        answer = []

        while num > 0:
            answer.append(str(num % 7))
            num = num // 7

        if is_negative:
            answer.append("-")

        return ''.join(reversed(answer))

