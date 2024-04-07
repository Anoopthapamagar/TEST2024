# x = 70
# y = 20
# z = 50

# if x > y and x > z:
#     print('x is greatest number')
# elif y > x and y > z:
#     print('y is greatest number')
# else:
#     print('z is greatest number')


# ***********************************************


# Math = int(input('enter marks of math: '))
# English = int(input('enter marks of english: '))
# Nepali = int(input('enter marks of nepali: '))
# Science = int(input('enter marks of science: '))
# Grammar = int(input('enter marks of grammar: '))

# TotalMarks = Math + English + Nepali + Science + Grammar
# Percentage = (TotalMarks / 500) * 100

# print('Total marks:', TotalMarks)
# print('Percentage:', Percentage)

# if Percentage >= 90 and Percentage <= 100:
#     print('Grade A+')
# elif Percentage >= 75 and Percentage < 90:
#     print('Grade A')
# elif Percentage >= 60 and Percentage < 75:
#     print('Grade B')
# elif Percentage >= 45 and Percentage < 60:
#     print('Grade C')
# else:
#     print('Fail')


# ***********************************************


# users=[
#     ['admin','admin002'],
#     ['ram','ram123']
# ]

# username=input('Enter your username: ')
# password=input('Enter your password: ')

# if users[0][0]==username and users[0][1]==password:
#     print('Hiii',username)
# elif users[1][0]==username and users[1][1]==password:
#     print('Hiii',username)
# else:
#     print('Invalid username or password')


# ***********************************************


# print('==========WELCOME TO ATM==========')

# password =1234
# Amount =100000

# PIN=int(input('Enter your PIN: '))

# if password==PIN:
#     print('1.Check balance')
#     print('2.Withdraw amount')
#     option=int(input('Enter your Option: '))
#     if option==1:
#         print('Your balance is:',Amount)
#     elif option==2:
#         NewAmount=int(input('Enter Withdraw Amount: '))
#         if NewAmount<=Amount:
#             Balance=Amount-NewAmount
#             print('Please collect your cash')
#             print('Your withdraw amount:',NewAmount)
#             print('Your new balance is:',Balance)
#         else:
#             print('Insufficient Balance')
#     else:
#         print('Invalid Option')
# else:
#     print('Wrong PIN')


# ***********************************************

# Dell = 40000
# MAP = 50000
# Toshiba = 60000

