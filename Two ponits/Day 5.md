# Day 5

## 题目  1  ：Valid Palindrome

Given a string `s`, return `true` if it is a **palindrome**, otherwise return `false`\.

A **palindrome** is a string that reads the same forward and backward\. It is also case\-insensitive and ignores all non\-alphanumeric characters\.

**Note:** Alphanumeric characters consist of letters `(A-Z, a-z)` and numbers `(0-9)`\.

**Example 1:**

```Java
Input: s = "Was it a car or a cat I saw?"Output: true
```

Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome\.

**Example 2:**

```Java
Input: s = "tab a cat"Output: false
```

Explanation: "tabacat" is not a palindrome\.

**Constraints:**

- `1 <= s.length <= 1000`

- `s` is made up of only printable ASCII characters\.

**思路： **

判断字符串是不是回文字符串。回文是指正读和反读都相同的字符串。它**不区分大小写**，并**忽略所有非字母数字**字符。

注意点：1\.去掉/跳过/忽略 其他不是字母和数字的 字符 ； 2\.字母大小写   3\.字符串长度奇偶。

isalnum\(\) 判断一个字符是不是字母或数字,可以用来去掉标点。

```Plain Text
def isPalindrome(self, s: str) -> bool:
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s +=char.lower()
    length = len(new_s)
    left = 0
    right = length-1
    while left<right:
        if new_s[left]==new_s[right]:
            left+=1
            right-=1
        else:
            return False
    return True
            
```

## 题目  2  ：Two Integer Sum II

Given an array of integers `numbers` that is sorted in **non\-decreasing order**\.

Return the indices \(**1\-indexed**\) of two numbers, `[index1, index2]`, such that they add up to a given target number `target` and `index1 < index2`\. Note that `index1` and `index2` cannot be equal, therefore you may not use the same element twice\.

There will always be **exactly one valid solution**\.

Your solution must use *O*\(1\) additional space\.

**Example 1:**

```Java
Input: numbers = [1,2,3,4], target = 3 Output: [1,2]
```

Explanation:
The sum of 1 and 2 is 3\. Since we are assuming a 1\-indexed array, `index1` = 1, `index2` = 2\. We return `[1, 2]`\.

**Constraints:**

- `2 <= numbers.length <= 1000`

- `-1000 <= numbers[i] <= 1000`

- `-1000 <= target <= 1000`

**思路： **

类似于day1的题目  3  ：Two Sum  ，这里注意的就是 这个序列不是递减的。从index=1 开始计数，找到和是target的两个index,并且index1\<index2，index不能相等。 题目设定 始终有唯一解。

这个是返回index 所以不能排序，排序就乱了。

遇到第一个数，就看集合里有没有，没有就 放里面继续，有就返回。

有个需要注意的  从index=1 开始计数   ！ 所以最后返回时候索引要\+1

```Plain Text
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    seen = {}
    for index,item in enumerate(numbers):
        need = target - numbers[index]
        if need in seen:
            return [seen[need]+1,index+1]
        seen[item]=index
```

**解析：**

**non\-decreasing order  非递减序列= 升序   我前面理解成了乱序的（还好结果没有影响）。**

那升序的情况就是  后面数字\>=前面数字。
也就是 如果 target\- nums\[index\]\<nums\[index\]  就不用往后找了。那其实就是  nums\[index\]一定是小于等于 target/2。  那就是找到target/2

利用数组有序，换成双指针。

```C++
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    i = 0
    j =len(numbers)-1
    while i<j:
        total = numbers[i]+numbers[j]
        if total < target:
            i+=1
        elif total >target:
            j =j-1
        else:
            return [i+1,j+1]
```

**当问题具有单调性（monotonic property）时，可以考虑双指针。**

## 题目  3  ：3Sum

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` where `nums[i] + nums[j] + nums[k] == 0`, and the indices `i`, `j` and `k` are all distinct\.

The output should *not* contain any duplicate triplets\. You may return the output and the triplets in **any order**\.

**Example 1:**

```Java
Input: nums = [-1,0,1,2,-1,-4]Output: [[-1,-1,2],[-1,0,1]]
```

Explanation:
`nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.`
`nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.`
`nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.`
The distinct triplets are `[-1,0,1]` and `[-1,-1,2]`\.

**Example 2:**

```Java
Input: nums = [0,1,1]Output: []
```

Explanation: The only possible triplet does not sum up to 0\.

**Example 3:**

```Java
Input: nums = [0,0,0]Output: [[0,0,0]]
```

Explanation: The only possible triplet sums up to 0\.

**Constraints:**

- `3 <= nums.length <= 1000`

- `-10^5 <= nums[i] <= 10^5`

**思路：**

在一个整数数组中，找三个数   满足nums\[i\] \+ nums\[j\] \+ nums\[k\] == 0  输出结果不能重复，按任意顺序返回输出结果和三元组。 这里只填数就行了， 而且没要求顺序，那就是我们可以改变顺序。

比如  nums = \[\-1,0,1,2,\-1,\-4\]  \-\>排序  new\_nums \[\-4,\-1,\-1,0,1,2\]

其实我觉得这个可以转变一下啊就是 sum2 在找的是两个数恰好等于 target，找到就return true,找不到false\. 

那其实这个题就是遍历nums ， 然后排序变成递增的。  然后遍历new\_nums 一个item 就是在剩下的数组里面找target 为这个 \-item的数！

注意： ***not***** contain any duplicate triplets\.  不能重复的**！ 所以这个new\_nums 遇到重复的item就跳过就好了

```C++
def twoSum(numbers, target):
    result = []
    seen = set() 
    for index,item in enumerate(numbers):
        
        need = target - numbers[index]
        if need in seen:
            pair = [need, item]
            if pair not in result:
                result.append(pair)
        seen.add(item)
    return result
def threeSum(nums):
    final_list = []
    new_nums = sorted(nums)
    seen =set()
    for index,item in enumerate(new_nums ):
        if item in seen :
            continue
        seen.add(item)

        pairs  = twoSum(new_nums [index+1:],-item )
        if pairs :
            for pair  in pairs:
                final_list.append([item]+pair  )
    return final_list
```

**解析：**

整体思路方向是对的，而且已经抓到 3Sum 的核心转化：

> 3Sum = 固定一个数 \+ 在剩余数组里解决 Two Sum
> 
> 

这是正确的。但是代码有几个关键问题。`twoSum` 用哈希可以，但是这里有坑。 

need\_list = twoSum\(new\_nums\[index\+1:\], need\)切片会产生新数组。

每次都会复制一份。复杂度会增加。

可以尝试上面说的 指针方法

```Plain Text
def twoSum(numbers,i,j,target):
    
    result = []
    while(i<j):
        if numbers[i]+numbers[j] ==target:
            pair = [numbers[i],numbers[j]]
            if pair not in result:
                result.append(pair)
            i += 1 
            j -= 1
        elif numbers[i]+numbers[j] >target:
            j=j-1
        else:
            i = i+1
    return result 
    


def threeSum(nums):
    final_list = []
    new_nums = sorted(nums)
    
    length = len(new_nums)
    for index,item in enumerate(new_nums ):
        if index > 0 and new_nums [index] == new_nums [index-1]: 
            continue
        
        target = -item
        pairs= twoSum(new_nums ,index+1,length-1,target )
        if pairs:
            for pair  in pairs:
                final_list.append([item]+pair  )
    return final_list 
        
    
        
```

