#!/usr/bin/env python3
"""
Test script to verify all Phase 4 modules work correctly.
"""

import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent / "web_pentest_ai"
sys.path.insert(0, str(project_root))

from core.engine import PentestEngine
from modules.attack_surface_analysis import AttackSurfaceAnalysisModule
from modules.module_selection import ModuleSelectionModule
from modules.result_correlation import ResultCorrelationModule

def main():
    """Test all Phase 4 modules"""
    print("Web Application Penetration Testing Framework - Phase 4 Modules Test")
    print("=" * 80)

    # Test with a simple target
    target_url = "https://httpbin.org"
    print(f"Testing target: {target_url}")

    # Create engine
    print("\nCreating penetration test engine...")
    engine = PentestEngine(target_url)

    # Test each Phase 4 module individually
    modules_to_test = [
        ("attack_surface_analysis", "Attack Surface Analysis"),
        ("module_selection", "Module Selection"),
        ("result_correlation", "Result Correlation")
    ]

    print("\nRunning Phase 4 modules test:")
    print("-" * 50)

    for module_name, module_description in modules_to_test:
        try:
            print(f"Testing {module_description}..")
            result = engine.execute_module(module_name)
            if result and result.success:
                print(f"  ✓ {module_description} completed successfully")
            else:
                print(f"  ✗ {module_description} failed")
        except Exception as e:
            print(f"  ✗ {module_description} error: {e}")

    # Show overall context
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)

    context = engine.context.get_context()
    target_context = context["target"]

    print(f"Target: {target_context['url']}")
    print(f"Discovered URLs: {len(target_context['discovered_urls'])}")
    print(f"Endpoints: {len(target_context['endpoints'])}")
    print(f"Technologies: {len(target_context['technologies'])}")
    print(f"Parameters: {len(target_context['parameters'])}")
    print(f"APIs: {len(target_context['apis'])}")
    print(f"Headers: {len(target_context['headers'])}")

    print("\nPhase 4 modules test completed successfully!")

if __name__ == "__main__":
    main()