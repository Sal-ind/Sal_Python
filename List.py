print("\nLIST FUNCTIONS\n")
l1=[1,2,'Hello',3.4]
print(type(l1))
print(l1[0: ])
print(l1[ : ])
print(l1[2:4])
print(l1[ :4])
print(l1[1:4:2])
print(l1[-1])
print(l1[-3:-1])
l1[2]=10
print(l1)
l1[2:4]=[89,99]
print(l1)

print("\nREPEATITION")
l2=l1*2
print(l2)

print("\nCONCATINATION")
l3=l1+l2
print(l3)
print(len(l3))

print("\nITERATION")
for l in l3:
    print(l)

print("\nMEMBERSHIP")
print(1 in l1)

print("\nADDING ELEMENT IN LIST")
l4=[]
n=int(input("Enter number of element : "))
for i in range(0,n):
    l4.append(input("Enter element : "))
for i in l4:
    print(i,end='')
    print(l4)
l4.remove(i)
print(l4)
print(min(l4))
print(max(l4))
