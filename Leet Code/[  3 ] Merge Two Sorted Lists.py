# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not list1: return list2
        if not list2: return list1

        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        p = head
        while list1:
            while list2 and list1.val > list2.val:
                p.next = list2
                p = p.next
                list2 = list2.next
            p.next = list1
            p = p.next
            list1 = list1.next
        
        p.next = list2
        return head
            