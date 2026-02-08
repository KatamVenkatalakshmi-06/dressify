from flask import Flask, render_template, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static')
app.secret_key = os.getenv('SECRET_KEY', 'your_secret_key_change_this_to_random_string')

# MySQL Configuration - Read from environment variables
MYSQL_CONFIG = {
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', 'password'),
    'database': os.getenv('MYSQL_DATABASE', 'dressify'),
    'port': int(os.getenv('MYSQL_PORT', '3306')),
    'autocommit': True
}

def get_db():
    """Get MySQL database connection"""
    try:
        connection = mysql.connector.connect(**MYSQL_CONFIG)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def init_db():
    """Initialize MySQL database with tables"""
    connection = get_db()
    if not connection:
        print("Failed to connect to MySQL")
        return
    
    cursor = connection.cursor()
    
    try:
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                email VARCHAR(255) UNIQUE NOT NULL,
                username VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                full_name VARCHAR(255),
                phone VARCHAR(20),
                address TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Saved designs table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS saved_designs (
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
            )
        ''')
        
        connection.commit()
        print("Database tables initialized successfully!")
    except Error as e:
        print(f"Error initializing database: {e}")
    finally:
        cursor.close()
        connection.close()

@app.route('/')
def index():
    return render_template('dressify-complete.html')

@app.route('/api/auth/signup', methods=['POST'])
def signup():
    """Register a new user"""
    try:
        data = request.get_json()
        
        # Validate input
        required_fields = ['full_name', 'username', 'email', 'password']
        if not all(field in data for field in required_fields):
            return jsonify({'success': False, 'message': 'Missing required fields'}), 400
        
        full_name = data.get('full_name', '').strip()
        username = data.get('username', '').strip()
        email = data.get('email', '').strip()
        phone = data.get('phone', '').strip()
        address = data.get('address', '').strip()
        password = data.get('password')
        
        # Validation
        if not full_name or len(full_name) < 2:
            return jsonify({'success': False, 'message': 'Full name must be at least 2 characters'}), 400
        
        if not username or len(username) < 3:
            return jsonify({'success': False, 'message': 'Username must be at least 3 characters'}), 400
        
        if not email or '@' not in email:
            return jsonify({'success': False, 'message': 'Invalid email format'}), 400
        
        if not password or len(password) < 6:
            return jsonify({'success': False, 'message': 'Password must be at least 6 characters'}), 400
        
        # Hash password
        hashed_password = generate_password_hash(password)
        
        connection = get_db()
        if not connection:
            return jsonify({'success': False, 'message': 'Database connection failed'}), 500
        
        cursor = connection.cursor(dictionary=True)
        
        try:
            # Check if email or username already exists
            cursor.execute('SELECT id FROM users WHERE email = %s OR username = %s', (email, username))
            if cursor.fetchone():
                cursor.close()
                connection.close()
                return jsonify({'success': False, 'message': 'Email or username already exists'}), 400
            
            # Insert new user
            cursor.execute('''
                INSERT INTO users (email, username, password, full_name, phone, address)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (email, username, hashed_password, full_name, phone, address))
            
            connection.commit()
            
            cursor.close()
            connection.close()
            
            return jsonify({
                'success': True,
                'message': 'Account created successfully! You can now login.',
                'user': {
                    'email': email,
                    'username': username,
                    'full_name': full_name
                }
            }), 201
        
        except Error as e:
            cursor.close()
            connection.close()
            return jsonify({'success': False, 'message': f'Error creating account: {str(e)}'}), 500
    
    except Exception as e:
        return jsonify({'success': False, 'message': f'Server error: {str(e)}'}), 500

@app.route('/api/auth/login', methods=['POST'])
def login():
    """Login user"""
    try:
        data = request.get_json()
        email = data.get('email', '').strip()
        password = data.get('password', '')
        
        if not email or not password:
            return jsonify({'success': False, 'message': 'Email and password required'}), 400
        
        connection = get_db()
        if not connection:
            return jsonify({'success': False, 'message': 'Database connection failed'}), 500
        
        cursor = connection.cursor(dictionary=True)
        
        try:
            cursor.execute('SELECT id, email, username, full_name, password FROM users WHERE email = %s', (email,))
            user = cursor.fetchone()
            
            if not user:
                cursor.close()
                connection.close()
                return jsonify({'success': False, 'message': 'Invalid email or password'}), 401
            
            if not check_password_hash(user['password'], password):
                cursor.close()
                connection.close()
                return jsonify({'success': False, 'message': 'Invalid email or password'}), 401
            
            # Store user in session
            session['user_id'] = user['id']
            session['email'] = user['email']
            session['username'] = user['username']
            
            cursor.close()
            connection.close()
            
            return jsonify({
                'success': True,
                'message': 'Login successful',
                'user': {
                    'id': user['id'],
                    'email': user['email'],
                    'username': user['username'],
                    'full_name': user['full_name']
                }
            }), 200
        
        except Error as e:
            cursor.close()
            connection.close()
            return jsonify({'success': False, 'message': f'Database error: {str(e)}'}), 500
    
    except Exception as e:
        return jsonify({'success': False, 'message': f'Server error: {str(e)}'}), 500

