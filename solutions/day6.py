from read_input import read_input
input_6 = read_input('input6.txt')
print(input_6)
for i in range(len(input_6)):
    if i >3:
        print(set(input_6[i-4:i]))
        if len(set(input_6[i-4:i])) ==4:

            print(i+1)
            break
for i in range(len(input_6)):
    if i >13:
        print(set(input_6[i-14:i]))
        if len(set(input_6[i-14:i])) ==14:
            print(i)
            break