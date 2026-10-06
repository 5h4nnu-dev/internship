"""
Tests for the web application penetration testing framework.
"""

import unittest
import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from core.engine import PentestEngine
from core.target import Target
from core.base_module import BaseModule, ModuleCategory
from modules.endpoint_discovery import EndpointDiscoveryModule

class TestTarget(unittest.TestCase):
    def test_target_creation(self):
        """Test target creation and properties"""
        target = Target("https://example.com/test")
        self.assertEqual(target.url, "https://example.com/test")
        self.assertEqual(target.base_url, "https://example.com/")
        self.assertEqual(target.scheme, "https")
        self.assertEqual(target.netloc, "example.com")
        self.assertEqual(target.path, "/test")

    def test_target_context(self):
        """Test target context generation"""
        target = Target("https://example.com/test")
        context = target.get_context()
        self.assertIn("url", context)
        self.assertIn("base_url", context)
        self.assertIn("endpoints", context)

class TestBaseModule(unittest.TestCase):
    def test_module_creation(self):
        """Test base module creation"""
        class TestModule(BaseModule):
            def __init__(self):
                super().__init__(
                    name="test_module",
                    description="Test module",
                    category=ModuleCategory.RECONNAISSANCE
                )

            def execute(self, context):
                return Mock(success=True, data={})

        module = TestModule()
        self.assertEqual(module.name, "test_module")
        self.assertEqual(module.description, "Test module")
        self.assertEqual(module.category, ModuleCategory.RECONNAISSANCE)

class TestEndpointDiscoveryModule(unittest.TestCase):
    def test_module_creation(self):
        """Test endpoint discovery module creation"""
        module = EndpointDiscoveryModule()
        self.assertEqual(module.name, "endpoint_discovery")
        self.assertEqual(module.category, ModuleCategory.RECONNAISSANCE)

class TestPentestEngine(unittest.TestCase):
    def test_engine_creation(self):
        """Test engine creation"""
        engine = PentestEngine("https://example.com")
        self.assertIsNotNone(engine.target)
        self.assertIsNotNone(engine.context)
        self.assertIsNotNone(engine.modules)

if __name__ == '__main__':
    unittest.main()