@app.route('/api/auth/logout', methods=['POST'])
def logout():
    """Logout user"""
    session.clear()
    return jsonify({'success': True, 'message': 'Logged out successfully'}), 200

@app.route('/api/auth/check', methods=['GET'])
def check_auth():
    """Check if user is logged in"""
    if 'user_id' in session:
        return jsonify({
            'authenticated': True,
            'user': {
                'id': session.get('user_id'),
                'email': session.get('email'),
                'username': session.get('username')
            }
        }), 200
    return jsonify({'authenticated': False}), 200

@app.route('/api/designs/save', methods=['POST'])
def save_design():
    """Save a design for authenticated user"""
    try:
        if 'user_id' not in session:
            return jsonify({'success': False, 'message': 'Please login to save designs'}), 401
        
        data = request.get_json()
        user_id = session['user_id']
        
        connection = get_db()
        if not connection:
            return jsonify({'success': False, 'message': 'Database connection failed'}), 500
        
        cursor = connection.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO saved_designs 
                (user_id, product_name, product_price, product_image, color, color_name, pattern, design, category, type)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                user_id,
                data.get('product_name'),
                data.get('product_price'),
                data.get('product_image'),
                data.get('color'),
                data.get('color_name'),
                data.get('pattern'),
                data.get('design'),
                data.get('category'),
                data.get('type')
            ))
            
            connection.commit()
            design_id = cursor.lastrowid
            
            cursor.close()
            connection.close()
            
            return jsonify({
                'success': True,
                'message': 'Design saved successfully',
                'design_id': design_id
            }), 201
        
        except Error as e:
            cursor.close()
            connection.close()
            return jsonify({'success': False, 'message': f'Error saving design: {str(e)}'}), 500
    
    except Exception as e:
        return jsonify({'success': False, 'message': f'Server error: {str(e)}'}), 500

@app.route('/api/designs/get', methods=['GET'])
def get_designs():
    """Get all designs for authenticated user"""
    try:
        if 'user_id' not in session:
            return jsonify({'success': False, 'message': 'Please login to view designs'}), 401
        
        user_id = session['user_id']
        
        connection = get_db()
        if not connection:
            return jsonify({'success': False, 'message': 'Database connection failed'}), 500
        
        cursor = connection.cursor(dictionary=True)
        
        try:
            cursor.execute('''
                SELECT * FROM saved_designs 
                WHERE user_id = %s 
                ORDER BY saved_at DESC
            ''', (user_id,))
            
            designs = cursor.fetchall()
            
            # Convert datetime objects to strings
            for design in designs:
                if design['saved_at']:
                    design['saved_at'] = design['saved_at'].isoformat()
            
            cursor.close()
            connection.close()
            
            return jsonify({
                'success': True,
                'designs': designs
            }), 200
        
        except Error as e:
            cursor.close()
            connection.close()
            return jsonify({'success': False, 'message': f'Database error: {str(e)}'}), 500
    
    except Exception as e:
        return jsonify({'success': False, 'message': f'Server error: {str(e)}'}), 500

@app.route('/api/designs/delete/<int:design_id>', methods=['DELETE'])
def delete_design(design_id):
    """Delete a design"""
    try:
        if 'user_id' not in session:
            return jsonify({'success': False, 'message': 'Please login'}), 401
        
        user_id = session['user_id']
        
        connection = get_db()
        if not connection:
            return jsonify({'success': False, 'message': 'Database connection failed'}), 500
        
        cursor = connection.cursor()
        
        try:
            # Verify design belongs to user
            cursor.execute('SELECT id FROM saved_designs WHERE id = %s AND user_id = %s', (design_id, user_id))
            if not cursor.fetchone():
                cursor.close()
                connection.close()
                return jsonify({'success': False, 'message': 'Design not found'}), 404
            
            cursor.execute('DELETE FROM saved_designs WHERE id = %s AND user_id = %s', (design_id, user_id))
            connection.commit()
            
            cursor.close()
            connection.close()
            
            return jsonify({'success': True, 'message': 'Design deleted'}), 200
        
        except Error as e:
            cursor.close()
            connection.close()
            return jsonify({'success': False, 'message': f'Error deleting design: {str(e)}'}), 500
    
    except Exception as e:
        return jsonify({'success': False, 'message': f'Server error: {str(e)}'}), 500

