# MenuCreator
Menu Creator is a Django-based application for creating daily menus, managing user-specific soups, main courses, 
salads, and side dishes.

# Please be aware!

I'd like to point out that there's a certain imperfection in my live version on Vercel. 
Specifically, during the registration of a new user 
(since this process involves cloning the database from the central database), the registration takes longer. 
Unfortunately, Vercel has a response timeout set to 10 seconds, so a 504: GATEWAY_TIMEOUT error appears. 
However, the user is successfully registered and can log in with the provided credentials. 

I have also set up an account for testing purposes, which can be accessed with the following credentials:

Username: Tester

Password: Tester123

This issue is primarily caused by the fact that I am using the free, hobby plan on Vercel. 
I can modify the code (I plan to optimize it), but the larger the database grows, the sooner this problem will reappear.




![main_menu](Screenshot.png)


## Table of Contents

- Python 3.9 or higher
- Django 3.9 or higher
- `requirements.txt`


1. Clone the repository:

    ```sh
    git clone https://https://github.com/Spinlerk/MenuGenerator
    cd menugenerator
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```
4. Set up the database:

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser account:

    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```


## Usage

Once the server is running, you can access the application at `http://127.0.0.1:8000/`

## Contributing

If you want to contribute to this project, please contact me at [rostislav.kominek@gmail.com].

## Testing

To run the tests, use the following command:
```sh
python manage.py test
or 
 python manage.py test --keepdb 
  ```

## Project structure
```sh
menu-generator/
├── Generator/
│ ├── migrations/
│ ├── templates/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── menu_generator/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── static/
├── manage.py
└── requirements.txt
  ```
## License

This project is licensed under a custom license that restricts modification and redistribution without prior written permission. See the `LICENSE` file for details.

## Database structure
```sh

Description:

User:
Represents a user of the application.
Each user can have their own profile and can create/manage their personalized data.
This model typically comes from Djangos built-in authentication system (django.contrib.auth.models.User).

UserMainCourse:
Represents main courses that users can create.
Each main course is associated with a user (ForeignKey to User) who created it.
Contains attributes such as name and description.

UserSoup:
Represents soups that users can create.
each soup is associated with a user (ForeignKey to User).
Contains attributes such as name and last_used.

UserSalad:
Represents salads that users can create.
Each salad is associated with a user (ForeignKey to User).
Contains attributes such as name and description.

UserSideDishes:
Represents side dishes that users can create.
Each side dish is associated with a user (ForeignKey to User).
Contains attributes such as name and description.

DailyMenu:
Represents a daily menu that combines various food items (soup, main courses, side dishes, salad).
Contains foreign keys to UserSoup, UserMainCourse, UserSideDishes, UserSalad.
Each daily menu is associated with a user (ForeignKey to User) who created or modified it.
Typically, it would have a date field to indicate which day the menu is for.
These models are interconnected through foreign key relationships, allowing users to create, manage, and associate various food items into daily menus. Users can customize their menus by adding their own soups, main courses, side dishes, and salads, and then combine them into daily menus for their meals.
  ```


![MenuGenerator_Schema ](databaseSchema%20.png)

