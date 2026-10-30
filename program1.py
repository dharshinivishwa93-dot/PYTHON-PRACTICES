a=int(input())
b=float(input())
c=input()
d=int(input())
e=float(input())
print(a)
print(b)
print(c)
print(d)
print(e)



Progressive Float Execution
import struct
a=float(input())
a=struct.unpack("f",struct.pack('f',a))[0]
print("%.5f" % a)
print("%.4f" % a)
print("%.3f" % a)
print("%.2f" % a)
print("%.1f" % a)
print("%.0f" % a)


Problem: Sum, Difference, Product, Division and Modulo.
A,B=map(int,input().split())
print(A+B)
print(A-B)
print(A*B)
print(int(A/B))
if A<0 or B<0:
  mod=abs(A)%abs(B)
  print(-1*mod)
else:
  print(A%B)



ASCII
n=int(input())
print(chr(n))

Update Counter
n=int(input())
result = (n+5)*2-3
print(result)


ODD or EVEN
n=int(input())
result="Even"if n%2==0 else "Odd"
print(result)


Greatest Among Three Numbers
a=int(input())
b=int(input())
c=int(input())
result=a if a>b and a>c else (b if b>c else c)
print(result)


Character Digit to Integer
ch=input().strip()
result=int(ch)
print(result)


Personalized Greeting
name=input()
print(f"Hi {name}, welcome to the programming class!")

Calculate Total and Average Marks
m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
total=m1+m2+m3+m4+m5
avg=total/5
print("Student Name:",name)
print("Total Marks:",mark)
print("Average Marks:",avg)



Shape Area Calculation
a = int(input())
l = int(input())
b = int(input())
r = int(input())
B = int(input())
h = int(input())
print("Area of Square=%d"%(a*a))
print("Area of Rectangle=%d"%(l*b))
print("Area of Circle=%.2f"%(3.14*r*r))
print("Area of Triangle=%d"%(int((0.5)*B*h)))


Shape Perimeter Calculation Program
a=int(input())
length=int(input())
width=int(input())
radius=int(input())
side1=int(input())
side2=int(input())
base=int(input())
print(4*a)
print(2*(length+width))
print("%.2f"%(2*3.14*radius))
print(side1+base+side2)



Handling Mixed Inputs
a=int(input())
b=input()
print(a)
print(b)


