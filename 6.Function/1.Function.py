# # ==============================function===============================================

# # def info():
# #     print('hello, world')
# # info()
# # info()

# # answer
# # hello, world
# # hello, world

# # next page..........


# def user(name,age):
#     print('hello',name,'and your age is',age)
# user('ram',20)

# # answer
# # hello ram

# def user(name,age=0):                        #for optional parameter age=0 and also it always stay in last
#     print('hello',name,'and your age is',age)
# user('ram')

# # answer
# # hello ram and your age is 0

# # next page..........
# def user(name):
#     print(name)
# user(['ram','sita','hari'])   


# def user(*name):
#     print(name)
# user('ram','sita','hari')

# # next page..........

# def user(*name,**about):
#     print(name)
#     print(about)
# user('ram','sita','hari',name='ram',age=20,address='ktm')

# # next page..........

# def add(x,y):
#     a = x+y
#     return a
# print(add(10,20))


# def add_sub(x,y):
#     a = x+y
#     b = x-y
#     return (a,b)
#     return [a,b]
# print(add_sub(10,20))


# # next page..........

# a=5
# def test():
#     b=a+100
#     print(b)
# test()

# a=5
# def test():
#     global a
#     a=a+200
#     print(a)
# test()



# next page..........

# a=lambda x,y: x+y
# print(a(10,40))

# # next page..........

# def fac(n):
#     if n==1:
#         return 1
#     else:
#         return n*fac(n-1)
    
# print(fac(5))

# 5-1=4=20
# 4-1=3=60
# 3-1=2=120
# 2-1=1=120          return 1


# next page..........

# ==============================function===============================================

# ************************************************************

# def add(x,y):
#     print(x+y)

# add(10,10)

# def substract(x,y):
#     print(x-y)

# add(10,10)

# def divide(x,y):
#     print(x/y)

# add(10,10)

# def multiply(x,y):
#     print(x*y)

# add(10,10)

# *********************************************************
# users=[
#     {'username':"admin","password":"admin002"},
#     {'username':"ram","password":"ram002"},
#     {'username':"shyam","password":"shyam002"}
# ]
# def login(username,password):
#    for user in users:
#       if user['username']==username and user['password']==password:
#          print("login successful")
#          return
#    print("login failed")
# uname=input("Enter username: ")
# pwd=input("Enter password: ")
# login(uname,pwd)

# ************************************************************

# numbers=[
#     [34,56,78,90,78],
#     [45,67,89,23,45],
#     [23,45,67,89,90]
# ]
# def even_number(numbers):
#     for number in numbers:
#         for num in number:  
#             if num%2==0:
#                 print("Even numbers are",num)
# even_number(numbers)
# ************************************************************

# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.now().date())
# print(datetime.datetime.now().time())
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().minute)
# print(datetime.datetime.now().day)


#next page*********

import datetime
oldYear=datetime.datetime(2020,1,1)
newYear=datetime.datetime.now()
print(newYear-oldYear)

# answer
# 1553 days

import datetime
joinDate='2020-01-01'
joinDate=datetime.datetime.strptime(joinDate,'%Y-%m-%d')              #for more we have to look in website


#next page*********

jobs=[
    {'title':'python developer','exp date':'2020-01-01'},
    {'title':'java developer','exp date':'2025-01-01'},
    {'title':'php developer','exp date':'2023-05-01'},
]
for job in jobs:
    expDate=job['exp date']
    expDate=datetime.datetime.strptime(expDate,'%Y-%m-%d')
    today=datetime.datetime.now()
    if expDate<today:
        print(f'{job['title']} is expired',today-expDate,'ago')
    else:
        print(f'{job['title']} is not expired')



# *********************************************************

import os          #it help us to check file
import sys          #we have to look in google