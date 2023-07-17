def display(arr,n,m):

    for i in range(n):
        for j in range(m):
            print(arr[i][j],end=" ")
        print()
def addition(arr1,arr2,n,m):
    arr=[]    
    for i in range(n):
        arrt=[]
        for j in range(m):
            arrt.append(arr1[i][j]+arr2[i][j])
            #print(arrt[i][j],end=" ")
        arr.append(arrt)
        #print("\n")
    display(arr,n,m)
def subtraction(arr1,arr2,n,m):
    arr=[]    
    for i in range(n):
        arrt=[]
        for j in range(m):
            arrt.append(arr1[i][j]-arr2[i][j])
            #print(arrt[i][j],end=" ")
        arr.append(arrt)
        #print("\n")
    display(arr,n,m)
def transpose(arr,n,m):
    temp=[]
    for i in range(n):
        temp1=[]
        for j in range(m):
            temp1.append(arr[j][i])
        temp.append(temp1)
    display(temp,n,m)

def multiplication(arr1,arr2,n,m):
    arr=[]
    for i in range(n):
        temp=[]
        for j in range(m):
            sum=0
            for k in range(m):
                sum+=arr1[i][k]*arr2[k][j]
            temp.append(sum)
        arr.append(temp)
    display(arr,n,m)
    
    
    
n=int(input("Enter rows :"))
m=int(input("Enter cols :"))
arr1=[]
print("Enter array 1:")
for i in range(n):
    arr=[]
    for j in range(m):
        arr.append(int(input()))
    arr1.append(arr)

print("Enter array 2:")
arr2=[]
for i in range(n):
    arr=[]
    for j in range(m):
        arr.append(int(input()))
    arr2.append(arr)
print("Array 1:")
display(arr1,n,m)
print("Array 2:")
display(arr2,n,m)
print("Addition :")
addition(arr1,arr2,n,m)
print("Subtraction :")
subtraction(arr1,arr2,n,m)
print("Transpose :")
transpose(arr1,n,m)
print("Multiplication :")
multiplication(arr1,arr2,n,m)