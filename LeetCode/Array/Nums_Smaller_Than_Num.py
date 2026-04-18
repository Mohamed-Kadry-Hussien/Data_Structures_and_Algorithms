# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n = len(nums)
        freq = [0] * (101)
        output = [0] * n 
        for num  in nums:
            freq[num]+=1 # is number of (num)'s in array 
        for i in range(1,101):
            freq[i] += freq[i-1] # number of elements <= i
        for i in range(n):
            num = nums[i]
            if num == 0 :
                output[i] = 0 
            else :
                output[i] = freq[num-1]
        return output 




        return count 
        