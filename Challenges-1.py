""" 1. Positive or Negative Number """
# method 1:ternary operator
a = int(input("Enter Number:"))
print("Positive" if a>0 else ("Negative" if a<0 else "Zero"))
# method 2: if-elif-else
b = int(input("Enter Number:"))
if b>0 :
    print("Positive")
elif b<0:
    print("Negative")
else:
    print("Zero")
""" 2. Even or Odd """
# method 1: ternary operator
c = int(input("Enter Number:"))
print("Even" if c%2==0 else "Odd")
# method 2 : if-else
d = int(input("Enter Number:"))
if d%2==0:
    print("Even")
else:
    print("Odd")
""" 3. Sum of N natural numbers """
# method 1: using sum() and range() function
e = int(input("Enter Number:"))
print(sum(range(e+1)))
# method 2: using for loop
f = int(input("Enter Number:"))
total = 0
for i in range(1,f+1):
    total += i # total = total + i
print(total)
""" 4. Sum of Numbers in a given range """
# method 1: using sum() and range() funtion
g = int(input("Enter Number:"))
h = int(input("Enter Number:"))
print(sum(range(g,h+1)))
# method 2: using for loop
k = int(input("Enter Number:"))
l = int(input("Enter Number:"))
result = 0
for i in range(k,l+1):
    result += i # result = result + i
print(result)
""" 5. Greatest of Two Numbers """
m = int(input("Enter Number:"))
n = int(input("Enter Number:"))
if m>n:
    print(f"{m} is Greatest")
elif n>m:
    print(f"{n} is Greatest")
else:
    print("Both Are Equal")
""" 6. Greatest of Three Numbers """
# method 1: using if else & logical operator
p = int(input("Enter Number:"))
q = int(input("Enter Number:"))
r = int(input("Enter Number:"))
if p == q == r :
    print("All are Equal")
elif p>q and p>r:
    print(f"{p} is Greater than {q} and {r}")
elif q>p and q>r :
    print(f"{q} is Greater than {p} and {r}")
elif p == q and p>r:
    print(f"{p} and {q} is Equal and Greater than {r}")
elif q == r and q>p:
    print(f"{q} and {r} is Equal and Greater than {p}")
elif r == p and r>q:
    print(f"{r} and {p} is Equal and Greater than {q}")
else:
    print(f"{r} is Greater than {p} and {q}")
""" 7.Find LCM of Two Numbers """
s = int(input("Enter Number:"))
t = int(input("Enter Number:"))
large = max(s,t)
lcm = large
while  not (lcm % s == 0 and lcm % t == 0):
    lcm += large
print(lcm)
""" 8.Find GCD or HCF of Two Numbers """
u = int(input("Enter Number:"))
v = int(input("Enter Number:"))
gcd = 0
for i in range(2,min(u,v)+1):
    if  u % i ==0 and v % i == 0:
        gcd = i
print(gcd)
""" 9.Check Two Numbers are Co-Prime or not """
w = int(input("Enter Number:"))
x = int(input("Enter Number:"))
hcf = 1
for i in range(2,min(w,x)+1):
    if  w % i ==0 and x % i == 0:
        hcf = i
print("Co-Prime" if hcf==1 else "Not Co Prime")
""" 10.Find All Divisors of a Number """
y = int(input("Enter Number:"))
for i in range(1,y+1):
    if y%i==0:
        print(i,end=" ")
print()
""" 11. Count Distinct Elements in an Array """
z = int(input("Enter length of an array:"))
array = []
for i in range(1,z+1):
    j = input("Enter Element:")
    array.append(j)
unique_array = set(array)
print(len(unique_array))