# Electrocare
ElectroCare is a Django-based web application designed to register and manage complaints related to electricity issues such as accidents, pole damage, fires, etc. The system provides real-time updates, SMS alerts, live chat support, and role-based access for different users (customers, section office admins, and line workers).
Features
Complaint Management:

Customers can register complaints with images and location.

Admins can verify and assign complaints to line workers.

Line workers can update complaint status and upload images after resolution.

Real-Time Updates:

Customers can track the status of their complaints in real-time.

SMS Alerts:

Customers and line workers receive SMS notifications for complaint registration, assignment, and resolution.

Live Chat Support:

Customers can chat with support or admins while filing or following up on complaints.

Role-Based Access:

Three user roles: Customer, Section Office Admin, and Line Worker.

Each role has specific permissions and access levels.

Location-Based Auto-Assignment:

Complaints are automatically assigned to the nearest line worker based on location.

Tech Stack
Frontend: HTML, CSS, JavaScript

Backend: Django, Django REST Framework (DRF)

Database: PostgreSQL

APIs: RESTful APIs for data interaction

Real-Time Communication: Django Channels (WebSockets)

SMS Integration: Twilio

Authentication: Django Allauth (Email-based password reset, JWT for API authentication)

Modules
PublicApp (For Customers):

Register & Login

File complaints with images and location

Track complaint status

Live chat with support/admin

Receive SMS alerts

AdminApp (For Section Office Admins):

Verify complaints

Assign complaints to line workers

Track complaints and resolutions

View reports and analytics

Respond to customer messages

LineWorkerApp (For Field Workers):

View assigned complaints in their area

Update complaint status (Pending → In Progress → Resolved)

Upload images after fixing issues

Receive SMS alerts for new complaints

Authentication (Common for All Users):

Email-based password reset

Secure login system

Role-based access control

Installation
Clone the Repository:

bash
Copy
git clone https://github.com/your-username/ElectroCare.git
cd ElectroCare
Set Up a Virtual Environment:

bash
Copy
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy
pip install -r requirements.txt
Set Up the Database:

Update the database settings in settings.py:

python
Copy
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'electrocare',
        'USER': 'your-username',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Run migrations:

bash
Copy
python manage.py migrate
Run the Development Server:

bash
Copy
python manage.py runserver
Access the Application:

Open your browser and go to http://127.0.0.1:8000.

Screenshots
Home Page
Complaint Registration
Admin Dashboard

Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeatureName).

Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
Name: Vishnu Raj C

Email: vishnurajcheerankuzhi@gmail.com

LinkedIn: [Your LinkedIn Profile]

GitHub: [Your GitHub Profile]

How to Use This Template
Replace placeholders (e.g., your-username, your-password, Your LinkedIn Profile) with your actual information.

Add screenshots of your project to the screenshots/ folder and update the links in the Screenshots section.

Customize the Features, Tech Stack, and Modules sections to match your project.

This README template provides a clear and professional overview of your project, making it easy for others to understand and contribute. Let me know if you need further assistance! 🚀


