#!/usr/bin/env python
"""
Setup verification script for Dressify
Checks if all dependencies are installed and database is ready
"""

import sys
import os
import sqlite3

def check_dependencies():
    """Check if required packages are installed"""
    print("=" * 50)
    print("CHECKING DEPENDENCIES")
    print("=" * 50)
    
    try:
        import flask
        print("✓ Flask is installed")
    except ImportError:
        print("✗ Flask is NOT installed")
        return False
    
    try:
        from werkzeug.security import generate_password_hash
        print("✓ Werkzeug is installed")
    except ImportError:
        print("✗ Werkzeug is NOT installed")
        return False
    
    return True

def check_database():
    """Check if database is initialized"""
    print("\n" + "=" * 50)
    print("CHECKING DATABASE")
    print("=" * 50)
    
    db_path = 'dressify.db'
    
    if os.path.exists(db_path):
        print(f"✓ Database file exists at {db_path}")
        
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            
            if tables:
                print(f"✓ Database has {len(tables)} tables:")
                for table in tables:
                    print(f"  - {table[0]}")
            else:
                print("✗ Database is empty, tables not initialized")
                conn.close()
                return False
            
            conn.close()
            return True
        except Exception as e:
            print(f"✗ Database error: {e}")
            return False
    else:
        print(f"ℹ Database file does not exist yet")
        print("  The database will be created when you run the app")
        return True

def check_templates():
    """Check if HTML templates exist"""
    print("\n" + "=" * 50)
    print("CHECKING TEMPLATES")
    print("=" * 50)
    
    templates = ['templates/dressify-complete.html', 'templates/index.html']
    
    for template in templates:
        if os.path.exists(template):
            print(f"✓ {template} exists")
        else:
            print(f"✗ {template} NOT found")
            return False
    
    return True

def main():
    print("\n")
    print("╔════════════════════════════════════════════════╗")
    print("║   DRESSIFY - SETUP VERIFICATION                ║")
    print("╚════════════════════════════════════════════════╝")
    
    all_good = True
    
    if not check_dependencies():
        print("\n✗ Please install dependencies:")
        print("  pip install -r requirements.txt")
        all_good = False
    
    if not check_templates():
        print("\n✗ HTML templates are missing!")
        all_good = False
    
    check_database()
    
    print("\n" + "=" * 50)
    if all_good:
        print("✓ ALL CHECKS PASSED!")
        print("=" * 50)
        print("\nYou can now run the app with:")
        print("  python app.py")
        print("\nThen open your browser to http://localhost:5000")
        return 0
    else:
        print("✗ SOME CHECKS FAILED")
        print("=" * 50)
        print("\nPlease fix the issues above and try again.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
