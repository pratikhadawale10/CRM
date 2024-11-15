
# CRM Platform - Open Source

Welcome to the **CRM Platform**, an open-source project built using **Django** and **HTML templates**. This platform is designed to manage all aspects of an organization, its users, and its operations efficiently. Developed with over 4 years of experience in CRM and software development, this project aims to provide a powerful, yet flexible solution for organizations and individual users alike.

## Features

### 1. Authentication Module
- Secure user authentication ✅
- Role-based access control for different user levels

### 2. Organization Management
- Create and manage organization
- User management within organization
- Real-time chat with audio and video call capabilities

### 3. Project Management
- Create and manage projects
- Assign users, plan tasks, and track issues
- Hierarchical user roles within projects for better collaboration

### 4. Custom Emailer
- Send quick emails or schedule automated emails
- Build and manage newsletters for organization communication

### 5. Payment Module
- Subscription management with flexible plans
- Basic lifetime free plan for organizations and their users

### 6. Human Resource Management
- Attendance, salary management, and payslip generation
- Handle leaves, holidays, and reimbursements
- Comprehensive tax management and tracking

### 7. Personal Space
- Personal storage for users to manage personal data and tasks
- To-do list and personal task tracker
- Advanced Calender
- Personal notes and reminders
- Cash flow management


## Technologies Used
- **Django**: High-level Python web framework ✅
- **HTML Templates**: For rendering the front-end ✅
- **PostgreSQL**: Database for storing application data ✅
- **Redis**: For handling asynchronous tasks and caching
- **Celery**: Distributed task queue for background job processing
- **WebSockets**: For real-time chat and call functionalities

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pratikhadawale10/CRM.git
   cd CRM
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Contribution Guidelines
Feel free to fork this repository and contribute to the project. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements
Special thanks to the open-source community for continuous support and inspiration.
