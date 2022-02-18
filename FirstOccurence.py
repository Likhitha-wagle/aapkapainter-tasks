a=[1,2,3,2,1]
# output=2
l=[]
f=[]
for i in a:
    if i not in l:
        l.append(i)
    else:
        f.append(i)
print(f[0])