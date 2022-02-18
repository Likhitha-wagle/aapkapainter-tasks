inp1="Mary"
inp2="Army"
l=[c for c in inp1.lower()]
m=[d for d in inp2.lower()]
count=0
if len(l)==len(m):
    for i in l:
        if i in m:
            count=count+1
            if count==len(l):
                print("Anagrams")
        else:
            print(i)
            print("Not anagrams")