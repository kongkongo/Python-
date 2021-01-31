Installing PIP
#If you did not install pip, let us do it now. 

zhang@ubuntu:~$ pip install pip
zhang@ubuntu:~$ python -m pip --version
pip 21.0.1 from /home/zhang/.local/lib/python3.6/site-packages/pip (python 3.6)



<!!Installing packages using pip>
##Installing packages using pip
zhang@ubuntu:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> numpy.version.version
'1.17.3'
>>> lst = [1, 2, 3,4, 5]
>>> np_arr = numpy.array(lst)
>>> np_arr
array([1, 2, 3, 4, 5])
>>> len(np_arr)
5
>>> np_arr * 2
array([ 2,  4,  6,  8, 10])
>>> np_arr  + 2
array([3, 4, 5, 6, 7])
>>>


#Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. 
Let's install the big brother of numpy, pandas:

asabeneh@Asabeneh:~$ pip install pandas
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas





###Let's import a web browser module, which can help us to open any website. 
We do not install this module, it is already installed by default with python 3. For instance 
if you like to open any number of websites at any time or if you like to schedule something, this webbrowser module can be of use.

import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://twitter.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)

#Uninstalling Packages



##If you do not like to keep the installed packages, you can remove them.

pip uninstall packagename
List of Packages
To see the installed packages on our machine. We can use pip followed by list.

pip list


<----!!!!Show Package---->
To show information about a package
asabeneh@Asabeneh:~$ pip show pandas
Name: pandas
Version: 0.25.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: python-dateutil, pytz, numpy
Required-by:

<-----Reading from URL------->

asabeneh@Asabeneh:~$ pip install requests

import requests # importing the request module
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website
response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page

<Response [200]>
200
{'date': 'Sun, 08 Dec 2019 18:00:31 GMT', 'last-modified': 'Fri, 07 Nov 2003 05:51:11 GMT', 'etag': '"17e9-3cb82080711c0;50c0b26855880-gzip"', 'accept-ranges': 'bytes', 'cache-control': 'max-age=31536000', 'expires': 'Mon, 07 Dec 2020 18:00:31 GMT', 'vary': 'Accept-Encoding', 'content-encoding': 'gzip', 'access-control-allow-origin': '*', 'content-length': '1616', 'content-type': 'text/plain', 'strict-transport-security': 'max-age=15552000; includeSubdomains; preload', 'content-security-policy': 'upgrade-insecure-requests'}



<----Creating a Package------>
We organize a large number of files in different folders and subfolders based on some criteria, so that we can find and manage them easily. As you know, a module can contain multiple objects, such as classes, functions, etc. A package can contain one or more relevant modules. A package is actually a folder containing one or more module files. Let's create a package named mypackage, using the following steps:
Create a new folder named mypacakge inside 30DaysOfPython folder Create an empty init.py file in the mypackage folder. Create modules arithmetic.py and greet.py with following code:


# mypackage/arithmetics.py
# arithmetics.py
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

def subtract(a, b):
    return (a - b)
    
def multiple(a, b):
    return a * b

def division(a, b):
    return a / b

def remainder(a, b):
    return a % b

def power(a, b):
    return a ** b
# mypackage/greet.py
# greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'
The folder structure of your package should look like this:
─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
Now let's open the python interactive shell and try the package we have created:

asabeneh@Asabeneh:~/Desktop/30Days












