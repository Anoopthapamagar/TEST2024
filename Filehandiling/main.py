# ***********************file types*******************
# modes: red, write, append, readwrite
# read : r , rb
# write : w , wb
# append : a , ab
# readwrite : r+ , rb+
# readwrite : w+ , wb+

# ***********************file types*******************
# about=open('Filehandiling/Sample.txt','w')
# about.write('hellooo')
# about.close()

# about=open('Filehandiling/Sample.txt','a')             #for row
# about.write('hellooo')
# about.close()

# about=open('Filehandiling/Sample.txt','a')             #for column
# about.write('hellooo\n')
# about.close()

# ***********************************************************************
# about=open('Filehandiling/Sample.txt','w')
# name=input('Enter your name: ')
# email=input('Enter your email: ')
# address=input('Enter your address: ')
# age=input('Enter your age: ')

# about.write(f'Hello {name}\n')
# about.write(f'Address: {address}\n')
# about.write(f'Email: {email}\n')
# about.write(f'Age: {age}\n')
# about.close()


# **************************************for read****************************

# about=open('Filehandiling/Sample.txt','r')
# print(about.read())          #real all
# print(about.readline())          #read first line only
# print(about.readlines())        #bring data in list

# with open('Filehandiling/Sample.txt','r') as file:
#     print(file.read())

# ****************************************for error*********************

# try:
#     with open('Filehandiling/Sample.txttttttttttttttttttttt','r') as file:
#         print(file.read())
# except Exception as e:
#     print(e)

# e=('Document is not matching')          #if we dont want system we can use our message like this


# *******************************************************************************
#*********************to create file*************************************
import os
if not os.path.exists('Filehandiling/SSSSSSSSSS.txt'):
    open('Filehandiling/SSSSSSSSSS.txt','w')
    print('File craeted')
    

