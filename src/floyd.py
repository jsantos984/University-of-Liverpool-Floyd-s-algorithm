
import sys
import itertools


MAX_LENGTH = 4


def floyd_recursive(sub_distance, k, i, j):
    """
        Base case: If the current value of distance[i][j] is greater than the distance from i to k plus k to j,
        update distance[i][j] to the sum of these distances.
    """

    if sub_distance[i][j] > sub_distance[i][k] + sub_distance[k][j]:
        sub_distance[i][j] = sub_distance[i][k] + sub_distance[k][j]

    if k == MAX_LENGTH - 1:
        return sub_distance

    """
        Check if we have iterated over all vertices
    """

    if i == MAX_LENGTH - 1 and j == MAX_LENGTH - 1:
        return sub_distance

    """
        Recursive case
    """

    if j == MAX_LENGTH - 1:
        return floyd_recursive(sub_distance, k + 1, i + 1, 0)
    else:
        return floyd_recursive(sub_distance, k, i, j + 1)


def floyd(sub_distance):
    """
    Iterate over all pairs of vertices (i, j) and call floyd_recursive to update the shortest path distances.
    """
    for k in range(MAX_LENGTH):
        for i in range(MAX_LENGTH):
            for j in range(MAX_LENGTH):
                sub_distance = floyd_recursive(sub_distance, k, i, j)
                """
                Check for negative cycles after each iteration of k
                """
                if has_negative_cycle(sub_distance):
                    return None
    return sub_distance


def has_negative_cycle(distance):
    # Check if any diagonal element is negative, indicating a negative cycle
    for i in range(MAX_LENGTH):
        if distance[i][i] < 0:
            return True
    return False


"""
Define a sample distance matrix
"""
distance = [
    [0, 5, sys.maxsize, 10],
    [sys.maxsize, 0, 3, sys.maxsize],
    [sys.maxsize, sys.maxsize, 0, 1],
    [sys.maxsize, sys.maxsize, sys.maxsize, 0]
]

"""
Run the Floyd algorithm and print the result
"""
result = floyd(distance)
"""
Check for negative cycles
"""
if has_negative_cycle(result):
    print("Negative cycle detected. Result set to None.")
    result = None
print("Result after running Floyd algorithm:")
for row in result:
    print(row)




