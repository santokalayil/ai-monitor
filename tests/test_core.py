"""
Tests for the core functionality of the AI monitor package.
"""
from ai.core import monitor_status, get_version

def test_monitor_status():
    """Test that monitor_status returns the expected string."""
    assert monitor_status() == "AI systems are operational"

def test_get_version():
    """Test that get_version returns a valid version string."""
    version = get_version()
    assert isinstance(version, str)
    assert len(version.split(".")) == 3  # Should be semantic versioning 