Count the number of digits
n = abs(int(input()))
count = 0
if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n //= 10
print(count)


Sum of Even Digitsn = int(input())
total = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        total += digit
    n //= 10
print(total)

Product of Digits
n = int(input())
product = 1

if n == 0:
    product = 0
else:
    n = abs(n)
    while n > 0:
        digit = n % 10
        product = product * digit
        n = n // 10

print(product)


Reverse a Number
n = int(input())
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print(reverse)

Palindrome Number

n = int(input())
temp = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if temp == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

First Digit of a Number
n = int(input())

while n >= 10:
    n = n // 10

print(n)


Count Zeros in a Number

n = input().strip()
count = n.count('0')
print(count)


Armstrong Number
n=int(input())
temp=n
digit=0
while n>0:
  n=n//10
  digit+=1
n=temp
sum=0
while n>0:
  last=n%10
  sum=sum+last**digit
if sum==temp:
  print("Armstrong")
else:
  print("Not Armstrong")


Strong Number
import math
n = int(input())
total = 0
for digit in str(n):
    total += math.factorial(int(digit))
if total == n:
    print("Strong")
else:
    print("Not Strong")

Check Perfect Number

n= int(input())
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i
if total == n:
    print("Perfect")
else:
    print("Not Perfect")































