k=98
r,c=5,5
key='word'
l1=list()
l2=list()
for i in key:
	l2.append(i)
l2.append('a')
l1.append(l2)
while(k<=122):
	l2=list()
	for i in range(5):
		l2.append(chr(k))
		k=k+1
		if(k==106 or k==100 or k==111 or k==114 or k==119):k=k+1
	l1.append(l2)
print(l1)
ip='russia attacks ukraine'
x=ip.split()
inp=''
for i in x:
	inp=inp+i
print(inp)
i=0
j=1
trans_inp=''
while(i<len(inp)):
	while(inp[i]!=inp[j]):
		trans_inp=trans_inp+inp[i]
		i=i+1
		j=j+1	
	else:
		trans_inp=trans_inp+'x'
		i=i+1
		j=j+1
		
	

		

