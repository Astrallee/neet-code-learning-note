# Day 7 

## 题目  1  ：Best Time to Buy and Sell Stock

You are given an integer array `prices` where `prices[i]` is the price of NeetCoin on the `ith` day\.

You may choose a **single day** to buy one NeetCoin and choose a **different day in the future** to sell it\.

Return the maximum profit you can achieve\. You may choose to **not make any transactions**, in which case the profit would be `0`\.

**Example 1:**

```Java
Input: prices = [10,1,5,6,7,1]Output: 6
```

Explanation: Buy `prices[1]` and sell `prices[4]`, `profit = 7 - 1 = 6`\.

**Example 2:**

```Java
Input: prices = [10,8,7,5,2]Output: 0
```

Explanation: No profitable transactions can be made, thus the max profit is 0\.

**Constraints:**

- `1 <= prices.length <= 100`

- `0 <= prices[i] <= 100`

**思路： **

给定一个整数数组 prices，其中 prices\[i\] 表示第 i 天 NeetCoin 的价格。在某一天卖了之后选择另一天去卖。返回能获得的最大利润。

哦！这个题！首先确定的是这个并没有要index 只要利润  那是不是可以排序？应该不能排序吧 时间本身就有序。

第一个暴力法：

就是把这个index 以及后面所有的index都过一遍\. 如果后面都比买的那天小就不卖了 默认是0

```Plain Text
def maxProfit(self, prices: List[int]) -> int:
    length = len(prices)
    max_profit =0
    for index,item in enumerate(prices[:length-1]):
        for price in prices[index+1:]:
            profit = price- item
            max_profit  = max(max_profit ,profit )
    return max_profit 
```

第二个 一次遍历 \+ 状态维护（Greedy / 贪心）： 之前天练习过了每次产生一个新的切片 会浪费不必要的空间

就是要找到最大值 以及最大值之前出现的最小值。  

```Plain Text
def maxProfit(self, prices: List[int]) -> int:
    min_price = prices[0]
    max_profit =0
    
    for index,item in enumerate(prices):
        profit = item-min_price
        min_price = min(min_price,item)
        max_profit = max(profit ,max_profit )
         
    return max_profit
            
```

## 题目  2  ：Longest Substring Without Repeating Characters

Given a string `s`, find the *length of the longest substring* without duplicate characters\.

A **substring** is a contiguous sequence of characters within a string\.

**Example 1:**

```Java
Input: s = "zxyzxyz"Output: 3
```

Explanation: The string `"xyz"` is the longest without duplicate characters\.

**Example 2:**

```Java
Input: s = "xxxx"Output: 1
```



**Constraints:**

- `0 <= s.length <= 1000`

- `s` may consist of printable ASCII characters\.

**思路： **

找这个字符串里最长的不重复字符的长度

遍历这个字符串， 没有在里面的加进去 ，如果有重复的了就开始重新找。

```Java
def lengthOfLongestSubstring(self, s: str) -> int:

    new_s = ""
    max_length = 1
    max_str = ""
    if len(s)<=0:
        return 0
    for char in s:
        if char in new_s:
            new_s = ""+char 
        else:
            new_s +=char
        max_length  = max(max_length ,len(new_s))

    return max_length  
```

这个方案不行， 遇到一个问题是 重复的和重复之间隔了很多个数，不应该彻底重找而是从这个后面的 开始记录。

所以类似于是个队列  遇到重复的先进先出。

比如dvdf  走到第二个d ，把第一个d pop出去 滑动窗口一样的东西

那就是一个指针指向头，一个指针指向尾部继续遍历， 当遇到一个就判断一下\[head:tail\]有没有重复的 如果有 就移动head 。

```Python
def lengthOfLongestSubstring(self, s: str) -> int:
    window = set()
    max_length = 0
    head= 0
    for tail in range(len(s)):
        while s[tail] in window:
            window.remove(s[head])
            head+=1
        window.add(s[tail])
        max_length = max(max_length, tail-head+1)

    return max_length
```

## 题目  3  ：Longest Repeating Character Replacement

You are given a string `s` consisting of only uppercase english characters and an integer `k`\. You can choose up to `k` characters of the string and replace them with any other uppercase English character\.

After performing at most `k` replacements, return the length of the longest substring which contains only one distinct character\.

**Example 1:**

```Java
Input: s = "XYYX", k = 2Output: 4
```

Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's\.

**Example 2:**

```Java
Input: s = "AAABABB", k = 1Output: 5
```

**Constraints:**

- `1 <= s.length <= 100,000`

- `0 <= k <= s.length`

- `s` consists of only uppercase English characters\.

**思路：**

一个字符串组成全是大写的英文字母，给一个k,  从字符串中选出最多k个字符 并替换任何其他的大写英文字符

最多执行k次， 返回那个 包含一个字符的子字符串最大长度。

比如  s = "XYYX", k = 2  选两个，替换两次  X X X X   /  YYYY  

比如  s = "AAABABB", k = 1  替换的是index=3的B  。

上一个题是窗口里面不能有重复字符。

这个：窗口里面允许重复，但是经过 k 次替换后，整个窗口必须变成同一个字符。

一个窗口什么时候合法？假设窗口长度window\_len  里面出现次数最多的字符数量：max\_count

比如：AAABABB     窗口选了 AAABAB  A:4 B：2  想要都变成A 最少k 是2\.
需要替换数量 = 窗口长度 \- 窗口内最高频字符数量

然后题目要求的就是 这个字符串最大长度 也就是窗口长度
 窗口长度  = 需要替换数量\+这个窗口内最高频字符数量
也就说   window\_len \- max\_count \<= k 窗口就是合法的 ，维持一个滑动窗口



```Plain Text
def characterReplacement(self, s: str, k: int) -> int:
    left = 0
    count = {}
    max_count = 0
    result = 0
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])
        while (right - left + 1) - max_count > k:             
            count[s[left]] -= 1             
            left += 1
        result = max(result, right - left + 1)
    return result
```



