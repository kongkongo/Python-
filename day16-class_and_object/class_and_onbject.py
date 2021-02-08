# #create  a  class创建一个类
# class   Person:
#     def     __init__(self,name):
#         self.name=name
# p=Person('Adbsjjd')
# print(p.name)
# print(p)

# # Let's add more parameters to the constructor function.
# class   Person:
#     def     __init__(self,firstname,lastname,age,country,city):
#         self.firstname=firstname
#         self.lastname=lastname
#         self.age=age
#         self.country=country
#         self.city=city
    
#     def    person_info(self):
#         return     f"{self.firstname}{self.lastname}is  {self.age}years  old.He  lives  in {self.city},{self.country}."

# p=Person('Asabench','Yetayeh',250,'Finland','Helsinki')
# #output
# print(p.firstname)
# print(p.lastname)
# print(p.age)
# print(p.country)
# print(p.city)

# #output
# p1=Person()
# print(p1.person_info())
# p2=Person("John",'Doe',30,'Nomanland','Norman  city')
# print(p2.person_info())


class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def  person_info(self):
          return  f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def     add_skill(self,skill):
        self.skills.append(skill)

p1=Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2=Person('John','Doe',30,'Nomanland','Noman  city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

#继承inheritance
class   Student(Person):
    pass

s1=Student('Eyob','Yetayeh',30,'Finland','Helsinki')
s2=Student('Lidiya','Teklemariam',28,'Finland','Espoo')
print(s1.person_info())
s1.add_skill('JavaSrcipt')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)


print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital   Marteting')
print(s2.skills)




