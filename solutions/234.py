# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        if not head:
            return True  # empty list is a palindrome
        
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.val != stack.pop():
                return False
            curr = curr.next
        
        return True
