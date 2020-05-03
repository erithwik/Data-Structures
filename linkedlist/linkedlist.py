#Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
#First, construct a head and point and record the head
pointer=head = ListNode(None)
#loop through all node
while pointer:
    print pointer.val
    pointer = pointer.next