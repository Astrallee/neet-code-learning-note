# Day 11


## 题目  1  ：Evaluate Reverse Polish Notation

You are given an array of strings `tokens` that represents a **valid** arithmetic expression in [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)\.

Return the integer that represents the evaluation of the expression\.

- The operands may be integers or the results of other operations\.

- The operators include `'+'`, `'-'`, `'*'`, and `'/'`\.

- Assume that division between integers always truncates toward zero\.

**Example 1:**

```Java
Input: tokens = ["1","2","+","3","*","4","-"]
Output: 5
Explanation: ((1 + 2) * 3) - 4 = 5
```

**Constraints:**

- `1 <= tokens.length <= 10000`\.

- tokens\[i\] is `"+"`, `"-"`, `"*"`, or `"/"`, or a string representing an integer in the range `[-200, 200]`\.



**思路：**

有一个字符串tokens ，包含了一个逆波兰表示法的有效算数表达式。  返回这个结果

题目都没看明白，去查了一下 逆波兰表示法（RPN），也称为后缀表示法，将数学运算符置于操作数之后（例如写成 `2 3 +` 而非 `2 + 3`）这种设计消除了对括号及运算优先级规则的需求，使计算机和基于栈的计算器能够轻松地从左至右处理各项。其工作原理如下：无需括号——无需额外符号即可明确运算顺序；从左至右扫描——按线性顺序读取各项；栈式存储——将数字压入栈中；遇到运算符时，从栈顶弹出最后两个数字进行运算，并将结果压回栈中。

\["1","2","\+","3","\*","4","\-"\]     

1 2 发现运算符是\+  弹出来  1\+2 =3  把3押进去  然后  3  3 发现是\* 都弹出来

```Plain Text
def evalRPN(self, tokens: List[str]) -> int:
    calculate_list = []
    for char in tokens:
        if char in "+-*/":
            value1 = calculate_list.pop()
            value2 = calculate_list.pop()
            if char == '+':
                result = value1 + value2
            elif char == '-':
                result = value2 - value1
            elif char == '*':
                result = value1 * value2
            else:
                result =int( value2 / value1)    
            calculate_list .append(result)
        else:
            calculate_list .append(int(char))
    return calculate_list[-1]
```





## 题目 2  ：Daily Temperatures

You are given an array of integers `temperatures` where `temperatures[i]` represents the daily temperatures on the `ith` day\.

Return an array `result` where `result[i]` is the number of days after the `ith` day before a warmer temperature appears on a future day\. If there is no day in the future where a warmer temperature will appear for the `ith` day, set `result[i]` to `0` instead\.

**Example 1:**

```Java
Input: temperatures = [30,38,30,36,35,40,28]Output: [1,4,1,2,1,0,0]
```

**Example 2:**

```Java
Input: temperatures = [22,21,20]Output: [0,0,0]
```

**Constraints:**

- `1 <= temperatures.length <= 100,000`\.

- `1 <= temperatures[i] <= 100`



**思路：**

有一个整数数组温度 ， 第i个代表i\-th天的温度

返回一个数组 `result`，其中 `result[i]` 表示在第 `i` 天之后，需要经过多少天才会出现气温更高的日子。

如果对于第 `i` 天而言，未来没有气温更高的日子，则将 `result[i]` 设为 0。

如果是递减数组，那么就是n个0。其实就是比大小 找到下一个比自己大的index。

虽然知道考察栈  但是暂时没想起来 先想个暴力的方法

```Plain Text
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    result = []
    for  index in range (len(temperatures)):
        j = index+1 
        while j <=len(temperatures)-1:
            if temperatures[j]>temperatures[index]:
                result.append(j-index)
                break
            else:
                j = j+1
        if j == len(temperatures):
            result.append(0)
    return result
```

优化:

暴力就是大力出奇迹，  超时间了 而且要训练 用栈的思维。

单调栈的核心思想：

**不要主动向后寻找答案，而是让未来的数字主动解决过去的问题。**

每一天都有一个问题：

> “未来哪一天比我温度高？”
> 
> 

因为栈顶代表最近还没解决的问题。

而且栈里面保持一个规律：

**温度递减。**

```Plain Text
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    n = len(temperatures)      
    result = [0] * n      
    # 存储还没有找到更高温度的日期下标     
    stack = []      
    
    for i in range(n):          
        # 当前温度比栈顶日期温度高         
        # 说明栈顶日期的问题解决了         
        while stack and temperatures[i] > temperatures[stack[-1]]:             
            prev_index = stack.pop()             
            result[prev_index] = i - prev_index          
            # 当前日期先放进去，等待未来解决         
        stack.append(i)      
    return result
            
```

