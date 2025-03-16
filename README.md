# NSS Certificate Management System

## **Overview**
The **NSS Certificate Management System** is a web-based Django application that allows **college NSS students** to securely download their certificates once **approved by the admin**. Admins can upload and manage certificates, ensuring only approved ones are accessible to students.

## **Features**
✅ **User Authentication** – Register, Login, Logout functionality for students.  
✅ **Admin Panel** – Admins can upload student certificates.  
✅ **Approval System** – Certificates are only downloadable after admin approval.  
✅ **Secure Access** – Students can only access their own approved certificates.  
✅ **File Management** – Supports certificate uploads in **PDF, JPG, PNG** formats.

## **Tech Stack**
- **Backend:** Django (Python)
- **Database:** SQLite (default)
- **Frontend:** HTML, CSS (Bootstrap)
- **Authentication:** Django’s built-in User model

## **Installation & Setup**
### **1. Clone the Repository**
```bash
git clone https://github.com/0xsreejith/NSS-Certificate-Portal.git
cd nss-certificate-system
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Create a Superuser (Admin)**
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### **6. Run the Server**
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

## **Usage**
### **For Students:**
1. Register an account.
2. Login and check for approved certificates.
3. Download available certificates.

### **For Admins:**
1. Login to the **Django Admin Panel** (`/admin`).
2. Upload certificates for students.
3. Approve certificates to allow downloads.

## **Project Structure**
```
/nss_portal/
│── manage.py
│── nss_portal/
│── certificates/
│   │── models.py        # Database models
│   │── views.py         # Application logic
│   │── urls.py          # URL routes
│   │── templates/       # HTML templates
│── templates/
│   │── certificates/
│   │   │── base.html
│   │   │── home.html
│   │   │── login.html
│   │   │── register.html
│   │   │── student_certificates.html
│   │   │── upload_certificate.html
```

## **Contributing**
Feel free to fork this project and submit pull requests. Suggestions and improvements are welcome!

## **License**
This project is **open-source** and available under the MIT License.

---

🚀 **Developed with Django** | **Author: Sreejith**

