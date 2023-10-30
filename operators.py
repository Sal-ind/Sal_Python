#arithematic operator
import operator
a = 4
b = 2
print("ADDITION")
print(operator.add(a,b))
print("SUBTRACTION")
print(operator.sub(a,b))
print("MULTIPICATION")
print(operator.mul(a,b))
print("DIVISION")
print(operator.truediv(a, b))
print(operator.floordiv(a, b))
print("MODULES")
print(operator.mod(a, b))
print("power")
print(operator.pow(a, b))

#comparison operators
B = 5
C = 45
print("Greater than")
print(operator.gt(B,C))
print("less than")
print(operator.lt(B,C))
print("Greater than or Equal to")
print(operator.ge(B,C))
print("Equal to")
print(operator.eq(B,C))
print("Not Equal")
print(operator.ne(B,C))

#logical operators
F = True
G = False
print("AND OPERATOR")
print(F and G)
print("OR OPERATOR")
print(F or G)
print("NOT OPERATOR")
print(not F)

#Bitwise operators
a = True
b = False
print("BITWISE AND")
print(a & b)
print("BITWISE OR")
print(a|b)
print("BITWISE NOT")
print(~a)
print("BITWISE XOR")
print(a^b)
print("BITWISE RIGHT SHIFT")
print(a>>b)
print("BITWISE LEFT SHIFT")
print(a<<b)

# assigment operator
a  = 2
b = 4
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a%=b
print(a)

#memebership operators
l = [45,54,63,75]
if(22 not in l):
    print( "22 is not preasent")
else:
    print("22 is presnt")
# identity operators
a = 5
if(5 is a):
    print("yes")
else:
    print("no")





