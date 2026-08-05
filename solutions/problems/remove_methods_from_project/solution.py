from collections import defaultdict, deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations):
        # Step 1: Build graph
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)

        # Step 2: Find all suspicious methods (reachable from k)
        suspicious = set()
        queue = deque([k])

        while queue:
            node = queue.popleft()
            if node in suspicious:
                continue
            suspicious.add(node)
            for nei in graph[node]:
                if nei not in suspicious:
                    queue.append(nei)

        # Step 3: Check if removal is valid
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))  # cannot remove anything

        # Step 4: Return remaining methods
        return [i for i in range(n) if i not in suspicious]