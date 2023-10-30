print("Hello World")
a=10
b=5.50
c=a+b
print(c)
print(type(a))
print("DataTypes")
name='Hi'
print('List')
d=[18,"Vivek",98.50]
print(d)
#tuple
t=(9,'Viv',18)
print(t)
#Boolean
e=True
print(type(e))
print(e)
print("Dictionary")
dict = {
  1: "Ford",
  2: "Mustang",
  "year": 1964
}
print(dict.keys())
print(dict.values())
print(dict)
#set
N=set([0,1,2,3,4,5,6,7,8,9])
print(N)
Animal = frozenset(['Cat',"Lion",'Tiger'])
print ('Tiger' in Animal)
print(Animal)
print("Range")

x = range(2, 18, 2)
for n in x:
  print(n)
