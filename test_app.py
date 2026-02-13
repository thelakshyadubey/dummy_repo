"""
Unit tests for the vulnerable application.
These tests verify functionality without executing vulnerable code paths.
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app

def test_safe_function():
    """Test that safe_function returns expected data."""
    result = app.safe_function()
    assert result == {"name": "test", "value": 42}

def test_calculate_basic():
    """Test calculate with safe literal expressions."""
    # Only test with safe literal expressions
    result = app.calculate("2 + 2")
    assert result == 4

def test_imports():
    """Test that required modules are imported."""
    assert hasattr(app, 'os')

if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
