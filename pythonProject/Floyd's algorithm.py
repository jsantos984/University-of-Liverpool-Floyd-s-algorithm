
import sys
import itertools

NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0,  2],
        [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])

def floyd(distance):
    for intermediate, start_node, end_node \
            in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
        if start_node == end_node:
            distance[start_node][end_node] = 0
        else:
            distance[start_node][end_node] = min(distance[start_node][end_node],
                                                 distance[start_node][intermediate] + distance[intermediate][end_node]
                                                 )


floyd(graph)
for row in graph:
    print(row)

#import unittest


def calculate_shortest_path(graph, param, param1):
    pass


#class TestGraphFunctions(unittest.TestCase):

   # def setUp(self):
        self.graph = [
            [0, 7, sys.maxsize, 8],
            [sys.maxsize, 0, 5, sys.maxsize],
            [sys.maxsize, sys.maxsize, 0, 2],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0]
        ]

    #def test_shortest_path(self):
        # Assuming the function returns the shortest path length
        path_length = calculate_shortest_path(self.graph, 0, 2)
        self.assertEqual(path_length, 12)  # Example test case

#if __name__ == '__main__':
    #unittest.main()


