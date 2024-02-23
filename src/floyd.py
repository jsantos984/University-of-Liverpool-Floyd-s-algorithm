
import sys
import itertools


MAX_LENGTH = 4
#print(MAX_LENGTH)


def floyd(distance):
    for intermediate, start_node, end_node \
            in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
        if start_node == end_node:
            distance[start_node][end_node] = 0
        else:
            distance[start_node][end_node] = min(distance[start_node][end_node],
                                                 distance[start_node][intermediate] + distance[intermediate][end_node]
                                                 )
#        check negative cycles
        if start_node == end_node and distance[start_node][end_node] < 0:
            return None
    return distance


# Define a sample distance matrix
distance = [
    [0, 5, sys.maxsize, 10],
    [sys.maxsize, 0, 3, sys.maxsize],
    [sys.maxsize, sys.maxsize, 0, 1],
    [sys.maxsize, sys.maxsize, sys.maxsize, 0]
]

# Run the Floyd algorithm and print the result
result = floyd(distance)
print("Result after running Floyd algorithm:")
for row in result:
    print(row)




