# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# f   =   open('./files/reading_file_example.txt')
# print(f)    # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>

# f = open('./files/reading_file_example.txt')
# txt=f.read(10)
# print(type(txt))
# print(txt)
# f.close()

# # readline(): read only the first line
# f = open('./files/reading_file_example.txt')
# line=f.readline()
# print(type(line))
# print(line)
# f.close()

# # readlines(): read all the text line by line and returns a list of lines

# f = open('./files/reading_file_example.txt')
# lines=f.readlines()
# print(type(lines))
# print(lines)
# f.close()

# Another way to get all the lines as a list is using splitlines():
# f = open('./files/reading_file_example.txt')
# lines=f.read().splitlines()
# print(type(lines))
# print(lines)
# f.close()

#with方法实现文件的打开，自动关闭
from typing import Type


with    open('./files/reading_file_example.txt')  as    f:
        lines=f.read().splitlines()
        print(type(lines))
        print(lines)
        f.close()

# Let's append some text to the file we have been reading:
with    open('./files/reading_file_example.txt','a')  as    f:
        f.write("This text has to be appended at the end")
# The method below creates a new file, if the file does not exist:
with    open('./files/reading_file_example.txt','w')  as    f:
        f.write("This text has to be appended at the end")

# Deleting Files
# import  os
# os.remove('./files/example.txt')

# If the file does not exist, the remove method will raise an error, so it is good to use a condition like this:
# import      os
# if      os.path.exists('./files/example.txt'):
#     os.remove('./files/example.txt')
# else:
#     os.remove('This  file   does    not     exist')

# File    Type
# File with json Extension
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
# person_json="{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"
# we use three quotes and make it multiple line to make it more readable

# person_json = '''{
#     "name":"Asabeneh",
#     "country":"Finland",
#     "city":"Helsinki",
#     "skills":["JavaScrip", "React","Python"]
# }'''
# print(person_json)

# Changing JSON to Dictionary
# To change a JSON to a dictionary, first we import the json module and then we use loads method.

import  json
#json
# person_json = '''{
#     "name":"Asabeneh",
#     "country":"Finland",
#     "city":"Helsinki",
#     "skills":["JavaScrip", "React","Python"]
# }'''
# # let's change JSON to dictionary
# person_dct=json.loads(person_json)
# print(person_dct)
# print(person_dct['name'])

# Changing Dictionary to JSON
import  json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
# person_json=json.dumps(person,indent=4)
# print(type(person_json))
# print(person_json)
# when you print it, it does not have the quote, but actually it is a string
# JSON does not have type, it is a string type.

# Saving as JSON File
import  json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

with    open('./files/json_example.json','w',encoding='utf-8')  as  f:
    json.dump(person, f, ensure_ascii=False, indent=4)

# File with csv Extension
import  csv
with    open('./files/csv_example.csv')     as  f:
    csv_reader=csv.reader(f,delimiter=',')# w use, reader method to read csv
    line_count=0
    for row     in  csv_reader:
        if  row    in   csv_reader==0:
            print(f'Column  names   are :{",".join(row)}')
            line_count+=1
        else:
            print(f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count+=1
    print(f'Number  of  lines:  {line_count}')

