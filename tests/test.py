import unittest
import sys
from src import floyd

NO_PATH = 12
graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]


# test = floyd.floyd(graph)
# print(test)


class TestFloyd(unittest.TestCase):

    def test_floyd_basic(self):
        # Define a sample distance matrix
        distance = [
            [0, 5, sys.maxsize, 10],
            [sys.maxsize, 0, 3, sys.maxsize],
            [sys.maxsize, sys.maxsize, 0, 1],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0]
        ]

        # Expected output after running Floyd algorithm
        expected_result = [
            [0, 5, 8, 9],
            [sys.maxsize, 0, 3, 4],
            [sys.maxsize, sys.maxsize, 0, 1],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0]
        ]

        # Run the Floyd algorithm
        result = floyd.floyd(distance)

        # Check if the result matches the expected result
        self.assertEqual(result, expected_result)

    def test_floyd_negative_cycle(self):
        # Define a sample distance matrix with a negative cycle
        distance = [
            [0, 1, sys.maxsize],
            [sys.maxsize, 0, -1],
            [-1, sys.maxsize, 0]
        ]

        # Expected output after running Floyd algorithm
        # Since there is a negative cycle, result should be None
        expected_result = None

        # Run the Floyd algorithm
        result = floyd.floyd(distance)

        # Check if the result is None
        self.assertIsNone(result)


def test_optimal_paths(self):
    # Define a sample distance matrix representing a graph with known shortest paths
    distance = [
        [0, 3, 6, sys.maxsize],  # Shortest path from node 0 to others: [0, 3, 6, inf]
        [sys.maxsize, 0, 2, sys.maxsize],  # Shortest path from node 1 to others: [inf, 0, 2, inf]
        [sys.maxsize, sys.maxsize, 0, 1],  # Shortest path from node 2 to others: [inf, inf, 0, 1]
        [sys.maxsize, sys.maxsize, sys.maxsize, 0]  # Shortest path from node 3 to others: [inf, inf, inf, 0]
    ]

    # Expected shortest paths matrix based on manual calculation
    expected_result = [
        [0, 3, 5, 6],
        [sys.maxsize, 0, 2, 3],
        [sys.maxsize, sys.maxsize, 0, 1],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0]
    ]

    # Run the Floyd algorithm
    result = floyd.floyd(distance)

    # Check if the result matches the expected shortest paths matrix
    self.assertEqual(result, expected_result, "Incorrect shortest paths computed by Floyd algorithm")

if __name__ == '__main__':
    unittest.main()


