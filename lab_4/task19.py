class Solution(object):
    def removeNthFromEnd(self, head, n):
        curr = head
        len = 0
        while curr:
            len += 1
            curr = curr.next
        step = len - n
        if step == 0:
            return head.next
        curr = head
        for i in range(step - 1):
            curr = curr.next
        curr.next = curr.next.next
        return head