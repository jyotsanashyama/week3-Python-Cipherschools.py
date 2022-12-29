#it have key value pair

#sq=-{1:1, 2:4, 3:9}
sq={num:num**2 for num in range(1,11)}
print(sq)

#sq of 1 is:1
sq={f"Square of {num} is":num**2 for num in range(1,11)}
for k,v in sq.items():
    print(f"{k} : {v}")

string="harshit"
word_count={char: string.count(char) for char in string}
print(word_count)