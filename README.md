# Role-Based Access Control (RBAC) System

This project implements a **Role-Based Access Control (RBAC)** system using Django. The application features secure authentication and authorization, enabling users to access dashboards based on their assigned roles: Admin, Moderator, or User.
## Live Demo

You can check out the live version of this project here:  
[**Live Blog Project**](https://a-code.harpreetsinghbansal.com/)

---

## **Features**

- **User Registration**: Users can register with roles (Admin, Moderator, or User).
- **Secure Login**: Supports login via username or email with password authentication.
- **Role-Based Dashboards**:
  - **Admin**: Manage users, view reports, access all data.
  - **Moderator**: Moderate content, manage user reports, view analytics.
  - **User**: View profile, update personal information, and access personalized content.
- **Session Management**: Includes secure logout functionality.
- **Error Handling**: Comprehensive error messages for invalid credentials or unauthorized access.

## Project Screenshots

Here are some images of the project:

### Register Page
![Register Page]()

### Login Page
![ Login Page]()

### Admin Dashboard
![Admin Panel]()

### Moderator Dashboard
![Moderator Panel]()

### User Dashboard
![User Panel]()

These images showcase the key features of the Role-Based Access Control (RBAC) system, including user registration, login authentication, and role-specific dashboards.

---

## Installation

### Prerequisites

- Python 3.11
- pip
- Django

### Step-by-Step Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Techie-Harpreet/Django-Role-Based-Access-Control-RBAC-System.git
    cd Django-Role-Based-Access-Control-RBAC-System-main
    ```

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv env
    source env/bin/activate  # For Linux/Mac
    env\Scripts\activate     # For Windows
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up the Database**:
    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```
    Access the project at `http://127.0.0.1:8000/register`.

## Contact Information

For any queries, suggestions, or issues, feel free to reach out to us:

- **Email**: contact@harpreetsinghbansal.com
- **GitHub Repository**: [Your GitHub Repo Link](https://github.com/Techie-Harpreet/Blog-Page)
