# COVID-19-Web-Tool
This is the project for developing a web tool applying the methods and results in respository 'COVID-19 project'.

# Required package
To run this project, you need to import 'django' package in your python. 

# Steps for running this server and test
For running this server, I suggest using PyCharm.

1. Install django package in your python environment.
2. Download all files in this respository and unzip it.
3. You should get a folder named "COVID-19-web-tool-main", change the terminal path of your python environment to this folder.
4. If the size of file db.sqlite3 is 1kB, it should contains two empty lines, you need to delete one empty line, then close that file. If the size becomes 0kB, then it will be fine.
5. Run the following command in the terminal > python manage.py runserver and click the link it gives. The message should be like "Starting development server at http://127.0.0.1:8000/"
6. That link will show a 404 page, then you change the url as "http://127.0.0.1:8000/myapp/welcome.html" and press enter, it will shows the website page.
