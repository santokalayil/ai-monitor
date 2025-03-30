"""
Tests for the core functionality of the AI monitor package.
"""
import os
import sys
import pytest
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Debug information
print(f"Python path: {sys.path}")
print(f"Current directory: {os.getcwd()}")
print(f"Project root: {project_root}")
print(f"Files in project root: {os.listdir(project_root)}")

try:
    from ai.core import monitor_status, get_version
except ImportError as e:
    print(f"Import error: {e}")
    print(f"Available modules: {os.listdir(project_root / 'ai')}")
    raise

def test_monitor_status():
    """Test that monitor_status returns the expected string."""
    result = monitor_status()
    assert isinstance(result, str)
    assert result == "AI systems are operational"

def test_get_version():
    """Test that get_version returns a valid version string."""
    version = get_version()
    assert isinstance(version, str)
    assert len(version.split(".")) == 3  # Should be semantic versioning
    # Check that each part is a number
    for part in version.split("."):
        assert part.isdigit() 