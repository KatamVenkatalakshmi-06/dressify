# Dressify Deployment Guide

## Pre-Deployment Checklist

### 1. Secure Your Credentials
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your actual values
# DO NOT commit .env to git!
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Test Locally
```bash
python app.py
# Visit http://localhost:5000
```

---

## Deployment Options

### Option 1: PythonAnywhere (RECOMMENDED - Easiest)

**Prerequisites:**
- GitHub account with code pushed to repository
- PythonAnywhere account (free tier available at pythonanywhere.com)

**Deployment Steps:**

1. **Create PythonAnywhere Account**
   - Go to [pythonanywhere.com](https://www.pythonanywhere.com)
   - Sign up for a free account

2. **Clone Your Repository**
   - Log in to PythonAnywhere
   - Open Bash console
   - Run: `git clone https://github.com/your-username/dressify.git`
   - Navigate: `cd dressify`

3. **Add Web App**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Flask"
   - Select Python 3.9+ (or available version)
   - Accept default path or specify custom path

4. **Configure WSGI File**
   - Go to Web app settings
   - Under WSGI configuration file, click the link to edit
   - Replace the Flask section with:
   ```python
   import sys
   path = '/home/yourusername/dressify'
   if path not in sys.path:
       sys.path.append(path)
   from app import app as application
   ```

5. **Set Environment Variables**
   - In Web app settings, scroll to "Environment variables"
   - Add each variable:
     - `MYSQL_HOST` = your MySQL host
     - `MYSQL_USER` = your MySQL username
     - `MYSQL_PASSWORD` = your MySQL password
     - `MYSQL_DATABASE` = dressify
     - `MYSQL_PORT` = 3306
     - `SECRET_KEY` = your-random-secret-key

6. **Install Dependencies**
   - Open Bash console
   - Run: `cd ~/dressify && pip install --user -r requirements.txt`

7. **Initialize Database**
   - In Bash console: `python ~/dressify/setup_check.py`

8. **Reload Web App**
   - Go back to Web tab
   - Click "Reload yourusername.pythonanywhere.com"

9. **Access Your App**
   - Visit `https://yourusername.pythonanywhere.com`

**PythonAnywhere Tips:**
- Free tier allows 100MB disk space
- MySQL database costs extra ($5/month)
- Check error log in Web tab for debugging
- Reload after any code changes via git pull

---

### Option 2: Render (Modern Alternative)

**Prerequisites:**
- GitHub account with code pushed
- Render account (free tier at render.com)
- External MySQL database (required - local SQLite not recommended for production)

**Deployment Steps:**

1. **Create Render Account**
   - Go to [render.com](https://www.render.com)
   - Sign up with GitHub account

2. **Create New Web Service**
   - Dashboard → New → Web Service
   - Connect your GitHub repository
   - Select the dressify repository
   - Choose "Python 3" as environment

3. **Configure Web Service**
   - **Name**: dressify (or your preferred name)
   - **Runtime**: Python 3
   - **Build Command**: 
     ```
     pip install -r requirements.txt
     ```
   - **Start Command**: 
     ```
     gunicorn app:app
     ```
   - **Instance Type**: Free (or paid if needed)

4. **Add Environment Variables**
   - In settings, go to "Environment"
   - Add each variable:
     - `MYSQL_HOST` = your MySQL host
     - `MYSQL_USER` = your MySQL username
     - `MYSQL_PASSWORD` = your MySQL password
     - `MYSQL_DATABASE` = dressify
     - `MYSQL_PORT` = 3306
     - `SECRET_KEY` = your-random-secret-key
     - `FLASK_ENV` = production

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically deploy
   - Monitor deployment in Logs tab

6. **Access Your App**
   - View live URL at top of page (e.g., `https://dressify.onrender.com`)

**Render Tips:**
- Free tier spins down after 15 minutes of inactivity (first request will be slow)
- Use PostgreSQL or external MySQL
- Auto-deploys on every git push to main branch
- SSL certificate included automatically

---

### Option 3: Heroku (Legacy)

**Prerequisites:**
- GitHub account with code pushed
- Heroku account

**Steps:**
1. Install Heroku CLI
2. `Procfile` already exists in project root
3. Deploy:
   ```bash
   heroku login
   heroku create your-app-name
   heroku config:set MYSQL_HOST=your_host
   heroku config:set MYSQL_USER=your_user
   heroku config:set MYSQL_PASSWORD=your_password
   heroku config:set MYSQL_DATABASE=dressify
   heroku config:set SECRET_KEY=your_random_key
   git push heroku main
   ```

---

## Important Security Notes

✅ **Before deploying:**
- [ ] Change `SECRET_KEY` in `.env` to a strong random string
- [ ] Use `.env` for ALL credentials (never hardcode)
- [ ] Set `FLASK_ENV=production` 
- [ ] `.gitignore` includes `.env`
- [ ] Don't commit `dressify.db` or `.env`
- [ ] Use HTTPS only (enforced by Render/PythonAnywhere)
- [ ] Validate all user inputs in forms
- [ ] Set password hashing properly (already done with werkzeug)

## Database Configuration for Deployment

For production deployment, use external MySQL:
- **PythonAnywhere MySQL**: $5/month add-on
- **Render**: Recommend using Render's PostgreSQL or external MySQL
- **Alternative**: Use managed MySQL services like AWS RDS, DigitalOcean MySQL

Update `.env` with your external database credentials before deploying.

✅ **In production:**
- Use HTTPS (SSL certificate)
- Keep dependencies updated
- Monitor error logs
- Use strong database passwords
- Enable database backups

---

## Quick Reference

| Platform | Cost | Difficulty | MySQL Included |
|----------|------|-----------|-----------------|
| PythonAnywhere | Free | Very Easy | Yes |
| Heroku | $7+/month | Easy | Need Add-on |
| Digital Ocean | $5/month | Medium | Need Setup |
| AWS | Variable | Hard | Yes |

**For beginners: Use PythonAnywhere**
