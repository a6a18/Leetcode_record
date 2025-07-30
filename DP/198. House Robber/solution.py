class Solution:
    def rob(self, nums: List[int]) -> int:
        # 有趣的題目，重點在於怎麼把前幾個房子的最優解想成另一個題目
        # 把每一次的局部最優解，想成另一個題目的全局最優解
        hashmap = {}
        for i in range(len(nums)):
            hashmap[i] = nums[i]
        
        nums.sort(reverse=True)
        robber = {}
        count = 0
        print("hashmap", hashmap)
        print(nums)
        for ii in range(len(nums)):
            if ii + 1 and ii -1 not in robber:
                count += hashmap[ii]
                robber[ii] = hashmap[ii]
        print(robber)
        return count
