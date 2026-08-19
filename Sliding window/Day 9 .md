# Day 9 

## 题目  1  ：Sliding Window Maximum

You are given an array of integers `nums` and an integer `k`\. There is a sliding window of size `k` that starts at the left edge of the array\. The window slides one position to the right until it reaches the right edge of the array\.

Return a list that contains the maximum element in the window at each step\.

**Example 1:**

```Java
Input: nums = [1,2,1,0,4,2,6], k = 3
Output: [2,2,4,4,6]
Explanation:
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
1 [2  1  0] 4  2  6         2
1  2 [1  0  4] 2  6         4
1  2  1 [0  4  2] 6         4
1  2  1  0 [4  2  6]        6
```

**Constraints:**

- `1 <= nums.length <= 100,000`

- `-10,000 <= nums[i] <= 10,000`

- `1 <= k <= nums.length`

**思路： **
一个整数数组 nums 一个整数k  有一个大小为k的滑动窗口  从数组的左边开始  每次向右滑动一个位置，直到到达数组的右边。  题目让返回一个列表  其中包含每次滑动过程中窗口最大元素。

比如示例  list\(nums \)  长度是7，k=3 ，那么滑动次数  7\-3\+1 = 5  也就是 n\-k\+1 （也可以多些例子测下这个结论）

对不起我又只能想到暴力

```Plain Text
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    
    len_nums = len(nums)
    if len_nums <=k:
        max_item = nums[0]
        for item in nums:
            max_item =max(max_item,item)
        return [max_item]
    
    left = 0
    max_lsit = []

    if k ==1:
        return nums
    else:
        right = k+left-1
        
    while right <=len_nums-1:
        max_num = nums[left]
        for num in nums[left:right+1]:
            max_num = max(max_num,num)
        max_lsit.append(max_num)
        
        right+=1
        left+=1
    return max_lsit
```



**优化：**

有点乱就先把思路写出来， 

虽然每次问窗口内谁最大 但是实际上就跳了一个格。 就是判断新增的那个数有没有大于前一个窗口的最大值 如果没有 就继续往下跳 如果有就取代这个最大值。但是注意  这个最大值的时效问题 就是这个最大值的index 一定要大于left   ，比如\[1,2,1,0,1,2,6\] k=3  当滑动窗口走到\[1,0,1\]  前一个窗口最大值是2  但是index\<left 



不要每次重新扫描整个窗口。

单调队列（deque）维护一个队列：里面存：**可能成为最大值的元素下标**不是存所有元素。

```Plain Text
from collections import deque  

def maxSlidingWindow(nums, k):     
    q = deque()     
    res = []
    
    for right in range(len(nums)):
        while q and q[0]<right-k+1:
            q.popleft()
        while q and nums[q[-1]] <=nums[right]:
            q.pop()
        
        q.append(right)
        
        if right>=k-1:
            res.append(nums[q[0]])
    return res
```



