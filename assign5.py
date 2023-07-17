def display(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
    print()
def selection(arr,n):
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if(arr[min]>arr[j]):
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    display(arr,n)
 
def bubble(arr,n):
    for i in range(n-1):
        for j in range(0,n-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
            #display(arr,n)
    print("Done")
    display(arr,n)
             
arr=[]
n=int(input("Enter no of ele :"))
for i in range(n):
    arr.append(int (input()))
selection(arr,n)
print()
#bubble(arr,n)
if(len(arr)>=5):
    print("Top 5 scores of students are :",arr[len(arr)-5:len(arr)])
    