"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        new_head = Node(head.val)
        node_table = {head: new_head}
        nodes = [head]

        while nodes[-1].next:
            next_node = nodes[-1].next
            node_table[next_node] = Node(next_node.val)
            nodes.append(next_node)

        for node in nodes:
            if node.next: node_table[node].next = node_table[node.next]
            if node.random: node_table[node].random = node_table[node.random]

        return new_head