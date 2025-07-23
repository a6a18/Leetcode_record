from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1  # 重要！處理剛好一開始就 sum == k 的情況

        for num in nums:
            prefix_sum += num
            # 如果 prefix_sum - k 存在，表示存在一段子陣列總和為 k
            count += prefix_map[prefix_sum - k]
            prefix_map[prefix_sum] += 1

        return count

        