list=[]

n=int(input("Enter no of elements\n"))


for i in range(0,n):
    ele=int(input())
    list.append(ele)
    
small=list[0]
greater=list[0]

for i in range(1,n) :
     if small>list[i] : small=list[i]
     if greater<list[i] :greater =list[i]
    
    
print("small no is",small)
print("greater no is",greater)    