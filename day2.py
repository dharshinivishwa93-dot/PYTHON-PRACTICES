Identify the Nature of a Number

import struct
a=float(input())
a=struct.unpack("f",struct.pack('f',a))[0]
print("%.5f" % a)
print("%.4f" % a)
print("%.3f" % a)
print("%.2f" % a)
print("%.1f" % a)
print("%.0f" % a)


Explore Math Functions
import math

a = float(input())
b = int(input())
c = int(input())
d = int(input())

print(math.floor(a))
print(math.ceil(a))
print(round(a))
print(int(math.sqrt(b)))
print(c ** d)


Smallest of Four Numbers
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(min(a, b, c, d))


Truncate to Two Decimal Places
import math
n = float(input())
print(math.trunc(n * 100) / 100)

Find Second Maximum Number
a=int(input())
b=int(input())
c=int(input())
if a == b == c:
    print("No second max")
elif a >= b and a >= c:
    if b >= c:
        print(b)
    else:
        print(c)
elif b >= a and b >= c:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if a >= b:
        print(a)
    else:
        print(b)


Triangle Angle Validation
a = int(input())
b = int(input())
c = int(input())

if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("VALID")

    if a == b == c:
        print("EQUILATERAL")
    elif a == b or b == c or a == c:
        print("ISOSCELES")
    else:
        print("SCALENE")
else:
    print("NOT VALID")
    print()



Number to Word
n = int(input())

words = ["zero", "one", "two", "three", "four",
         "five", "six", "seven", "eight", "nine"]

print(words[n])


Vowel or Consonant
ch = input()

if ch in "aeiouAEIOU":
    print("vowel")
else:
    print("consonant")

Leap Year Checker

year = int(input())

if year % 400 == 0:
    print("yes")
elif year % 100 == 0:
    print("no")
elif year % 4 == 0:
    print("yes")
else:
    print("no")


Fun Grade Calculator

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

avg = (a + b + c + d + e) / 5

if avg >= 90:
    print("Excellent!")
elif avg >= 80:
    print("Great Job!")
elif avg >= 70:
    print("Good Effort!")
elif avg >= 50:
    print("Keep Trying!")
else:
    print("Better Luck Next Time!")


Train Berth Type Finder

n = int(input())
r = n % 8

if r == 1 or r == 4:
    print("LB")
elif r == 2 or r == 5:
    print("MB")
elif r == 3 or r == 6:
    print("UB")
elif r == 7:
    print("SL")
else:
    print("SU")




Electricity Bill Calculator
units = float(input())

if units <= 50:
    bill = units * 1
elif units <= 150:
    bill = 50 + (units - 50) * 2
elif units <= 250:
    bill = 50 + 200 + (units - 150) * 3
else:
    bill = 50 + 200 + 300 + (units - 250) * 4

if bill > 150:
    bill = bill + bill * 0.20

print(int(bill) if bill == int(bill) else bill)


Thala vs Thalapathy Game

n = int(input())

if n % 3 == 0 and n % 5 == 0:
    print("ThalaThalapathy")
elif n % 3 == 0:
    print("Thala")
elif n % 5 == 0:
    print("Thalapathy")
else:
    print(n)

Train Fare Calculator
age = int(input())
distance = int(input())

fare = distance * 5

if age < 12:
    fare = fare * 0.5
elif age >= 60:
    fare = fare * 0.75

print(int(fare) if fare == int(fare) else fare)


Average Marks Calculator

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

avg = (a + b + c + d + e) / 5

if avg.is_integer():
    print(int(avg))
else:
    print(f"{avg:.2f}")

Fun Character Case Converter

ch = input()

if ch.islower():
    print(ch.upper())
elif ch.isupper():
    print(ch.lower())
else:
    print("abcd theriyatha?")

































































