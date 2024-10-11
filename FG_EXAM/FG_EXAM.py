print("1.Algorithm Simulations")
print("Before:")
x=[1,2,3,4,5]
y=[]
z=[]
print(x)
print(y)
print(z)
print("After:")
y.append(x.pop())
y.append(x.pop())
z.append(x.pop())
z.append(x.pop())
z.append(x.pop())
z.sort()
print(x)
print(y)
print(z)
print("---------------------------------------------")
print("2.")
X=[1,2,21,33,45,65,12]
print(X)
print("Insertion Sort:")
for i in range(1,len(X)):
    key=X[i]
    j=i-1
    while j>=0 and key>X[j]:
        X[j+1]=X[j]
        j-=1
    X[j+1]=key
print(X)
print("Selection Sort:")
for i in range(len(X)):
    min_idx=i
    for j in range(i+1,len(X)):
        if X[min_idx]>X[j]:
            min_idx=j
    X[i],X[min_idx]=X[min_idx],X[i]
print(X)