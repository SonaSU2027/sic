k=0
number=int(input('enter the total no. of oranges:'))
diameter=input('enter the diameter of oranges separated by space:')
list=diameter.split()
#key=list[-1]
for i in range(len(list)):
    if int(list[i])<=int(list[-1]):
        list[k],list[i]=list[i],list[k]
        k=k+1
#list[k],list[i]=list[i],list[k]
list2=[]
for i in list:
    list2.append(int(i))
print(list2)
