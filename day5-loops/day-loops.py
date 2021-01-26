#loops循环

# count=0
# while   count<5:
#         print(count)
#         count=count+1
#         if  count==3:
#                 break
# else    :
#         print(count)

#for循环
# numbers=[0,1,2,4,5,6,7]
# for     number      in      numbers :
#     print(number)
    
#example:For loop with string
# language    =   "Python"
# for     letter  in  language:
#     print(letter)
# example:  For loop with tuple
# tuple_l    =    (0,1,2,3,4,5)
# for     tuple_m     in      tuple_l:
#     print(tuple_m)

#For loop with dictionary
# person={
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':["JavaScript",'React','Node','MongoDB','Python'],
#     'address':{
#         'street'    :   'Space   street',
#         'zipcode':'02210'
#     }
# }
# for     key     in      person:
#     print(key)

# for     key, value      in   person.items():
#     print(key,':',value)

#For loop  with set
# it_companies    =   {'Facebook','Goole','Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# for     company     in      it_companies:
#     print(company)


#Nested  For    Loop(嵌套循环)
# person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }

# for     key    in   person:
#     if  key     ==      'skills':
#         for     skill   in     person['skills']:
#             print(skill)

#For    Else
for     number  in   range(11):
        print(number)
else:
        print('The  loop  stops at',    number)

#pass
for     number      in      range(6):
    pass
