#PARKING USAGE SURVEY BY PATROLLING METHOD
a,b,t=[],[],[]
n=8
#cap=int(input("enter capacity of parking"))
nvs=[0,0,0,0,0,0,0,0,0]
while(n):
    print("enter space separated vehicle numbers in the row:")
    s=input()
    s=s.split()
    s=list(s)
    a.append(s)
    b.extend(s)
    n-=1
temp=b
b=set(b)
for i in b:
    c=temp.count(i)
    nvs[c]+=1
x=nvs.copy()
duration=[0,.5,1,1.5,2,2.5,3,3.5,4]
for i in range(0,9):
    x[i]=x[i]*duration[i]

#print(x,nvs)
summ=0
for i in x:
    summ=summ+i
print("parking load is :",summ)
#pt=summ/cap
su=nvs[1]+nvs[2]
parkturn=((summ-su)*10)+(su*5)
print("parking turnover is :",parkturn)


