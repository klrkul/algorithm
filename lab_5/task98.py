class Solution(object):
    def isValidBST(self, root):
        def validate(node, low=None, high=None):
            if not node:
                return True
            if low is not None and node.val <= low:
                return False
            if high is not None and node.val >= high:
                return False
            if not validate(node.left, low, node.val):
                return False
            return validate(node.right, node.val, high)

        return validate(root)