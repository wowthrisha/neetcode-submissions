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

        # Original Node -> Copied Node
        originalToCopy = {None: None}

        # ------------------------
        # Pass 1: Create all copies
        # ------------------------
        original = head

        while original:
            copiedNode = Node(original.val)
            originalToCopy[original] = copiedNode
            original = original.next

        # ------------------------
        # Pass 2: Connect pointers
        # ------------------------
        original = head

        while original:
            #access the copied node using the original node like a->a'
            copiedNode = originalToCopy[original]

            copiedNode.next = originalToCopy[original.next]
            copiedNode.random = originalToCopy[original.random]

            original = original.next

        # Return the copied head
        return originalToCopy[head]