# **PService**

PService is a Flask-based API service for managing customers and orders. It provides functionalities to add, view, and manage customers and their orders while utilizing SQL Server as the database backend.

## **🚀 Live Demo**
[View the deployed service](https://pservice-vvj1rep78-emmanuel-sandes-projects.vercel.app)

## **🛠 Tech Stack**
- **Backend:** Flask (Python)
- **Database:** SQL Server
- **Deployment:** Vercel
- **Authentication:** Token-based authentication (OpenID Connect)
- **CI/CD:** GitHub Actions

## **📂 Project Structure**
pservice/
│── api/
│   ├── index.py       # Entry point for the application
│   ├── create_app.py  # Flask app factory
│   ├── routes/        # API route definitions
│   ├── models/        # Database models
│   ├── services/      # Business logic
│── .vercel/           # Vercel project configuration
│── vercel.json        # Vercel deployment configuration
│── requirements.txt   # Dependencies
│── README.md          # Project documentation


## **⚙️ Installation & Setup**
### **Prerequisites**
Ensure you have:
- Python installed (`>= 3.9`)
- `pip` package manager
- SQL Server installed and running

### **Clone the Repository**
```bash
git clone https://github.com/your-repo/pservice.git
cd pservice

# **Install dependencies**
pip install -r requirements.txt


### **Run locally**
python api/index.py


### **Deployment on vercel**
vercel --prod --force

### **Automatic deployment (CI/CD)**
Push changes to GitHub, and Vercel will automatically deploy the latest commit.

### **API endpoints**
Method     	    Endpoint                  Description
POST             /customers               Add a new customer
POST             /orders                  Add a new order