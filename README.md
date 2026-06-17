Online Examination Management System (FastAPI)

Project Overview

Online Examination Management System built using FastAPI, SQLAlchemy ORM, SQLite, and JWT Authentication.

This system manages students, exams, questions, exam attempts, results, and leaderboard rankings.

Features

Authentication

* User Registration
* User Login
* JWT Authentication
* Role Based Access

  * Admin
  * Student

Student Management

* Create Student
* View Student Exams
* Unique email validation

Exam Management

* Create Exams
* Exam category support
* Active/Inactive exam control
* Exam duration validation

 Question Management

* Add questions to exams
* Multiple choice options
* Correct answer storage
* Minimum question validation

Exam Attempt System

* Start exam
* Submit exam
* Auto score calculation
* Prevent duplicate attempts

Results & Ranking

* Generate results automatically
* Store score permanently
* Leaderboard ranking

Filtering & Pagination

* Filter exams by category
* Filter results by student
* Filter attempts by status
* Pagination support

Background Tasks

* Exam completion email notification
* Result notification

 Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* JWT
* Pydantic
* Uvicorn

Project Structure


online_exam_system/

app/
│
├── main.py
├── database.py
│
├── models/
│   ├── user.py
│   ├── student.py
│   ├── exam.py
│   ├── question.py
│   ├── attempt.py
│   ├── answer.py
│   └── result.py
│
├── schemas/
│
├── routes/
│   ├── auth.py
│   ├── students.py
│   ├── exams.py
│   ├── questions.py
│   ├── attempts.py
│   └── results.py
│
├── services/
│
└── utils/
```

Installation

Clone repository:


git clone <repository-url>


Create virtual environment:


python -m venv venv


Activate:

Windows:


venv\Scripts\activate


Install dependencies:


pip install -r requirements.txt


 Run Application


uvicorn app.main:app --reload


Application runs at:


http://127.0.0.1:8000


Swagger Documentation:


http://127.0.0.1:8000/docs


API Flow

1. Register User


POST /api/v1/auth/register


2. Login


POST /api/v1/auth/login


3. Authorize JWT Token

4. Create Student


POST /api/v1/students


5. Create Exam


POST /api/v1/exams


6. Add Questions


POST /api/v1/questions


7. Start Exam


POST /api/v1/attempts/start


8. Submit Exam


POST /api/v1/attempts/submit


9. View Results


GET /api/v1/results


10. View Leaderboard

GET /api/v1/results/leaderboard


Database

Database:

SQLite

Tables:

* users
* students
* exams
* questions
* attempts
* answers
* results

Security

* Password hashing
* JWT authentication
* Role based authorization
* Protected APIs

Future Improvements

* PostgreSQL support
* Alembic migrations
* Docker deployment
* Advanced analytics
* Real email integration
