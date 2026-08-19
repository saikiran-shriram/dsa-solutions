# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode()
        if not lists :
            return None
        result = lists[0]
        def MergeTwoLists(list1, list2) :
            dummy = ListNode(0)
            current = dummy
            while list1 and list2 :
                if list1.val < list2.val :
                    current.next = list1
                    current= current.next
                    list1 = list1.next
                else :
                    current.next = list2
                    current  = current.next
                    list2= list2.next
            if list1 :
                current.next = list1
            if list2 :
                current.next = list2
            return dummy.next
        for i in range(1,len(lists)):
            result = MergeTwoLists(result,lists[i])
        return result