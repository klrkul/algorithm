class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        curr = head
        save = 0
        while l1 or l2 or save:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            total = v1 + v2 + save
            save = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next