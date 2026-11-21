import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).parent


def load_solution(folder: str):
    path = ROOT / folder / "solution.py"
    spec = importlib.util.spec_from_file_location(folder.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module.Solution()


class TestKthLargest(unittest.TestCase):
    def test_examples(self):
        solution = load_solution("kth-largest")
        self.assertEqual(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)


class TestLargestNumber(unittest.TestCase):
    def test_examples_and_zeroes(self):
        solution = load_solution("largest-number")
        self.assertEqual(solution.largestNumber([10, 2]), "210")
        self.assertEqual(solution.largestNumber([3, 30, 34, 5, 9]), "9534330")
        self.assertEqual(solution.largestNumber([0, 0]), "0")


class TestNetworkDelay(unittest.TestCase):
    def test_reachable_and_unreachable(self):
        solution = load_solution("network-delay-time")
        self.assertEqual(solution.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2)
        self.assertEqual(solution.networkDelayTime([[1, 2, 1]], 2, 2), -1)


class TestMinCostConnectPoints(unittest.TestCase):
    def test_examples(self):
        solution = load_solution("min-cost-to-connect-all-points")
        self.assertEqual(solution.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]), 20)
        self.assertEqual(solution.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]), 18)


class TestEditDistance(unittest.TestCase):
    def test_examples_and_empty_words(self):
        solution = load_solution("edit-distance")
        self.assertEqual(solution.minDistance("horse", "ros"), 3)
        self.assertEqual(solution.minDistance("intention", "execution"), 5)
        self.assertEqual(solution.minDistance("", "abc"), 3)
        self.assertEqual(solution.minDistance("same", "same"), 0)


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_examples_and_strict_order(self):
        solution = load_solution("longest-increasing-subsequence")
        self.assertEqual(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]), 4)
        self.assertEqual(solution.lengthOfLIS([7, 7, 7, 7]), 1)
        self.assertEqual(solution.lengthOfLIS([5]), 1)


class TestGasStation(unittest.TestCase):
    def test_possible_and_impossible_circuits(self):
        solution = load_solution("gas-station")
        self.assertEqual(solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)
        self.assertEqual(solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]), -1)
        self.assertEqual(solution.canCompleteCircuit([5], [4]), 0)


class TestWordSearch(unittest.TestCase):
    def test_paths_reuse_and_board_restoration(self):
        solution = load_solution("word-search")
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ]
        original = [row[:] for row in board]

        self.assertTrue(solution.exist(board, "ABCCED"))
        self.assertEqual(board, original)
        self.assertTrue(solution.exist(board, "SEE"))
        self.assertFalse(solution.exist(board, "ABCB"))
        self.assertEqual(board, original)


if __name__ == "__main__":
    unittest.main()


