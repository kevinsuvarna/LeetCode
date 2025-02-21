# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getLength(self, head):
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        len1 = self.getLength(l1)
        len2 = self.getLength(l2)
        if len1 >= len2:
            flag = 1
        else:
            flag = 2
        if flag == 2:
            l1, l2 = l2, l1
        sum = 0
        carry = 0
        head = ListNode(0)
        curr = head
        while(l2.next):
            sum = (l1.val + l2.val + carry)
            carry = sum // 10
            sum = sum % 10
            l1 = l1.next
            l2 = l2.next
            curr.next = ListNode(sum)
            curr = curr.next
        sum = (l1.val + l2.val + carry)
        carry = sum // 10
        sum = sum % 10
        curr.next = ListNode(sum)
        curr = curr.next
        if not l1.next:
            if carry >= 1:
                curr.next = ListNode(carry)
            curr = curr.next
            result = head.next
            return result
        l1 = l1.next
        while(l1.next):
            sum = (l1.val + carry)
            carry = sum // 10
            sum = sum % 10
            l1 = l1.next
            curr.next = ListNode(sum)    
            curr = curr.next
        sum = (l1.val + carry)
        carry = sum // 10
        sum = sum % 10
        curr.next = ListNode(sum)  
        curr = curr.next
        if carry >= 1:
            curr.next = ListNode(carry)
        # curr = curr.next
        result = head.next
        return result