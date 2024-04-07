# 1.number

age =2024
print(type(age))
print(dir(age))

# next page..........

a =5+6
print("real",a.real)
print("image",a.imag)

# answer
# real 11
# image 0

# next page..........

a =5+6j
print("real",a.real)
print("image",a.imag)

# answer
# real 5.0
# image 6.0

# confused j is accepted but b c d is not accepted !!!!!!!!!!!!!!!!!!!!
# next page..........

a =5.123
b =5
print(type(a))
print(type(b))

# answer
# <class 'float'>
# <class 'int'>

# next page..........

x =input('enter x:')
y =input('enter y:')
print(x+y)                    # in terminal we have to put name and age and then only it will finished
                            
# answer
# enter x:6
# enter y:9
# 69

# Because x and y is a string type, strings will not be added

# next page..........

x =input('enter x:')
print(type(x))
x =int(x)
print(type(x))       
y =input('enter y:')
print(type(y))
y =int(y)
print(type(y))         
print(x+y)   

# we had convert x =int(x) y =int(y) str to int

# answer
# enter x:6
# <class 'str'>
# <class 'int'>
# enter y:6
# <class 'int'>
# <class 'int'>
# 12

# shorcut
x =int(input('enter x:'))
y =int(input('enter y:'))
print(x+y)    

# next page..........

a=63
print(bin(a))          # for binary number system
print(chr(a))          # for character code(search in google for ascii table)

a="b"
print(ord(a))           # for order code(for alphabet)(search in google for ascii table)
