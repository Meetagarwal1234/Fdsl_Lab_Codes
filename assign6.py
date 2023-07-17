def quicksort(arr,left,right):
    if left<right: 
        partition_pos=partition(arr,left,right)
        quicksort(arr,0,partition_pos-1)
        quicksort(arr,partition_pos+1,right)
def partition(arr,left,right):
    pivot=arr[right]
    i=left
    j=right-1
    while(i<j):
        while(arr[i]<pivot and i<right):
            i+=1
        while(arr[j]>pivot and j>left):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    if(arr[i]>pivot):
        arr[i],arr[right]=arr[right],arr[i]
    return i
n=int(input("Enter the number of students :"))
arr=[]
for i in range(0,n,1):
    arr.append(int(input()))
quicksort(arr,0,len(arr)-1)
if(len(arr)>=5):
    print(arr[len(arr)-6:len(arr)])
    
