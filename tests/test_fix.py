#!/usr/bin/env python3
"""
Simple test to verify the framework loads without circular import issues.
"""

import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent / "web_pentest_ai"
sys.path.insert(0, str(project_root))

try:
    # Test importing core components
    from core.engine import PentestEngine
    from core.base_module import BaseModule
    from core.target import Target
    from core.context import AssessmentContext
    from core.finding import Finding

    print("✓ Core components imported successfully")

    # Test importing modules
    from modules.endpoint_discovery import EndpointDiscoveryModule
    from modules.technology_detection import TechnologyDetectionModule
    from modules.sql_injection_test import SQLInjectionTestModule
    from modules.xss_test import XSSTestModule

    print("✓ All modules imported successfully")

    # Test creating engine
    engine = PentestEngine("https://httpbin.org")
    print("✓ Engine created successfully")

    # Test loading modules
    engine.load_modules()
    print(f"✓ Modules loaded successfully: {len(engine.modules)} modules")

    print("\n🎉 Framework is working correctly!")
    print("All circular import issues have been resolved.")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()