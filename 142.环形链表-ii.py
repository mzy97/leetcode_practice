#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        # 当2*遍历和1*遍历的快慢指针相遇的时候：
        # f=2nb，s=nb b为圈的节点数
        # 如果让指针从链表头部一直向前走并统计步数k，那么所有 走到链表入口节点时的步数 是：k=a+nb a为环前面的节点数
        # 所以慢指针再走 a 步就到达了入口节点
        # 用快指针 *1 step的方法，再次相遇的时候就是入口节点
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast

        
# @lc code=end

