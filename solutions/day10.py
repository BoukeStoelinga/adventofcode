from read_input import read_input

input_10 = read_input('input10.txt')
# print(input_10)
cycle_list = []
for i, command in enumerate(input_10.split("\n")):
    if len(command.split(' ')) == 1:
        cycle_list.append(0)
    else:
        to_add = int(command.split(" ")[1])
        cycle_list.append(0)
        cycle_list.append(to_add)

x = 1
to_sum = [20,60,100,140,180,220]
ans = 0
# print(f"{len(cycle_list)=}")
for cycle,add in enumerate(cycle_list):
    signal_strength = (cycle + 1) * x
    x += add
    if cycle+1 in to_sum:
        # print(cycle+cycle1,x)
        # print(signal_strength)
        ans += signal_strength

print(ans)
start_str = ""
x= 1
for cycle,add in enumerate(cycle_list):
    current_pixel = (cycle)%40

    print("-*-")
    print(current_pixel)
    print(x)
    if current_pixel in [x-1,x,x+1]:
        start_str += "#"
        print("#")
    else:
        start_str += "."
        print(".")
    if current_pixel ==39:
        start_str += "\n"
    x += add
print(start_str)
