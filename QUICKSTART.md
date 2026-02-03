# Quick Start Guide

## Installation & Running

### Step 1: Install Requirements
Open PowerShell and navigate to the capstone folder:
```powershell
cd c:\Users\DELL\Desktop\capstone
pip install -r requirements.txt
```

### Step 2: Run the Flask App
```powershell
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

### Step 3: Access in Browser
Open your browser and go to: `http://localhost:5000`

## Using the App

### 1. Signup (Create Account)
- Click "Sign up here" link on the login page
- Fill in the signup form with your details:
  - Full Name: Your complete name
  - Username: Choose a unique username (minimum 3 characters)
  - Email: Your email address
  - Phone: Optional phone number
  - Address: Optional address
  - Password: Create a password (minimum 6 characters)
  - Confirm Password: Re-enter your password
- Click "Create Account"
- You'll see a success message if account is created
- The form will automatically populate your email in the login field

### 2. Login
- Enter the email you registered with
- Enter your password
- Click "Login"
- You'll be logged into the dashboard

### 3. Logout
- Click the "Logout" button in the sidebar

## Database

The database is automatically created when the app first runs. It stores:

**User Information:**
- Email and username
- Hashed password (secure)
- Full name, phone, address
- Account creation date

**Design Saves:**
- All customized outfit designs
- Product details
- Customization options (color, pattern, style)
- Save timestamps

## File Locations

| File | Purpose |
|------|---------|
| `app.py` | Main Flask backend application |
| `dressify.db` | SQLite database (auto-created) |
| `templates/dressify-complete.html` | Main frontend HTML |
| `requirements.txt` | Python dependencies |

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, modify `app.py`:
```python
if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='localhost', port=5001)  # Change 5000 to 5001
```

### Database Issues
To reset the database, delete `dressify.db` and restart the app.

### Dependencies Not Installing
```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

## Security Notes

- Passwords are hashed before storing in database
- Change the secret key in production:
  ```python
  app.secret_key = 'your_new_secret_key_here'
  ```
- Never commit the database or secret keys to version control
- Use HTTPS in production

## Next Steps

Once you're comfortable with the basic setup, you can:
1. Add more product categories
2. Implement payment processing
3. Add social sharing features
4. Create admin dashboard
5. Deploy to a web server
