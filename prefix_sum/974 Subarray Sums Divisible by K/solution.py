from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        # 重點在記錄餘數，因為餘數一樣就代表中間連續陣列剛好差一個k

        hashmap = defaultdict(int)
        hashmap[0] = 1
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder in hashmap:
                count += hashmap[remainder]
            
            hashmap[remainder] += 1
        
        return count