# CONFIGURATION & DEPLOYMENT GUIDE

## Environment Setup

### Development Environment
Currently configured for development with:
- Debug mode: `True`
- Host: `localhost`
- Port: `5000`

### Configuration File (in app.py)

```python
app.secret_key = 'your_secret_key_change_this'  # Line 9
DATABASE = 'dressify.db'  # Line 11
```

## How to Change Configuration

### 1. Change Server Port
Edit `app.py` last line:
```python
if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='localhost', port=5001)  # Change 5000 to any port
```

### 2. Change Host (Allow Remote Access)
Edit `app.py` last line:
```python
if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)  # 0.0.0.0 accepts all IPs
```

### 3. Disable Debug Mode (Production)
Edit `app.py` last line:
```python
if __name__ == '__main__':
    init_db()
    app.run(debug=False, host='localhost', port=5000)  # debug=False for production
```

### 4. Change Secret Key (IMPORTANT for Production)
Edit `app.py` line 9:
```python
import secrets
app.secret_key = secrets.token_hex(32)  # Generate secure random key
```

## Database Configuration

### Change Database File Location
Edit `app.py` line 11:
```python
DATABASE = 'path/to/dressify.db'  # Change to desired location
```

### Use PostgreSQL Instead (Advanced)
Replace SQLite with PostgreSQL:
```python
import psycopg2
DATABASE_URL = 'postgresql://user:password@localhost/dressify'
```

## Deployment Options

### Option 1: Gunicorn (Recommended for Production)

Install Gunicorn:
```bash
pip install gunicorn
```

Run with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Option 2: Docker Deployment

Create `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t dressify .
docker run -p 5000:5000 dressify
```

### Option 3: AWS EC2 Deployment

1. Launch EC2 instance
2. SSH into instance
3. Clone your repo
4. Install dependencies
5. Run with Gunicorn
6. Set up Nginx as reverse proxy

### Option 4: Heroku Deployment

Create `Procfile`:
```
web: gunicorn app:app
```

Create `runtime.txt`:
```
python-3.9.0
```

Deploy:
```bash
heroku create dressify-app
git push heroku main
```

## SSL/HTTPS Setup

### For Production (Let's Encrypt + Nginx)

1. Install Certbot:
```bash
sudo apt-get install certbot python3-certbot-nginx
```

2. Get certificate:
```bash
sudo certbot certonly --nginx -d yourdomain.com
```

3. Configure Nginx to use certificate

### For Development (Self-signed)
```bash
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```

Run Flask with SSL:
```python
app.run(ssl_context=('cert.pem', 'key.pem'))
```

## Environment Variables

Create `.env` file:
```
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your_secret_key_here
DATABASE_URL=dressify.db
```

Load in `app.py`:
```python
from dotenv import load_dotenv
load_dotenv()
import os
app.secret_key = os.getenv('SECRET_KEY')
```

## Performance Optimization

### 1. Enable Compression
```python
from flask_compress import Compress
Compress(app)
```

### 2. Database Connection Pooling
```python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///dressify.db', poolclass=StaticPool)
```

### 3. Caching
```python
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
```

### 4. Load Balancing
Use multiple Gunicorn workers:
```bash
gunicorn -w 8 -b 0.0.0.0:5000 app:app
```

## Monitoring & Logging

### Add Logging
```python
import logging
logging.basicConfig(
    filename='dressify.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)
```

### Monitor Database
```python
import time
start = time.time()
# Database operation
duration = time.time() - start
if duration > 1:
    app.logger.warning(f'Slow query: {duration}s')
```

## Scaling the Application

### Database Scaling
- SQLite → PostgreSQL for concurrent users
- Add database indexes
- Implement connection pooling

### Application Scaling
- Use load balancer (nginx, HAProxy)
- Run multiple app instances
- Use message queue (Celery + Redis)

### File Storage Scaling
- Move uploads to cloud (S3, Google Cloud Storage)
- CDN for static files

## Backup & Recovery

### Database Backup
```bash
# Daily backup script
sqlite3 dressify.db ".backup dressify_backup_$(date +%Y%m%d).db"
```

### Automated Backup (Cron)
```bash
0 2 * * * /path/to/backup.sh
```

### Recovery
```bash
sqlite3 dressify.db < backup.db
```

## Security Checklist

- [ ] Change secret key
- [ ] Disable debug mode in production
- [ ] Use HTTPS/SSL
- [ ] Implement rate limiting
- [ ] Add CORS headers if needed
- [ ] Validate all inputs
- [ ] Use environment variables for secrets
- [ ] Regular backups
- [ ] Monitor logs for suspicious activity
- [ ] Keep dependencies updated

## Testing

### Unit Tests
```bash
pip install pytest
pytest tests/
```

### Load Testing
```bash
pip install locust
locust -f locustfile.py
```

## Maintenance

### Update Dependencies
```bash
pip list --outdated
pip install --upgrade package_name
```

### Database Maintenance
```bash
# Vacuum (optimize) database
sqlite3 dressify.db "VACUUM;"
```

## Support & Troubleshooting

### Common Issues
1. Port already in use → Change port
2. Module not found → Reinstall requirements
3. Database locked → Restart app
4. Permission denied → Check file permissions

### Debug Mode
Enable Flask debug mode:
```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
python app.py
```

## Production Checklist

1. ✓ Use strong secret key
2. ✓ Enable HTTPS
3. ✓ Disable debug mode
4. ✓ Use production database (PostgreSQL)
5. ✓ Set up backups
6. ✓ Configure logging
7. ✓ Set up monitoring
8. ✓ Use reverse proxy (Nginx)
9. ✓ Use app server (Gunicorn)
10. ✓ Test thoroughly before deploying

## Contact & Support

For issues or questions, check:
- README.md - Full documentation
- QUICKSTART.md - Quick start guide
- IMPLEMENTATION_SUMMARY.md - Feature overview
