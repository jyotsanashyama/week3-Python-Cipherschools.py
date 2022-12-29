#sets: unordered collection of unique items
#no key value pair
#unique items
#no indexing
#we can remove duplicates from lists using set
l=[1,2,3,4,34,4,56,7,3,2,2,4,1]
s={1,2,3}
#it removes duplicate
s2=list(set(l))
print(s2)

s.add(4) #add item 4
print(s)

s.remove(3) #will throw error if that value is not i the set
s.discard(3) #will not throw any error if that value is not in the set

s1=s.copy()

#we can't store list, dictionary, tuple in set

