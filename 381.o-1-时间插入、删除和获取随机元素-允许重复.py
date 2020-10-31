#
# @lc app=leetcode.cn id=381 lang=python3
#
# [381] O(1) 时间插入、删除和获取随机元素 - 允许重复
#

# @lc code=start
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 采用 dict 执行线性查找
        self.list1 = []
        self.dict1 = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        # 取得插入元素的索引，放到对应的dict中
        l_len = len(self.list1)
        v_set = self.dict1.get(val)
        self.list1.append(val)
        if v_set:
            # 如果检查到，append到 value上
            self.dict1[val].add(l_len)
            return False
        else:
            # 如果没有 创建新的key value pair
            self.dict1[val] = {l_len}
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        #查找元素是否存在
        v_set = self.dict1.get(val)
        l_len = len(self.list1)
        if v_set:
            last_val = self.list1[-1]
            # 如果恰好为最后一个，直接在索引中删除
            if val == last_val:
                v_set.remove(l_len - 1)
            else:
                # 如果不是，交换最后一个到前面，删除最后一个
                # 弹出待删除的索引
                v_index = v_set.pop()
                # 将最后一位复制给该索引
                self.list1[v_index] = last_val
                # get 到最后一位值的索引列表
                last_set = self.dict1.get(last_val)
                # 删除
                last_set.remove(l_len - 1)
                #更新
                last_set.add(v_index)
            # list的删除只有删除最后一个才是O(1)
            self.list1.pop()
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.list1)




# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

