# Given an adjacency matrix for a simple unweighted 
# undirected graph, do a breadth-first search of all the vertices
# and list them in the order they were discovered.

# Vertices are lettered and ties are broken lexicographically.

# first input matrix
#     a   b   c   d   e   f   g   h   i   j
# a   -   0   1   1   1   0   0   0   0   0
# b   0   -   0   0   1   1   0   0   0   0
# c   1   0   -   1   0   1   0   0   0   0
# d   1   0   1   -   0   0   0   0   0   0
# e   1   1   0   0   -   1   0   0   0   0
# f   0   1   1   0   1   -   0   0   0   0
# g   0   0   0   0   0   0   -   1   0   1
# h   0   0   0   0   0   0   1   -   1   0
# i   0   0   0   0   0   0   0   1   -   1
# j   0   0   0   0   0   0   1   0   1   -
# 
# output queue: 

# first_matrix[row][column]
first_matrix = [[0, 0, 1, 1, 1, 0, 0, 0, 0, 0], # a
                [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], # b
                [1, 0, 0, 1, 0, 1, 0, 0, 0, 0], # c
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 0], # d
                [1, 1, 0, 0, 0, 1, 0, 0, 0, 0], # e
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], # f
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 1], # g
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0], # h
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 1], # i
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0]] # j

# the output list of vertices, always start with 'a'
queue = ["a"] 