# MySQL Setup Guide for Dressify

## Step 1: Install MySQL & MySQL Connector
If not already installed, download MySQL Community Server from: https://dev.mysql.com/downloads/mysql/

## Step 2: Set Up Database & Tables
Open MySQL Command Line Client (or Command Prompt with MySQL):
```
mysql -u root -p
```
Enter your MySQL password (set during installation)

Then run these commands:

```sql
-- Create database
CREATE DATABASE dressify;
USE dressify;

-- Create users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create saved_designs table
CREATE TABLE saved_designs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_name VARCHAR(255),
    product_price VARCHAR(50),
    product_image LONGTEXT,
    color VARCHAR(50),
    color_name VARCHAR(50),
    pattern VARCHAR(50),
    design VARCHAR(50),
    category VARCHAR(50),
    type VARCHAR(50),
    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

exit;
```

## Step 3: Update Configuration in app.py
Edit `app.py` and change the MYSQL_CONFIG (lines 13-20):

```python
MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'root',           # Change if your MySQL username is different
    'password': 'YOUR_PASSWORD',  # ← CHANGE TO YOUR MYSQL PASSWORD
    'database': 'dressify',
    'autocommit': True
}
```

## Step 4: Install Python Dependencies
```
pip install -r requirements.txt
```

## Step 5: Run the Flask Server
```
python app.py
```

The server will start on `http://localhost:5000`

## Step 6: Test the Application
1. Open browser to `http://localhost:5000`
2. Click "Sign Up" button
3. Enter any email, username, and password (no restrictions)
4. Submit to register - data saved in MySQL!
5. Login with your credentials
6. Browse products and save designs

## Verify Data in MySQL
To check if data is being saved:
```
mysql -u root -p dressify
SELECT * FROM users;
SELECT * FROM saved_designs;
exit;
```

## Troubleshooting

**Error: "1045 - Access denied for user 'root'@'localhost'"**
- Check your MySQL password in app.py MYSQL_CONFIG matches your actual MySQL password

**Error: "1049 - Unknown database 'dressify'"**
- Run the database creation SQL commands from Step 2

**Error: "No module named 'mysql'"**
- Run: `pip install mysql-connector-python`

**Flask server won't start**
- Make sure no other application is using port 5000
- Check Python version is 3.8+
