# coding: utf-8
# @FileName: test_203.py
# @Time: 2022/8/13 10:43
# @Author: QHB

# 第 203 题 移除链表元素
class ListNode:
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_elements(head, val):
    # 添加一个虚拟节点
    dummy_head = ListNode(next=head)
    cur = dummy_head
    while cur.next is not None:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy_head.next


print(remove_elements(head=[1, 2, 6, 3, 4, 5, 6], val=6))
