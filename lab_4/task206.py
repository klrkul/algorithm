class Solution(object):
    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        return prev