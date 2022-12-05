from read_input import read_input
input_2= read_input('input2.txt')
split = input_2.split("\n")

keydict = {'X':0,'Y':3,'Z':6,'A':1,'B':2,'C':3}
c2= [keydict[entry[0]] for entry in split]
c1 = [keydict[entry[2]] for entry in split]
score =0
for i in range(len(c1)):
	if c1[i] == c2[i]:
		score += 3
	elif (c1[i] == 1 and c2[i]==3) or(c1[i] == 2 and c2[i]==1) or (c1[i] == 3 and c2[i]==2):
		score += 6
		
score += sum(c1)
score2 =0
for i in range(len(c2)):
	print("c1",c1[i])
	print("c2",c2[i])
	
	if c1[i] == 3:
		add = c2[i]
	elif c1[i] == 0:
		add= (c2[i]+1)%3+1
	elif c1[i] == 6:
		add = (c2[i]+3)%3+1
	score2+= add
	print(add)
score2 += sum(c1)		
print(score2)