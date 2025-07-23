from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0
        preDic = defaultdict(int)
        preDic[0] = -1
        maxLen = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                prefix_sum += -1
            else:
                prefix_sum += 1
            
            if prefix_sum in preDic:
                maxLen = max(i - preDic[prefix_sum], maxLen)
            else:
                preDic[prefix_sum] = i
        
        return maxLen


        