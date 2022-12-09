from read_input import read_input
import numpy as np

# input_8 = read_input('input8.txt')
# matrix = [list(map(int,list(row))) for row in input_8.split("\n")]
# matrix = np.array(matrix)
# marker = np.zeros(matrix.shape)
# # part 1
# def check_direction(trees):
#     index_list = []
#     for i,row in enumerate(trees):
#         for j,entry in enumerate(row):
#             # print(row)
#             # print(row[:j+1])
#             # print(entry)
#             # # print(np.all(row[:j]<entry))
#             #
#             # print(np.all(row[:j ] < entry))
#             if np.all(row[:j]<entry):
#                 # print(i,j)
#                 index_list.append((i,j))
#     return index_list
# for i in range(4):
#
#     matrix = np.rot90(matrix)
#     marker = np.rot90(marker)
#     indices = check_direction(matrix)
#     # print(indices)
#     # print(marker)
#     for index in indices:
#         marker[index] = 1
#     # print(marker)
# print(np.count_nonzero(marker))
# part 2
input_8 = """30373
25512
65332
33549
35390"""
input_8 = read_input('input8.txt')
matrix = [list(map(int, list(row))) for row in input_8.split("\n")]
matrix = np.array(matrix)
print(matrix)


def check_row_count(row, val):
    count = 0
    max = -1
    for i,entry in enumerate(row):
        if entry >= val:
            count += 1
            break
        if entry < val:
            count +=1
        # if entry < val and entry
        #
        # if entry <= val and entry >= max:
        #     max = entry
        #     count += 1
        # else:
        #     count += 1
        #     break
    # print(f"count: {count}")
    return count


def check_scene(matrix):
    score_list = []
    for i, row in enumerate(matrix):
        for j, entry in enumerate(row):
            left = row[:j][::-1]
            right = row[j + 1:]
            top = matrix[:, j][:i][::-1]
            bottom = matrix[:, j][i + 1:]
            # print(f"entry:{entry}")
            # print(left,right,top,bottom)
            score =check_row_count(left,entry) * check_row_count(right, entry) *\
                              check_row_count(top,entry) * check_row_count(bottom, entry)
            # print(f"score: {score}")
            score_list.append(score)
    return score_list
test_list = [4,9]
check_row_count(test_list,3)
score_list = check_scene(matrix)
score_mat = np.reshape(score_list,matrix.shape)

print(score_list)
print(score_mat)
print(np.max(score_mat))

print(score_list)