# Items = input('Enter item: ')
# Quantity = int(input('Enter quantity: '))
# if Items == 'Dell':
#     TotalAmount = Quantity * Dell
#     print("Total Amount:", TotalAmount)
#     print('1.Home delivery: 100')
#     print('2.Pickup: 0')
#     Option =int(input('Option: '))
#     if Option ==1:                   #1111
#         HomeDelivery = 100
#         AllTotalAmount = TotalAmount + HomeDelivery
#         print(f'Total amount: {TotalAmount} + Home delivery: {HomeDelivery} = {AllTotalAmount}')
#         print('Packing Option')
#         print('1.Plastic: 100')
#         print('2.Box: 200')
#         PackingOption =int(input('Packing Option: '))
#         if PackingOption ==1:                    #22222
#             Plastic =100
#             AllTotal =AllTotalAmount + Plastic
#             print(f'Total amount: {AllTotalAmount} + Plastic Packing: {Plastic} = {AllTotal}')
#             print('Choose location')
#             print('1.Kathmandu 13%')
#             print('2.Out of valley 0%')
#             Chooselocation =int(input('Location Option: '))
#             if Chooselocation ==1:
#                 Kathmandu =13/100
#                 TaxAmount =Kathmandu*AllTotal
#                 GrantTotal =AllTotal + TaxAmount
#                 print(f'Total amount: {AllTotal} + Tax Amount: {TaxAmount} = {GrantTotal}')
#                 print(f'Items: {Items}')
#                 print(f'Quantity: {Quantity}')
#                 print(f'Tax Amount: {TaxAmount}')
#                 print(f'Grant Total: {GrantTotal}')
#             elif Chooselocation ==2:
#                 OutOfValley =0
#                 GrantTotal =AllTotal + OutOfValley
#                 print(f'Total amount: {AllTotal} + Tax Amount: {OutOfValley} = {GrantTotal}')
#                 print(f'Items: {Items}')
#                 print(f'Quantity: {Quantity}')
#                 print(f'Tax Amount: {OutOfValley}')
#                 print(f'Grant Total: {GrantTotal}')
#             else:
#                 print('Please Choose location')         
#         elif PackingOption ==2:                    #22222
#             Box =200
#             AllTotal =AllTotalAmount + Box
#             print(f'Total amount: {AllTotalAmount} + Box Packing: {Box} = {AllTotal}')
#             print('Choose location')
#             print('1.Kathmandu 13%')
#             print('2.Out of valley 0%')
#             Chooselocation =int(input('Location Option: '))
#             if Chooselocation ==1:
#                 Kathmandu =13/100
#                 TaxAmount =Kathmandu*AllTotal
#                 GrantTotal =AllTotal + TaxAmount
#                 print(f'Total amount: {AllTotal} + Tax Amount: {TaxAmount} = {GrantTotal}')
#                 print(f'Items: {Items}')
#                 print(f'Quantity: {Quantity}')
#                 print(f'Tax Amount: {TaxAmount}')
#                 print(f'Grant Total: {GrantTotal}')
#             elif Chooselocation ==2:
#                 OutOfValley =0
#                 GrantTotal =AllTotal + OutOfValley
#                 print(f'Total amount: {AllTotal} + Tax Amount: {OutOfValley} = {GrantTotal}')
#                 print(f'Items: {Items}')
#                 print(f'Quantity: {Quantity}')
#                 print(f'Tax Amount: {OutOfValley}')
#                 print(f'Grant Total: {GrantTotal}')
#             else:
#                 print('Please Choose location')     
#         else:
#             print('Please choose option')
#     elif Option ==2:                    #1111
#         Pickup = 0
#         AllTotalAmount = TotalAmount + Pickup
#         print(f'Total amount: {TotalAmount} + Pickup: {Pickup} = {AllTotalAmount}')
#         print('Packing Option')
#         print('1.Plastic: 100')
#         print('2.Box: 200')
#         PackingOption =int(input('Packing Option: '))
#         if PackingOption ==1:                    #22222
#             Plastic =100
#             AllTotal =AllTotalAmount + Plastic
#             print(f'Total amount: {AllTotalAmount} + Plastic Packing: {Plastic} = {AllTotal}')
#             print('Choose location')
#             print('1.Kathmandu 13%')
#             print('2.Out of valley 0%')
#             Chooselocation =int(input('Location Option: '))
#             if Chooselocation ==1:
#                 Kathmandu =13/100
#                 TaxAmount =Kathmandu*AllTotal
#                 GrantTotal =AllTotal + TaxAmount
#                 print(f'Total amount: {AllTotal} + Tax Amount: {TaxAmount} = {GrantTotal}')
#                 print(f'Items: {Items}')
#                 print(f'Quantity: {Quantity}')
#                 print(f'Tax Amount: {TaxAmount}')
#                 print(f'Grant Total: {GrantTotal}')
#             elif Chooselocation ==2:
#                 OutOfValley =0
#                 GrantTotal =AllTotal + OutOfValley
#                 print(f'Total amount: {AllTotal} + Tax Amount: {OutOfValley} = {GrantTotal}')
#                 print(f'Items: {Items}')
#                 print(f'Quantity: {Quantity}')
#                 print(f'Tax Amount: {OutOfValley}')
#                 print(f'Grant Total: {GrantTotal}')
#             else:
#                 print('Please Choose location')  
#         elif PackingOption ==2:                     #22222
#             Box =200
#             AllTotal =AllTotalAmount + Box
#             print(f'Total amount: {AllTotalAmount} + Box Packing: {Box} = {AllTotal}')
#             print('Choose location')
#             print('1.Kathmandu 13%')
#             print('2.Out of valley 0%')
#             Chooselocation =int(input('Location Option: '))
#             if Chooselocation ==1:
#                 Kathmandu =13/100
#                 TaxAmount =Kathmandu*AllTotal
#                 GrantTotal =AllTotal + TaxAmount
#                 print(f'Total amount: {AllTotal} + Tax Amount: {TaxAmount} = {GrantTotal}')
#                 print(f'Items: {Items}')
#                 print(f'Quantity: {Quantity}')
#                 print(f'Tax Amount: {TaxAmount}')
#                 print(f'Grant Total: {GrantTotal}')
#             elif Chooselocation ==2:
#                 OutOfValley =0
#                 GrantTotal =AllTotal + OutOfValley
#                 print(f'Total amount: {AllTotal} + Tax Amount: {OutOfValley} = {GrantTotal}')
#                 print(f'Items: {Items}')
#                 print(f'Quantity: {Quantity}')
#                 print(f'Tax Amount: {OutOfValley}')
#                 print(f'Grant Total: {GrantTotal}')
#             else:
#                 print('Please Choose location')  
#         else:
#             print('Please choose option')
#     else:
#         print('Please choose option')
# elif Items == 'MAP':
#     TotalAmount = Quantity * MAP
#     print("Total Amount:", TotalAmount)
# elif Items == 'Toshiba':
#     TotalAmount = Quantity * Toshiba
#     print("Total Amount:", TotalAmount)
# else:
#     print('Item not found')

