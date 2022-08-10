# coding: utf-8
# @FileName: :backtracking.py
# @Time: 2022/8/10 13:45
# @Author: QHB

"""

回溯算法: 进行选择; 递归; 撤回选择 -- 一种纯暴力的搜索方式, 最多做做剪枝

解决  排列问题  子集问题 组合问题  切割问题  棋盘问题(n皇后 解数独)


=====================  代码模板 ==========================

    void backtracking(parameters){
         if (终止条件) {
            收集结果
            return
         }

         # 进入单层搜索的逻辑
         for (集合的元素){
            处理节点
            递归函数
            回溯操作 -- 撤销处理节点的情况
         }
         return

    }

=====================  代码模板 ==========================


参考学习链接:
https://www.bilibili.com/video/BV1cy4y167mM?spm_id_from=333.337.search-card.all.click&vd_source=7111d4cfa9354342c253c06ecdd64e2f


"""






