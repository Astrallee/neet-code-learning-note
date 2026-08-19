# Day 10

## 题目  1  ：Valid Parentheses

You are given a string `s` consisting of the following characters: `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`\.

The input string `s` is valid if and only if:

1. Every open bracket is closed by the same type of close bracket\.

2. Open brackets are closed in the correct order\.

3. Every close bracket has a corresponding open bracket of the same type\.

Return `true` if `s` is a valid string, and `false` otherwise\.

**Example 1:**

```Java
Input: s = "[]"Output: true
```

**Example 2:**

```Java
Input: s = "([{}])"Output: true
```

**Example 3:**

```Java
Input: s = "[(])"Output: false
```

Explanation: The brackets are not closed in the correct order\.

**Constraints:**

- `1 <= s.length <= 1000`



**思路： **

字符串s都是各种括号组成的， 要验证这个s是不是有效的  ，需要满足：

\(1\)每个左括号都有对应的右括号   成对出现

\(2\)关的顺序应该也相同 比如 \[\(\]\)就是错的

如果这个s满足上面两个情况就是 true ，不然就是false

这个地方考察的应该是栈吧 ， 就遍历字符串 如果是左括号 就append进去， 然后遍历到右括号就把对应的左括号pop出来。

如果pop出来的跟指到的对应的括号 是一对就继续 如果不是就返回false。

```Plain Text
def isValid(self, s: str) -> bool:
    
    len_s = len(s)
    
    stack_list = []
    
    for index in range(len_s):
         if s[index] in "({[":
             stack_list.append(s[index])
         else:
             if not stack:                 
                 return False
                 
             char_bracket = stack_list.pop()
             if s[index] == ')' and char_bracket !="(":
                 return False
             if s[index] == '}' and char_bracket !="{":
                 return False
             if s[index] == ']' and char_bracket !="[":
                 return False
     return len(stack) == 0
   
```



## 题目  2  ：Min Stack

Design a stack class that supports the `push`, `pop`, `top`, and `getMin` operations\.

- `MinStack()` initializes the stack object\.

- `void push(int val)` pushes the element `val` onto the stack\.

- `void pop()` removes the element on the top of the stack\.

- `int top()` gets the top element of the stack\.

- `int getMin()` retrieves the minimum element in the stack\.

Each function should run in O\(1\)*O*\(1\) time\.

**Example 1:**

```Java
Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
Output: [null,null,null,null,0,null,2,1]
Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); *// return 0*
minStack.pop();
minStack.top();    *// return 2*
minStack.getMin(); *// return 1*
```

**Constraints:**

- `-2^31 <= val <= 2^31 - 1`\.

- `pop`, `top` and `getMin` will always be called on **non\-empty** stacks\.

```Python
class MinStack:

    def __init__(self):
        self.stack = []         
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:             
            self.min_stack.append(val)
    def pop(self) -> None:
        value  = self.stack.pop()
        if value == self.min_stack[-1]:             
            self.min_stack.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        

```

