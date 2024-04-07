# import TESTModule1

# print(TESTModule1.name)           #this are variable
# print(TESTModule1.brand)           #this are variable
# print(TESTModule1.add(5,9))           #this are function
# print(TESTModule1.info())           #this are function

# ***********************************************************import processs

# from TESTModule1 import add     #if there is same variable and function in different file then import don't support
# print(add(5,9))

# from TESTModule1 import name
# print(name)

# from TESTModule1 import *                    #For all we used *
# print(name)

# ***********************************************************import processs
# from TESTModule1 import add          #if there is same variable and function in different file then import don't support
# from TESTModule3 import add as about
# print(add(5,9))
# print(about())



# next page1111111111111111111111111111111111111111111
# *********************************for result folder*****************

# import result.resultTEST as s
# print(s.mark())

# from result import resultTEST
# print(resultTEST.mark())


from result import *                    #to active this we have to put __init__.py
print(resultTEST.mark())