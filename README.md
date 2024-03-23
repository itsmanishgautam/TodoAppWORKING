This is a TODO APP built using Django Framework
its simple for basic understanding

To run the app bash following commands.

Create a Virtual Environment:

python -m venv myenv
This command creates a new Python virtual environment named myenv in the current directory.

myenv\Scripts\activate
This command activates the virtual environment. 
Once activated, the terminal prompt typically changes to indicate that the virtual environment is active.

python manage.py makemigrations
This command instructs Django to create migrations for any changes you've made to your models. 
Django uses migrations to manage changes to the database schema.

python manage.py migrate
This command applies the migrations to your database. 
It synchronizes the database schema with the current state of your models.

Run the Development Server:

python manage.py runserver
This command starts the Django development server, allowing you to test your application locally. 
By default, the server runs on http://127.0.0.1:8000/.

Make sure to execute these commands in the root directory of your Django project where the manage.py file is located.
Additionally, ensure that your virtual environment is activated before running Django commands.
