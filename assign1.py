def avg(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    ans=sum/len(arr)
    return ans
def highlow(arr):
    min=arr[0]
    max=0
    for i in range(len(arr)):
        if(min>arr[i]):
            min=arr[i]
        if(max<arr[i]):
            max=arr[i]
    print("The Max and Min scores are :",max," and ",min)    
def highf(arr):
    max_count=0
    max_freq=arr[0]
    count=0
    for i in range(len(arr)):
        curr=arr[i]
        count=0
        for j in range (i,len(arr)):
            if(curr==arr[j]):
                count=count+1
        if(max_count<count):
            max_count=count
            max_freq=curr
    return max_freq
arr=[]
absent=0
n=int(input("Enter no of students :"))
for i in range(n):
    inp=input("Was the stud absent or present :(Type Y or N)\n")
    if(inp=='Y'):
        arr.append(int(input()))
    else:
        absent=absent+1
print("The avg of all marks of students :",avg(arr))
highlow(arr)
print("The number of stud absent for the test is :",absent)
print("Highest freq :",highf(arr))
