# Given an adjacency matrix for a simple unweighted 
# undirected graph, do a breadth-first search of all the vertices
# and list them in the order they were discovered.

# Vertices are lettered and ties are broken lexicographically.


# ************ GLOBAL VARIABLES ************
# index to vertex mapping for first graph
V = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e",
	5: "f", 6: "g", 7: "h", 8: "i", 9: "j"}

# list to hold the order in which vertices were visited
found = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# distance from the starting vertex
count = 0

# ******************************************

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# INPUT matrices
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

# columns: 			 a  b  c  d  e  f  g  h
second_matrix = [[0, 1, 0, 0, 1, 0, 0, 0],# a
				[1, 0, 1, 0, 0, 1, 0, 0], # b
				[0, 1, 0, 1, 0, 0, 1, 0], # c
				[0, 0, 1, 0, 0, 0, 0, 1], # d
				[1, 0, 0, 0, 0, 1, 0, 0], # e
				[0, 1, 0, 0, 1, 0, 1, 0], # f
				[0, 0, 1, 0, 0, 1, 0, 1], # g
				[0, 0, 0, 1, 0, 0, 1, 0]] # h
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# This is a function that will get the adjacency 
# list of a certain row 
# @vertex: the index of the vertex (ie a = 0)
# @matrix: the matrix to get row from
# @return: a queue of indices
def get_row(vertex, matrix):
	# initialize the queue that will be returned
	temp_queue = []
	
	# read the values from the specific row
	for row in range(vertex, vertex + 1): 
		for col in range(len(matrix[vertex])):
			# if there is an edge between vertices...
			if (matrix[row][col] == 1):
				# get the name of the adjacent vertex
				temp_queue.append(col)
	
	return temp_queue

# the bulk of the work is done here
# @vertex: the index to run BFS on
def BFS(vertex, matrix):
	global count	# access global variable
	count += 1
	found[vertex] = count
	temp_queue = [vertex]

	while (len(temp_queue) != 0):
		adj = get_row(temp_queue[0], matrix)		# adj holds adj list of param vertex
		for w in range(len(adj)):
			if (found[adj[w]] == 0):
				count += 1
				found[adj[w]] = count
				temp_queue.append(adj[w])
		del temp_queue[0] 	# remove the front item w/o returning it

def main():
	# change global variables
	global found
	global count

	# run the test for first_matrix
	for v in range(len(found)):
		if (found[v] == 0):
			BFS(v, first_matrix)
	
	final_list = []
	for i in range(len(found)):
		final_list.insert(found[i] - 1, V.get(i))
	print("output for first_matrix: ", final_list)

	# reset the found and final lists to all 0's again
	found = [0, 0, 0, 0, 0, 0, 0, 0]
	count = 0
	
	# run the test for second_matrix
	for v in range(len(found)):
		if (found[v] == 0):
			BFS(v, second_matrix)

	final_list = []
	for i in range(len(found)):
		final_list.insert(found[i] - 1, V.get(i))
	print("output for second_matrix: ", final_list)
	
if __name__ == "__main__":
	main()