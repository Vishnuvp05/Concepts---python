a=[1,2,3,3,2,3,4,5,2]
c=[]
for i in range(1,len(a)):
    if a[i] == a[i-1]:
        c.append(a[i])
print(c)


