#!/usr/bin/python
# -*- coding: GBK -*-

# 面试题 16.25. LRU缓存
# 设计和构建一个“最近最少使用”缓存，该缓存会删除最近最少使用的项目。缓存应该从键映射到值(允许你插入和检索特定键对应的值)，并在初始化时指定最大容量。当缓存被填满时，它应该删除最近最少使用的项目。

# 它应该支持以下操作： 获取数据 get 和 写入数据 put 。

# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

# 示例:

# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        #存储容量大小
        self.capacity = capacity
        #存储KV对
        self.kv_dict = OrderedDict()
        #当前缓存中的条数
        self.amount = 0

    def get(self, key: int) -> int:
        #如果key不存在，则返回-1
        if key not in self.kv_dict:
            return -1

        #key存在，则返回值，并更新当前order值为最新值
        ret = self.kv_dict[key]
        #更新词典中顺序
        value = self.kv_dict.pop(key)
        self.kv_dict[key] = value

        return ret

    def put(self, key: int, value: int) -> None:
        #已经存在，直接更新值和最后一次访问时间
        if key in self.kv_dict:
            self.kv_dict.pop(key)
            self.kv_dict[key] = value
        #不存在，
        #  判断缓存大小，还有缓存，则存入当前key val
        #  无缓存，需删除最近最少使用的数据值，再写入
        else:
            if self.amount == self.capacity:
                #找到需要退出缓存的key
                self.kv_dict.popitem(last=False)
                self.amount -= 1
            self.kv_dict[key] = value
            self.amount += 1
        # print(self.kv_dict)

if __name__ == "__main__":
    # Your LRUCache object will be instantiated and called as such:
    # capacity = 2
    # cache = LRUCache(capacity)

    # cache.put(1, 1)
    # cache.put(2, 2)
    # print(cache.get(1)) # 返回  1
    # cache.put(3, 3) # 该操作会使得密钥 2 作废
    # print(cache.get(2)) # 返回 - 1 (未找到)
    # cache.put(4, 4) # 该操作会使得密钥 1 作废
    # print(cache.get(1)) # 返回 - 1 (未找到)
    # print(cache.get(3)) # 返回  3
    # print(cache.get(4)) # 返回  4

    capacity = 2
    cache = LRUCache(capacity)

    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    print(cache.get(1))
    print(cache.get(2))
