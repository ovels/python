# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         rnums = []
#         for num1 in nums:
#             for num2 in nums:
#                 if num1 != num2 & num1+num2 == target:
#                     rnums.append(nums.index(num1))
#                     rnums.append(nums.index(num2))
#                     return rnums
#                 else:
#                     return 