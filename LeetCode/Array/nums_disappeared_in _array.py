# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        freq = [0] * (n+1)
        output = []
        for num in nums :
            freq[num] += 1
        for i in range(1,n+1) : 
                if freq[i] == 0 :
                    output.append(i)
        return output 
# another sol by using set
class Solution(object):
    def findDisappearedNumbers(self, nums):
         n = len(nums)
         output = []
         s = set(nums)

         for i in range (1 ,n+1):
              if i not in s :
                   output.append(i)
         return output 


