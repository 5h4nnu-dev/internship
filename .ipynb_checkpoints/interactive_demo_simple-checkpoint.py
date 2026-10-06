#!/usr/bin/env python3
"""
Minimal working example to demonstrate interactive module selection.
This shows the core functionality without complex imports.
"""

import sys
import os
from pathlib import Path

def show_available_modules():
    """Show available modules for selection"""
    modules = [
        "endpoint_discovery",
        "technology_detection",
        "javascript_endpoint_extraction",
        "parameter_discovery",
        "api_discovery",
        "security_header_analysis",
        "attack_surface_analysis",
        "sql_injection_test",
        "xss_test",
        "authentication_test"
    ]

    print("Available modules:")
    print("-" * 30)
    for i, module in enumerate(modules, 1):
        print(f"{i}. {module}")
    print()
    print("Select modules by number (e.g., '1 3 5' for modules 1, 3, and 5)")
    print("Or type 'all' to run all modules")
    print()

def get_user_selection():
    """Get user's module selection"""
    try:
        selection = input("Enter your selection: ").strip()
        if selection.lower() == 'all':
            return 'all'
        else:
            # Parse numbers
            numbers = [int(x) - 1 for x in selection.split() if x.isdigit()]
            return numbers
    except KeyboardInterrupt:
        print("\nSelection cancelled.")
        return None
    except Exception as e:
        print(f"Error in selection: {e}")
        return None

def main():
    """Main demonstration"""
    print("Web Application Penetration Testing Framework")
    print("=" * 50)
    print()

    # Get target
    target = input("Enter target URL: ").strip()
    if not target:
        print("No target provided. Exiting.")
        return

    print(f"\nTarget: {target}")
    print()

    # Show available modules
    show_available_modules()

    # Get user selection
    selection = get_user_selection()

    if selection is None:
        print("No selection made.")
        return

    if selection == 'all':
        print("Running all modules...")
        print("✓ endpoint_discovery")
        print("✓ technology_detection")
        print("✓ javascript_endpoint_extraction")
        print("✓ parameter_discovery")
        print("✓ api_discovery")
        print("✓ security_header_analysis")
        print("✓ attack_surface_analysis")
        print("✓ sql_injection_test")
        print("✓ xss_test")
        print("✓ authentication_test")
    else:
        print("Selected modules:")
        selected_modules = []
        for num in selection:
            if 0 <= num < 10:  # Valid range
                modules = [
                    "endpoint_discovery",
                    "technology_detection",
                    "javascript_endpoint_extraction",
                    "parameter_discovery",
                    "api_discovery",
                    "security_header_analysis",
                    "attack_surface_analysis",
                    "sql_injection_test",
                    "xss_test",
                    "authentication_test"
                ]
                selected_modules.append(modules[num])
                print(f"✓ {modules[num]}")

    print("\n✅ Interactive module selection demo completed!")
    print("The actual framework supports this same interface.")

if __name__ == "__main__":
    main()