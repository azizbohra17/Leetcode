class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        sum1 = 0
        temp = x
        while temp > 0:
            rem = temp % 10
            sum1 = sum1 * 10 + rem
            temp = temp // 10
        if sum1 == x:
            return True
        else:
            return False


obj = Solution()
print(obj.isPalindrome(91))
