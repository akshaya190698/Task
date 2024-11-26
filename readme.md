Billing System Project
This README provides instructions to set up, run, and test the Django-based billing system project. Follow the steps carefully to ensure the project runs smoothly on your machine.
Prerequisites
Before running this project, ensure that you have the following installed:
•	Python (>= 3.13.0)
•	pip (Python package manager)
•	Virtualenv (optional but recommended)
Project Setup
Step 1: Clone the Repository
Clone the project repository to your local machine:
git clone <repository-url>
cd <project-directory>
Step 2: Create and Activate a Virtual Environment
Create a virtual environment to isolate the project's dependencies:
python -m venv env
On Windows: env\Scripts\activate
Step 3: Install Dependencies
Install the required Python packages:
pip install -r requirements.txt
Step 4: Set Up Environment Variables
Create a .env file in the project's root directory and configure the following variables:
SECRET_KEY=<your-django-secret-key>
EMAIL_HOST=<your-email-host>
EMAIL_PORT=<your-email-port>
EMAIL_HOST_USER=<your-email-username>
EMAIL_HOST_PASSWORD=<your-email-password>
EMAIL_USE_TLS=True  # Set to False if not using TLS
Step 5: Configure the Database
By default, the project uses SQLite. If you want to use another database (e.g., PostgreSQL), update the DATABASES configuration in settings.py and install the necessary database drivers.
Step 6: Apply Migrations
Run the following commands to create the database and apply migrations:
python manage.py makemigrations
python manage.py migrate
Step 7: Run the Development Server
Start the Django development server:
python manage.py runserver
Access the application at http://127.0.0.1:8000/.
________________________________________
Project Features
1.	Billing Page: Allows users to input customer email, add products, and calculate bills.
2.	Dynamic Form Handling: Add new product fields dynamically.
3.	Denomination Handling: Calculates balance denominations based on available values.
4.	Invoice Generation: Generates and sends invoices asynchronously via email.
5.	Previous Purchases: View and retrieve past purchases for any customer.
________________________________________
Testing the Project
Functional Testing
1.	Access the billing page and enter the required customer details.
2.	Add products using the "Add New" button.
3.	Input denominations and the cash paid by the customer.
4.	Click "Generate Bill" to calculate the total and send an invoice.
5.	Navigate to the "Previous Purchases" section to view past transactions.
Unit Testing
Run the Django test suite to verify the functionality:
python manage.py test
________________________________________
Troubleshooting
1.	Email Sending Issues:
o	Verify the email credentials in the .env file.
o	Ensure your email provider allows SMTP connections.
3.	Dependency Issues:
o	Run pip install --upgrade -r requirements.txt to update dependencies.
4.	Database Issues:
o	Delete the db.sqlite3 file and rerun migrations if you encounter database errors.
________________________________________


