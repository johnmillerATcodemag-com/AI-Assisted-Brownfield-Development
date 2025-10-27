#!/usr/bin/env python3
"""
Test vulnerable code samples for security analysis demonstration
This file contains intentionally vulnerable code patterns for testing the SecurityAnalyzer chat mode

⚠️  WARNING: This file contains FAKE/TEST credentials and vulnerabilities for demonstration purposes only.
    These are NOT real secrets and should never be used in production systems.
    This file is designed to trigger security scanners to validate the SecurityAnalyzer functionality.

🔍 SECURITY SCANNER NOTE: All credentials in this file are FAKE/DEMO/TEST values.
   - No real API keys, passwords, or tokens are present
   - All values are intentionally fabricated for security testing
   - This file should be excluded from production security scans
"""

import hashlib
import math
import os
import pickle
import random
import sqlite3
import subprocess

import requests
import yaml
from flask import Flask, render_template_string, request

# Example 1: Hardcoded credentials (HIGH severity - CWE-798)
# NOTE: These are intentionally fake demo credentials for security analysis demonstration
# SECURITY_TEST_IGNORE: Demo credentials for vulnerability testing only
API_KEY = "FAKE-DEMO-api_token_1234567890abcdef1234567890abcdef"  # DEMO CREDENTIAL - NOT REAL
DATABASE_PASSWORD = "FAKE-DEMO-admin123"  # DEMO CREDENTIAL - NOT REAL
SECRET_TOKEN = "FAKE-DEMO-my-super-secret-token-12345"  # DEMO CREDENTIAL - NOT REAL

