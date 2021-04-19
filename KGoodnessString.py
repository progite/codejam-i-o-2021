t=int(input())
for j in range(t):
    n,k=[int(x) for x in input().split()]
    s=input()
    counter=0 
    ans=0
    for i in range(0,n//2):
        x=s[i]
        y=s[n-(i+1)]
        if x!=y:
            counter+=1 
    if counter<k:
        for i in range(0,n//2):
            x=s[i]
            y=s[n-(i+1)]
            if counter==k:
                break
            if x==y:
                counter+=1
                ans+=1 
    elif counter>k:
        for i in range(0,n//2):
            x=s[i]
            y=s[n-(i+1)]
            if counter==k:
                break
            if x!=y:
                counter-=1
                ans+=1
    print("Case #",(j+1),": ",ans,sep="")
