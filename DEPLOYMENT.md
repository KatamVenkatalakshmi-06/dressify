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

**Steps:**
1. Go to [pythonanywhere.com](https://www.pythonanywhere.com)
2. Create a free account
3. Upload your project via git:
   ```bash
   git clone https://your-github-repo.git
   ```
4. Go to Web tab → Add a new web app → Flask
5. Configure to use your project's `app.py`
6. Add environment variables in PythonAnywhere settings:
   - MYSQL_HOST
   - MYSQL_USER
   - MYSQL_PASSWORD
   - MYSQL_DATABASE
   - SECRET_KEY
7. Reload the web app
8. Your app is live at `yourusername.pythonanywhere.com`

---

### Option 2: Heroku

**Prerequisites:**
- GitHub account with your code pushed
- Heroku account

**Steps:**
1. Install Heroku CLI
2. Create `Procfile` in project root:
   ```
   web: gunicorn app:app
   ```
3. Add to requirements.txt:
   ```
   gunicorn==20.1.0
   ```
4. Deploy:
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

### Option 3: Digital Ocean / Linode (Best for Production)

**Setup Ubuntu Server:**
1. Buy $5/month droplet
2. SSH into server
3. Install Python, MySQL, Nginx
4. Clone your repo
5. Run Flask with Gunicorn + Nginx proxy

---

## Important Security Notes

✅ **Before deploying:**
- [ ] Change `SECRET_KEY` in `.env`
- [ ] Use `.env` for all credentials
- [ ] Set `FLASK_DEBUG=False`
- [ ] `.gitignore` includes `.env`
- [ ] Don't commit `dressify.db`

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
