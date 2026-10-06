#!/usr/bin/env python3
"""
Example usage of the web application penetration testing framework.
"""

import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent / "web_pentest_ai"
sys.path.insert(0, str(project_root))

from core.engine import PentestEngine
from core.target import Target
from modules.endpoint_discovery import EndpointDiscoveryModule

def main():
    """Demonstrate framework usage"""
    print("Web Application Penetration Testing Framework Demo")
    print("=" * 60)

    # Create a target
    target_url = "https://httpbin.org"
    print(f"Creating target for: {target_url}")

    target = Target(target_url)
    print(f"Target created successfully")
    print(f"Base URL: {target.base_url}")
    print(f"Discovered URLs: {len(target.discovered_urls)}")

    # Create engine
    print("\nCreating penetration test engine...")
    engine = PentestEngine(target_url)
    print("Engine created successfully")

    # Show available modules
    print("\nAvailable modules:")
    module_info = engine.get_module_info()
    for module in module_info:
        print(f"  - {module['name']}: {module['description']}")

    # Run endpoint discovery
    print("\nRunning endpoint discovery...")
    results = engine.execute_modules(["endpoint_discovery"])

    # Display results
    context = engine.context.get_context()
    target_context = context["target"]

    print(f"\nDiscovery Results:")
    print(f"  Discovered URLs: {len(target_context['discovered_urls'])}")
    print(f"  Endpoints: {len(target_context['endpoints'])}")
    print(f"  Forms: {len(target_context['forms'])}")
    print(f"  APIs: {len(target_context['apis'])}")

    if target_context['endpoints']:
        print("\nFirst few endpoints:")
        for i, endpoint in enumerate(target_context['endpoints'][:3]):
            print(f"  {i+1}. {endpoint.get('url', 'Unknown')}")

    print("\nDemo completed successfully!")

if __name__ == "__main__":
    main()