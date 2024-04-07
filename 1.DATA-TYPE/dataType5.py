about ={
    'name':'ram',
    'age':45
}

print(about['name'])          # ram
print(about['age'])          # 45

print(about.keys())          # dict_keys(['name', 'age'])
print(about.values())          # dict_values(['ram', 45])
# value and key don't support this # print(about.get('address','teku')) 

print(about.get('address','teku'))          # teku     # if we want to add some then we can do this
print(about.get('name','teku'))          # ram

# next page..........

user ={
    'name':'sita',
    'address':{
        'city':'kathmandu',
        'city1':'pokhara'
    }
}
print(user['address']['city1'])          #pokhara

# next page..........

students=[
    {
        'name':"ram",
        "country":[
            {
                'cname':"nepal",
                'capital':"ktm"
            },
            {
                'cname':"india",
                'capital':"delhi"
            }
        ]
        
    },
    {
        'name':"sita",
        "country":[
            {
                'cname':"nepal",
                'capital':"ktm"
            },
            {
                'cname':"china",
                'capital':"beijing"
            }
        ]
    }
]

print(students[0]['name'])
print(students[0]['country'][0]['cname'])

# answer
# ram
# nepal