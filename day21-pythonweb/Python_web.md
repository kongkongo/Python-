 首先创建好所需的文件夹
 ├── Procfile
├── app.py
├── env
│   ├── bin
├── requirements.txt
├── static
│   └── css
│       └── main.css
└── templates
    ├── about.html
    ├── home.html
    ├── layout.html
    ├── post.html
    └── result.html
    
    Setting up your project directory
    
    pip install virtualenv
    
    
 asabeneh@Asabeneh:~/Desktop$ mkdir python_for_web
asabeneh@Asabeneh:~/Desktop$ cd python_for_web/
asabeneh@Asabeneh:~/Desktop/python_for_web$ virtualenv env
asabeneh@Asabeneh:~/Desktop/python_for_web$ source env/bin/activate
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip install Flask
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1


#let's      import  the     flask
from    flask   import      Flask, render_template
import  os # importing operating system module

app=Flask(__name__)

@app.route('/')#this  decorator     create  the     home    route
def     home():
    # return  '<h1>Welcome</h1>'
    techs=['HTML','CSS','Flask','Python']
    name='30Days    of  Python      Programming'
    return  render_template('home.html',techs=techs,name=name,title='Home')

@app.route('/about')
def     about():
    # return    '<h1>About    us</h1>'
    name='30  days  of  python  programming'
    return   render_template('about.html',name=name,title='About  Us')

if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
