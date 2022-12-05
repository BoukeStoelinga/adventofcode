from read_input import read_input
moves = read_input('input5.txt')
# board = """
#     [H]         [H]         [V]
#     [V]         [V] [J]     [F] [F]
#     [S] [L]     [M] [B]     [L] [J]
#     [C] [N] [B] [W] [D]     [D] [M]
# [G] [L] [M] [S] [S] [C]     [T] [V]
# [P] [B] [B] [P] [Q] [S] [L] [H] [B]
# [N] [J] [D] [V] [C] [Q] [Q] [M] [P]
# [R] [T] [T] [R] [G] [W] [F] [W] [L]
#  1   2   3   4   5   6   7   8   9
#  """

board = [["G,P,N,R"],
["H,V,S,C,L,B,J,T"],
["L,N,M,B,D,T"],
["B,S,P,V,R"],
["H,V,M,W,S,Q,C,G"],
["J,B,D,C,S,Q,W"],
["L,Q,F"],
["V,F,L,D,T,H,M,W"],
["F,J,M,V,B,P,L" ]]
board = [lst[0].split(",") for lst in board]
[lst.reverse() for lst in board]

# b1.append("a")
def pop_more(list,number):
    popped = [list.pop() for i in range(number)]
    popped.reverse()
    return list,popped
split = moves.split("\n")
for row in split:
    row_split = row.split(" ")
    n_to_move = int(row_split[1])
    move_from = int(row_split[3])-1
    move_to = int(row_split[5])-1
    board[move_from],popped_items = pop_more(board[move_from],n_to_move)
    board[move_to].extend(popped_items)
print(board)
print("".join([l[-1] for l in board]))