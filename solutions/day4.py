from read_input import read_input
input_4 = read_input('input4.txt')
split =[entry.split(",") for entry in input_4.split("\n")]
count =0
for i, ranges in enumerate(split):
	l1 = list(map(int,ranges[0].split("-")))
	l2 = list(map(int,ranges[1].split("-")))
	s1 = set(range(l1[0],l1[1]+1))
	s2 = set(range(l2[0],l2[1]+1))
	if i==0:
		print(s1,s2)
	if len(s1.intersection(s2))!=0:
		count += 1
print(count)