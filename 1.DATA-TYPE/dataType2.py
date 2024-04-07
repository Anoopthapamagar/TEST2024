# 2.string

name ="raj"
print(type(name))
print(dir(name))
print(id(name))          # location of store in computer storage
print(len(name))

# next page..........

about ="my name is shyam"
print(about.title())
print(about.capitalize())
print(about.upper())

# next page..........

class human:
    age =50

    def info(self):
        print('I am superman')

h =human()
h.info()

# this is about bracket(h.info()) and line

# next page..........

# example
# 0     1     2     3     4      positive
# s     h     y     a     m
# -5   -4    -3    -2    -1      negative

name ="shyam"
print(name[2])

# answer
# y

about ='we are learning python'
print(about[6:])

# answer
#  learning python

about ='we are learning python'
print(about[6:12])

# answer          
# learn

# in google we can go in regexr.com for fast