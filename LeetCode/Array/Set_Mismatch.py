# https://leetcode.com/problems/set-mismatch/
class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        missing = 0 
        duplicate = 0 
        count= [0]*(n+1)
        count[0] = 1
        for num in nums:
            count[num]+=1
        for c in range(n+1):
            if count[c] == 2 :
                duplicate = c
            elif count[c] == 0 :
                missing = c 
        arr = [duplicate,missing]
        return arr 




        