# - P13 Collection Pop .

# - Description:
- Inventory application of a collection of POP figurines.

# - 1: Project online:
- Go to the following address: "https://www.collectionpop.fr/"

# - 2: Initialization of the project locally:
- 1: To initialize the virtual environment: `pipenv install`.
- 2: To position yourself in pipenv : `pipenv shell`.

# - 3: Launch the project locally:
- : If you have already initialized the virtual environment.
- 1: Execute the command to create the database:
        - `python manage.py makemigrations`
        - `python manage.py migrate`
- 3: Creating a super user: `python manage.py createsuperuser`
- 4: To run the app: `python manage.py runserver`.
- 5: Once launched, go to your browser and enter the following url: "http://127.0.0.1:8000/".

# - 4: Test:
- : To launch the unit tests execute in the terminal the command `coverage run --source='.' manage.py test`.
- : To view the test report: `coverage report`.
