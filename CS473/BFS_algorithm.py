# Given an adjacency matrix for a simple unweighted 
# undirected graph, do a breadth-first search of all the vertices
# and list them in the order they were discovered.

# Vertices are lettered and ties are broken lexicographically.

# index to vertex mapping for first graph
lookup_dict = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h",
        8: "i",
        9: "j"
    }

# first_matrix[row][column]
# columns:       a  b  c  d  e  f  g  h  i  j
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
queue = [["a"]] 

# implement according to Levitin

# V is the set of edges (dict)
V = { "a":0, "b":1, "c":2, "d":3, "e":4,
    "f":5, "g":6, "h":7, "i":8, "j":9 }
  
# the indices are a little extra since its a square
for row in range(0,  len(first_matrix[0])): 
    temp_queue = []
    for col in range(0, len(first_matrix[row])):
        # check the cells of each row|col
        
        if (first_matrix[row][col] == 1):
            # check if the vertex is in the queue
            temp_queue.append(lookup_dict.get(col))
            #if (queue.count(lookup_dict.get(col)) == 0):
                #queue.append(lookup_dict.get(col))
    queue.append(temp_queue)

print(queue)