def distribute(cand):
    cand=sorted(cand)
    print(cand)
    #print(cand[1])
    i=0
    count=0
    while i<(len(cand)-1) and i+1!=len(cand):
        #print("item",i)
        if (cand[i]!=cand[i+1]):
            diff=cand[i+1]-cand[i]
            while diff!=0:
                if diff>=5:
                    diff=diff-5
                    count+=1
                    cand=[item+5 for item in cand]
                    cand[i+1]=cand[i+1]-5
                    print("added 5")
                elif diff>=2:
                    diff=diff-2
                    count+=1
                    cand=[item+2 for item in cand]
                    cand[i+1]=cand[i+1]-2
                    print("added 2")
                elif diff>=1:
                    diff=diff-1
                    count+=1
                    cand=[item+1 for item in cand]
                    cand[i+1]=cand[i+1]-1
                    print("added 1")
#                 print("d",diff)
#                 print("c",count)
                print("After",count," iteration/s ->",cand)
        i+=1
    #print(count)          
    return count

valid=False
while not valid:
    n=int(input("No of test cases:"))
    if 0<n<100:
        #print("Enter test cases less than 100")
        valid=True
    else:
        print("Enter no of test cases less than 100\n")
for i in range(0,n):
    cand=[]
    excess=False
    while not excess:
        s=int(input("\nEnter no of interns in Fenixwork: "))
        if (s)>10000:
            excess=False
        else:
            for i in range(0,s):
                e=int(input("No of given candies:"))
                cand.append(e)
            print("No of iterations: ",distribute(cand))
            
                
                    
            #print("Test case #",i+1,":",comb(s))
            excess=True


