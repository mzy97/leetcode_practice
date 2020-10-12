#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        这道题可以换一种表述：给定一个只包含正整数的非空数组 nums[0]
        判断是否可以从数组中选出一些数字，使得这些数字的和等于整个数组
        的元素和的一半

        '''
        nums = sorted(nums)
        index = len(nums) - 1

        def add_all(parts):
            sum = 0
            for i in parts:
                sum += i
            return sum

        while index != 0:
            part1 = nums[:index]
            part2 = nums[index:]
            sum_part1 = add_all(part1)
            sum_part2 = add_all(part2)
            if sum_part1 < sum_part2:
                return False
            if sum_part1 == sum_part2:
                return True
            index -= 1
        
        return False
        
        
# @lc code=end

