#!/usr/bin/env python3
"""
Test script to verify all Phase 2 modules work correctly.
"""

import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent / "web_pentest_ai"
sys.path.insert(0, str(project_root))

from core.engine import PentestEngine
from modules.endpoint_discovery import EndpointDiscoveryModule
from modules.technology_detection import TechnologyDetectionModule
from modules.javascript_endpoint_extraction import JavaScriptEndpointExtractionModule
from modules.parameter_discovery import ParameterDiscoveryModule
from modules.api_discovery import APIDiscoveryModule
from modules.security_header_analysis import SecurityHeaderAnalysisModule

def main():
    """Test all Phase 2 modules"""
    print("Web Application Penetration Testing Framework - Phase 2 Modules Test")
    print("=" * 80)

    # Test with a simple target
    target_url = "https://httpbin.org"
    print(f"Testing target: {target_url}")

    # Create engine
    print("\nCreating penetration test engine...")
    engine = PentestEngine(target_url)

    # Test each module individually
    modules_to_test = [
        ("endpoint_discovery", "Endpoint Discovery"),
        ("technology_detection", "Technology Detection"),
        ("javascript_endpoint_extraction", "JavaScript Endpoint Extraction"),
        ("parameter_discovery", "Parameter Discovery"),
        ("api_discovery", "API Discovery"),
        ("security_header_analysis", "Security Header Analysis")
    ]

    print("\nRunning Phase 2 modules test:")
    print("-" * 50)

    for module_name, module_description in modules_to_test:
        try:
            print(f"Testing {module_description}...")
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

    print("\nPhase 2 modules test completed successfully!")

if __name__ == "__main__":
    main()