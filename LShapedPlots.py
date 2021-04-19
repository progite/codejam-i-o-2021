t=int(input())
for count in range(t):
    r,c=[int(x) for x in input().split()]
    a=[]
    for counter in range(r):
        a.append([int(x) for x in input().split()]) 
    rcount=0
    ans=0
    
    for rcount in range(r):
        for ccount in range(c):
            x=a[rcount][ccount]
            j=0
            check1=[]
            check2=[]
            if x!=0:
                l1=0
                for j in range(rcount,r):
                    y=a[j][ccount]
                    if y==0:
                        j=j-1 
                        rcount=j+1
                        break 
                    elif y==1:
                        check1.append([j+1,ccount+1])
                        l1+=1 
                    if l1>=2:
                        e=ccount
                        l2=0
                        check2=[]
                        for i in range(e,-1,-1):
                            y=a[j][i]
                            if y==0:
                                i=i+1 
                                break 
                            elif y==1:
                                check2.append([j+1,i+1])
                                l2+=1 
                            if l2>=2:
                                if l1==l2*2 or l2==l1*2:
                                    #print("check1",check1,"check2",check2)
                                    ans+=1 
                        check2=[]
                        l3=0
                        for i in range(e,c):
                            y=a[j][i]
                            if y==0:
                                i=i-1 
                                break 
                            elif y==1:
                                check2.append([j+1,i+1])
                                l3+=1 
                            if l3>=2:
                                if l1==l3*2 or l3==l1*2:
                                    #print("check1",check1,"check2",check2)
                                    ans+=1
    for ccount in range(0,c):
        for rcount in range(0,r):
            x=a[rcount][ccount]
            j=ccount
            if x!=0:
                l1=0
                check1=[]
                for j in range(ccount,c):
                    y=a[rcount][j]
                    if y==0:
                        j=j-1
                        ccount=j+1 
                        break 
                    elif y==1:
                        check1.append([rcount+1,j+1])
                        l1+=1 
                    if l1>=2:
                        e=rcount
                        l3=0
                        check2=[]
                        for i in range(e,r):
                            y=a[i][j]
                            if y==0:
                                i=i-1

                                break 
                            elif y==1:
                                check2.append([i+1,j+1])
                                l3+=1 
                            if l3>=2:
                                if l1==l3*2 or l3==l1*2:
                                    #print("check1",check1,"check2",check2)
                                    ans+=1
    for ccount in range(c-1,-1,-1):
        for rcount in range(0,r):
            x=a[rcount][ccount]
            j=ccount
            if x!=0:
                l1=0
                while True:
                    y=a[rcount][j]
                    if j<0:
                        break 
                    if y==0:
                        j=j-1 
                        break 
                    elif y==1:
                        #check1.append([rcount+1,j+1])
                        l1+=1 
                    if l1>=2:
                        e=rcount
                        l3=0
                        check2=[]
                        for i in range(e,r):
                            y=a[i][j]
                            if y==0:
                                i=i-1 
                                break 
                            elif y==1:
                                check2.append([i+1,j+1])
                                l3+=1 
                            if l3>=2:
                                if l1==l3*2 or l3==l1*2:
                                    #print("check1",check1,"check2",check2)
                                    ans+=1
                    j-=1
    print("Case #",count+1,": ",ans,sep="")
