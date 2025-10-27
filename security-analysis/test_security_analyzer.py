#!/usr/bin/env python3
"""
Test script to demonstrate the Security Analyzer functionality
"""

import os
import sys

# Add the scripts directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.github', 'scripts'))

def test_security_scanner():
    """Test the security scanner on the vulnerable code file"""
    print("🔍 Testing Security Scanner...")
    print("=" * 50)

    try:
        from security_scanner import SecurityChecker

        # Create a security checker instance
        checker = SecurityChecker()

        # Scan the test vulnerable code file
        test_file = 'test_vulnerable_code.py'
        if os.path.exists(test_file):
            print(f"Scanning {test_file}...")
            checker.scan_file(test_file)

            # Generate report
            report = checker.generate_report()

            # Display results
            print("\n📊 Security Scan Results:")
            print(f"Total findings: {report['summary']['total']}")
            print(f"Critical: {report['summary']['critical']}")
            print(f"High: {report['summary']['high']}")
            print(f"Medium: {report['summary']['medium']}")
            print(f"Low: {report['summary']['low']}")

            # Show first few findings
            print("\n🔍 Sample Findings:")
            for i, finding in enumerate(report['findings'][:5]):
                severity_emoji = {
                    'CRITICAL': '🔴',
                    'HIGH': '🟠',
                    'MEDIUM': '🟡',
                    'LOW': '🟢'
                }.get(finding['severity'], '⚪')

                print(f"{severity_emoji} {finding['severity']} - {finding['description']}")
                print(f"   File: {finding['file']}:{finding['line']}")
                print(f"   Rule: {finding['rule']}")
                print(f"   CWE: {finding['cwe']}")
                print()

            if len(report['findings']) > 5:
                print(f"... and {len(report['findings']) - 5} more findings")

            return True

        else:
            print(f"❌ Test file {test_file} not found")
            return False

    except ImportError as e:
        print(f"❌ Failed to import security scanner: {e}")
        return False
    except Exception as e:
        print(f"❌ Error during security scan: {e}")
        return False

def test_configuration():
    """Test the security configuration"""
    print("\n⚙️ Testing Security Configuration...")
    print("=" * 50)

    try:
        from security_config import (
            CUSTOM_PATTERNS,
            SEVERITY_LEVELS,
            VULNERABILITY_LABELS,
        )

        print("✅ Severity levels configured:")
        for level, config in SEVERITY_LEVELS.items():
            print(f"   {config['emoji']} {level}: {config['response_time']}")

        print(f"\n✅ Vulnerability labels: {len(VULNERABILITY_LABELS)} categories")
        print(f"✅ Custom patterns: {len(CUSTOM_PATTERNS)} additional patterns")

        return True

    except ImportError as e:
        print(f"❌ Failed to import security configuration: {e}")
        return False
    except Exception as e:
        print(f"❌ Error loading configuration: {e}")
        return False

def test_chat_mode():
    """Test the chat mode file"""
    print("\n💬 Testing Security Analyzer Chat Mode...")
    print("=" * 50)

    chatmode_file = '.github/chatmodes/SecurityAnalyzer.chatmode.md'
    if os.path.exists(chatmode_file):
        print("✅ SecurityAnalyzer.chatmode.md exists")

        with open(chatmode_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for key components
        components = [
            "# Name: Security Analyzer",
            "@security-scan",
            "@owasp-check",
            "@auth-review",
            "@create-issues",
            "Security Vulnerability Report"
        ]

        missing_components = []
        for component in components:
            if component not in content:
                missing_components.append(component)

        if missing_components:
            print(f"⚠️ Missing components: {missing_components}")
        else:
            print("✅ All key components present in chat mode")

        return len(missing_components) == 0
    else:
        print(f"❌ Chat mode file not found: {chatmode_file}")
        return False

def test_workflow():
    """Test the GitHub Actions workflow"""
    print("\n🔄 Testing GitHub Actions Workflow...")
    print("=" * 50)

    workflow_file = '.github/workflows/security-analysis.yml'
    if os.path.exists(workflow_file):
        print("✅ security-analysis.yml workflow exists")

        with open(workflow_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for key workflow components
        components = [
            "name: Security Analysis and Issue Creation",
            "security-analysis:",
            "create-security-issues:",
            # SECURITY_TEST_IGNORE: This is checking for workflow token reference, not a hardcoded secret - Issue #449
            "GITHUB_TOKEN:",  # FAKE-DEMO-token-reference for workflow validation only
            "python .github/scripts/security_scanner.py",
            "python .github/scripts/create_security_issues.py"
        ]

        missing_components = []
        for component in components:
            if component not in content:
                missing_components.append(component)

        if missing_components:
            print(f"⚠️ Missing workflow components: {missing_components}")
        else:
            print("✅ All key workflow components present")

        return len(missing_components) == 0
    else:
        print(f"❌ Workflow file not found: {workflow_file}")
        return False

def main():
    """Main test function"""
    print("🛡️ Security Analyzer Test Suite")
    print("=" * 60)

    tests = [
        ("Security Scanner", test_security_scanner),
        ("Configuration", test_configuration),
        ("Chat Mode", test_chat_mode),
        ("Workflow", test_workflow)
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        try:
            if test_func():
                print(f"✅ {test_name} test PASSED")
                passed += 1
            else:
                print(f"❌ {test_name} test FAILED")
        except Exception as e:
            print(f"❌ {test_name} test ERROR: {e}")

    print("\n" + "=" * 60)
    print(f"🏁 Test Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed! Security Analyzer is ready to use.")
        print("\n🚀 Next Steps:")
        print("1. Commit and push these changes to your repository")
        print("2. Try the chat mode: @SecurityAnalyzer @security-scan")
        print("3. Run the GitHub Actions workflow to create security issues")
        print("4. Review and remediate the identified security vulnerabilities")
    else:
        print(f"⚠️ {total - passed} tests failed. Please review the errors above.")

    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
