# try:
#     print(10/0)
# except ZeroDivisionError as a:          #Exception is also use as ZeroDivisionError
#     print(a)


# print('I am a boy')



def add(x,y):
    if y==0:
        raise Exception('Cant put 0 in Y')
    return x+y

try:
    print(add(3,0))
except Exception as a:
    print(a)