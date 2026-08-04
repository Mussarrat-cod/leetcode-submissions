class Solution:
    def validPath(self, n, edges, source, destination):
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu != pv:
                parent[pu] = pv

        return find(source) == find(destination)