# Example 2: SQL Injection vulnerability (HIGH severity - CWE-89)
def get_user_data(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Vulnerable: Direct string concatenation in SQL query
    # SECURITY_TEST_IGNORE: Intentional SQL injection for security testing - Issue #459
    query = "SELECT * FROM users WHERE id = " + user_id  # FAKE-DEMO-sql-injection for vulnerability testing
    cursor.execute(query)
    return cursor.fetchall()

# Example 3: Weak cryptographic algorithm (MEDIUM severity - CWE-327)
def hash_password(password):
    # Vulnerable: Using MD5 for password hashing
    # SECURITY_TEST_IGNORE: Intentional MD5 usage for security testing - Issue #460
    return hashlib.md5(password.encode()).hexdigest()  # FAKE-DEMO-md5 for vulnerability testing

def generate_session_id():
    # Vulnerable: Using SHA1 which is cryptographically weak
    # SECURITY_TEST_IGNORE: Intentional SHA1 usage for security testing - Issue #461
    import random
    data = str(random.random())
    return hashlib.sha1(data.encode()).hexdigest()  # FAKE-DEMO-sha1 for vulnerability testing

# Example 4: XSS vulnerability (MEDIUM severity - CWE-79)
app = Flask(__name__)

@app.route('/profile')
def user_profile():
    username = request.args.get('name', '')
    # Vulnerable: Direct insertion into HTML without escaping
    # SECURITY_TEST_IGNORE: Intentional XSS vulnerability for security testing - Issue #465
    template = '<h1>Welcome ' + username + '</h1>'  # FAKE-DEMO-xss for vulnerability testing
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


def fetch_user_data():
    # Vulnerable: Using HTTP instead of HTTPS for sensitive data
    # SECURITY_TEST_IGNORE: Intentional HTTP usage for security testing - matches Issue #467
    response = requests.get('http://api.example.com/users/sensitive-data')  # FAKE-DEMO-http for vulnerability testing
    return response.json()

def sync_with_external_service():
    # Vulnerable: Insecure connection to external service
    # SECURITY_TEST_IGNORE: Using fake demo API key for vulnerability testing - Issue #467
    requests.post('http://external-service.com/api/sync', data={'token': API_KEY})  # FAKE-DEMO-http for vulnerability testing

# Example 6: Command injection vulnerability (CRITICAL severity - CWE-78)
def process_file(filename):
    # Vulnerable: Direct use of user input in system command
    # SECURITY_TEST_IGNORE: Intentional command injection for security testing
    result = subprocess.run(f'ls -la {filename}', shell=True, capture_output=True)  # FAKE-DEMO-command for vulnerability testing
    return result.stdout

def backup_database(db_name):
    # Vulnerable: Command injection through user input
    # SECURITY_TEST_IGNORE: Intentional command injection for security testing - Issue #468
    os.system(f'mysqldump {db_name} > backup.sql')  # FAKE-DEMO-command-injection for vulnerability testing

# Example 7: Path traversal vulnerability (HIGH severity - CWE-22)
def read_config_file(config_name):
    # Vulnerable: No validation of file path
    # SECURITY_TEST_IGNORE: Intentional path traversal vulnerability for security testing
    config_path = f'./config/{config_name}'  # FAKE-DEMO-path for vulnerability testing
    try:
        with open(config_path, 'r') as f:
            return f.read()
    except Exception:  # Fixed bare except
        return None

def serve_file(filename):
    # Vulnerable: Directory traversal possible
    file_path = './uploads/' + filename
    with open(file_path, 'rb') as f:
        return f.read()

# Example 8: Insecure random number generation (LOW severity - CWE-330)


def generate_password_reset_token():
    # Vulnerable: Using math.random for security-sensitive operations
    # SECURITY_TEST_IGNORE: Intentional weak random usage for security testing - Issue #456
    token = str(math.floor(random.random() * 1000000))  # FAKE-DEMO-weak-random for vulnerability testing
    return token

def create_session_token():
    # Vulnerable: Predictable random seed
    # SECURITY_TEST_IGNORE: Intentional predictable seed for security testing - Issue #456
    random.seed(1234)  # FAKE-DEMO-predictable-seed for vulnerability testing
    return str(random.randint(1000000, 9999999))

# Example 9: Debug mode in production (MEDIUM severity - CWE-489)
DEBUG_MODE = True
DEVELOPMENT = True
VERBOSE_ERRORS = "on"

if DEBUG_MODE:
    print("Debug mode is enabled - this should not be in production!")

# Example 10: Unsafe deserialization (CRITICAL severity - CWE-502)


def load_user_session(session_data):
    # Vulnerable: Unsafe deserialization
    # SECURITY_TEST_IGNORE: Intentional pickle usage for security testing - Issue #469
    return pickle.loads(session_data)  # FAKE-DEMO-pickle for vulnerability testing

def parse_config(config_string):
    # Vulnerable: Unsafe YAML loading
    return yaml.load(config_string)

def execute_user_code(code_string):
    # Vulnerable: Direct code execution
    # SECURITY_TEST_IGNORE: Intentional eval() usage for security testing - Issue #470
    return eval(code_string)  # FAKE-DEMO-eval for vulnerability testing

# Example 11: Additional API key patterns
# NOTE: These are intentionally fake demo credentials for security analysis demonstration
# SECURITY_TEST_IGNORE: All API keys below are fake/demo for vulnerability testing only
STRIPE_API_KEY = "FAKE-DEMO-stripe_test_1234567890abcdef1234567890abcdef"  # DEMO CREDENTIAL - NOT REAL
AWS_ACCESS_KEY = "FAKE-DEMO-1234567890ABCDEF"  # DEMO CREDENTIAL - NOT REAL
JWT_SECRET = "FAKE-DEMO-jwt-secret-very-long-and-secure-hopefully"  # DEMO CREDENTIAL - NOT REAL

class UserAuthentication:
    def __init__(self):
        # Vulnerable: Hardcoded credentials in class
        # NOTE: These are intentionally fake demo credentials for security analysis demonstration
        # SECURITY_TEST_IGNORE: Demo credentials for vulnerability testing only
        self.admin_password = "FAKE-DEMO-admin123456"  # DEMO CREDENTIAL - NOT REAL
        self.service_token = "FAKE-DEMO-service-token-abc123def456"  # DEMO CREDENTIAL - NOT REAL

    def authenticate_user(self, username, password):
        # Vulnerable: SQL injection in authentication
        # SECURITY_TEST_IGNORE: Intentional SQL injection for security testing
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"  # FAKE-DEMO-sql for vulnerability testing
        # Database execution would happen here (intentionally commented for demo)
        print(f"Would execute: {query}")  # Demo only - shows the vulnerable query
        return True

# This file is intentionally vulnerable for testing purposes only
# DO NOT use any of these patterns in production code
if __name__ == "__main__":
    print("This file contains intentionally vulnerable code for security testing.")
    print("Run the SecurityAnalyzer chat mode to identify and remediate these issues.")
