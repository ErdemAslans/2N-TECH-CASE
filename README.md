# Company Management System

This project is a Django-based application designed to manage employee attendance, leaves, and monthly work reports for a company. It provides separate dashboards and functionalities for employees and authorized personnel.

---

## Features

### Employee Features
- Login and logout functionality.
- Submit leave requests.
- View remaining annual leave days.

### Authorized Personnel Features
- Approve or reject employee leave requests.
- Receive notifications about tardiness or insufficient leave days.
- View monthly work reports for all employees.

---

## Installation

### Step 1: Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/your-repo/company-management.git
cd company-management
```

### Step 2: Set Up the Environment
Create a Python virtual environment and install the required dependencies:

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
.env\Scriptsctivate   # Windows
pip install -r requirements.txt
```

### Step 3: Configure the Database
Update the `DATABASES` section in the `settings.py` file with your PostgreSQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Step 4: Apply Migrations
Run the following commands to apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser
Create an admin user to access the Django admin panel:

```bash
python manage.py createsuperuser
```

### Step 6: Start the Server
Run the development server to test the application locally:

```bash
python manage.py runserver
```

---

## Project Structure

```plaintext
project/
│
├── hesaplar/                # Custom user management app
│   ├── models.py            # CustomUser model
│   ├── views.py             # Login, logout views
│   ├── urls.py              # URLs for user-related actions
│   ├── admin.py             # Admin configurations for CustomUser
│
├── personel/                # Employee-specific app
│   ├── views.py             # Employee dashboard and leave request logic
│   ├── urls.py              # URLs for employee actions
│   ├── templates/
│       ├── dashboard.html   # Employee dashboard template
│       ├── izin_talep.html  # Leave request template
│
├── yetkili/                 # Authorized personnel app
│   ├── views.py             # Leave approval, monthly reports
│   ├── urls.py              # URLs for personnel actions
│   ├── templates/
│       ├── dashboard.html   # Authorized personnel dashboard template
│       ├── izin_talepleri.html # Leave requests template
│       ├── aylik_rapor.html # Monthly report template
│
├── yoklama/                 # Attendance tracking app
│   ├── models.py            # Attendance model
│
├── izinler/                 # Leave management app
│   ├── models.py            # Leave model
│
├── manage.py                # Django command-line utility
├── requirements.txt         # Dependencies
├── templates/               # Shared templates
│
└── settings.py              # Django project settings
```

---

## Notifications

### Triggers
- **Low Annual Leave Notification**: Employees with less than 3 days of annual leave trigger a notification to authorized personnel.
- **Tardiness Notification**: If an employee is late for work, a notification is sent to the authorized personnel.

---

## Email Configuration
Configure email settings in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_password'
```

---

## Usage

### Employee Workflow
1. Employees can log in via `/hesaplar/login/`.
2. They can view their remaining annual leave days on the dashboard.
3. Employees can submit leave requests, which are sent to authorized personnel for approval.

### Authorized Personnel Workflow
1. Authorized personnel log in via the same login page.
2. They can view pending leave requests and approve or reject them.
3. Notifications are sent for employee tardiness or insufficient leave days.
4. They can view monthly reports summarizing employee attendance and tardiness.

---

## Future Enhancements
- **Asynchronous Notifications**: Implement Celery for background task processing.
- **Real-Time Notifications**: Use WebSockets for real-time updates on dashboards.
- **Enhanced UI/UX**: Use frontend frameworks like React or Vue.js to improve user experience.
- **Containerization**: Add Docker support for containerized deployment.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.
