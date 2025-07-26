class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        # 多了個條件
        # 陣列最少要2個元素
        # 事實上就是在找連續陣列最長的類似題目，只是這裡只要找到最短大於2就行，因此hashmap要記的是index
        # 然後這題要避開一個陷阱，不能直接用 hashmap = defaultdict(int)，會對未出現過的 key 自動回傳 0
        hashmap = {}
        hashmap[0] = -1
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            remainder = prefix_sum % k

            if remainder in hashmap:
                if i - hashmap[remainder] >= 2:  # 👈 確保長度 ≥ 2
                    return True
            else:
                hashmap[remainder] = i
        
        return False