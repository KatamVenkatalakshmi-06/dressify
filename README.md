# Dressify - Outfit Customization Web App

## Overview
Dressify is an outfit customization platform where users can:
- Create an account with signup
- Save user details to a database
- Login securely
- Customize and save outfit designs

## Setup Instructions

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```

The application will start on `http://localhost:5000`

### 3. Access the Application
- Open your browser and go to `http://localhost:5000`
- You'll see the login page with a "Sign up here" link
- Click on "Sign up here" to create a new account

## Database

### SQLite Database Structure
The app uses SQLite with two main tables:

**Users Table:**
- id (Primary Key)
- email (Unique)
- username (Unique)
- password (Hashed)
- full_name
- phone
- address
- created_at (Timestamp)

**Saved Designs Table:**
- id (Primary Key)
- user_id (Foreign Key to Users)
- product_name
- product_price
- category
- clothing_type
- color
- color_name
- pattern
- design_style
- product_image
- saved_at (Timestamp)

The database (`dressify.db`) is automatically created when you first run the app.

## API Endpoints

### Authentication
- **POST /api/auth/signup** - Register new user
- **POST /api/auth/login** - Login user
- **POST /api/auth/logout** - Logout user
- **GET /api/auth/check** - Check if user is authenticated

### Designs
- **POST /api/designs/save** - Save a design
- **GET /api/designs/get** - Get all user designs
- **DELETE /api/designs/delete/<id>** - Delete a design

### User Profile
- **GET /api/user/profile** - Get user profile

## Features

### Signup Form
The signup modal includes:
- Full Name (required)
- Username (required, min 3 characters)
- Email (required, valid email format)
- Phone Number (optional)
- Address (optional)
- Password (required, min 6 characters)
- Confirm Password (required, must match)

### Validation
- Client-side validation for all fields
- Server-side validation for security
- Email and username uniqueness check
- Password hashing using Werkzeug

### Security Features
- Passwords are hashed using Werkzeug security
- Session-based authentication
- CSRF protection ready
- Input validation on both client and server

## Folder Structure
```
capstone/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── dressify.db            # SQLite database (auto-created)
├── templates/
│   ├── dressify-complete.html
│   ├── index.html
│   └── logo.png
└── README.md
```

## Future Enhancements
1. Email verification
2. Password reset functionality
3. User profile management
4. Social login (Google, Facebook)
5. Payment integration
6. Design sharing and collaboration
7. Mobile app version
