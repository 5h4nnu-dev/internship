#!/usr/bin/env python3
"""
Simple test to verify modules can be imported correctly.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from web_pentest_ai.modules.command_injection_test import CommandInjectionTestModule
    print("✓ CommandInjectionTestModule imported successfully")

    from web_pentest_ai.modules.ldap_injection_test import LDAPInjectionTestModule
    print("✓ LDAPInjectionTestModule imported successfully")

    from web_pentest_ai.modules.nosql_injection_test import NoSQLInjectionTestModule
    print("✓ NoSQLInjectionTestModule imported successfully")

    from web_pentest_ai.modules.broken_authentication_test import BrokenAuthenticationTestModule
    print("✓ BrokenAuthenticationTestModule imported successfully")

    print("\nAll new modules imported successfully!")
    print("The framework now has enhanced OWASP Top 10 vulnerability detection capabilities.")

except Exception as e:
    print(f"Error importing modules: {e}")
    import traceback
    traceback.print_exc()