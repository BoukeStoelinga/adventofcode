from read_input import read_input
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
input_9 = read_input('input9.txt')
board_string = """..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
.........................."""

board = np.array([list(line) for line in board_string.split("\n")])
board = np.array([["." for i in range(400)] for j in range(400)])
# print(board.shape)
# print(np.array(board))
# init_i, init_j = np.where(board == 'H')
# init_i, init_j = init_i[0], init_j[0]
init_i,init_j = 200,200
print(init_i,init_j)


# print(init_i,init_j)
# print(input_9)
class RopePart:
    def __init__(self, init_pos=(200, 200),marker="H"):
        self.y = init_pos[0]
        self.x = init_pos[1]
        self.marker = str(marker)
        self.directions = {"R": (0, 1), "U": (-1, 0), "L": (0, -1), "D": (1, 0)}

    def move(self, direction):
        self.x = self.x + self.directions[direction][1]
        self.y = self.y + self.directions[direction][0]

    def is_close_enough(self, other):
        a1 = self.x - other.x
        a2 = self.y - other.y
        return all([abs(a1) <= 1, abs(a2) <= 1])

    def move_to_point(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        adx, ady = abs(dx), abs(dy)
        if adx == 2:
            if dx> 0:
                self.x += 1
            else:
                self.x += -1
            if ady == 1:
                self.y += dy
        if ady == 2:
            if dy > 0:
                self.y += 1
            else:
                self.y += -1
            if adx == 1:
                self.x += dx
def draw_board(rope,board_string):
    board = np.array([list(line) for line in board_string.split("\n")])
    newboard = board
    for ropepart in rope[::-1]:
        newboard[ropepart.y,ropepart.x] = ropepart.marker
    string_board = "\n".join("".join(val for val in line)for line in newboard)
    print(string_board)
    # print(np.array2string(board))
rope= [RopePart((init_i,init_j),marker="H")]
[rope.append(RopePart((init_i,init_j),marker=i)) for i in range(1,10)]
# draw_board(rope,board_string)
tail_index_list = []
for line in input_9.split("\n"):
    direction = line.split()[0]
    steps = int(line.split()[1])
    # print(direction, steps)
    for i in range(steps):
        rope[0].move(direction)
        for j in range(1,len(rope)):
            rope[j].move_to_point(rope[j-1])

        # draw_board(rope,board_string)
        tail_index_list.append((rope[-1].x,rope[-1].y))
print(len(set(tail_index_list)))
def update_index(index: tuple, direction: str):
    if direction == "R":
        newindex = (index[0], index[1] + 1)
        return newindex
    elif direction == "U":
        newindex = (index[0] - 1, index[1])
        return newindex
    elif direction == "L":
        newindex = (index[0], index[1] - 1)
        return newindex
    elif direction == "D":
        newindex = (index[0] + 1, index[1])
        return newindex


def is_close_enough(head_index, tail_index):
    a1 = head_index[0] - tail_index[0]
    a2 = head_index[1] - tail_index[1]
    return all([abs(a1) <= 1, abs(a2) <= 1])


# def draw_board(head_index, tail_index, board):
#     # board = np.array([["." for i in range(400)] for j in range(400)])
#     board[tail_index] = "T"
#     board[head_index] = "H"
#     print(board)
#     # board[tail_index]


# main loop:
# []
# current_head = (init_i, init_j)
# current_tail = (init_i, init_j)
# draw_board(current_head, current_tail, board)
# tail_index_list = []
# for line in input_9.split("\n"):
#     direction = line.split()[0]
#     steps = int(line.split()[1])
#     # print(direction, steps)
#     for i in range(steps):
#         # print(current_head)
#         current_head = update_index(current_head, direction)
#         if not is_close_enough(current_head, current_tail):
#             a1 = current_head[0] - current_tail[0]
#             a2 = current_head[1] - current_tail[1]
#             if abs(a1) + abs(a2) >= 3:
#                 # diagonal step
#
#                 if a1 >= 1 and a2 >= 1:
#                     current_tail = update_index(current_tail, 'D')
#                     current_tail = update_index(current_tail, 'R')
#                 elif a1 >= 1 and a2 <= -1:
#                     current_tail = update_index(current_tail, 'D')
#                     current_tail = update_index(current_tail, 'L')
#                 elif a1 <= -1 and a2 >= 1:
#                     current_tail = update_index(current_tail, 'U')
#                     current_tail = update_index(current_tail, 'R')
#                 elif a1 <= -1 and a2 <= -1:
#                     current_tail = update_index(current_tail, 'U')
#                     current_tail = update_index(current_tail, 'L')
#
#             else:
#                 if a1 >= 2:
#                     current_tail = update_index(current_tail, 'D')
#                 if a2 >= 2:
#                     current_tail = update_index(current_tail, 'R')
#                 if a1 <= -2:
#                     current_tail = update_index(current_tail, 'U')
#                 if a2 <= -2:
#                     current_tail = update_index(current_tail, 'L')
#         tail_index_list.append(current_tail)
#         # draw_board(current_head, current_tail)
# tail_index_set = set((tail_index_list))
# print(len(tail_index_set))
# print(np.unique(tail_index_list))
