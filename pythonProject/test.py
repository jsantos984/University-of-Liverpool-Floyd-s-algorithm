import unittest
import floyd
import sys

NO_PATH = 12
graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0,  2],
        [NO_PATH, NO_PATH, NO_PATH, 0]]

test = floyd.floyd(graph)
print(test)

#for row in graph:
    #print(row))

