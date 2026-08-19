# Day15

## 题目  1  ：Search in Rotated Sorted Array

You are given an array of length `n` which was originally sorted in ascending order\. It has now been **rotated** between `1` and `n` times\. For example, the array `nums = [1,2,3,4,5,6]` might become:

- `[3,4,5,6,1,2]` if it was rotated `4` times\.

- `[1,2,3,4,5,6]` if it was rotated `6` times\.

Given the rotated sorted array `nums` and an integer `target`, return the index of `target` within `nums`, or `-1` if it is not present\.

You may assume all elements in the sorted rotated array `nums` are **unique**,

A solution that runs in `O(n)` time is trivial, can you write an algorithm that runs in `O(log n) time`?

**Example 1:**

```Java
Input: nums = [3,4,5,6,1,2], target = 1Output: 4
```

**Example 2:**

```Java
Input: nums = [3,5,6,0,1,2], target = 4Output: -1
```

**Constraints:**

- `1 <= nums.length <= 1000`

- `-1000 <= nums[i] <= 1000`

- `-1000 <= target <= 1000`

- All values of `nums` are **unique**\.

- `nums` is an ascending array that is possibly rotated\.



### **思路：**

给了一个长度为n的数组，总是增序。旋转1\~n次，

旋转四次变成\[3,4,5,6,1,2\]  将数组旋转 4 次会把数组末尾的四个元素移到开头

旋转六次 变成  \[1,2,3,4,5,6\] 旋转 6 次则会还原为原始数组。

给你一个数组nums,和一个target ， 返回这个target对应的index。 如果没有就是\-1\.

这个题跟前一个类似 前一个找最小值，这个找target\.



这个是增序，那么就找区间呗。

比如 mid == target   return mid

mid\< target  ，mid \> right  说明在mid右边存在下降， 在 mid:right里面存在一个小的增序  ，  这边不会找到对应的数据    right = mid\-1

mid \>target  mid\>right，在mid右边存在下降， target 说不定在里面   left = mid\+1

mid\<target  mid\<right， 说明 在mid右边是上升的。  target在这里面  left = mid\+1

Mid \>target  mid\<right  在右边上升， target 在左边， right = mid\-1



```Plain Text
def search(self, nums: List[int], target: int) -> int:

    n = len(nums)
    
    left = 0
    right = n-1
    
    while left<=right:
        mid = left + (right-left)//2
        
        if nums[mid]==target:
            return mid
        
        if nums[mid]>nums[right]:  # 左边有序
            if nums[left] <= target < nums[mid]:
                right= mid-1
            else:
                left = mid+1
        
        else: # 右边有序
            if nums[mid]<target<= nums[right]:
                left = mid+1
            else:
                right= mid-1

    return -1
```





## 题目  2  ：Time Based Key\-Value Store

Design a time\-based key\-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp\.

Implement the `TimeMap` class:

- `TimeMap()` Initializes the object of the data structure\.

- `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`\.

- `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`\. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`\. If there are no values, it returns `""`\.

**Example 1:**

```Java
Input:["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]Output:[null, null, "happy", "happy", null, "sad"]Explanation:TimeMap timeMap = new TimeMap();
timeMap.set("alice", "happy", 1);  *// store the key "alice" and value "happy" along with timestamp = 1.*
timeMap.get("alice", 1);           *// return "happy"*
timeMap.get("alice", 2);           *// return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.*
timeMap.set("alice", "sad", 3);    *// store the key "alice" and value "sad" along with timestamp = 3.*
timeMap.get("alice", 3);           *// return "sad"*
```

**Constraints:**

- `1 <= key.length, value.length <= 100`

- `key` and `value` only include lowercase English letters and digits\.

- `0 <= timestamp <= 10^7`

- All the timestamps of `set` are strictly increasing\.

- At most `2 * 10^5` calls will be made to `set` and `get`\.

### **思路：**



设计一个基于时间的 key\-value 数据结构，不同的时间戳为同一个key可以存放多个value，并能检索特定时间戳下的键对应的值。



