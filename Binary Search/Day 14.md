# Day 14

## 题目  1  ：Koko Eating Bananas

You are given an integer array `piles` where `piles[i]` is the number of bananas in the `ith` pile\. You are also given an integer `h`, which represents the number of hours you have to eat all the bananas\.

You may decide your bananas\-per\-hour eating rate of `k`\. Each hour, you may choose a pile of bananas and eats `k` bananas from that pile\. If the pile has less than `k` bananas, you may finish eating the pile but you can not eat from another pile in the same hour\.

Return the minimum integer `k` such that you can eat all the bananas within `h` hours\.

**Example 1:**

```Java
Input: piles = [1,4,3,2], h = 9   Output: 2
```

Explanation: With an eating rate of 2, you can eat the bananas in 6 hours\. With an eating rate of 1, you would need 10 hours to eat all the bananas \(which exceeds h=9\), thus the minimum eating rate is 2\.

**Example 2:**

```Java
Input: piles = [25,10,23,4], h = 4   Output: 25
```

**Constraints:**

- `1 <= piles.length <= 10,000`

- `piles.length <= h <= 1,000,000,000`

- `1 <= piles[i] <= 1,000,000,000`



### **思路：**

有一个整数数组piles      `piles[i]`  的第i个堆的香蕉数量。 同样给了你一个整数h   代表你必须吃掉所有数量香蕉的时间。  设定每小时吃k个 ，如果这堆香蕉少于k个 你就能吃完这个pile, 但是不能吃其他pile\.

返回能让你在 `h` 小时内吃完所有香蕉的最小整数 `k`。

piles = \[1,4,3,2\], h = 9          

如果每小时 吃两个，     第一个pile 一小时  第二、三个pile分别两个小时 最后一个pile一个小时    那么  总共time=1\+2\+2\+1=6  \<9 可以吃完。

Time = pile\[0\]/k \+ pile\[1\]/k\+\.\.\.\.\+pile\[i\]/k

找到最小的一个k 可以满足 time\<=h

有个隐含的是 就算 这个k = max\(pile\[i\]\), min\_time = len\(pile\)

这个数字可以从小到大排序 顺序没有强制要求 

如果给的h  = len\(pile\) 选择 max\(pile\[i\]\)

如果 h\>len\(pile\)    k就可以在0\~max\(pile\[i\]\)   里找 那么这个就可以利用二分法 找得快\.



```Plain Text
def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
    n = len(piles)
    piles_new = sorted(piles)
    if n==h:
        # 找这个piles最大值
        return piles_new[-1]
    else:
        #h>n 
        min_k = piles_new[-1]
        
        left = 1
        right = min_k - 1
        
        while left<=right:
            mid = left+(right-left)//2
            hours =0
            for item in piles:
                time = math.ceil(item /mid)
                hours +=time 
            
            ## 再找有没有更小的
            if hours <= h:
                right = mid-1
                min_k = min(min_k ,mid)
            if hours > h:
                left = mid +1
        return min_k 
            
                
```





## 题目  2  ：Find Minimum in Rotated Sorted Array

You are given an array of length `n` which was originally sorted in ascending order\. It has now been **rotated** between `1` and `n` times\. For example, the array `nums = [1,2,3,4,5,6]` might become:

- `[3,4,5,6,1,2]` if it was rotated `4` times\.

- `[1,2,3,4,5,6]` if it was rotated `6` times\.

Notice that rotating the array `4` times moves the last four elements of the array to the beginning\. Rotating the array `6` times produces the original array\.

Assuming all elements in the rotated sorted array `nums` are **unique**, return the minimum element of this array\.

A solution that runs in `O(n)` time is trivial, can you write an algorithm that runs in `O(log n) time`?

**Example 1:**

```Java
Input: nums = [3,4,5,6,1,2]Output: 1
```

**Example 2:**

```Java
Input: nums = [4,5,0,1,2,3]Output: 0
```

**Example 3:**

```Java
Input: nums = [4,5,6,7]Output: 4
```

**Constraints:**

- `1 <= nums.length <= 1000`

- `-1000 <= nums[i] <= 1000`



### **思路：**

有一个数组 长度为n 总是增序，旋转1\~n次。 

`nums = [1,2,3,4,5,6]`  

旋转四次变成\[3,4,5,6,1,2\]  将数组旋转 4 次会把数组末尾的四个元素移到开头

旋转六次 变成  \[1,2,3,4,5,6\] 旋转 6 次则会还原为原始数组。

假设旋转后的有序数组 `nums` 中的所有元素均不重复，请返回该数组中的最小元素。



找到第一个 index  满足 nums\[index\]\<nums\[index\-1\]   index 就是旋转次数

N\-index ：n  都是小的增序    0：index是大的增序数列

题目要求O\(logn\)很明显要求二分法

如果nums\[mid\] \> nums\[right\]  那么 在mid右边存在下降 最小值一定在：\[mid\+1,right\]

nums\[mid\] \< nums\[right\]    mid到right已经递增。最小值可能就是mid。或者 \[left:mid\]

```Plain Text
def findMin(self, nums: List[int]) -> int:
    n = len(nums)
    left = 0
    right = n-1
    
    while left<right：
        mid = left + (right-left)//2
        
        if nums[mid]>nums[right]:
            left = mid+1
        else:
            right = mid
     return nums[left]  
            
```

另一个写法

```SQL
def findMin(self, nums: List[int]) -> int:
    left = 0
    right = len(nums)-1
    ans = nums[0]

    while left <= right:
        mid = left + (right-left)//2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            ans = min(ans, nums[mid])
            right = mid - 1

    return ans
```



