dict={'one':1,'two':2,'five':5,'ten':10}
user_input=int(input('enter the amount required:'))
digit=[]
j=0
while rem!=0:
    for i in dict.keys():
       rem=user_input%i
       if rem == 0:
           digit.append(rem)
    j=max(digit)
    user_input=j
