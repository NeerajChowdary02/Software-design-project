The requirements for the virtual environment are given in the file "requirements.txt". Use the following command to
recreate the virtual env: `pip install -r requirements.txt`.
For more info: https://stackoverflow.com/questions/65558323/transferring-a-python-project-to-different-computers
More Info: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

There is a file called 'script.sql' in this directory which can be used to recreate the database in postgresql.

For Mac users, in order to setup the virtual environment install -r requirements.txt, but ignore any kivy related errors
as it is based on windows and the virtual environment should work without Kivy.

In order to set the Virtual environment up on mac follow these steps:

1. Install the project from Github
2. Place the project in a easy to find location such as desktop
3. Make sure that postgres, flask and postgres admin are installed
4. Initialize and start postgres by setting up a user in postgres admin
5. Open terminal and cd into the project
6. create a virtual environment and use the command flask run to fully setup the venv
