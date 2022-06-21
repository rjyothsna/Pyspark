'''

python is high level,interpreted and object oriented scripting language
it is easy to read and write.
it supports the artificial intelligence and machine learning projects
it is a most popular and widely used and can run any operating system

python is open source programming language
python features
     1.easy to learn
     2.easy to read
     3.easy to maintenance
     4.abroad standard library
     5.interactive mode
     6.portable
     7.python is interpreted
     8.python is object oriented

python deletes unwanted objects the automatically ,whenever the referral count is 0 then that time
it will be garbage collection .
using gc module we can do it
and we can destroy objects manually

python is an interpreted programming language because it goes through an interpreted,which turns the code
you write into the language understood by computer process

python is dynamically programming language because we don't have the declare the type of the variable
while assigning value to a variable in python .there is no strict declaration in python

compile vs runtime
compile : compile time is when the programming code is converted to machine code
runtime : runtime is when program is running and generally occurs in compile time

a namespace is a system that has a each and every object in python

variable is a name which is refers to the memory location of value.

types of variables:

global variables can be accessed globally in the entire program,
local variables can be accessed only within the function or block in which they are defined.

memory allocation can be defined as allocating a block of space in the computer memory to a
program.in python memory allocation and de-allocation method is automatic as the python
developers created a garbage collection for python so that the user does not have to do
manual garbage collection
tokens
tokens are small individual objects in python . all statements and instructions that are in the python

'''

x = 10
print(type(x))

print(id(x))

print(x)
a= 11
print(a)

x = "@l23"
y = "#456"
z = "$789"
print(type(x),type(y),type(z))

x = 10.4
print(type(x))
print(id(x))

print(x)



x = 10
y = 20
z = 30
print("--------------")
print(id(x),type(x),id(y),type(y),type(z))
del x
print("====")
print(id(y),id(z))
print("93499999943hh")
x = 10
print(id(x))

print("sum of tw0 umbers")

c = 3 + 3.5j
d = 4+5.2j
e = c+d
print("ejf",e)

# a program to converts the numbers from octal,binary and hexadecimal systems into decimal number systems

n1 = 0o1563
n2 = 0B1110010
n3 = 0X1c2
n = int(n1)
print("octal 17:",n)
n = int(n2)
print("binary :",n)
n = int(n3)
print("hexa:",n)

n1 = "17"
n2 = "1110010"
n3 = "1c2"
n = int(n1,8)
print("octal 17:",n)
n = int(n2,2)
print("binary :",n)
n = int(n3,16)
print("hexa:",n)
a = 17
b= oct(a)
print(b)

a = 1
b = 2
if a<b: #a>b
    print("hello")
'''
if the codition is true then it wiil print hello otherwise they dont print a
anything
'''

c = a>b
print(c)
'''
if the condition is true then it print true condition is false thne it false
'''
# a python progrsm to careat the byte array, raed and display the elements of the array

elements =  [1,2,3,4,5]
x = bytes(elements) # converters to byte type of arrays
print(x)
for i in x:
    print(i)
#a python program to create the bytearray type, replace the values and display the elements of the array
elements =  [1,2,3,4,5]
x = bytes(elements) # convetrs to byte type of arrays
print(x)
for i in x:
    print(i)

ele = [2,32,98,64,43]
a = bytearray(ele)
a[0]= 11
a[3]= 12
print("length of the a",len(a))
le = 0
for i  in a:
    le+=1
print("length of the a:",le)
print(a)
for i in a:
    print(i)
r = range(10)
for i in r:
    print(i)
r = range(30,40,2)
'''
here the starting size is 30, and ending is 39 ,if every time it will be increased by 2

'''
for i in r:
    print(i)
lst = list(range(10,30,3))
print(lst)
print("-----------set---------")

s = {12,3,4,3,6,7,45}
print(s)
ch = set("helo")
print(ch)

str = 'bharat'
for i in str:
    print(i)

str = 'bharat'
print(str[2])
str = 'bharat'
str[0].islower()
print("find the square root")
n = 6.2
num_sqt = n**0.5
print(num_sqt)

print("area of the trangle")
a = 394
b = 39
s = (a+b)/2
a = (s*(s-a)*(s-b))**6
print("areaa of the triangle",a)


