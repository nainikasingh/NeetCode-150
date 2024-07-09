class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=1
        n=len(nums)
        for i in range(0,n-1):
            for j in range (1,n):
                a = nums[i]+nums[j]
                if a == target:
                    break
            if a == target:
                break
        b = [i,j]
        return b
