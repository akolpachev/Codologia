x=input()
s=list(x)
f=[]

for i in range(len(s)):
    f.append(s[i])
    if (s[i] == "," or s[i] == ".") and (s[i+1] != " "):
        f.append(" ")

res = "".join(f)
print(res)
