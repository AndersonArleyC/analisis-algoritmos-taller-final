from collections import defaultdict
from typing import DefaultDict, List, Tuple
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """Compute single-source shortest paths with Dijkstra's algorithm."""
        graph: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)
        for source, target, weight in times:
            graph[source].append((target, weight))

        queue: List[Tuple[int, int]] = [(0, k)]
        distances = {}

        while queue:
            elapsed, node = heapq.heappop(queue)
            if node in distances:
                continue

            distances[node] = elapsed

            for neighbor, weight in graph[node]:
                if neighbor not in distances:
                    heapq.heappush(queue, (elapsed + weight, neighbor))

        if len(distances) != n:
            return -1
        return max(distances.values())


