#with the help of this we can create in just one line
 #create list of squares from 1 to 10
#basic approach
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)

#list comprihension
square2=[i**2 for i in range(1,11)]
print(square2)

neg=[]
for i in range(1,11):
    neg.append(-i)
print(neg)

new_neg=[-i for i in range(1,11)]

names=['hello','world','mars']
#new_list = ['h','w','m']
new_list=[]
for name in names:
    new_list.append(name[0])
print(new_list)

list_comp= [name[0] for name in names]
print(list_comp)

