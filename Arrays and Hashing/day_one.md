

# Day1   

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



## 题目  3  ：Two Sum

Given an array of integers `nums` and an integer `target`, return the indices `i` and `j` such that `nums[i] + nums[j] == target` and `i != j`\.

You may assume that *every* input has exactly one pair of indices `i` and `j` that satisfy the condition\.

Return the answer with the smaller index first\.

**思路：**题目说可以解析每一个输入都恰好存在一对，那么边界问题（比如数组只有一个数）就可以暂时不考虑。

那么就是遍历这个数组？ 比如 i， 那么就看target\-nums\[i\]在不在剩余的 nums\[i:\]里面。在的话就返回对应索引。

```Plain Text
for index in range(0,len(nums)):
    value = target - nums[index]
    if value in nums[index+1:]:
        second_index = nums[index+1:].index(value) + index +1
        return [index,second_index]
```

**解析：**

思路**正确**，是暴力优化版。但是有优化问题，if value in nums\[index\+1:\] 切片会创建新数组，O\(n\)。

nums\[index\+1:\]\.index\(value\) 又遍历一次，O\(n\)。  整体时间复杂度是 O\(n²\) 。更好的方案是用 hash 表。

不去找当前数字需要的另一个数字，而是遍历的时候记住之前有哪些数字，位置在哪。

比如：nums=\[2,7,11,15\]   target=9

遍历 2：  9\-2=7  之前没有 就记录 \{2:0\},

遍历到7 ，9\-7=2，查一下 2 在没在，发现2在记录里。 返回\[0,1\]。

比如： nums = \[4,5,6\], target = 10

遍历 4： 10\-4=6 ，啥也没有 记录\{4:0\}

遍历5： 10\-5 = 5，没有 记录\{5:1\}

遍历6： 10\-6 = 4，发现4 ，返回\[0,2\]

```Plain Text
seen = {}
for i,num in enumerate(nums):
    need = target - num
    if need in seen:
        return [seen[need],i]
    seen[num]=i
```









