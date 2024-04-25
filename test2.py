class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n =len(nums)
        nums.sort()

        b = n - 1
        for a in range(n):
            if a>0 and nums[a]== nums[a-1]:
                continue

            while a<b and nums[a]  + nums[b] > target :
                b -= 1
            if a==b:
                break
                if nums[a] + nums[b] == target:
                    return [nums[a], nums[b]]

        return[]