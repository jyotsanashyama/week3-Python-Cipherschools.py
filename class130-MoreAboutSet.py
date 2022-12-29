# in keywords in sets and for loop
s={'a','b','c'}

#in keyword to check if item is present or not
if 'a' in s:
    print('yes')
else:
    print('no')

#for loop
for item in s:
    print(item)

#set maths

s1={1,2,3,4}
s2={3,4,5,6}

#union
union_set = s1 | s2
print(union_set)

#intersection
int_set = s1 & s2
print(int_set)