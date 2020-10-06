#
# @lc app=leetcode.cn id=834 lang=python3
#
# [834] 树中距离之和
#

# @lc code=start
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(N)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        # init base case：nodeNum 为 1，distSum 为 0。
        dist_sum = [0 for _ in range(N)]
        node_num = [1 for _ in range(N)]
# eg [[1, 2], [0], [0, 3, 4, 5], [2], [2], [2]]

        # 计算节点 所在的子树中的节点，与它的距离和
        # from bottom to top 后序遍历
        def post_order(node, parent):
            for n in graph[node]:
                if n == parent:
                    continue
                post_order(n, node)
                node_num[node] += node_num[n]
                dist_sum[node] += dist_sum[n] + node_num[n]
'''
节点2所在的子树的节点个数为nodeNum[2]，这nodeNum[2]个节点，从计算distSum[0]变成计算distSum[2]：从节点 0 到这些节点，变成从节点 2 到这些节点，每个节点都少走了一步，一共少走了nodeNum[2]步。

子树以外的节点呢，有N - nodeNum[2]个，从计算distSum[0]变成计算distSum[2]：从节点 0 到这些节点，变成从节点 2 到这些节点，每个节点都多走了一步，一共多走了N-nodeNum[2]步。

所以，我们找到distSum[i]与distSum[root]之间的递推关系：

distSum[i] = distSum[root] - nodeNum[i] + (N - nodeNum[i])
top to bottom 前序遍历
'''
        def pre_order(node, parent):
            for n in graph[node]:
                if n == parent:
                    continue
                dist_sum[n] = dist_sum[node] - node_num[n] + (N - node_num[n])
                pre_order(n, node)
        
        post_order(0, -1)
        pre_order(0, -1)
        return dist_sum

        
# @lc code=end
# 
# 

# edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# N = 6

# graph = [[] for _ in range(N)]
# for edge in edges:
#     graph[edge[0]].append(edge[1])
#     graph[edge[1]].append(edge[0])
# dist_sum = [0 for _ in range(N)]
# node_num = [1 for _ in range(N)]

# print(graph)
