# Merge Two Sorted Lists - Beat 100%
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy
        while list1 and list2 :
            if list1.val < list2.val :
                current.next = list1
                current = current.next
                list1 = list1.next
            else:
                current.next = list2
                current = current.next
                list2 = list2.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy.next


# Linked List Cycle - Beat 100%
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack = []
        dummy = ListNode(0)
        current = dummy
        while head :
            stack.append(head)
            head =head.next
        while stack :
            current.next = stack.pop()
            current = current.next
        current.next = None
        return dummy.next


# Reverse Linked List -  Beat 100%
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # visited = set()
        # while head :
        #     if head in visited:
        #         return True
        #     visited.add(head)
        #     head = head.next
        # return False
        slow = head
        fast = head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
            if (fast==slow) :
                return True
        return False

