# Django Student Management Project

This Django project is designed to manage student information, including their address details and enrolled courses. The project supports one-to-one and one-to-many relationships between the student, address, and course entities.

## Project Structure

The project is structured as follows:

- **studentinfo:** Manages student information.
- **address:** Represents the address details of students with a one-to-one relationship.
- **course:** Represents the courses enrolled by students with a many-to-one relationship.

## Setting Up the Project

1. Clone the repository:

    ```bash
    git clone https://github.com/abdullahnaveedan/Fun-Sol
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    cd your-repo
    python -m venv venv
    myenv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the Django Admin interface at http://127.0.0.1:8000/admin/ to manage database records.

## Database Relationships

- **StudentInfo and Address (One-to-One):** Each student has a unique address.

- **StudentInfo and Course (One-to-Many):** A student can be enrolled in multiple courses.

## CSV Import/Export

### Importing Student Information

1. Navigate to the 'Upload Student CSV' page in the Django Admin.
2. Choose a CSV file containing student information.
3. Click 'Upload.'

### Importing Course Information

1. Navigate to the 'Upload Course CSV'.
2. Choose a CSV file containing course information.
3. Click 'Upload.'

### Exporting Student Information

1. Navigate to the 'Student Info'.
2. Select the students you want to export.
3. Click 'Export Selected' to download a CSV file.

### Exporting Course Information

1. Navigate to the 'Course'.
2. Select the courses you want to export.
3. Click 'Export Selected' to download a CSV file.
