class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # 解法完全等於 560，就只是把k換成goal。代碼完全複製
        count = 0
        prefix_sum = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1  # 重要！處理剛好一開始就 sum == goal 的情況

        for num in nums:
            prefix_sum += num
            # 如果 prefix_sum - goal 存在，表示存在一段子陣列總和為 goal
            count += prefix_map[prefix_sum - goal]
            print(prefix_map)
            print("count", count)
            prefix_map[prefix_sum] += 1

        return count