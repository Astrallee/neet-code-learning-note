# Day1   Arrays and Hashing

## 题目  1  ：Contains Duplicate

Given an integer array `nums`, return `true` if any value appears **more than once** in the array, otherwise return `false`\.

**思路： **

粗暴点的：一个新的遍历这个数组， 如果出现一个值在这个新的list里出现了就退出遍历返回true\.

```Plain Text
nums_list = []
for item in nums:
    if item in nums_list:
        return true
    else:
        nums_list.append(item)
 return false
```

**解析：**

逻辑没有问题，但是效率不行。查找是O\(n\)，最外层也遍历了n次， 最坏是O\(n^2\)，用哈希表。  **set（哈希表） 哈希表查找是O\(1\)\.**

```Plain Text
seen = set()

for item in nums:
    if item in seen:
        return True
    seen.add(item)

return False
```

小结：总是忘记哈希表！！总习惯用列表遍历！！





## 题目  2  ：Valid Anagram\(异位词 / 字母重排\)

Given two strings `s` and `t`, return `true` if the two strings are anagrams of each other, otherwise return `false`\.

An **anagram** is a string that contains the exact same characters as another string, but the order of the characters can be different\.

**思路： anagram 指两个字符串里面的字符种类和数量完全一样，但是顺序可以不同。**

粗暴点的：

1. 两个字符串里面的每一个字符都可以在另一个找到。那么可以把字符串一个个进行匹配， 比如s的某一个字符只要出现在t里，那么就过了。

2. 两个字符串长度应该也一致

3. 字符的数量也要一样   对出现的每个字符进行count 

大概就是对每个字符串整一个dict  \{“字符”：“数量”\} 比一下keys\(\)一不一样，然后对应数量一不一样。

```Plain Text
result_t = {}
result_s = {}
for char1 in s:
    result_t[char1] = result_t.get(char1 , 0) + 1
for char2 in t:
    result_s[char2] = result_s.get(char2, 0) + 1
    
for key , value in result_t.items():
    if key not in result_s.keys():
        return False
    if value != result_s.get(key):
        return False
return True
```

**解析：**

1. 其实不用判断 if key not in result\_s\.keys\(\)， 是上面列举满足条件的惯性思维，因为没在这个里面 那么result\_s\.get\(key\) 就拿不到那个数已经满足不相等了。

2. 需要长度校验，上面这个解法出现一个问题，示例：s = "a" t = "ab"    这样的情况就容易被错判。

需要加一个 if len\(s\) \!= len\(t\):     return False

```Python
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    result_t = {}
    result_s = {}
    for char1 in s:
        result_t[char1] = result_t.get(char1 , 0) + 1
    for char2 in t:
        result_s[char2] = result_s.get(char2, 0) + 1
        
    for key , value in result_t.items():
        if value != result_s.get(key,0):
            return False
    return True
```

3. 还有一个解法是排序解法。 **anagram 只关心字符和数量，不关心顺序**。 那么就需要对两个str进行重排序。排序后一样，说明字符和数量一样。

```Python
def isAnagram(s, t):     
    if len(s) != len(t):         
        return False      
    return sorted(s) == sorted(t)
```

复杂度：`sorted()` 底层一般是 O\(nlogn\)  所以：时间：O\(nlogn\) 空间：O\(n\)（因为生成排序后的数组）

另外一个小点：Python 的 `sorted()` 返回的是 list，不会修改原字符串，因为字符串不可变。

## 题目  3  ：Valid Anagram\(异位词 / 字母重排\)

