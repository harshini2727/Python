# 1.
fruits=["apple", "mango", "banana"]
print(fruits[0],fruits[2])
print(len(fruits))    
fruits[1]="pineapple"
print(fruits)

# 2.
x=["harish", "naresh", "suresh", "mahesh"]
print(id(x))
x[2]="kiran"
print(x)
print(id(x))

# 3.
data=[1,2,[4,5],[6,7],8,"something"]
print(data[2][0])
print(data[3][1])
print(data[5][2])

# 4.
mixed=[1,2,"hi",12.5,True]
print(f"Value: {mixed[0]}, Type: {type(mixed[0])}")
print(f"Value: {mixed[2]}, Type: {type(mixed[2])}")

