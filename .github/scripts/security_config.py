# Security Analysis Configuration

# Security Scanner Configuration
SECURITY_SCAN_PATHS = [
    "src/",
    "lib/",
    "app/",
    "components/",
    "pages/",
    "api/",
    "services/",
    "utils/",
    "models/",
    "controllers/",
    "middleware/",
    "routes/"
]

# File extensions to scan
SCAN_EXTENSIONS = [
    ".py", ".js", ".ts", ".jsx", ".tsx",
    ".php", ".java", ".cs", ".rb", ".go",
    ".cpp", ".c", ".h", ".swift", ".kt"
]

# Directories to exclude from scanning
EXCLUDE_DIRECTORIES = [
    ".git", "node_modules", "__pycache__", ".venv", "venv",
    "dist", "build", ".next", "coverage", "logs", "tmp",
    ".pytest_cache", ".mypy_cache", "vendor", "packages",
    "security-analysis"  # Exclude security test files with intentional vulnerabilities
]

# Files to exclude from security scanning (test/demo files with intentional vulnerabilities)
EXCLUDE_FILES = [
    "test_vulnerable_code.py",  # Security testing file with fake credentials
    "security_test_samples.py",
    "**/test_*_vulnerable_*.py",
    "**/demo_*_insecure_*.py"
]

# Patterns to ignore in security scanning (for test/demo purposes)
SECURITY_TEST_IGNORE_PATTERNS = [
    r"FAKE-DEMO-.*",  # All fake demo credentials
    r".*DEMO CREDENTIAL.*",  # Demo credential markers
    r"SECURITY_TEST_IGNORE:",  # Explicit test ignore markers
]

# Security pattern severity levels
SEVERITY_LEVELS = {
    "CRITICAL": {
        "priority": 1,
        "color": "red",
        "emoji": "🔴",
        "response_time": "immediate"
    },
    "HIGH": {
        "priority": 2,
        "color": "orange",
        "emoji": "🟠",
        "response_time": "1-2 days"
    },
    "MEDIUM": {
        "priority": 3,
        "color": "yellow",
        "emoji": "🟡",
        "response_time": "1 week"
    },
    "LOW": {
        "priority": 4,
        "color": "green",
        "emoji": "🟢",
        "response_time": "2 weeks"
    }
}

# GitHub issue labels by vulnerability type
VULNERABILITY_LABELS = {
    "injection": ["injection", "sql-injection", "command-injection"],
    "xss": ["xss", "cross-site-scripting"],
    "authentication": ["auth", "authentication", "session"],
    "authorization": ["authz", "authorization", "access-control"],
    "cryptography": ["crypto", "encryption", "hashing"],
    "configuration": ["config", "security-headers", "cors"],
    "dependencies": ["dependency", "supply-chain", "cve"],
    "privacy": ["privacy", "gdpr", "data-protection"]
}

# Compliance frameworks
COMPLIANCE_FRAMEWORKS = {
    "OWASP_TOP_10": {
        "A01": "Broken Access Control",
        "A02": "Cryptographic Failures",
        "A03": "Injection",
        "A04": "Insecure Design",
        "A05": "Security Misconfiguration",
        "A06": "Vulnerable and Outdated Components",
        "A07": "Identification and Authentication Failures",
        "A08": "Software and Data Integrity Failures",
        "A09": "Security Logging and Monitoring Failures",
        "A10": "Server-Side Request Forgery"
    },
    "CWE_TOP_25": [
        "CWE-79", "CWE-89", "CWE-20", "CWE-125", "CWE-119",
        "CWE-78", "CWE-416", "CWE-22", "CWE-352", "CWE-434",
        "CWE-306", "CWE-190", "CWE-502", "CWE-287", "CWE-476",
        "CWE-798", "CWE-918", "CWE-362", "CWE-269", "CWE-94",
        "CWE-863", "CWE-276", "CWE-200", "CWE-522", "CWE-732"
    ]
}

# Security testing integration
SECURITY_TOOLS = {
    "sast": {
        "semgrep": {
            "enabled": True,
            "config": "auto",
            "output_format": "json"
        },
        "bandit": {
            "enabled": True,
            "confidence": "medium",
            "severity": "medium"
        }
    },
    "dependency_scanning": {
        "npm_audit": {
            "enabled": True,
            "audit_level": "moderate"
        },
        "safety": {
            "enabled": True,
            "full_report": True
        }
    },
    "secrets_detection": {
        "trufflesecurity": {
            "enabled": False,
            "entropy_threshold": 3.0
        }
    }
}

# Notification settings
NOTIFICATIONS = {
    "critical_vulnerabilities": {
        "enabled": True,
        "channels": ["github_issues", "security_team"],
        "immediate": True
    },
    "high_vulnerabilities": {
        "enabled": True,
        "channels": ["github_issues"],
        "immediate": False
    },
    "weekly_summary": {
        "enabled": True,
        "day": "monday",
        "time": "09:00"
    }
}

# GitHub issue template settings
ISSUE_SETTINGS = {
    "duplicate_check": {
        "enabled": True,
        "lookback_days": 30,
        "similarity_threshold": 0.8
    },
    "auto_assignment": {
        "enabled": True,
        "assign_by_component": True,
        "default_assignee": None
    },
    "milestones": {
        "critical": "Security Sprint",
        "high": "Next Sprint",
        "medium": "Backlog",
        "low": "Future"
    }
}

# Custom security patterns (extend the default patterns)
CUSTOM_PATTERNS = {
    "api_key_exposure": {
        "pattern": r"(?i)(api_key|apikey|api-key)\s*[=:]\s*['\"][a-zA-Z0-9]{20,}['\"]",
        "severity": "HIGH",
        "cwe": "CWE-798",
        "description": "Exposed API key in source code"
    },
    "debug_mode_production": {
        "pattern": r"(?i)(debug|development)\s*[=:]\s*(true|1|yes|on)",
        "severity": "MEDIUM",
        "cwe": "CWE-489",
        "description": "Debug mode potentially enabled in production"
    },
    "unsafe_deserialization": {
        "pattern": r"(?i)(pickle\.loads|yaml\.load|eval\(|exec\()",
        "severity": "CRITICAL",
        "cwe": "CWE-502",
        "description": "Unsafe deserialization or code execution"
    }
}
