vLength of a string
a=input()
print(len(a))

Join the strings

a=input()
b=input()
print (a +" "+b)

Compare the Strings

a = input()
b = input()
if a==b:
  print("true")
else:
  print("false")


First character of a string
a=input()
print(a[0])


Last character of a string

a=input()
print(a[-1])

Join first & last characters of a string
a=input()
print(a[0]+a[-1])


Uppercase check

a=input()
if a.isupper():
  print ("true")
else :
  print("false")

Lowercase check
a=input()
if a.islower():
  print ("true")
else :
  print("false")

String lengths equal or not

a=input()
b=input()
if len(a)==len(b):
  print("true")
else:
  print("false")

Reverse a string

a=input()
print(a[::-1])

Split strings by comma
a=input()
b=a.split(",")
for i in b:
  print(i)




remove vowels
a=input()
vow="aeiouAEIOU"
for i in a:
  if i in vow:
    a=a.replace(i,"")
print(a)
    

Reverse the character case

a=input()
print(a.swapcase())

Print ascii value

a=input()
print(ord(a))

Remove occurrences of a char

a=input()
b=input()
print(a.replace(b,""))

Search for a word

a=input()
b=input()
print( "true"if b in a else"false")

Count vowels and consonants
a=input()
v=0
c=0
vow="aeiouAEIOU"
for i in a:
  if i in vow:
    v+=1
  else:
    c+=1
print(v)
print(c)

Anagram check

a=input().lower().replace(" ","")
b=input().lower().replace(" ","")
if sorted(a)==sorted(b):
  print("true")
else:
  print("false")

Palindrome check
a=input()
if a==a[::-1]:
  print("true")
else:
  print("false")












