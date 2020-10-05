#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
'''
利用多行数组辅助进行模拟，flag指示是否反向添加，最后按照数组顺序拼接
'''
# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)
# @lc code=end

