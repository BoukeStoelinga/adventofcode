from read_input import read_input
input_1 = read_input('input1.txt')

split = [sum(list(map(int,line.split("\n")))) for line in input_1.split("\n\n")]
split.sort(reverse=True)
ans = sum(split[:3])
print(ans)