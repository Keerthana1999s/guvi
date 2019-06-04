x=int(input())
y=int(input())
z=int(input())
if y<=x and z<=x:
    print(x)
elif x<=y and z<=y:
    print(y)
else:
    print(z)