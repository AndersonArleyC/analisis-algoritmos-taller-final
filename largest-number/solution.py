from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """Arrange the values so their concatenation is lexicographically maximal."""
        values = [str(value) for value in nums]

        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        values.sort(key=cmp_to_key(compare))

        if values[0] == "0":
            return "0"
        return "".join(values)


