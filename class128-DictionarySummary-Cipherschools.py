#summary
#unordered collection of data

d={'name':'jyotsana','age':18} #key-value pair

d1=dict(name='jyotsana',age='18') #we can create using dict as well

d2={
    'name':'jyotsana',
    'age':18
    }
#syntax for printing
print(d['name'])

#add data inside empty dict
empty_dict={}
empty_dict['key1']='value1'
print(empty_dict)

#check key
if 'name'in d:
    print("yes")

#iterate
for key, value in d.items():
    print(f'key in {key}')

#to print all values
for i in d.values():
    print(i)

#get method:to access any key and check its existence
print(d.get('name'))

#delete
print(d.pop('name'))

#popitem
