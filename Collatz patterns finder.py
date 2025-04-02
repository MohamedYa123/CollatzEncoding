import math
import time
from QuickFinder import *
#import numpy as np
G=int(input("Enter G factor: "))
while G&1==0:
	print("G factor must be odd")
	G=int(input("Enter G factor: "))
pattern=[]
PatternVerified=[]
v=-1
sm=0
while (v!=0):
	try:
		v=int(input("::"))
	except:
		v=0
	sm+=v
	if v!=0:
		pattern.append(v)
		if (len(pattern)==1):
			PatternVerified.append(1)
		else:
			PatternVerified.append(0)
def checkAddedValue(numt,a,nP):
	#return 1
	nP=2*3**nP
	zP=2**a
	fvalue=((numt>>a)+1)
	#if not fvalue &1==1:
	#	[]#fvalue +=1
	numtsq=fvalue<<a#next number
	vfixed=numtsq-numt
	A=zP//2
	B=nP//2
	c=vfixed//2
	n,_=find_n_z(A, B, c)
	if n==0:
		n=1
	return n
	addvalue=vfixed
	addvaluen=0
	vn=0
	vz=0
	zaddition,rem=divmod((nP-vfixed),zP)#(nP-vfixed) // zP
	if rem==0:
		zaddition-=1
	lastaddedn=-1
	loops=0
	while addvalue!=addvaluen or not fvalue &1==1:#not (((numtsq>>a)<<a==numt and numt>=numtsq)):
		if addvaluen<addvalue or (not fvalue &1==1 and addvalue==addvaluen):
			addvaluen+=nP
			lastaddedn=1	
			vn+=1
		elif addvalue<addvaluen:
			if lastaddedn==1:
				addvalue+=zP*zaddition
				vz+=1*zaddition
			else:
				addvalue+=zP
				vz+=1
			lastaddedn=-1
		fvalue=(((numt+addvalue)>>a))
		loops+=1
		#if(not fvalue &1==1 and vn==vz)
	print("Loops:",loops)
	return vn
#next is to search for the number having this pattern
num=2**pattern[0]-G
if num<0:
	print("G factor not suitable for the first bits")
	exit()
n=pattern[0]
end=-1
lastverifiednumt=3**pattern[0]-G
while(end==-1):
	i=0
	nzs=0
	numt=num
	patternfound=[]
	l=pattern[0]
	adds=0
	nP=0
	indx=-1
	for a in pattern:
		indx+=1
		if (PatternVerified[indx]==1):
			numt=lastverifiednumt
			if i%2==0:
				nP+=a
			i+=1
			nzs+=a
			continue
		#find n and z of the num
		if i%2==0:
			#find n
			#add 1 and calc log
			vnt=numt
			zn=numt+G
			n=numt+G
			dnumt=n
			n=0
			#print(dnumt&1)
			while(dnumt&1==0):
				dnumt=dnumt>>1
				n+=1
			l=n
			patternfound.append(l)
			#n=math.log(n)/math.log(2)
			while numt&1!=0:
				numt=(numt*3+G)#/2
				numt=numt>>1
			if n!=a:
				lastverifiednumt=vnt
				adds=checkAddedValue(zn,a,nP)
				break
			else:
				lastverifiednumt=numt
				PatternVerified[indx]=1
		else:
			#find z
			#print(numt)
			z=0
			zn=numt
			while numt&1==0:
				numt=numt>>1
				#numt/=2
				#print(numt)
				z+=1
			l=z
			patternfound.append(l)
			if z!=a:
				lastverifiednumt=zn
				adds=checkAddedValue(zn,a,nP)
				#now find it
				break
			else:
				lastverifiednumt=numt
				PatternVerified[indx]=1
		if i%2==0:
			nP+=a
		nzs+=a
		i+=1
	if i==len(pattern):
		break
	else:
		num+=2*2**(nzs)*adds
		lastverifiednumt+=2*3**(nP)*adds
		#print(num,":",nzs,":",patternfound)
		#time.sleep(0.1)
print("Number found : ",num)
bv=bin(num)[2:]
print("2^",len(bv))
print("Found Bits:  ",bv)
h=""
i=0
for a in pattern:
	if i%2==0:
		h+="1"*a
	else:
		h+="0"*a
	i+=1
print("Hidden Bits: ",h)
print("Num of Bits: ",len(bv))
print("Carrying Bits: ",sm)
print("Diff: ",2*2**sm-num)
#print(2**78)