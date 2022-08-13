# coding: utf-8
# @FileName: basic.py
# @Time: 2022/8/13 10:32
# @Author: QHB


# 参考链接:
# https://programmercarl.com/%E9%93%BE%E8%A1%A8%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html#%E5%8D%95%E9%93%BE%E8%A1%A8


# 链表: 是一种通过指针串联在一起的线性结构, 每一个节点由两部分组成, 一个是数据域, 一个是指针域
# 指针域用于存放指向下一个节点的指针, 最后一个节点的指针域指向Null, 即空指针的意思
# 链表的入口节点称为链表的头结点, 即head

# ===============  链表的类型 ================
# 单链表  双链表  循环链表

# ===============  链表的存储方式 =============
# 数组在内存中是连续分布的, 但是链表在内存中不是连续分布的, 链表通过指针域的指针链接在内存中的各个节点
# 链表中的节点在内存中散乱分布, 分配机制取决于操作系统的内存管理

# 链表的定义 笔试ACM模式需要自己写链表
class ListNode:
    def __int__(self):
        self.val = None
        self.next = None


# 定义对链表的操作
class ListNode_handle:
    def __init__(self):
        self.cur_node = None

    def add(self, data):
        """
        添加链表节点
        :param data:
        :return:
        """
        # 增加一个新的node指向之前的node
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

    @staticmethod
    def print_ListNode(node):
        """
        打印链表
        :param node:
        :return:
        """
        while node:
            print("node:", node, " value:", node.val, " next:", node.next)
            node = node.next

    @staticmethod
    def reverse_(nodelist):
        """
        反转链表
        :param nodelist:
        :return:
        """
        list_ = []
        while nodelist:
            list_.append(nodelist.val)
            nodelist = nodelist.next
        _result = ListNode()
        result_handle = ListNode_handle()
        for i in list_:
            _result = result_handle.add(i)
        return _result


# 实例化一个链表
l1 = ListNode()
# 实例化一个链表操作
ListNode11 = ListNode_handle()
# 生成要转成链表的列表
l1_list = [1, 8, 3]
# 遍历列表
for i in l1_list:
    # 逐个加入链表
    l1 = ListNode11.add(i)
ListNode11.print_ListNode(l1)
l1 = ListNode11.reverse_(l1)
ListNode11.print_ListNode(l1)
