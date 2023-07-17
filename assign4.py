def sorting(arr,left,right):
    if(left<right):
        partition_ind=partition(arr,left,right)
        sorting(arr,0,partition_ind-1)
        sorting(arr,partition_ind+1,right)
def partition(arr,left,right):
    i=left
    j=right-1
    pivot=arr[right]
    while(i<j):
        while(arr[i]<pivot and i<right):
            i+=1
        while(arr[j]>=pivot and j>left):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    if(arr[i]>pivot):
        arr[right],arr[i]=arr[i],arr[right]
    return i

def ternary_search(arr,left,right,key):
    while(left<=right):
        mid1=left+(right-left)//3
        mid2=right-(right-left)//3
        if(key==mid1 or key==mid2):
            return 1
        elif(key<mid1):
            ternary_search(arr,left,mid1-1,key)
        elif(key>mid2):
            ternary_search(arr,mid2+1,right,key)
        else:
            ternary_search(arr,mid1+1,mid2-1,key)
    return 0
        
        
arr=[]
n=int(input("Enter the number of elements you want :\n"))
for i in range(n):
    arr.append(int(input()))
sorting(arr,0,len(arr)-1)
print(arr)
key=int(input("Enter key to search :\n"))
b=ternary_search(arr,0,len(arr)-1,key)
if(b==1):
    print("Element found")
else:
    print("Element not found")