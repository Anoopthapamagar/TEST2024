# x =1
# while x<=10:
#     print(x)
#     x+=1

# x =10
# while x>=1:
#     print(x)
#     x-=1

# x =1
# while x<=10:
#     print('RAM')
#     x+=1

# x =1
# while x<=10:
#     print(x)
#     x+=1

# ********************************************************************************

# data =[10,20,30,40,90,100]
# x =0
# while x<len(data):
#     print(data[x])
#     x+=1
    
# data =[19,3,4,9,8,11,14,19,100]
# x =0
# while x<len(data):
#     if data[x]%2==0:
#         print(data[x])
#     x+=1


x =3
y =4
while x<=30:
    print(x)
    x+=3
while y<=40:
    print(y)
    y+=4

# ************************************************************************************

# users=[]
# num=int(input('Enter the number of users'))

# for i in range(num):
#     name=input('Enter your name: ')
#     users.append(name)

# print('==========USER LIST==========')
# for user in users:
#     print(user)

# *******************************************************************

# users=[]
# num=int(input('Enter the number of users'))

# for i in range(num):
#     name=int(input('Enter your name: '))
#     users.append(name)

# print('==========USER LIST==========')
# for user in users:
#     if user%2==0:
#         print(user)
        

# # **************************************************************************

# for x in range(1,4):
#     print(f'=========ROW: {x}==========')
#     for a in range(1,11):
#         print(a,end='')
#     print()


# # *********************************************************************

# for x in range(6,11):
#     print(f'Table===================={x}')
#     for a in range(1,11):
#         print(f'{x}*{a}={a*x}')

# *************************************************************

# print('==========STUDENT RESULT==========')
# num = int(input('Enter the number of students: '))
# students_marks=[]
# for X in range(1,num+1):
#     print(f'==========STUDENT: {X}==========')
#     for marks in range(1):
#         nep =int(input('Enter marks'))
#         eng=int(input('Enter marks'))
#         math=int(input('Enter marks'))
#         sci=int(input('Enter marks'))
#         com=int(input('Enter marks'))
#         total=nep+eng+math+sci+com
#         students_marks.append(total)
        
# print('==========TOTAL==========')
# student_num=1
# print('S.N\t Total\t Percentage\t Grade')
# for totalamt in students_marks:
#     per =totalamt/5
#     grade=''
#     if per>35 and per<45:
#         grade ='C Grade'
#     elif per>45 and per<60:
#         grade ='B Grade'
#     elif per>60 and per<75:
#         grade ='A Grade'
#     elif per>75 and per<100:
#         grade ='A+ Grade'
#     else:
#         garde ='FAIL'
#     print(f'{student_num}\t {totalamt}\t {per}\t {grade}')
#     student_num+=1

# ****************************************************************
    
# for i in range(1,6):
#     print('*'*i)

# for j in range(6,1,-1):
#     print('*'*j)


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()


# for i in range(7,0,-1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()

# for i in range(1,8):
#     for j in range(1,i+1):
#         if i==6:
#             print('*moon*',end='')
#             break
#         else:
#             print('*',end='')
#     print()
# for i in range(1,8):
#     for j in range(1,i+1):
#         if i==6:
#             print('*sun**',end='')
#             break
#         else:
#             print('*',end='')
#     print()