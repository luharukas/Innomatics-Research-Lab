# Count bits

class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for pow in range(0, 32):
            start, end = 1<<pow, 1<<(pow + 1)
            if start > num: break

            for j in range(start, min(num+1,end)):
                dp[j] = dp[j-start] + 1
        return dp  
        