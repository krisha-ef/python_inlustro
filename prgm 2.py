def permute(s,n):
    if len(s)==0 and n not in result:
        result.append(n)
    for i in range(len(s)):
        ch=s[i]
        left=s[:i]
        right=s[i+1:]
        permute(left+right,n+ch)
result=[]
permute("aab","")
for p in result:
    print(p)