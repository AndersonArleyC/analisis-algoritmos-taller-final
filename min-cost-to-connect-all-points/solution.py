from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """Return the weight of the Manhattan-distance MST using dense Prim."""
        n = len(points)
        in_tree = [False] * n
        min_cost = [float("inf")] * n
        min_cost[0] = 0
        total = 0

        for _ in range(n):
            next_point = -1
            for point in range(n):
                if not in_tree[point] and (
                    next_point == -1 or min_cost[point] < min_cost[next_point]
                ):
                    next_point = point

            in_tree[next_point] = True
            total += min_cost[next_point]
            x1, y1 = points[next_point]

            for point in range(n):
                if in_tree[point]:
                    continue
                x2, y2 = points[point]
                distance = abs(x1 - x2) + abs(y1 - y2)
                if distance < min_cost[point]:
                    min_cost[point] = distance

        return total


