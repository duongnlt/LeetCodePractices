# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    mod = 0
    res = tempList = ListNode()
    while l1 or l2 or mod:
        val1 = val2 = 0
        if l1:
            val1 = l1.val
            l1 = l1.next
        if l2:
            val2 = l2.val
            l2 = l2.next
        temp = val1 + val2 + mod
        mod = temp//10
        tempList.next = ListNode(temp%10)
        tempList = tempList.next
    return res.next


