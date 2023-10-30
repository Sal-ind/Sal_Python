print("IF")
var1=100
if var1:
        print("if statements")
        print(var1)
print("Outside if\n")
print("IF ELSE")
var1 = 100
if var1:
        print("In if statements")
        print(var1)
else:
        print("Outside if")
print("\nELIF")
amount = int(input("Enter the Amount "))
if amount<1000:
        discount=amount*0.5
        print("Discount",discount)
elif amount<500:
        discount=amount*0.2
        print("Discount ",discount)
else:
         print("Discount",discount)

print("FOR LOOP")
n = 5
for i in range(0, n):
	print(i)
a=["First",1,2.0]
for i in a:
    print(i)
print("\nCONTINUE")
# Prints all letters except 'e' and 'p'
for b in 'DypcetKop':
    if b == 'e' or b =='p':
        continue
    print(b)
print("BREAK")
for l in 'DypcetKop':
    if l == 'e' or l == 'p':
        break
    print('Letter :', l)
print("\nPass")
for letter in 'DypcetKop':
	pass
print('Last Letter :', letter)
print("\nWHILE LOOP")
count = 0
while count < 5:
    count=count+1
    print("Hello Dypcet")
a=[1,2,3,4]
while a:
    print(a.pop())
print("Else With While")
count = 0
while (count < 3):
	print(count)
	count = count + 1
else:
	print(count)
Name = input('Enter Name ')
print(Name)
