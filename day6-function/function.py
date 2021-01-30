# def     greetings   (name):
#     message =   name  + ",  welcome   to    Python   to   everyone"
#     return      message
# print(greetings('Asabeneh'))

# def     add_ten(num):
#     ten=10
#     return      num+ten
# print(add_ten(90))
#正方形的面积
# def     square_number(x):
#     return  x*x
# print(square_number(2))
# #圆的面积
# def     area_of_circle(r):
#     PI =   3.14
#     area    =   PI*r**2
#     return  area
# print(area_of_circle(10))
#累加和
# def     sum_of_number(n):
#     total   =0
#     for i   in  range(n+1):
#             total=total+i
#     print(total)
# sum_of_number(10)

# def add_two_numbers (num1, num2):
#     total = num1 + num2
#     print(total)
# add_two_numbers(num2=3, num1=2) # Order does not matter

#奇数偶数判断
# def     is_even(n):
#     if  n%2==0:
#         return  True
#     return      False
# print(is_even(10))
# print(is_even(7))

# def weight_of_object (mass, gravity = 9.81):
#     weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
#     return weight
# print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
# print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon 

def     sum_all_nums(*nums):
    total   =0
    for     num     in      nums:
        total   +=  num
    return      total
print(sum_all_nums(2,3,5))
