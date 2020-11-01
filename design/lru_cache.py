#!/usr/bin/python
# -*- coding: GBK -*-

# ������ 16.25. LRU����
# ��ƺ͹���һ�����������ʹ�á����棬�û����ɾ���������ʹ�õ���Ŀ������Ӧ�ôӼ�ӳ�䵽ֵ(���������ͼ����ض�����Ӧ��ֵ)�����ڳ�ʼ��ʱָ����������������汻����ʱ����Ӧ��ɾ���������ʹ�õ���Ŀ��

# ��Ӧ��֧�����²����� ��ȡ���� get �� д������ put ��

# ��ȡ���� get(key) - �����Կ (key) �����ڻ����У����ȡ��Կ��ֵ�����������������򷵻� -1��
# д������ put(key, value) - �����Կ�����ڣ���д��������ֵ�������������ﵽ����ʱ����Ӧ����д��������֮ǰɾ���������ʹ�õ�����ֵ���Ӷ�Ϊ�µ�����ֵ�����ռ䡣

# ʾ��:

# LRUCache cache = new LRUCache( 2 /* �������� */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // ����  1
# cache.put(3, 3);    // �ò�����ʹ����Կ 2 ����
# cache.get(2);       // ���� -1 (δ�ҵ�)
# cache.put(4, 4);    // �ò�����ʹ����Կ 1 ����
# cache.get(1);       // ���� -1 (δ�ҵ�)
# cache.get(3);       // ����  3
# cache.get(4);       // ����  4

class LRUCache:

    def __init__(self, capacity: int):
        #�洢������С
        self.capacity = capacity
        #�洢KV��
        self.kv_list = dict()
        #�洢���һ�η��ʵ�˳��
        self.kv_order = dict()
        #˳��get����putʱ��������1
        self.order = 0
        #��ǰ�����е�����
        self.amount = 0

    def get(self, key: int) -> int:
        #���key�����ڣ��򷵻�-1
        if key not in self.kv_list:
            return -1

        #key���ڣ��򷵻�ֵ�������µ�ǰorderֵΪ����ֵ
        ret = self.kv_list[key]
        self.kv_order[key] = self.order

        #����orderֵ
        self.order += 1

        return ret

    def put(self, key: int, value: int) -> None:
        #�Ѿ����ڣ�ֱ�Ӹ���ֵ�����һ�η���ʱ��
        if key in self.kv_list:
            self.kv_list[key] = value
            self.kv_order[key] = self.order
            self.order += 1
        #�����ڣ�
        #  �жϻ����С�����л��棬����뵱ǰkey val
        #  �޻��棬��ɾ���������ʹ�õ�����ֵ����д��
        else:
            if self.amount == self.capacity:
                #�ҵ���Ҫ�˳������key
                min_key = float('inf')
                min_order = float('inf')
                for k, v in self.kv_order.items():
                    if min_order > v:
                        min_key = k
                        min_order = v
                del(self.kv_list[min_key])
                del(self.kv_order[min_key])
                self.amount -= 1
            self.kv_list[key] = value
            self.kv_order[key] = self.order
            self.order += 1
            self.amount += 1

if __name__ == "__main__":
    # Your LRUCache object will be instantiated and called as such:
    capacity = 2
    cache = LRUCache(capacity)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1)) # ����  1
    cache.put(3, 3) # �ò�����ʹ����Կ 2 ����
    print(cache.get(2)) # ���� - 1 (δ�ҵ�)
    cache.put(4, 4) # �ò�����ʹ����Կ 1 ����
    print(cache.get(1)) # ���� - 1 (δ�ҵ�)
    print(cache.get(3)) # ����  3
    print(cache.get(4)) # ����  4
