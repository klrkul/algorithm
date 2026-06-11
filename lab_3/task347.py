class Solution(object):
    def topKFrequent(self, nums, k):
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        list_pairs = list(counts.items())
        list_pairs.sort(key=lambda x: x[1], reverse=True)
        res = []
        i = 0
        while len(res) < k:
            number = list_pairs[i][0]
            res.append(number)
            i = i + 1
        return res