# ***********************************************

# x=8
# y=6
# z=10
# if z>x:
#     if z>y:
#         print('z is greater')
#     else:
#         print('y is greater')
# elif y>x:
#     if y>z:
#         print('y is greater')
#     else:
#         print('z is greater')
# else:
#     if x>z:
#         print('x is greater')
#     else:
#         print('z is greater')
        
# **************************************************


# a=int(input('Put vcalue of a: '))
# b=int(input('Put vcalue of b: '))
# if a>b:
#     print('hello')
#     c=int(input('Put vcalue of c: '))
#     if c<b:
#         print('hello ram')
#     else:
#         print('Sorry')
# else:
#     print('End')

# **************************************************

# print('Call Option')
# print('1.ntc to ntc: Per 10 minutes = 2.5 Bonus')
# print('2.ncell to ntc: Per 10 minutes = 3.5 Bonus')
# print('3.ntc to ncell: Per 10 minutes = 4.5 Bonus')
# print('4.ncell to ncell: Per 10 minutes = 5.5 Bonus')
# Option =int(input('Please choose call option: '))
# CallTime=int(input('Call time in minute: '))
# if Option ==1:
#     if 1 <= CallTime <= 10:
#         NtcToNtc=2.5
#         CallCal=NtcToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NtcToNtc} = {CallCal}')
#     elif 11 <= CallTime <= 20:
#         NtcToNtc=5
#         CallCal=NtcToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NtcToNtc} = {CallCal}')
#     elif 21 <= CallTime <= 30:
#         NtcToNtc=7.5
#         CallCal=NtcToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NtcToNtc} = {CallCal}')
#     elif 31 <= CallTime <= 40:
#         NtcToNtc=10
#         CallCal=NtcToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NtcToNtc} = {CallCal}')
#     elif 41 <= CallTime <= 50:
#         NtcToNtc=12.5
#         CallCal=NtcToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NtcToNtc} = {CallCal}')
#     elif 51 <= CallTime <= 60:
#         NtcToNtc=15
#         CallCal=NtcToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NtcToNtc} = {CallCal}')
#     elif 61 <= CallTime <= 70:
#         NtcToNtc=17.5
#         CallCal=NtcToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NtcToNtc} = {CallCal}')
#     elif 71 <= CallTime <= 80:
#         NtcToNtc=20
#         CallCal=NtcToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NtcToNtc} = {CallCal}')
#     elif 81 <= CallTime <= 90:
#         NtcToNtc=22.5
#         CallCal=NtcToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NtcToNtc} = {CallCal}')
#     elif 91 <= CallTime <= 100:
#         NtcToNtc=25
#         CallCal=NtcToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NtcToNtc} = {CallCal}')
#     else:
#         print('Bonus is not available')
# elif Option ==2:               
#     if 1 <= CallTime <= 10:
#         NcellToNtc=3.5
#         CallCal=NcellToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNtc} = {CallCal}')
#     elif 11 <= CallTime <= 20:
#         NcellToNtc=7
#         CallCal=NcellToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNtc} = {CallCal}')
#     elif 21 <= CallTime <= 30:
#         NcellToNtc=10.5
#         CallCal=NcellToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNtc} = {CallCal}')
#     elif 31 <= CallTime <= 40:
#         NcellToNtc=14
#         CallCal=NcellToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNtc} = {CallCal}')
#     elif 41 <= CallTime <= 50:
#         NcellToNtc=17.5
#         CallCal=NcellToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNtc} = {CallCal}')
#     elif 51 <= CallTime <= 60:
#         NcellToNtc=21
#         CallCal=NcellToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNtc} = {CallCal}')
#     elif 61 <= CallTime <= 70:
#         NcellToNtc=24.5
#         CallCal=NcellToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNtc} = {CallCal}')
#     elif 71 <= CallTime <= 80:
#         NcellToNtc=28
#         CallCal=NcellToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNtc} = {CallCal}')
#     elif 81 <= CallTime <= 90:
#         NcellToNtc=31.5
#         CallCal=NcellToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNtc} = {CallCal}')
#     elif 91 <= CallTime <= 100:
#         NcellToNtc=35
#         CallCal=NcellToNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNtc} = {CallCal}')
#     else:
#         print('Bonus is not available')
# elif Option ==3:               
#     if 1 <= CallTime <= 10:
#         Ntctoncell=4.5
#         CallCal=Ntctoncell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {Ntctoncell} = {CallCal}')
#     elif 11 <= CallTime <= 20:
#         Ntctoncell=9
#         CallCal=Ntctoncell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {Ntctoncell} = {CallCal}')
#     elif 21 <= CallTime <= 30:
#         Ntctoncell=13.5
#         CallCal=NcellTNtctoncelloNtc+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {Ntctoncell} = {CallCal}')
#     elif 31 <= CallTime <= 40:
#         Ntctoncell=18
#         CallCal=Ntctoncell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {Ntctoncell} = {CallCal}')
#     elif 41 <= CallTime <= 50:
#         Ntctoncell=22.5
#         CallCal=Ntctoncell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {Ntctoncell} = {CallCal}')
#     elif 51 <= CallTime <= 60:
#         Ntctoncell=27
#         CallCal=Ntctoncell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {Ntctoncell} = {CallCal}')
#     elif 61 <= CallTime <= 70:
#         Ntctoncell=31.5
#         CallCal=Ntctoncell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {Ntctoncell} = {CallCal}')
#     elif 71 <= CallTime <= 80:
#         Ntctoncell=36
#         CallCal=Ntctoncell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {Ntctoncell} = {CallCal}')
#     elif 81 <= CallTime <= 90:
#         Ntctoncell=40.5
#         CallCal=Ntctoncell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {Ntctoncell} = {CallCal}')
#     elif 91 <= CallTime <= 100:
#         Ntctoncell=45
#         CallCal=Ntctoncell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {Ntctoncell} = {CallCal}')
#     else:
#         print('Bonus is not available')
# elif Option ==4:               
#     if 1 <= CallTime <= 10:
#         NcellToNcell=5.5
#         CallCal=NcellToNcell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNcell} = {CallCal}')
#     elif 11 <= CallTime <= 20:
#         NcellToNcell=11
#         CallCal=NcellToNcell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNcell} = {CallCal}')
#     elif 21 <= CallTime <= 30:
#         NcellToNcell=16.5
#         CallCal=NcellToNcell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNcell} = {CallCal}')
#     elif 31 <= CallTime <= 40:
#         NcellToNcell=22
#         CallCal=NcellToNcell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNcell} = {CallCal}')
#     elif 41 <= CallTime <= 50:
#         NcellToNcell=27.5
#         CallCal=NcellToNcell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNcell} = {CallCal}')
#     elif 51 <= CallTime <= 60:
#         NcellToNcell=33
#         CallCal=NcellToNcell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNcell} = {CallCal}')
#     elif 61 <= CallTime <= 70:
#         NcellToNcell=38.5
#         CallCal=NcellToNcell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNcell} = {CallCal}')
#     elif 71 <= CallTime <= 80:
#         NcellToNcell=44
#         CallCal=NcellToNcell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNcell} = {CallCal}')
#     elif 81 <= CallTime <= 90:
#         NcellToNcell=49.5
#         CallCal=NcellToNcell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNcell} = {CallCal}')
#     elif 91 <= CallTime <= 100:
#         NcellToNcell=55
#         CallCal=NcellToNcell+CallTime
#         print(f'Call Time: {CallTime} + Bonus Call: {NcellToNcell} = {CallCal}')
#     else:
#         print('Bonus is not available')
# else:
#     ('Please put option')

# **************************************************

print('==========BUS PARK==========')
print('1) 1km to 5km: Kathmandu to Lalitpur')
print('2) 1km to 10km: Kathmandu to Bhaktapur')
print('5km = 15Rupees')
TravelOption =int(input('Please choose travel option: '))
Person=int(input('Are you (1.student and 2.old passenger)?: '))
if TravelOption ==1:
    Amount =15
    if Person ==1:
        Student=15/100
        print('15 percent discount to student')
        print('Total amount:',(Amount-Student))
    elif Person ==2:
        print('Total amount:',(Amount))
    else:
        print('Please choose option')
elif TravelOption ==2:
    Amount =30
    if Person ==1:
        Student=15/100
        print('15 percent discount to student')
        print('Total amount:',(Amount-Student))
    elif Person ==2:
        print('Total amount:',(Amount))
    else:
        print('Please choose option')
else:
    print('Please choose travel option')

# **************************************************




