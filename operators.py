# find simple interest 
# Formula :  (SI=P*T*R/100)
P = int(input("Enter principal amount : "))
T = int(input("Enter time period : "))
R = int(input("Enter rate of interest : "))
SI = (P*T*R)/100
print(f"Simple interest will be : {SI}")

# Temperature convertion (Celsius to Fahrenheit)
# Formula :  F=(C*9/5)+32
Celsius = float(input("Enter celcuis value : "))
Fahrenheit = (Celsius*9/5)+32
print(f"{Celsius} celsius is converted to {Fahrenheit} fahrenheit value")

# Average of three numbers
# Formula : Average = (n1+n2+n3)/3
n1 = int(input("Enter the first value : "))
n2 = int(input("Enter the second value : "))
n3 = int(input("Enter the third value : "))
Average = (n1+n2+n3)/3
print(f"Average of three numbers is : {Average}")

# find area of circle
# Formula : Area=pi*r*r = 3.14*r*r
r = int(input("Enter radius of the circle : "))
Area = 3.14*r*r
print(f"Area of circle is : {Area}")