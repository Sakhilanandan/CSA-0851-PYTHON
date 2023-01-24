n=int(input("enter theno.of namber:"))
L1=[]
while True:
    num=int(input("enter number="))
    if num=="":
        break
    else:
        L1.append(num)
        if len(L1)==n:
            break
print(L1)
def sumsquare(L1):
    odd=[]
    even=[]
    L2=[]
    for i in range(0,len(L1)):
        if L1[i]%2==0:
            even.append(L1[i])
        else:
            odd.append(L1[i])
    print(odd,even)
    evensquare=sum([x**2 for x in even])
    L2.append(evensquare)
    oddsquare=sum([x**2 for x in odd])
    L2.append(oddsquare)
    return(L2)
print(sumsquare(L1))
    
            

