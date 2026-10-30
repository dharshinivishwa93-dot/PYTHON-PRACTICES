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
