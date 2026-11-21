from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Return the unique valid starting station, or -1 if none exists."""
        total_balance = 0
        current_balance = 0
        candidate = 0

        for station in range(len(gas)):
            balance = gas[station] - cost[station]
            total_balance += balance
            current_balance += balance

            if current_balance < 0:
                candidate = station + 1
                current_balance = 0

        if total_balance < 0:
            return -1
        return candidate
