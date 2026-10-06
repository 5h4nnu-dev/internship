#!/usr/bin/env python3
"""
Working demonstration of the web application penetration testing framework.
"""

import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent / "web_pentest_ai"
sys.path.insert(0, str(project_root))

from core.engine import PentestEngine
from core.logger import setup_logger
import logging

# Setup logger
logger = setup_logger("web_pentest_ai_demo", "logs/web_pentest_ai_demo.log")

def demo_framework():
    """Demonstrate framework functionality"""
    print("Web Application Penetration Testing Framework")
    print("=" * 50)

    try:
        # Test basic engine creation
        print("1. Creating engine...")
        engine = PentestEngine("https://httpbin.org")
        print("   ✓ Engine created successfully")

        # Test module loading
        print("2. Loading modules...")
        engine.load_modules()
        print(f"   ✓ Loaded {len(engine.modules)} modules")

        # Show available modules
        print("3. Available modules:")
        module_info = engine.get_module_info()
        for i, module in enumerate(module_info[:5], 1):  # Show first 5
            print(f"   {i}. {module['name']}")
        if len(module_info) > 5:
            print(f"   ... and {len(module_info) - 5} more modules")

        print("\n✅ Framework is ready for use!")
        print("\nTo run tests:")
        print("  python run.py --target https://example.com --interactive")
        print("  python run.py --target https://example.com --modules endpoint_discovery technology_detection")

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    demo_framework()