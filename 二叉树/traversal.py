# coding: utf-8
# @FileName: traversal.py
# @Time: 2022/8/15 10:29
# @Author: QHB

# 前序遍历-递归-LC144_二叉树的前序遍历
def preorder_traversal(root):
    # 保存结果
    result = []

    def traversal(root):
        if root is None:
            return
        result.append(root.val)  # 前序
        traversal(root.left)  # 左
        traversal(root.right)  # 右

    traversal(root)
    return result


# 中序遍历-递归-LC94_二叉树的中序遍历
def inorder_traversal(root):
    result = []

    def traversal(root):
        if root is None:
            return
        traversal(root.left)  # 左
        result.append(root.val)  # 中序
        traversal(root.right)  # 右

    traversal(root)
    return result


# 后序遍历-递归-LC145_二叉树的后序遍历
def postorder_traversal(root):
    result = []

    def traversal(root):
        if root is None:
            return
        traversal(root.left)  # 左
        traversal(root.right)  # 右
        result.append(root.val)  # 后序

    traversal(root)
    return result


# 层序遍历
def level_order(root):
    results = []
    if not root:
        return results

    from collections import deque
    que = deque([root])

    while que:
        size = len(que)
        result = []
        for _ in range(size):
            cur = que.popleft()
            result.append(cur.val)
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
        results.append(result)

    return results





