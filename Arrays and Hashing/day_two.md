# Day2   

## 题目  1  ：Group Anagrams

Given an array of strings `strs`, group all *anagrams* together into sublists\. You may return the output in **any order**\.

An **anagram** is a string that contains the exact same characters as another string, but the order of the characters can be different\.

**思路： **

一个字符串数组，分组分到子列表。 这个就是对这个字符串进行分类， 参考之前题目Valid Anagram 的处理方式。

那就是遍历一个list, 然后每个item都跑一下？ 是不是有点暴力了。

每个字符串 \-\> 算一个分类标识 \-\> 放入对应组

```Plain Text

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    new_dict = {}
    new_strs=[]
    for index,item in enumerate(strs):
        if sorted(item) in new_dict.keys():
            new_dict[sorted(item)].append(item)
        else:
            new_dict[sorted(item)] = [item]
    for key,value in new_dict.items():
        new_strs.append(value )
    return new_strs
                
```

**解析：**

有几个优化点。 

1. if sorted\(item\) in new\_dict\.keys\(\):   可以直接：  if sorted\(item\) in new\_dict:

2. 最大的问题 sorted\(item\)调用的太多了，不用排那么多次。同时有个需要注意的是sorted得到的是一个list \[\] ！

3. 写法可以再优雅一点，想到什么写什么的话 整体不好看。

```Python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    new_dict = {}
    for index,item in enumerate(strs):
        key_sorted = ''.join(sorted(item))
        if key_sorted not in new_dict:             
            new_dict[key_sorted ] = []
        new_dict[key_sorted].append(item)
    
    return list(new_dict.values())
     
```

## 题目  2  ：Top K Frequent Elements

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements within the array\.

The test cases are generated such that the answer is always **unique**\.

You may return the output in **any order**\.

**思路： **

一个数组 一个整数k, 返回数组中出现频率最高的k个元素。其实就是把数组里面的数做个统计，然后选取top\_k个数。

```Plain Text
result = {}
for num in nums:
    result[num] = result.get(num, 0) + 1
sorted_dict = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))

return list(sorted_dict.keys())[:k] 
```

**解析：**有几个优化点。 

用了排序sorted\_dict = dict\(sorted\(result\.items\(\), key=lambda x: x\[1\], reverse=True\)\) 复杂度：

统计：O\(n\)  排序：O\(m log m\)   总：O\(n \+ mlogm\)

更好的方案：小顶堆。不过这题 NeetCode 常用的是 **桶排序 Bucket Sort**。

已知每个元素出现次数，找出现次数最高的 k 个。区别在于：

- **堆（Heap）**：适合“只要 Top K”，不用关心全部排序。 

- **桶排序（Bucket Sort）**：利用“频率范围有限”，直接按频率取。

1. 小顶堆（Min Heap）

假设   nums = \[1,1,1,2,2,3\]   k = 2  统计：count = \{     1:3,     2:2,     3:1 \}

如果排序 的话 k很小，比如1000个里面 取一个，全都排一遍就很浪费。

只维护一个大小为 k 的堆 ，堆里面存\(频率, 数字\)

```Plain Text
import heapq
count = {}
for num in nums:
    count[num] = count.get(num,0)+1
heap = []
for num, freq in count.items():
    heapq.heappush(heap,(freq,num))

    if len(heap) > k:
        heapq.heappop(heap)

return [num for freq,num in heap]
```

2. 桶排序（Bucket Sort）

一个数字出现次数最多是多少？n。

nums=\[1,1,1,2,2,3\]   频率范围： 1\~6

所以建立桶：  数组下标代表频率。  频率 \-\> 一堆数字

bucket = \[  \[\],  \[3\],  \[2\],  \[1\],  \[\],  \[\],  \[\] \]

bucket\[1\] = 出现1次的数字   bucket\[2\] = 出现2次的数字      bucket\[3\] = 出现3次的数字

然后倒着遍历，取够 k 个停止。

```Plain Text
count = {}  
for num in nums:     
    count[num] = count.get(num,0)+1 

bucket = [[] for _ in range(len(nums)+1)]    //len+1个桶  按照次数来

for num, freq in count.items():     
    bucket[freq].append(num)
res = []  
for freq in range(len(bucket)-1,0,-1):     # 倒叙查找
    for num in bucket[freq]:         
        res.append(num)          
        if len(res) == k:             
            return res
```

## 题目  3  ：Encode and Decode Strings

Design an algorithm to encode **a list of strings** to **a string**\. The **encoded string** is then sent over the network and is **decoded** back to the **original list** of strings\.

**Machine 1 \(sender\)** has the function:

```Java
String encode(List<String> strs) {*// ... your code*return encoded_string;}
```

**Machine 2 \(receiver\)** has the function:

```Java
List<String> decode(String encoded_string) {*// ... your code*return decoded_strs;}
```

So **Machine 1** does:

```Java
String encoded_string = encode(strs);
```

and **Machine 2** does:

```Java
List<String> decoded_strs = decode(encoded_string);
```

`decoded_strs` in Machine 2 should be the **same** as the input `strs` in Machine 1\.

Implement the `encode` and `decode` methods\.

**思路： **

题目：设计一个算法，把一个字符串列表encode成一个字符串，然后decode 方：把这个字符串decode成原来的字符串list。

1. 需要考虑信息不能丢失的问题， 那么就是全部的字符都需要保留。

2. 保留信息断点问题（每个字符串在哪里结束） 比如 hi morning\. 断句点需要知道

3. 选择这个结束的标识符应该考虑下特殊字符可能会在输入中本身就存在。

那么可能的思考方向就是：
能不能在编码的时候，额外记录一些信息，比如 长度\+内容？或者编码的时候给一些结构信息

位置\_数量\+item\_1 \+位置\_数量\+item\_2？

```Python
def encode(self, strs: List[str]) -> str:
    strs_str = ""
    if len(strs)>=1:
        for index,item in enumerate(strs):
            strs_str += index+"_"+str(len(item))+item
        return strs_str 
     else  :
         return ""  
```

**解析： **

可以是可以啊，但是**index 其实是不需要的**。长度 \+ 内容就够了， 加一个\_也会让整个协议复杂化。

长度可能是两位数甚至更多位。**内容本身也可能是数字。  给长度加边界。**

长度\+\#\+内容

```Python
def encode(self, strs: List[str]) -> str:
    strs_str = ""
    if len(strs)>=1:
        for index,item in enumerate(strs):
            strs_str += str(len(item))+"#"+item
        return strs_str 
     else  :
         return ""  
```

**思路：**

解码的时候 就不能简单正则去切分，而是需要加一个验证，比如我们找到的分割是否符合我们的“数量xxx\(内容\)”

维护一个指针 `i` \-\>从 `i` 开始读取数字，得到长度 \-\>根据长度截取字符串\-\>移动指针继续

**长度可能是两位数甚至更多位。内容本身也可能是数字。**

```Plain Text
def decode(self, s: str) -> List[str]:
    strs_list = []
    i = 0
    while i <len(s):
        j = i
        # 找长度结束位置         
        while s[j] != "#":            
            j += 1
        length = int(s[i:j])
        i = j + 1
        item = s[i:i+length]
        strs_list.append(item)
        i += length
     return strs_list
    
```

