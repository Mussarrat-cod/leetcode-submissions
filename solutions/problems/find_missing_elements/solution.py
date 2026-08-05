from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []

        for i in range(len(nums) - 1):
            curr = nums[i]
            next_val = nums[i + 1]

            # fill gap
            for x in range(curr + 1, next_val):
                res.append(x)

        return res