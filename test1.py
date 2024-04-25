# class Solution :
#     def searchInsert (self,nums:List[int],target:int) -> int;
#     left,right =0,len(nums) -1
#     while left <= right:
#         mid=(left+right)//2
#         if nums[mid] < target:
#             left = mid+ 1
#         elif nums[mid]>target:
#             right =mid -1
#         else:
#             return mid
#         return left
# #
def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


# 示例
nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))  # 输出 2，因为 5 在数组中的索引是 2

target = 2
print(searchInsert(nums, target))  # 输出 1，因为 2 不在数组中，它将会被插入到索引为 1 的位置