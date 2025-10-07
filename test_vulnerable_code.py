#!/usr/bin/env python3
"""
Test vulnerable code samples for security analysis demonstration
This file contains intentionally vulnerable code patterns for testing the SecurityAnalyzer chat mode

⚠️  WARNING: This file contains FAKE/TEST credentials and vulnerabilities for demonstration purposes only.
    These are NOT real secrets and should never be used in production systems.
    This file is designed to trigger security scanners to validate the SecurityAnalyzer functionality.
"""

import hashlib
import os
import sqlite3

from flask import Flask, render_template_string, request

# Example 1: Hardcoded credentials (HIGH severity - CWE-798)
# NOTE: These are intentionally fake demo credentials for security analysis demonstration
API_KEY = "demo-api-key-1234567890abcdef1234567890abcdef"  # DEMO CREDENTIAL
DATABASE_PASSWORD = "admin123"
SECRET_TOKEN = "my-super-secret-token-12345"

# Example 2: SQL Injection vulnerability (HIGH severity - CWE-89)
def get_user_data(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Vulnerable: Direct string concatenation in SQL query
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    return cursor.fetchall()

# Example 3: Weak cryptographic algorithm (MEDIUM severity - CWE-327)
def hash_password(password):
    # Vulnerable: Using MD5 for password hashing
    return hashlib.md5(password.encode()).hexdigest()

def generate_session_id():
    # Vulnerable: Using SHA1 which is cryptographically weak
    import random
    data = str(random.random())
    return hashlib.sha1(data.encode()).hexdigest()

# Example 4: XSS vulnerability (MEDIUM severity - CWE-79)
app = Flask(__name__)

@app.route('/profile')
def user_profile():
    username = request.args.get('name', '')
    # Vulnerable: Direct insertion into HTML without escaping
    template = '<h1>Welcome ' + username + '</h1>'
    return render_template_string(template)

@app.route('/comment')
def show_comment():
    comment = request.args.get('comment', '')
    # Vulnerable: Using innerHTML with user input
    html = f"""
    <script>
    document.getElementById('comment').innerHTML = '{comment}';
    </script>
    """
    return html

# Example 5: Insecure HTTP connections (MEDIUM severity - CWE-319)
import requests


def fetch_user_data():
    # Vulnerable: Using HTTP instead of HTTPS for sensitive data
    response = requests.get('http://api.example.com/users/sensitive-data')
    return response.json()

def sync_with_external_service():
    # Vulnerable: Insecure connection to external service
    requests.post('http://external-service.com/api/sync', data={'token': API_KEY})

# Example 6: Command injection vulnerability (CRITICAL severity - CWE-78)
def process_file(filename):
    import subprocess
    # Vulnerable: Direct use of user input in system command
    result = subprocess.run(f'ls -la {filename}', shell=True, capture_output=True)
    return result.stdout

def backup_database(db_name):
    # Vulnerable: Command injection through user input
    os.system(f'mysqldump {db_name} > backup.sql')

# Example 7: Path traversal vulnerability (HIGH severity - CWE-22)
def read_config_file(config_name):
    # Vulnerable: No validation of file path
    config_path = f'./config/{config_name}'
    try:
        with open(config_path, 'r') as f:
            return f.read()
    except:
        return None

def serve_file(filename):
    # Vulnerable: Directory traversal possible
    file_path = './uploads/' + filename
    with open(file_path, 'rb') as f:
        return f.read()

# Example 8: Insecure random number generation (LOW severity - CWE-330)
import math
import random


def generate_password_reset_token():
    # Vulnerable: Using math.random for security-sensitive operations
    token = str(math.floor(random.random() * 1000000))
    return token

def create_session_token():
    # Vulnerable: Predictable random seed
    random.seed(1234)
    return str(random.randint(1000000, 9999999))

# Example 9: Debug mode in production (MEDIUM severity - CWE-489)
DEBUG_MODE = True
DEVELOPMENT = True
VERBOSE_ERRORS = "on"

if DEBUG_MODE:
    print("Debug mode is enabled - this should not be in production!")

# Example 10: Unsafe deserialization (CRITICAL severity - CWE-502)
import pickle

import yaml


def load_user_session(session_data):
    # Vulnerable: Unsafe deserialization
    return pickle.loads(session_data)

def parse_config(config_string):
    # Vulnerable: Unsafe YAML loading
    return yaml.load(config_string)

def execute_user_code(code_string):
    # Vulnerable: Direct code execution
    return eval(code_string)

# Example 11: Additional API key patterns
# NOTE: These are intentionally fake demo credentials for security analysis demonstration
STRIPE_API_KEY = "fake-stripe-key-1234567890abcdef1234567890abcdef"  # DEMO CREDENTIAL
AWS_ACCESS_KEY = "FAKE1234567890ABCDEF"  # DEMO CREDENTIAL  
JWT_SECRET = "demo-jwt-secret-key-very-long-and-secure-hopefully"  # DEMO CREDENTIAL

class UserAuthentication:
    def __init__(self):
        # Vulnerable: Hardcoded credentials in class
        # NOTE: These are intentionally fake demo credentials for security analysis demonstration
        self.admin_password = "admin123456"  # DEMO CREDENTIAL
        self.service_token = "demo-service-token-abc123def456"  # DEMO CREDENTIAL

    def authenticate_user(self, username, password):
        # Vulnerable: SQL injection in authentication
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        # Database execution would happen here
        return True

# This file is intentionally vulnerable for testing purposes only
# DO NOT use any of these patterns in production code
if __name__ == "__main__":
    print("This file contains intentionally vulnerable code for security testing.")
    print("Run the SecurityAnalyzer chat mode to identify and remediate these issues.")
