class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = sorted((v, i)for i, v in enumerate(nums))
        L = 0
        R = len(nums) - 1

        while L < R:
            total = pairs[L][0] + pairs[R][0]
            if total > target:
                R-= 1
            elif total < target:
                L += 1
            else:
                return sorted([pairs[L][1], pairs[R][1]])
        return []

        