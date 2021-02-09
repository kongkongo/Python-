Setting up Virtual Environments

zhang@ubuntu:~$ pip install virtualenv



After installing the virtualenv package go to your project folder and create a virtual env by writing:

For Mac/Linux:
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project/$ virtualenv venv
For Windows:
C:\Users\User\Documents\30DaysOfPython\flask_project>python3 -m venv venv


I prefer to call the new project venv, but feel free to name it differently. Let's check if the the venv was created by using ls (or dir for windows command prompt) command.
zhang@ubuntu:~/桌面/30DaysOfPython$ ls venv/


Let's activate the virtual environment by writing the following command at our project folder.
For Mac/Linux:
zhang@ubuntu:~/桌面/30DaysOfPython$ source venv/bin/activate
For Windows:
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\activate

Now, lets check the available packages in this project by writing pip freeze. You will not see any packages.
We are going to do a small flask project so let's install flask to this project.

(venv) zhang@ubuntu:~/桌面/30DaysOfPython$ pip install Flask


Now, let's write pip freeze to see a list of installed packages in the project:
(venv) zhang@ubuntu:~/桌面/30DaysOfPython$ pip freeze
click==7.1.2
Flask==1.1.2
itsdangerous==1.1.0
Jinja2==2.11.3
MarkupSafe==1.1.1
Werkzeug==1.0.1


When you finish you should dactivate active project using deactivate.
(venv) zhang@ubuntu:~/桌面/30DaysOfPython$ deactivate


