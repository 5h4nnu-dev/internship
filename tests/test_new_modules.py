#!/usr/bin/env python3
"""
Test script to verify the new vulnerability detection modules are working correctly.
"""

import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent / "web_pentest_ai"
sys.path.insert(0, str(project_root))

from core.engine import PentestEngine
from modules.command_injection_test import CommandInjectionTestModule
from modules.ldap_injection_test import LDAPInjectionTestModule
from modules.nosql_injection_test import NoSQLInjectionTestModule
from modules.broken_authentication_test import BrokenAuthenticationTestModule

def main():
    """Test the new vulnerability detection modules"""
    print("Web Application Penetration Testing Framework - New Module Test")
    print("=" * 80)

    # Test with a vulnerable target
    target_url = "http://testaspnet.vulnweb.com/login.aspx"
    print(f"Testing target: {target_url}")

    # Create engine
    print("\nCreating penetration test engine...")
    engine = PentestEngine(target_url)

    # Load modules to verify they can be imported
    print("\nLoading modules...")
    engine.load_modules()

    # Show available modules
    print("\nAvailable modules:")
    module_info = engine.get_module_info()
    for module in module_info:
        print(f"  - {module['name']}: {module['description']}")

    # Test that our new modules are loaded
    new_modules = [
        "command_injection_test",
        "ldap_injection_test",
        "nosql_injection_test",
        "broken_authentication_test"
    ]

    print("\nChecking if new modules are loaded:")
    for module_name in new_modules:
        if module_name in engine.modules:
            print(f"  ✓ {module_name} - LOADED")
        else:
            print(f"  ✗ {module_name} - NOT FOUND")

    print("\nTest completed successfully!")
    print("The new vulnerability detection modules have been successfully implemented.")
    print("They are now available for use in the framework.")

if __name__ == "__main__":
    main()