Problem Link

https://neetcode.io/problems/remove-node-from-end-of-linked-list/question?list=neetcode150

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0, head)
        left = right = temp
        for _ in range(n + 1):
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return temp.next
```