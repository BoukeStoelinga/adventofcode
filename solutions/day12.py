from read_input import read_input
import string
import numpy as np
input_12 = read_input('input12.txt')
board = [list(line) for line in input_12.split()]
alphabet = string.ascii_lowercase
E_index = [(index1,index2) for index1,value1 in enumerate(board) for index2,value2 in enumerate(value1) if value2=="E"][0]
S_index = [(index1,index2) for index1,value1 in enumerate(board) for index2,value2 in enumerate(value1) if value2=="S"][0]
board_numerical = np.array([[alphabet.find(str) for str in line] for line in board])
board_numerical[E_index[0],E_index[1]] = 26
print(board_numerical)
def can_move(index1,index2):
    # print(index1, index2)
    if index2[0] <0 or index2[1]<0:
        return False
    if index2[0] > len(board)-1 or index2[1] >len(board[0])-1:
        return False

    return board_numerical[index2[0],index2[1]]-board_numerical[index1[0],index1[1]]<=1
# make a graph:
graph = {}
for i,line in enumerate(board_numerical):
    for j,node in enumerate(line):
        current_ind = (i,j)
        print(current_ind)
        ind_list = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
        graph[current_ind] = []
        for ind in ind_list:
            if can_move(current_ind,ind):
                graph[current_ind].append(ind)
print(graph)
def BFS_SP(graph, start, goal):
    explored = []
    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        # print("Same Node")
        return

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    # print("Shortest path = ", *new_path)
                    return path
            explored.append(node)

    # Condition when the nodes
    # are not connected
    # print("So sorry, but a connecting" \
    #       "path doesn't exist :(")
    return
start = S_index
goal = E_index
path = BFS_SP(graph,start,goal)
path_lengths = []
a_indices = [(index1,index2) for index1,value1 in enumerate(board) for index2,value2 in enumerate(value1) if value2=="a"]
for a_index in a_indices:
    path = BFS_SP(graph,a_index,goal)
    if path is not None:
        len_path = len(path)
        print(len_path)
        path_lengths.append(len_path)
print(min(path_lengths))
# print(len(path))
# print(board_numerical)
