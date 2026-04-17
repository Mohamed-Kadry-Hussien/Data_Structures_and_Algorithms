# https://leetcode.com/problems/concatenation-of-array/
class Solution(object):
    def getConcatenation(self , nums):
        length = len(nums)
        ans = [0]*(2*length)
        for i in range(2):
            for j in range(length):
                ans[j+i*length] = nums[j]
        return ans
    
#another solution
class Solution(object):
    def getConcatenation(self , nums):
        length = len(nums)
        ans = [0] *(2*length)
        for i in range(2*length):
            ans[i] =  nums[i%length]
        return ans
    
#another solution
class Solution(object):
    def getConcatenation(self , nums):
        return nums * 2

