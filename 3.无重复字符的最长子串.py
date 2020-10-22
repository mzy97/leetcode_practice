#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # 使用一个辅助变量来暂时存储匹配的子串
        # ans = ''
        # tep = ''
        # for i in s:
        #     # 遍历，若不重复则记录该字符
        #     if i not in tep:
        #         tep += i
        #     # 如果遇到了已经存在的字符，则找到该字符所在位置，删除该字符，并保留该位置之后的子串，并把当前字符加入到最后，完成更新
        #     else:
        #         tep = tep[tep.index(i)+1:]
        #         tep += i   
        #     # 如果是当前最长的，就替换掉之前存储的最长子串
        #     if len(tep) > len(ans): 
        #             ans = tep 
        # return len(ans)
    # another solution
        if not s:
            return 0
        left = 0
        # lookup = []
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                # lookup = lookup[1:]
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            # lookup.append(s[i])
            lookup.add(s[i])
        return max_len



# @lc code=end

