# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head):

        dummy = ListNode(0, head)

        fast = slow = dummy
        while fast.next and fast.next.next:

            fast = fast.next.next
            slow = slow.next

        slow.next = slow.next.next 
        return dummy.next