#https://leetcode.com/problems/n-th-tribonacci-number/

class Solution(object):
    memo = dict()
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
          return 0
        elif n <= 2:
          return 1
        elif not self.memo.get(n):
          self.memo[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)  
        return self.memo[n]