# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_node = l1
        l2_node = l2

        overflow_val = 0

        head_node = None
        previous_node = None

        while l1_node or l2_node or overflow_val != 0:
            val = 0
            val += l1_node.val if l1_node else 0
            val += l2_node.val if l2_node else 0

            node_value = (val + overflow_val) % 10

            if previous_node is None:
                head_node = ListNode(node_value)
                previous_node = head_node
            else:
                previous_node.next = ListNode(node_value)
                previous_node = previous_node.next
            
            overflow_val += val
            overflow_val = overflow_val // 10

            l1_node = l1_node.next if l1_node else None
            l2_node = l2_node.next if l2_node else None
        
        return head_node
