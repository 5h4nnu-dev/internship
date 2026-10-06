#!/usr/bin/env python3
"""
Demonstration of the interactive mode for the web application penetration testing framework.
"""

import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent / "web_pentest_ai"
sys.path.insert(0, str(project_root))

from core.engine import PentestEngine

def demo_interactive_mode():
    """Demonstrate the interactive module selection"""
    print("Web Application Penetration Testing Framework - Interactive Mode Demo")
    print("=" * 70)

    # Create a simple engine to show available modules
    engine = PentestEngine("https://httpbin.org")
    engine.load_modules()

    print("Available modules in the framework:")
    print("-" * 40)

    module_info = engine.get_module_info()
    for i, module in enumerate(module_info, 1):
        print(f"{i}. {module['name']}")
        print(f"   Description: {module['description']}")
        print(f"   Category: {module['category']}")
        print()

    print("The framework now supports interactive module selection!")
    print("You can run it in interactive mode with:")
    print("  python run.py --target https://example.com --interactive")
    print()
    print("Or with the default behavior:")
    print("  python run.py --target https://example.com")

if __name__ == "__main__":
    demo_interactive_mode()