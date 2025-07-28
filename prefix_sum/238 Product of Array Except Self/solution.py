# 這題是和prefix sum類似觀念，但不是sum，而是乘積。
# 其實left可以省去，但為了簡單理解還是定義一下left。
# 詳細可以看網頁解釋。

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # 1️⃣ 左乘積
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]
        
        # 2️⃣ 右乘積
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        
        return answer
