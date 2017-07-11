 

In the toplevel directory of the project there is a requirements.txt file with all the python dependencies, required for this project to run. Install them with

`pip install -r requirements.txt`

You'll also need a working instance of MongoDB - install it as an apt package in your system with:

`sudo aptitude install mongodb`

After that you'll need to create a database in MongoDB, called `project`, where this project's collections will be stored.

To run this project with django development server, just go to `project` folder and say:

`python manage.py runserver`

 
