#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 传统解法
        count = [0 for _ in range(3)]
        for i in nums:
            count[i] += 1
        start_index = 0
        for i in range(3):
            for j in range(count[i]):
                nums[start_index+j] = i
            start_index+=count[i]
        # 两趟扫描
        n = len(nums)
        ptr = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        # 一趟扫描
        n = len(nums)
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1
        #三指针解法
        l,r=0,len(nums)-1
        cur=0
        while cur<=r:

            if nums[cur]==0:
                if nums[l]!=0:
                    nums[cur],nums[l]=nums[l],nums[cur]
                l+=1
                cur+=1
            
            elif nums[cur]==2:
                if nums[r]!=2:
                    nums[r],nums[cur]=nums[cur],nums[r]
                r-=1

            else:
                cur+=1



# @lc code=end

