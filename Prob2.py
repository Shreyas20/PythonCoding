#This function multiplies all the elements in the list and returns an integer answer.
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total


def comb(bee):
    out = [[] for i in range(len(bee)-2)] #List of list having no of lists equal to non-peripheral elements
    i = 0
    if len(set(bee)) == 1:
        return 1
    if len(set(bee)) == 2:
        return 4
    else:
        l=[]
        while i < len(bee)-2:    #This loop fill the inner lists for corresponding position which contains all possible element that position can hold
            out[i].append(bee[i])
            out[i].append(bee[i+1])
            out[i].append(bee[i+2])
            out[i]=list(set(out[i]))
            i += 1
        c=i
        #print(c)
        for i in range(0,c):
            l.append(len(out[i]))
        if bee[0]!=bee[1]:
            c1=2
        else:
            c1=1
        
        if bee[len(bee)-2]!=bee[len(bee)-1]:
            c3=2
        else:
            c3=1
        c2=multiply(l)
        return c1*c2*c3
    
#combos(w)

valid=False
while not valid:
    n=int(input("No of test cases:"))
    if 1<n<100:
        #print("Enter test cases less than 100")
        valid=True
    else:
        print("Enter no of test cases less than 100\n")
for i in range(0,n):
    excess=False
    while not excess:
        s=input("\nEnter string: ")
        if len(s)>5:
            excess=False
        else:
            print("Test case #",i+1,":",comb(s))
            excess=True
