# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        stack = []
        dummy = ListNode(0, head)
        head = dummy
        curr = head
        pos = 0
        while pos != left -1 : 
            head = head.next 
            curr = curr.next
            pos +=1
        prev = head
        while pos != left :
            pos += 1
            curr = curr.next
        while pos != right +1 :
            stack.append(curr)
            curr = curr.next
            pos += 1
        while stack :
            prev.next = stack.pop()
            prev = prev.next
        prev.next = curr
        return dummy.next