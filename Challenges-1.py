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