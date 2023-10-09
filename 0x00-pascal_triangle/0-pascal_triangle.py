#!/usr/bin/python3
"""Function that returns list of lists of integers
representing pascal triangle of n"""


def pascal_triangle(n):
    '''Create a function that returns a list of lists of integers
    representing Pascal's Triangle of a given integer n.'''
    triangle = []
    if not isinstance(n, int) or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            else:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle
