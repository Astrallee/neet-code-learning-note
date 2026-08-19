# Day4

## 题目  1  ：Longest Consecutive Sequence

Given an array of integers `nums`, return *the length* of the longest consecutive sequence of elements that can be formed\.

A *consecutive sequence* is a sequence of elements in which each element is exactly `1` greater than the previous element\. The elements do *not* have to be consecutive in the original array\.

You must write an algorithm that runs in `O(n)` time\.

**Example 1:**

```Java
Input: nums = [2,20,4,10,3,4,5]Output: 4
```

Explanation: The longest consecutive sequence is `[2, 3, 4, 5]`\.

**Example 2:**

```Java
Input: nums = [0,3,2,5,4,6,1,1]Output: 7
```

**Constraints:**

- `0 <= nums.length <= 1000`

- `-10^9 <= nums[i] <= 10^9`

**思路： **

连续序列是指每个元素都比前一个元素大 1 的序列。这些元素在原数组中**不必是连续的**。

一个nums 数组，找到这个数组里面最长连续序列，返回这个长度。

审题：**不必是连续的**



```Plain Text
def longestConsecutive(self, nums: List[int]) -> int:
    length =len(nums)
    if length <=1:
        return length 
    new_nums = sorted(nums)
    order_len = 1
    max_order_len = 1
    for index in range(1,length):
        if new_nums[index] == new_nums[index-1]+1:
            order_len +=1
            
        elif new_nums[index] == new_nums[index-1]:
            continue
        else:
            order_len = 1
        max_order_len = max(max_order_len, order_len)
    return max_order_len  
```

**解析：**

如果用set的话 有一个更好的解法。

```Python
def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # 只有没有前驱的数字，才作为起点
        if num - 1 not in num_set:
            current = num
            length = 1

            # 不断寻找后面的连续数字
            while current + 1 in num_set:
                current += 1
                length += 1

            max_length = max(max_length, length)

    return max_length
```

