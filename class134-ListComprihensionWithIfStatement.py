num = list(range(1,11))
print(num)

#basic approach
nums=[]
for i in num:
    if i%2==0:
        nums.append(i)
print(nums)
#list comprehension
even_num=[i for i in num if i%2==0 ]
odd_num=[i for i in range(1,11) if i%2!=0]
print(even_num)
print(odd_num)