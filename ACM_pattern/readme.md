
### ACM模式

    实际笔试的时候使用的都是ACM模式, 这种模式下除了核心的逻辑代码之外, 输入和输出也都是需要自己写的.
    平时刷力扣, 输入和输出都是给好的, 只需要写核心的算法部分和逻辑部分的代码就可以了.
    如果不准备一下ACM模式的模板, 真正笔试的时候往往会容易出问题, 会把大量的时间浪费在写输入输出上.
    


### 练习的网站

    用于练习输入模式捕获的网址链接:
    
    https://ac.nowcoder.com/acm/contest/5657


### 牛客网OJ练习题 --> 练习写输入输出

链接: https://ac.nowcoder.com/acm/contest/5652

+ a+b的和  
  - A. 多组空格分隔的两个正整数   
  [oj_1](/ACM_pattern/牛客网OJ_input/oj_1.py)
  - B. 第一行组数接空格分隔的两个正整数  
  [oj_2](/ACM_pattern/牛客网OJ_input/oj_2.py)  
  - C. 空格分隔的两个正整数为0 0结束  
  [oj_3](/ACM_pattern/牛客网OJ_input/oj_3.py)  
  - D. 每行第一个为个数后带空格分割整数为0结束  
  [oj_4](/ACM_pattern/牛客网OJ_input/oj_4.py)  
  - E. 第一行组数接第一个个数接空格分开的整数  
  [oj_5](/ACM_pattern/牛客网OJ_input/oj_5.py)  
  - F. 每行第一个为个数后带空格分割整数  
  [oj_6](/ACM_pattern/牛客网OJ_input/oj_6.py)  
  - G. 多组空格分隔的正整数  
  [oj_7](/ACM_pattern/牛客网OJ_input/oj_7.py)  


+ 字符串排序
  - H. 第一行个数第二行字符串  
  [oj_8](/ACM_pattern/牛客网OJ_input/oj_8.py)
  - I. 多行空格分开的字符串  
  [oj_9](/ACM_pattern/牛客网OJ_input/oj_9.py)
  - J. 多行逗号分开的字符串  
  [oj_10](/ACM_pattern/牛客网OJ_input/oj_10.py)


### sys.stdin输入格式模板

python常用的两种标准化的输入方式: sys.stdin 和 input
input更简单, 但sys.stdin更多样(其实不建议用sys, 因为sys.stdin.readline()获取标准输入的时候也会获取末尾的'\n'
这个需要用 sys.stdin.readline( ).strip('\n') 处理掉, 但是实际笔试给的数据谁也不知道是怎样的, 为减少不必要的风险, 
建议还是input朴实无华些)




