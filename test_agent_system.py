#!/usr/bin/env python3
"""
Test script to verify the agent system implementation
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'web_pentest_ai'))

from agents.root_agent import RootAgent
from agents.child_agent import ChildAgent
from agents.base_agent import AgentContext
from core.agent_engine import AgentPentestEngine

def test_agent_system():
    """Test the agent system implementation"""
    print("Testing agent system implementation...")

    # Test 1: Create root agent
    print("\n1. Testing RootAgent creation...")
    try:
        root_agent = RootAgent("http://example.com")
        print(f"✓ RootAgent created successfully: {root_agent.name}")
        print(f"  Type: {root_agent.agent_type.value}")
        print(f"  Target: {root_agent.target}")
    except Exception as e:
        print(f"✗ Failed to create RootAgent: {e}")
        return False

    # Test 2: Test child agent creation
    print("\n2. Testing ChildAgent creation...")
    try:
        child_agent = ChildAgent("endpoint_discovery")
        print(f"✓ ChildAgent created successfully: {child_agent.name}")
        print(f"  Type: {child_agent.agent_type.value}")
        print(f"  Module: {child_agent.module_name}")
    except Exception as e:
        print(f"✗ Failed to create ChildAgent: {e}")
        return False

    # Test 3: Test agent context
    print("\n3. Testing AgentContext...")
    try:
        context = AgentContext(
            target="http://example.com",
            findings=[],
            modules_executed=[],
            execution_history=[]
        )
        print(f"✓ AgentContext created successfully")
        print(f"  Target: {context.target}")
    except Exception as e:
        print(f"✗ Failed to create AgentContext: {e}")
        return False

    # Test 4: Test engine with agent system
    print("\n4. Testing AgentPentestEngine...")
    try:
        engine = AgentPentestEngine("http://example.com")
        print(f"✓ AgentPentestEngine created successfully")
        print(f"  Engine type: {type(engine).__name__}")

        # Check if sandboxing is available
        sandbox_status = engine.sandbox_manager is not None
        print(f"  Sandbox manager available: {sandbox_status}")

    except Exception as e:
        print(f"✗ Failed to create AgentPentestEngine: {e}")
        return False

    print("\n✓ All tests passed! Agent system implementation is working correctly.")
    return True

if __name__ == "__main__":
    test_agent_system()