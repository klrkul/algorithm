class Solution(object):
    def levelOrder(self, root):
        res = []

        def dfs(node, level):
            if not node:
                return
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return res