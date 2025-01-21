# django-demo/django-demo/README.md

# Django Demo Project

This is a demo project built using the Django framework. It includes features for user login, registration, and profile editing.

## Features

- User registration
- User login
- User profile editing

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd django-demo
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Navigate to `http://127.0.0.1:8000/` to access the application.
- Use the registration page to create a new user account.
- Log in with your credentials to access the user profile editing features.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.