# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        stack = []
        def fun(head):
            count =  0
            start = head
            while head and count < k :
                head = head.next
                count += 1
            if count < k: 
                return start 
                
            current = start
            while current != head:
                stack.append(current)
                current = current.next
            new_head = stack.pop()
            prev = new_head 
            while stack:
                node = stack.pop()
                prev.next = node
                prev = node
            remaining = fun(head)
            start.next = remaining
            return new_head
        return fun(head)
           
