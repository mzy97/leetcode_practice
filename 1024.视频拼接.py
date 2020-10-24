#
# @lc app=leetcode.cn id=1024 lang=python3
#
# [1024] 视频拼接
#

# @lc code=start
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        #动态规划
        # dp[i] 表示将区间（0，i]覆盖的最少子区间数量
        # 枚举 i，搜索所有区间如果满足aj < i <= bj，则aj到i的部分可以被覆盖，最优数值为dp[aj] + 1
        # 代码中的min(dp[i], dp[aj] + 1) dp[i]的作用为防止遍历clips的时候前面的最优结果被覆盖
        dp = [0] + [float("inf")] * T
        for i in range(1, T + 1):
            for aj, bj in clips:
                if aj < i <= bj:
                    dp[i] = min(dp[i], dp[aj] + 1)
        return -1 if dp[T] == float("inf") else dp[T]
# @lc code=end

