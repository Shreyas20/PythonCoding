import re
def merge(l,r):
    count=0
    global clist
    clist=[]
    result = []
    i,j = 0, 0
    while i<len(l) and j< len(r):
        
        if l[i] <= r[j]:
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
            j+=1
            count+=1

    result += l[i:]
    result += r[j:]
    clist.append(count)
    return result


def mergesort(lst):
    if(len(lst) <= 1):
        return lst
    mid = int(len(lst)/2)
    l = mergesort(lst[:mid])
    r = mergesort(lst[mid:])
    return merge(l,r)
valid=False
while not valid:
    tc=int(input("No of test cases:"))
    if tc<100:
        #print("Enter test cases less than 100")
        valid=True
    else:
        print("Enter test cases less than 100\n")
        
for i in range(0,tc):
    arr=[]
    enough=False
    while not enough:
        noIp=int(input("No of input strings:"))
        if noIp<10:
            
            enough=True
        else:
            print("Enter no of elements less than 10\n")
            
    c=0
    while c<noIp:
        #print("pre c",c)
        ele=input("element:")
        if not re.match("^[a-zA-Z ]*$", ele):
            print("Contains number or symbol\n")
            continue
        nl=0
        for l in ele:
            nl+=1
        #print("nl",nl)
        if nl>=100:
            print("Enter less than 100 characters\n")
            continue
        if(ele.count(" ")>1):
            print("Contains more than 1 spaces\n")
            continue
        c+=1
        #print("post c",c)
        arr.append(ele)
    print("Entered cards:",arr)
    print("Sorted cards",mergesort(arr),"\n")
    print("Test case #",i+1,":",clist[0],"\n")
