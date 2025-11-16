Tuple = ("1","2","3")
Set = {"1","2","3"}

print(Tuple[0]) 
print(Tuple[-1]) 
print(Tuple[0:2])
count = 1
for i in Tuple:
    print(f"{count} = {i}")
    count += 1

num1 = {1,2,3}
num2 = {3,4,5}

print(num1.union(num2))
print(num1.intersection(num2))
print(num1.difference(num2))

