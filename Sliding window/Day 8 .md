# Day 8 

## 题目  1  ：Permutation in String

You are given two strings `s1` and `s2`\.

Return `true` if `s2` contains a permutation of `s1`, or `false` otherwise\. That means if a permutation of `s1` exists as a substring of `s2`, then return `true`\.

Both strings only contain lowercase letters\.

**Example 1:**

```Java
Input: s1 = "abc", s2 = "lecabee"Output: true
```

Explanation: The substring `"cab"` is a permutation of `"abc"` and is present in `"lecabee"`\.

**Example 2:**

```Java
Input: s1 = "abc", s2 = "lecaabee"Output: false
```

**Constraints:**

- `1 <= s1.length, s2.length <= 1000`



**思路： **
长字符串的截取window中: 1\. 满足有短的字符串里所有的字符  2\.不能隔空  必须相连     3\.不在乎字符顺序  4\.window长度就是等于短的字符串的



ps：挺好的 过个周末回来就是这样脑袋转不动 只能暴力  暴力万岁 暴力解决一切

```Plain Text
def count_s(s):
    count ={}
    for item in s:
        if count.get(item, 0) ==0:
            count[item] = 1
        else:
            count[item] += 1
    return count 


def checkInclusion(self, s1: str, s2: str) -> bool:
    len_s1 = len(s1)
    len_s2 = len(s2)
    
    count_s1 = count_s(s1)
    
    left = 0
    for right in range(len_s1-1,len_s2):
        count_short = count_s(s2[left:right+1])
        if count_short == count_s1:
            return True
        else:
            left+=1
    
    return False
            
```

**优化：**

这章一直在讲 滑动窗口 ，那就是利用窗口滑动 ，更新进出的元素 

比如新进来的元素 累计超过了要求的 需要滑动   如果没有就不滑了就找到了



```Python
def checkInclusion(self, s1: str, s2: str) -> bool:
    len_s1 = len(s1)
    len_s2 = len(s2)
    if len_s1 > len_s2:         
        return False
    count_s1 = {}     
    for char in s1:         
        count_s1[char] = count_s1.get(char, 0) + 1   
        
        
    window = {}     
    left = 0
    for right in range(len_s2):
        # 加入右边字符         
        window[s2[right]] = window.get(s2[right], 0) + 1
        
        # 保持窗口长度等于 s1长度         
        if right - left + 1 > len_s1:
            left_char = s2[left]             
            window[left_char] -= 1
            if window[left_char] == 0:                 
                del window[left_char]
            left += 1 
        # 判断当前窗口是否满足排列         
        if window == count_s1:             
            return True
    return False
```

## 题目  2  ：Minimum Window Substring

Given two strings `s` and `t`, return the shortest **substring** of `s` such that every character in `t`, including duplicates, is present in the substring\. If such a substring does not exist, return an empty string `""`\.

You may assume that the correct output is always unique\.

**Example 1:**

```Java
Input: s = "OUZODYXAZV", t = "XYZ"Output: "YXAZ"
```

Explanation: `"YXAZ"` is the shortest substring that includes `"X"`, `"Y"`, and `"Z"` from string `t`\.

**Example 2:**

```Java
Input: s = "xyz", t = "xyz"Output: "xyz"
```

**Example 3:**

```Java
Input: s = "x", t = "xy"Output: ""
```

**Constraints:**

- `1 <= s.length <= 1000`

- `1 <= t.length <= 1000`

- `s` and `t` consist of uppercase and lowercase English letters\.



**思路： **

两个字符串 s和t，返回 s 的最短子串，使得 t 中的每个字符（包括重复字符）都包含在该子串中。如果这样的子串不存在，则返回空字符串 ""。

s = "OUZODYXAZV", t = "XYZ"     

Output: "YXAZ"

从示例看 不要求顺序 只要有就够了

那就遍历s 发现一个char 同时也在t 就打个标记。

就是在s里面找t的一个字符，找到了就放一个left指针，然后right指针再遍历s找t的第二个、第三个\.\.\.第n个。  最后子串就是 【left：right】。

右指针不断扩大，让窗口满足条件。满足后： 左指针收缩，尝试变短。

```Plain Text
def minWindow(self, s: str, t: str) -> str:
     len_s = len(s)
     len_t = len(t)
     if len_s <len_t:
         return ""
     count_t = {}
     for item in t:     
         count_t [item] = count_t .get(item, 0) + 1
     
     need =len_t
     left = 0
     window_char_count = {}
     res = ""
     for right in range(len_s):
         # 第一个数 先加到window窗口计数
         item = s[right]
         window_char_count[item] = window_char_count.get(item,0)+1
         # 如果这个数就是在t里 并且目前窗口里的字符数量≤ t里对应的数量
         if item in count_t and window_char_count[item]<=count_t[item]
             need -=1
         # 全部的数都找到了， 如果这个时候s还没遍历完那么就尝试找最短的
         while need ==0:
             if not res or right-left+1<len(res):
                 res = s[left:right+1]
             
             left_char = s[left]
             window_char_count[left_char] -=1
             
             if left_char in count_t and window_char_count[left_char]<count_t[left_char]:
                 need+=1
             left+=1
     return res
         
```



