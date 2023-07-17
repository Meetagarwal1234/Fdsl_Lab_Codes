def union(a,b):
    u=a.copy()
    for i in a:
        if i not in b:
            u.append(i)
    return u
def intersection(a,b):
    u=[]
    for i in a:
        if i in b:
            u.append(i)
    return u
def minus(a,b):
    m=[]
    for i in a:
        if i not in b:
            m.append(i)
    return m
c=input("Enter info for cricket :").split(',')
f=input("Enter info for football :").split(',')
b=input("Enter info for badminton :").split(',')
u=union(f,union(b,c))
print("List of students who play both cricket and badminton :",union(c,b))
print("List of students who play either cric or badminton but not both :",union(minus(c,b),minus(b,c)))
print("List of students who play neither cricket nor badminton",minus(u,union(c,b))
print("List of stud who play both cric and foot but not badminton :",minus(union(c,f),b))

