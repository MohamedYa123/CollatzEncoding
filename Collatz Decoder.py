num=int(input("Enter number to decode: "))
G=int(input("Enter G factor: "))
while G&1==0:
	print("G factor must be odd")
	G=int(input("Enter G factor: "))
stoplen=int(input("num of steps: "))
pattern=[]
num2=num
while stoplen>0 and num2>4:
	stp=0
	while num2&1==0 and stoplen>0:
		#even
		num2=num2>>1
		stoplen-=1
		stp+=1
	if stp!=0:
		pattern.append(stp)
	stp=0
	while num2&1!=0 and stoplen>0:
		#even
		num2=(num2*3+G)
		num2=num2>>1
		stoplen-=1
		stp+=1
	if stp!=0:
		pattern.append(stp)
bv=bin(num)[2:]
print("2^",len(bv))
print("num Bits:     ",bv)
h=""
i=0
sm=0
for a in pattern:
	if i%2==0:
		h+="1"*a
	else:
		h+="0"*a
	sm+=a
	i+=1
print("Hidden Bits: ",h)
print("Num of Bits: ",len(bv))
print("Carrying Bits: ",sm)
print("Pattern:",pattern)