@app.route('/api/user/profile', methods=['GET'])
def get_profile():
    """Get user profile"""
    try:
        if 'user_id' not in session:
            return jsonify({'success': False, 'message': 'Please login'}), 401
        
        user_id = session['user_id']
        
        connection = get_db()
        if not connection:
            return jsonify({'success': False, 'message': 'Database connection failed'}), 500
        
        cursor = connection.cursor(dictionary=True)
        
        try:
            cursor.execute('''
                SELECT id, email, username, full_name, phone, address, created_at 
                FROM users WHERE id = %s
            ''', (user_id,))
            
            user = cursor.fetchone()
            
            cursor.close()
            connection.close()
            
            if not user:
                return jsonify({'success': False, 'message': 'User not found'}), 404
            
            return jsonify({
                'success': True,
                'user': user
            }), 200
        
        except Error as e:
            cursor.close()
            connection.close()
            return jsonify({'success': False, 'message': f'Database error: {str(e)}'}), 500
    
    except Exception as e:
        return jsonify({'success': False, 'message': f'Server error: {str(e)}'}), 500

@app.route('/api/auth/forgot-password', methods=['POST'])
def forgot_password():
    """Initiate password reset"""
    try:
        data = request.get_json()
        email = data.get('email', '').strip()
        
        if not email or '@' not in email:
            return jsonify({'success': False, 'message': 'Invalid email format'}), 400
        
        connection = get_db()
        if not connection:
            return jsonify({'success': False, 'message': 'Database connection failed'}), 500
        
        cursor = connection.cursor(dictionary=True)
        
        try:
            cursor.execute('SELECT id, email FROM users WHERE email = %s', (email,))
            user = cursor.fetchone()
            
            cursor.close()
            connection.close()
            
            if not user:
                # Don't reveal if email exists for security
                return jsonify({'success': True, 'message': 'If email exists, password reset link would be sent'}), 200
            
            return jsonify({'success': True, 'message': 'If email exists, password reset link would be sent'}), 200
        
        except Error as e:
            cursor.close()
            connection.close()
            return jsonify({'success': False, 'message': f'Database error: {str(e)}'}), 500
    
    except Exception as e:
        return jsonify({'success': False, 'message': f'Server error: {str(e)}'}), 500

@app.route('/api/auth/reset-password', methods=['POST'])
def reset_password():
    """Reset password with email verification"""
    try:
        data = request.get_json()
        email = data.get('email', '').strip()
        new_password = data.get('new_password', '')
        confirm_password = data.get('confirm_password', '')
        
        # Validate inputs
        if not email or '@' not in email:
            return jsonify({'success': False, 'message': 'Invalid email format'}), 400
        
        if not new_password or len(new_password) < 6:
            return jsonify({'success': False, 'message': 'Password must be at least 6 characters'}), 400
        
        if new_password != confirm_password:
            return jsonify({'success': False, 'message': 'Passwords do not match'}), 400
        
        connection = get_db()
        if not connection:
            return jsonify({'success': False, 'message': 'Database connection failed'}), 500
        
        cursor = connection.cursor(dictionary=True)
        
        try:
            # Check if user exists
            cursor.execute('SELECT id FROM users WHERE email = %s', (email,))
            user = cursor.fetchone()
            
            if not user:
                cursor.close()
                connection.close()
                return jsonify({'success': False, 'message': 'Email not found in our system'}), 404
            
            # Hash new password
            hashed_password = generate_password_hash(new_password)
            
            # Update password
            cursor.execute('UPDATE users SET password = %s WHERE email = %s', (hashed_password, email))
            connection.commit()
            
            cursor.close()
            connection.close()
            
            return jsonify({
                'success': True,
                'message': 'Password reset successfully! You can now login with your new password.'
            }), 200
        
        except Error as e:
            cursor.close()
            connection.close()
            return jsonify({'success': False, 'message': f'Database error: {str(e)}'}), 500
    
    except Exception as e:
        return jsonify({'success': False, 'message': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='localhost', port=5000)
