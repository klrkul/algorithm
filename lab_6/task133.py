class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None

        cloned = {}
        from collections import deque
        queue = deque([node])
        cloned[node] = Node(node.val, [])
        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                cloned[current].neighbors.append(cloned[neighbor])

        return cloned[node]