print("swapping the two numbers")
x =9
y = 8

temp = x
x = y
y = temp

print(x)
print(y)

print("variables")
f = 0 # here declare a variable and initialize it
print("f is the variavle:",f)
# here the f value is re-declaring the varible works
f = '12'
print("f is the another variable:",f)
del f
#print(f)
# #once you delete the  f and  print f it will showes the error it means already f is deleted

num1 = 12#int(input("enter a number:"))
num2 = 21#int(input("enter a number:"))
# swapping the numbars using b variable
b=num1
num1=num2
num2 = b
print("after swapping the num1:",num1)
print("after swapping the num2:",num2)

print("------------------OPERATOR--------------")
print("------------ARITHMETIC OPERATOR---------")
'''
Arithmetic Operators include +,-,*,/,%
** exponential, // floor division
floor division rounds the output to nearest whole number
functionality : take number (int , float) input and perform arithmetic operations
'''
var1 = int(input("Enter var1"))
var2 = int(input("Enter var2"))
var3 = var1 + var2
print("Sum of variables is " , var1)
print("Difference is ", var1-var2)
print("Product is ", var1*var2)
print("Divident is ",var1/var2)
print("Remainder is ", var1%var2)
print("Floor Divident ", var1//var2)
print("Exponentation is ", var1**var2)


print('----------Relational(Comparison) Operators------------')
'''
== : equality
!= : notequal
> : greater than
< : less than
>= : greater than are equal to
<= : less than are equal to

'''
var1 = int(input("Enter var1"))
var2 = int(input("Enter var2"))
print("var1 == var2", var1==var2 )
print("var1 != var2", var1!=var2 )
print("var1 > var2", var1>var2 )
print("var1 < var2", var1<var2 )
print("var1 >= var2", var1>=var2 )
print("var1 <= var2", var1<=var2 )

print("---------Assignment Operators --------")
'''
+= : addition and
-= : subtract and
*= : multiplication and
/= : division and
%= : modulus and
**= : exponent and
//= : floor division and

'''
a = int(input("enter a number:"))

c += a
print("addition and:=",c)
c -= a
print("substract and=",c)
c *= a
print("multiple and:",c)
c/= a
print("division and=",c)
c**=a
print("exponent and =",c)
c//=a
print('floor division = ',c)


print("----------logical operators------------")
'''
and
or 
not
'''
var1 = 23
var2 = 34
var3 = 21
print( var1 > 34 and var2 < var3)
print(var2>45 or var3 < var1)
print(not(var2>var3 and var3 <var1))


print('----------------Binary operators------------------')
'''
& : Binary AND
| : Binary OR
^ : Binary XOR
~ : Binary Ones Complement
<< : Binary Left Shift
>> : Binary Right Shift

'''
a = 10
b = 20
print("binary and =",a&b)
print("binary or = ",a|b)
print('binary xor=',a^b)

print("---------KEYWORDS---------")
'''
 
keyword	      Description
---------------------------------
and	   :A logical operator
as	   :To create an alias
assert :	For debugging
break	: To break out of a loop
class	 :To define a class
continue	:To continue to the next iteration of a loop
def	 : To define a function
del : 	To delete an object
elif	: Used in conditional statements, same as else if
else	: Used in conditional statements
except	: Used with exceptions, what to do when an exception occurs
False:	Boolean value, result of comparison operations
finally	:Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for : 	To create a for loop
from :	To import specific parts of a module
global :	To declare a global variable
if	 : To make a conditional statement
import :	To import a module
in	 : To check if a value is present in a list, tuple, etc.
is	: To test if two variables are equal
lambda: To create an anonymous function
None	:Represents a null value
nonlocal:	To declare a non-local variable
not	:A logical operator
or	 : A logical operator
pass:	A null statement, a statement that will do nothing
raise:	To raise an exception
return	:To exit a function and return a value
True	: Boolean value, result of comparison operations
try	: To make a try...except statement
while: 	To create a while loop
with	:  Used to simplify exception handling
yield: 	To end a function, returns a generator
'''

word = "tea"
print("word:",word)

word = 10
print(word)

a=10
b=122
c=19
print("a:",a,"b:",b,"c:",c)

word = 22
print(word)