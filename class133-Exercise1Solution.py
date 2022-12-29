def reverse_strings(l):
    return[name[::-1] for name in l]

print(reverse_strings(["abc",'vbn','bjhj']))

#basic approach
def rev(l):
    new_list=[]
    for name in l:
        new_list.append(name[::-1])
    return new_list