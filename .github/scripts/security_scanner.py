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
        self.patterns = {
            'hardcoded_secrets': {
                'pattern': r'(?i)(password|secret|key|token|api_key)\s*[=:]\s*["\']([^"\']{8,})["\']',
                'severity': 'HIGH',
                'cwe': 'CWE-798',
                'description': 'Potential hardcoded secret or credential'
            },
            'sql_injection': {
                'pattern': r'(?i)(SELECT|INSERT|UPDATE|DELETE).*\+.*["\']',
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
                'pattern': r'http://(?!localhost|127\.0\.0\.1|0\.0\.0\.0)',
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
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()

            for rule_name, rule_config in self.patterns.items():
                matches = re.finditer(rule_config['pattern'], content, re.MULTILINE)
                for match in matches:
                    line_num = content[:match.start()].count('\n') + 1

                    # Get some context around the match
                    lines = content.split('\n')
                    start_line = max(0, line_num - 2)
                    end_line = min(len(lines), line_num + 3)
                    context = '\n'.join(lines[start_line:end_line])

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
            # Skip common directories that shouldn't be scanned
            dirs[:] = [d for d in dirs if d not in [
                '.git', 'node_modules', '__pycache__', '.venv', 'venv',
                'dist', 'build', '.next', 'coverage', 'logs'
            ]]

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
