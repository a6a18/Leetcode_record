from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 加到偶數沒差 跟0一樣
        # 把基數當1，偶數當0
        # 解法完全等於 930
        hashmap = defaultdict(int)
        hashmap[0] = 1
        prefix_sum = 0
        count = 0

        for num in nums:
            if num % 2 == 0:
                pass
            else:
                prefix_sum += 1

            if prefix_sum - k in hashmap:
                count += hashmap[prefix_sum - k]
            
            hashmap[prefix_sum] += 1
        
        return count