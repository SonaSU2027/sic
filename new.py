import sys
a=list(map(int ,input('enter the array').split()))
low=0
high=len(a)-1
mid=low+high//2
key=int(input('enter the key:'))
while low<high:
    if key==a[mid]:
        print('key found')
        sys.exit()
    elif key<a[mid]:
        high=a[mid]
    else:
        low=a[mid+1]
print('key not found')