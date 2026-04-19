# https://leetcode.com/problems/build-an-array-with-stack-operations/
class Solution(object):
    def buildArray(self, target, n):
        output = []
        target_set = set(target)
        last_element = target[-1]
        for i in range( 1 , last_element + 1 ):
            output.append("Push")
            if  (i not in target_set) :
                output.append("Pop")
        return output 