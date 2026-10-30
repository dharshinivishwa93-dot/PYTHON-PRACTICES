Find Index of a Key Number in an Array
a=int(input())
b=list(map(int,input().split()))
c=int(input())
if c in b:
  print(b.index(c))
else:
  print(-1)

Sum of Array Elements

a=int(input())
b=list(map(int,input().split()))
print(sum(b))

Sum of Odd and Even Elements in an Array

a=int(input())
b=list(map(int,input().split()))
odd=even=0
for i in b:
  if i%2==0:
    even+=i
  else:
    odd+=i
print(even,end=" ")
print(odd,end=" ")

Sum of Elements at Odd and Even Indices in an Array

a=int(input())
b=list(map(int,input().split()))
odd=even=0
for i in range(a):
  if i%2==0:
    even+=b[i]
  else:
    odd+=b[i]
print(odd,even)

Find Maximum Element in an Array

a=int(input())
b=list(map(int,(input().split())))
print(max(b))

Find Minimum Element in an Array
a=int(input())
b=list(map(int,(input().split())))
print(min(b))

Find Maximum Odd and Even Elements in an Array
a = int(input())
b = list(map(int, input().split()))
even = []
odd = []
for i in b:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
if even:
    print(max(even))
else:
    print("None")
if odd:
    print(max(odd))
else:
    print("None")
  
 Check if a Key Number Exists in an Array
 
 a=int(input())
b=list(map(int,input().split()))
c=int(input())
if c in b:
  print("Yes")
else:
  print("No")   

Find Index of a Key Number in an Array


a=int(input())
b=list(map(int,input().split()))
c=int(input())
if c in b:
  print(b.index(c))
else:
  print(-1)













































































































