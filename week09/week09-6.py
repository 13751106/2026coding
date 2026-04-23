# week09-6.py
# LeetCode 328. Odd Even Linked List
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while head:
            a.append( head.val )
            head = head.next

        N = len(a)
        now = ans = ListNode()
        for i in range(0, N, 2):
            now.next = ListNode( a[i] )
            now = now.next
        for i in range(1, N, 2):
            now.next = ListNode( a[i] )
            now = now.next
        return ans.next
