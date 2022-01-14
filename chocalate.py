

while(1):
    try:
        N=int(input("Enter no of chocalate\t"))
        M=int(input("Enter no of chocalate to father\t"))
        if((N>=1 and N<=1000) and (M>=1 and M<=N)):
            break
        else:
            continue
    except:
        print("not valid format")
        continue

A=[]

for ele in range(N):
    while(1):
        try:
            taste=int(input("Taste of chocalate-{}\t".format(ele+1)))
            if(taste>0):
                A.append(taste)
                break
            else:
                continue
        except:
            print("not valid format")
            continue

print(A)
A.sort()
print(A)
tastecount=1
