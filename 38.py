# Definition for a binary tree node (LeetCode style).
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten_recursive(root: TreeNode) -> None:
    """
    Flatten tree in-place to a 'right-pointer-only' list in preorder.
    """

    def helper(node: TreeNode):
        # Returns the tail node of the flattened list for this subtree.
        if not node:
            return None
        # If leaf node, it's its own tail.
        if not node.left and not node.right:
            return node

        # Flatten left and right subtrees
        left_tail = helper(node.left)
        right_tail = helper(node.right)

        if left_tail:
            # Insert the flattened left between node and node.right
            left_tail.right = node.right
            node.right = node.left
            node.left = None

        # The new tail is right_tail if present, else left_tail, else node itself
        return right_tail or left_tail or node

    helper(root)
