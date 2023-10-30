print("#LIST FUNCTIONS#")
l1=[1,2,'Hola',3.4]
print(type(l1))
print(l1[0:])
print(l1[:])
print(l1[2:4])
print(l1[:4])
print(l1[1:4:2])
print(l1[-1])
print(l1[-3:-1])
l1[2]=10
print(l1)
l1[2:4]=[89,36]
print(l1)

print("\n#REPETITION#")
l2=l1*2
print(l2)

print("\n#CONCATENATION#")
l3=l1+l2
print(l2)
print(len(l3))

print("\n#ITERATION#")
for l in l3:
    print(l)

print("\n#MEMBERSHIP#")
print(l in l1)

print("\n#PRINT ADDING ELEMENTS IN LIST#")
l4=[]
n=int(input("Enter Number of Element"))
for i in range(0,n):
    l4.append(input("Enter Element : "))
for i in l4:
    print(i,end='')
    print(l4)

l4.remove (i)
print(l4)
print (len(l4))
print(min(l4))
print(max(l4))


