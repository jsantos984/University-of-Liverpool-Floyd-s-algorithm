
import sys
import itertools


MAX_LENGTH = 4
print(MAX_LENGTH)


def floyd(distance):
    for intermediate, start_node, end_node \
            in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
        if start_node == end_node:
            distance[start_node][end_node] = 0
        else:
            distance[start_node][end_node] = min(distance[start_node][end_node],
                                                 distance[start_node][intermediate] + distance[intermediate][end_node]
                                                 )
    return distance






