# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        stack =[]
        dummy = ListNode(0)
        current = dummy
        slow = head 
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        while second :
            stack.append(second)
            second = second.next
        current = head
        while stack :
            node = stack.pop()
            node.next = current.next
            current.next = node
            current = node.next
       