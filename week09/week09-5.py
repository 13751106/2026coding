# week09-5.py
# LeetCode 2095. Delete the Middle Node of a Linked List
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None: return None
        prev = fast = slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next
        # print( slow.val )
        return head
