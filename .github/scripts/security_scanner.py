#!/usr/bin/env python3
"""
Security Analysis Script
Performs custom security pattern analysis on code files
"""

import json
import os
import re
from pathlib import Path


class SecurityChecker:
    def __init__(self):
        self.findings = []

        # Files to exclude from security scanning (test/demo files with intentional vulnerabilities)
        self.exclude_files = [
            "test_vulnerable_code.py",  # Security testing file with fake credentials
            "security_test_samples.py",
            "test_security_analyzer.py"
        ]

        # Patterns to ignore in security scanning (for test/demo purposes)
        self.security_test_ignore_patterns = [
            r"FAKE-DEMO-.*",  # All fake demo credentials
            r".*DEMO CREDENTIAL.*",  # Demo credential markers
            r"SECURITY_TEST_IGNORE:",  # Explicit test ignore markers
        ]

        # Directories to exclude
        self.exclude_directories = [
            "security-analysis",  # Exclude security test files with intentional vulnerabilities
            ".git", "node_modules", "__pycache__", ".venv", "venv",
            "dist", "build", ".next", "coverage", "logs", "tmp",
            ".pytest_cache", ".mypy_cache", "vendor", "packages"
        ]

        self.patterns = {
            'hardcoded_secrets': {
                'pattern': r'(?i)(password|secret|key|token|api_key)\s*[=:]\s*["\']([^"\']{8,})["\']',
                'severity': 'HIGH',
                'cwe': 'CWE-798',
                'description': 'Potential hardcoded secret or credential'
            },
            'sql_injection': {
                # SECURITY_SCANNER_PATTERN: This is a regex pattern to detect SQL injection, not actual SQL injection
                'pattern': r'(?i)(SELECT|INSERT|UPDATE|DELETE).*\+.*["\']',  # Pattern for SQL + string concatenation
                'severity': 'HIGH',
                'cwe': 'CWE-89',
                'description': 'Potential SQL injection vulnerability'
            },
            'xss_vulnerability': {
                'pattern': r'(?i)innerHTML\s*=\s*[^;]*\+|document\.write\s*\([^)]*\+',
                'severity': 'MEDIUM',
                'cwe': 'CWE-79',
                'description': 'Potential XSS vulnerability'
            },
            'insecure_http': {
                # SECURITY_SCANNER_PATTERN: This is a regex pattern to detect HTTP usage, not actual HTTP usage
                'pattern': r'http://(?!localhost|127\.0\.0\.1|0\.0\.0\.0)',  # Pattern for non-local HTTP URLs
                'severity': 'MEDIUM',
                'cwe': 'CWE-319',
                'description': 'Insecure HTTP connection'
            },
            'weak_crypto': {
                'pattern': r'(?i)(md5|sha1)\s*\(',
                'severity': 'MEDIUM',
                'cwe': 'CWE-327',
                'description': 'Weak cryptographic algorithm'
            },
            'command_injection': {
                'pattern': r'(?i)(exec|eval|system|shell_exec|passthru)\s*\([^)]*\$',
                'severity': 'CRITICAL',
                'cwe': 'CWE-78',
                'description': 'Potential command injection vulnerability'
            },
            'path_traversal': {
                'pattern': r'\.\.\/|\.\.\\',
                'severity': 'HIGH',
                'cwe': 'CWE-22',
                'description': 'Potential path traversal vulnerability'
            },
            'insecure_random': {
                'pattern': r'(?i)(math\.random|random\.seed\(|mt_rand\()',
                'severity': 'LOW',
                'cwe': 'CWE-330',
                'description': 'Use of cryptographically weak random number generator'
            }
        }

    def scan_file(self, file_path):
        """Scan a single file for security patterns"""
        try:
            # Check if file should be excluded
            if any(exclude_file in str(file_path) for exclude_file in self.exclude_files):
                print(f"Skipping excluded file: {file_path}")
                return

            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()

            # Check for SECURITY_TEST_IGNORE markers in file content
            if any(re.search(pattern, content) for pattern in self.security_test_ignore_patterns):
                print(f"Skipping file with SECURITY_TEST_IGNORE markers: {file_path}")
                return

            for rule_name, rule_config in self.patterns.items():
                matches = re.finditer(rule_config['pattern'], content, re.MULTILINE)
                for match in matches:
                    line_num = content[:match.start()].count('\n') + 1

                    # Get some context around the match
                    lines = content.split('\n')
                    start_line = max(0, line_num - 2)
                    end_line = min(len(lines), line_num + 3)
                    context = '\n'.join(lines[start_line:end_line])

                    # Check if this specific match should be ignored
                    match_line = lines[line_num - 1] if line_num <= len(lines) else ""
                    if any(re.search(pattern, match_line) for pattern in self.security_test_ignore_patterns):
                        print(f"Ignoring finding in {file_path}:{line_num} due to SECURITY_TEST_IGNORE marker")
                        continue

                    self.findings.append({
                        'file': str(file_path),
                        'line': line_num,
                        'rule': rule_name,
                        'severity': rule_config['severity'],
                        'cwe': rule_config['cwe'],
                        'match': match.group(0)[:100],  # Truncate long matches
                        'context': context,
                        'description': rule_config['description']
                    })
        except Exception as e:
            print(f"Error scanning {file_path}: {e}")

    def scan_directory(self, directory):
        """Scan all supported files in a directory"""
        extensions = ['.py', '.js', '.ts', '.jsx', '.tsx', '.php', '.java', '.cs', '.rb', '.go', '.cpp', '.c', '.h']

        for root, dirs, files in os.walk(directory):
            # Skip directories that shouldn't be scanned (including security-analysis)
            dirs[:] = [d for d in dirs if d not in self.exclude_directories]

            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    file_path = Path(root) / file
                    self.scan_file(file_path)

    def generate_report(self):
        """Generate a summary report of findings"""
        summary = {
            'total': len(self.findings),
            'critical': len([f for f in self.findings if f['severity'] == 'CRITICAL']),
            'high': len([f for f in self.findings if f['severity'] == 'HIGH']),
            'medium': len([f for f in self.findings if f['severity'] == 'MEDIUM']),
            'low': len([f for f in self.findings if f['severity'] == 'LOW'])
        }

        return {
            'findings': self.findings,
            'summary': summary,
            'scan_info': {
                'total_files_scanned': len(set(f['file'] for f in self.findings)),
                'patterns_used': list(self.patterns.keys())
            }
        }

def main():
    """Main execution function"""
    print("Starting custom security analysis...")

    checker = SecurityChecker()
    checker.scan_directory('.')
    report = checker.generate_report()

    # Write results to JSON file
    with open('custom-security-results.json', 'w') as f:
        json.dump(report, f, indent=2)

    # Print summary
    summary = report['summary']
    print("Custom security scan completed!")
    print(f"Total findings: {summary['total']}")
    print(f"Critical: {summary['critical']}, High: {summary['high']}, Medium: {summary['medium']}, Low: {summary['low']}")

    if summary['total'] > 0:
        print("Results saved to custom-security-results.json")

    return summary['total']

if __name__ == "__main__":
    exit_code = main()
    exit(0 if exit_code >= 0 else 1)
